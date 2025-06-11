import os
import datetime
import uuid
from flask import Flask, render_template, request
import folium
import navigation_core as core

app = Flask(__name__)

def load_history():
    history = []
    if os.path.exists("delivery_log.txt"):
        with open("delivery_log.txt", encoding="utf-8") as f:
            for line in f:
                # split into 7 parts: id, date, client, driver, route, distance, time
                parts = line.strip().split(",", 6)
                if len(parts) == 7:
                    history.append(parts)
    return history

@app.route("/", methods=["GET", "POST"])
def index():
    result   = None
    map_html = None

    if request.method == "POST":
        pickup   = request.form["pickup"]
        delivery = request.form["delivery"]
        client   = request.form["client"]
        driver   = request.form["driver"]

        try:
            # 1) Geocode & build graph
            pick_coords           = core.geocode_address(pickup)
            del_coords            = core.geocode_address(delivery)
            graph, full_path, _, duration = core.get_route_data(pickup, delivery)

            # 2) Shortest path
            start_node, end_node  = core.find_closest_node(pick_coords, graph), \
                                    core.find_closest_node(del_coords, graph)
            path, meters          = core.dijkstra(graph, start_node, end_node)

            # 3) Timestamp, format & log
            now                    = datetime.datetime.now()
            date_str               = now.strftime("%Y-%m-%d %H:%M:%S")
            delivery_id            = uuid.uuid4().hex[:8]
            miles                  = round(meters * 0.000621371, 2)

            result = {
                "id":       delivery_id,
                "date":     date_str,
                "client":   client,
                "driver":   driver,
                "route":    f"{pickup} → {delivery}",
                "distance": f"{miles} mi",
                "time":     duration
            }

            # Write to log
            with open("delivery_log.txt", "a", encoding="utf-8") as f:
                f.write(
                    f"{delivery_id},{date_str},{client},{driver},"
                    f"{pickup} → {delivery},{miles:.2f} mi,{duration}\n"
                )

            # 4) Build Folium map embed
            m = folium.Map(location=full_path[0], zoom_start=13)
            folium.Marker(full_path[0], icon=folium.Icon(color="green")).add_to(m)
            folium.Marker(full_path[-1], icon=folium.Icon(color="red")).add_to(m)
            folium.PolyLine(full_path, weight=5).add_to(m)
            map_html = m._repr_html_()
        except Exception as e:
            result = {"error": str(e)}

    return render_template(
        "index.html",
        result=result,
        map_html=map_html
    )

@app.route("/history")
def history_page():
    history = load_history()
    return render_template("history.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)



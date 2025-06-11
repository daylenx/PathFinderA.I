# PathFinderAI

PathFinderAI is a Python-based delivery route planner that calculates the shortest driving route between two locations using the Google Maps and Directions APIs along with Dijkstra’s algorithm. It offers both a desktop GUI (Tkinter) and a web interface (Flask) with interactive map visualizations and delivery history tracking.

## 🛠️ Features

* **Address geocoding** via Google Maps Geocoding API
* **Shortest path calculation** using Dijkstra’s Algorithm
* **Interactive map** rendered with Folium
* **Web interface** built with Flask and Jinja2
* **Desktop GUI** (legacy) built with Tkinter
* **Delivery history** logging and display with timestamps
* **History page** accessible via a dedicated route
* **Environment-based API key** loading for secure configuration

## 📦 Tech Stack

* Python 3.10+
* Flask, Jinja2 (web framework and templating)
* Google Maps API (Geocoding & Directions)
* Folium (map rendering)
* polyline (decode Google polyline)
* heapq, uuid, math, os (core Python libraries)
* Tkinter (desktop GUI, legacy)

<<<<<<< HEAD
## 📂 File Structure

=======
Web interface built with Flask and Jinja2

Desktop GUI (legacy) built with Tkinter

Delivery history logging and display

History page accessible via a dedicated route

Environment-based API key loading for secure configuration

📦 Tech Stack

Python 3.10+

Flask, Jinja2 (web framework and templating)

Google Maps API (Geocoding & Directions)

Folium (map rendering)

polyline (decode Google polyline)

heapq, uuid, math, os (core Python libraries)

Tkinter (desktop GUI, legacy)

📂 File Structure
>>>>>>> 5f5b75224a0de7a8a827e8870582e6c4fc130f0d
```
PathFinderAI/
├── __pycache__/
│   └── navigation_core.cpython-313.pyc
├── .vscode/
│   └── settings.json
├── static/
│   └── css/
│       └── style.css
├── templates/
<<<<<<< HEAD
│   ├── index.html
│   └── history.html
├── app.py
├── navigation_core.py
├── navigation_gui.py
├── delivery_log.txt
├── requirements.txt
└── README.md
```

## 🚀 Getting Started
=======
│   ├── index.html         # Main page (form + map + history button)
│   └── history.html       # Delivery history page
└── static/
    └── css/
        └── style.css      # CSS for web interface
```
🚀 Getting Started
>>>>>>> 5f5b75224a0de7a8a827e8870582e6c4fc130f0d

### 1. Clone the repository

```bash
git clone https://github.com/daylenx/PathFinderA.I.git
cd PathFinderAI
```

<<<<<<< HEAD
### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Google Maps API key

Set the `GOOGLE_MAPS_API_KEY` environment variable before running:

* **Windows PowerShell**

  ```powershell
  $Env:GOOGLE_MAPS_API_KEY = "YOUR_API_KEY_HERE"
  ```

* **macOS/Linux**

  ```bash
  export GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE"
  ```

### 4. Run the web application

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000/` to access the web interface.

### 5. (Optional) Run the desktop GUI

```bash
python navigation_gui.py
```

## 📝 Usage
=======
2. Install dependencies
```
pip install -r requirements.txt
```
3. Set your Google Maps API key
```
Set the GOOGLE_MAPS_API_KEY environment variable before running:
```
Windows PowerShell
```
$Env:GOOGLE_MAPS_API_KEY = "YOUR_API_KEY_HERE"
```
macOS/Linux
```
export GOOGLE_MAPS_API_KEY="YOUR_API_KEY_HERE"
```
4. Run the web application
```
python app.py
```
Open your browser and navigate to http://127.0.0.1:5000/ to access the web interface.

5. (Optional) Run the desktop GUI

If you prefer the Tkinter version, simply:
```
python navigation_gui.py
```
📝 Usage
>>>>>>> 5f5b75224a0de7a8a827e8870582e6c4fc130f0d

1. **Enter** client name, driver name, pickup address, and delivery address.
2. **Submit** the form to calculate the route.
3. **View** the calculation timestamp, route details, and interactive map.
4. **Click** “View Delivery History” to see all past deliveries with timestamps.

## 🗃️ Delivery History

All deliveries are logged in `delivery_log.txt` (UTF-8 encoded) with a datetime stamp. You can view them via the web history page or open the file directly.

---

<<<<<<< HEAD
*Designed by Daylen Hall, Eric Cheeley, and Ashari Joiner (2025) — Delivering optimized, fast, and reliable route planning.*
=======
🗃️ Delivery History

All deliveries are logged in delivery_log.txt (UTF-8 encoded). You can view them via the web history page or open the file directly.
>>>>>>> 5f5b75224a0de7a8a827e8870582e6c4fc130f0d

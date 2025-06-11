import googlemaps
import os
import math
import polyline
from collections import defaultdict
import heapq

API_KEY = "AIzaSyDL9lE41UUGw-AfAqRPulvHGP5HLX7zMS8"
gmaps = googlemaps.Client(key=API_KEY)

def geocode_address(address):
    result = gmaps.geocode(address)
    if result:
        loc = result[0]['geometry']['location']
        return (loc['lat'], loc['lng'])
    else:
        raise ValueError("Invalid address")

def haversine(coord1, coord2):
    R = 6371000
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def get_route_data(start, end):
    directions = gmaps.directions(start, end, mode='driving')
    legs = directions[0]['legs'][0]
    steps = legs['steps']
    overview = directions[0]['overview_polyline']['points']
    decoded = polyline.decode(overview)
    graph = defaultdict(list)
    for s in steps:
        a = (s['start_location']['lat'], s['start_location']['lng'])
        b = (s['end_location']['lat'],   s['end_location']['lng'])
        graph[a].append((b, s['distance']['value']))
    return graph, decoded, legs['distance']['value'], legs['duration']['text']

def dijkstra(graph, start, end):
    heap = [(0, start)]
    dist = {start: 0}
    prev = {}
    while heap:
        cd, node = heapq.heappop(heap)
        if node == end: break
        for nbr, w in graph.get(node, []):
            nd = cd + w
            if nbr not in dist or nd < dist[nbr]:
                dist[nbr] = nd
                prev[nbr] = node
                heapq.heappush(heap, (nd, nbr))
    path = []
    cur = end
    while cur in prev:
        path.insert(0, cur)
        cur = prev[cur]
    if path:
        path.insert(0, start)
    return path, dist.get(end, float('inf'))

def find_closest_node(coord, graph):
    """
    Given a (lat,lng) tuple and a graph whose keys and neighbors
    are also (lat,lng) tuples, return the node nearest to coord.
    """
    # collect every node in the graph
    all_nodes = list(graph.keys()) + [
        nbr for neighbors in graph.values() for nbr, _ in neighbors
    ]
    # pick the one with minimum haversine distance
    return min(all_nodes, key=lambda node: haversine(coord, node))


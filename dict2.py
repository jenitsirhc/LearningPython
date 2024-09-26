map_dict = [

    {'start': 'a', 'end': 'b', 'length': 5, 'time': 55},

    {'start': 'a', 'end': 'c', 'length': 8, 'time': 125},

    {'start': 'b', 'end': 'd', 'length': 10, 'time': 130}

]



def create_graph_from_map(map_dict):

    """convert a dictionary of start/end information into a directed graph"""

    graph = {}

    for info in map_dict:

        start_city = info['start']

        if not start_city in graph:

            graph[start_city] = []

        edge = (info['end'], info['length'], info['time'])

        graph[start_city].append(edge)



    return graph



def show_edges(graph, start_city):

    for edge in graph[start_city]:

        end_city, length, travel_time = edge

        print(F"{start_city} -> {end_city}, length={length}, time={travel_time}")



# main

graph = create_graph_from_map(map_dict)

show_edges(graph, 'a')
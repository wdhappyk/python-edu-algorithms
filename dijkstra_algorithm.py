graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "a": {
        "fin": 1
    },
    "b": {
        "a": 3,
        "fin": 5
    },
    "fin": {}
}


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def search_short_way(graph, start):
    infinity = float("inf")
    costs = {}
    parents = {}

    for v in graph:
        parents[v] = None
        costs[v] = infinity
    for v in graph[start]:
        parents[v] = start
        costs[v] = graph[start][v]

    del costs[start]
    del parents[start]

    processed = []
    node = find_lowest_cost_node(costs, processed)

    if node is not None:
        print("-o- Select lowelest cost node is " + str(node))

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            print('-w- Watch path ' + node + ' - ' + n)
            new_cost = cost + neighbors[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
                print('-c- Set new cost for node ' + n + ': ' + str(new_cost))
                print('-p- Set new parent for node ' + n + ': ' + node)
        else:
            print('-np- No path from node ' + node)

        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

        if node is not None:
            print("-o- Select lowelest cost node is " + str(node))

    print("!!! Complete")

    print()
    print("Costs:")
    print(costs)
    print()
    print("Parents")
    print(parents)
    print()


search_short_way(graph, "start")

# for ex. 7.1

graphA = {
    "start": {
        "a": 5,
        "b": 2
    },
    "a": {
        "c": 4,
        "d": 2
    },
    "b": {
        "a": 8,
        "d": 7
    },
    "c": {
        "fin": 3,
        "d": 6
    },
    "d": {
        "fin": 1
    },
    "fin": {}
}

graphB = {
    "start": {
        "a": 10
    },
    "a": {
        "b": 20
    },
    "b": {
        "c": 1,
        "fin": 30
    },
    "c": {
        "a": 1
    },
    "fin": {}
}

graphC = {
    "start": {
        "a": 2,
        "b": 2
    },
    "a": {
        "b": 2,
        "c": -1
    },
    "b": {
        "c": 2,
        "fin": 2
    },
    "c": {
        "fin": 2
    },
    "fin": {}
}

print("---------------------------------")
search_short_way(graphA, "start")
print("---------------------------------")
search_short_way(graphB, "start")
print("---------------------------------")
search_short_way(graphC, "start")

graphD = {
    "start": {
        "a": 5,
        "b": 0
    },
    "a": {
        "b": -7
    },
    "b": {
        "fin": 35
    },
    "fin": {}
}

print("----ERROR------------------------")
search_short_way(graphD, "start")

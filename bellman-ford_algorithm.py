graph = {
    "start": {
        "a": 5,
        "b": 10
    },
    "a": {
        "c": 10
    },
    "b": {
        "c": 10
    },
    "c": {
        "d": 11,
        "g": -7,
        "e": -100
    },
    "d": {
        "fin": -7,
        "g": 0
    },
    "g": {
        "d": 0,
        "fin": 20
    },
    "e": {},
    "fin": {}
}


def bellman_ford(graph, start):
    infinity = float("inf")
    costs = {}
    parents = {}

    for v in graph:
        parents[v] = None
    for v in graph[start]:
        parents[v] = start

    del parents[start]

    for e in graph:
        costs[e] = infinity
    costs[start] = 0

    for i in range(1, len(graph) - 1):
        count = 0
        for v in graph:
            print('-?- Watch V: ' + v)
            for e in graph[v].keys():
                print('--?- Watch E: ' + v + '-' + e)
                new_cost = graph[v][e] + costs[v]
                if costs[e] > new_cost:
                    count += 1
                    print('---C- Set new cost E(' + v + ', ' + e + '): ' + str(new_cost))
                    costs[e] = new_cost
                    parents[e] = v
                    if costs[e] + costs[v] < graph[v][e]:
                        print('-NEGATIVE- Detected negative cycle E(' + v + ', ' + e + ')')
                        return
        if count == 0:
            break

    print(costs)
    print(parents)


bellman_ford(graph, "start")

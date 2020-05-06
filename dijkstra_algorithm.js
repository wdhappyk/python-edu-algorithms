const graph = {
    'a': {
        'b': 3,
        'c': 5,
    },
    'b': {
        'd': 4,
    },
    'c': {
        'd': 1,
    },
    'd': {
        'e': 3,
        'j': 1,
    },
    'e': {
        'f': 2,
    },
    'j': {
        'e': 1,
    },
};

function getShortPathSize(graph, start, finish) {
    const costs = {};

    function _helper(targetV) {
        const cost = costs[targetV] || 0;
        for (const v in graph[targetV]) {
            const c = cost + graph[targetV][v];
            if (costs[v] === undefined || c < costs[v]) costs[v] = c;

            _helper(v);
        }
    }

    _helper(start);

    return costs[finish];
}

console.log(`Short path: ${getShortPathSize(graph, 'a', 'f')}`);
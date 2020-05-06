graph = {
    'you': ['alice', 'bob', 'kler'],
    'alice': ['peggi'],
    'bob': ['anuj', 'peggi'],
    'kler': ['tom', 'jonny'],
    'peggi': ['anjela'],
    'anuj': [],
    'tom': [],
    'jonny': [],
    'anjela': []
}

sellers = ['anjela', 'tom']


def search(name):
    search_queue = []
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.pop(0)

        if not person in searched:
            print('? check person ' + person)

            if person_is_seller(person):
                print('!!! ' + person + ' is a mango seller!')
                return True
            else:
                print('- ' + person + ' is not a mango seller =(')

                search_queue += graph[person]
                searched.append(person)

                if len(graph[person]):
                    print('+ add to search list: ' + ', '.join(graph[person]))

    return False


def search_short_way(name):
    search_queue = []
    search_queue += graph[name]
    searched = []

    short_way = 1
    steps = 0
    next_steps = [len(graph[name]), 0]

    while search_queue:
        if steps >= next_steps[0]:
            print('*** next level')
            short_way += 1
            next_steps[0] = next_steps[1]
            next_steps[1] = 0
            steps = 0

        steps += 1

        person = search_queue.pop(0)

        if not person in searched:
            print('? check person ' + person)

            if person_is_seller(person):
                print('!!! ' + person + ' is a mango seller!')
                return short_way
            else:
                print('- ' + person + ' is not a mango seller =(')

                search_queue += graph[person]
                searched.append(person)
                next_steps[1] += len(graph[person])

                if len(graph[person]):
                    print('+ add to search list: ' + ', '.join(graph[person]))

    return None


def person_is_seller(name):
    return name in sellers


search('you')
print()
print('~~~ Short way is ' + str(search_short_way('you')) + ' steps')

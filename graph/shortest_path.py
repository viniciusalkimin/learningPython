from collections import deque

graph = {}

graph["I"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Thom", "Jonny"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Jonny"] = []
graph["Thom"] = []


def search_shortest_path(name):
    search_queue = deque()
    search_queue += graph[name]
    verified = []
    while search_queue:
        person = search_queue.popleft()
        if not person in verified:
            if is_mango_seller(person):
                print(person + " is a mango saller!")
                return True
            else:
                search_queue += graph[person]
                verified.append(person)
    return False


def is_mango_seller(name):
    return name[-1] == "m"


search_shortest_path("I")
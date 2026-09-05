# import shlex

# def load_city(path, mode):
#     cities = []

#     with open(path, mode, encoding="utf-8") as file:
#         for line in file:
#             parts = shlex.split(line.strip())

#             city = parts[0]
#             lat = float(parts[1])
#             lon = float(parts[2])

#             cities.append((city, lat, lon))

#     return cities

def load_city(path, mode):
    cities = []

    with open(path, mode, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()

            city = " ".join(parts[:-2]).strip('"')
            lat = float(parts[-2])
            lon = float(parts[-1])

            cities.append((city, lat, lon))

    return cities


def compterOccurrences(elem, text):
    count = 0

    for i in text:
        if i.lower() == elem.lower():
            count += 1

    return count


def frequency(text):
    tab = {}

    for x in text:
        key = x.lower()

        if key not in tab:
            tab[key] = compterOccurrences(x, text)

    return tab


list_city = load_city("City.txt", "r")

city = []

for i in list_city:
    city.append(i[0])


def distance(cityA, cityB):
    dist = ((cityB[1] - cityA[1])**2 + (cityB[2] - cityA[2])**2) ** 0.5

    return round(dist, 2)


def itinerary_greedy(start_city, cities):
    '''
    this is a approche that goes from the first city and then scans
    all the cities for the closest one
    this is bad for larger city data since i go from one to all
    then i do the same treatment again
    (1 to N then 1 to N )
    effectively N to N problem.
    '''
    visited_cities = []
    current_city = start_city
    visited_cities.append(start_city)

    while len(visited_cities) < len(cities):
        nearest_city = None
        nearest_distance = None

        for i in cities:
            if i not in visited_cities:
                dist = distance(i, current_city)

                if nearest_distance is None or dist < nearest_distance:
                    nearest_distance = dist
                    nearest_city = i

        visited_cities.append(nearest_city)
        current_city = nearest_city

    return visited_cities


def total_distance(route):
    total = 0

    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])

    return round(total, 2)


route = itinerary_greedy(list_city[9], list_city)
distance_total = total_distance(route)


print("----------------------------")
print("Total number of cities:", len(list_city))
print("----------------------------")
print("Route found:", " -> ".join(city[0] for city in route))
print("----------------------------")
print("Total distance:", distance_total)

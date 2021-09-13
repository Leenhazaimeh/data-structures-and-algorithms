def business_trip(name, list):

    city = False
    city_two = False
    cost = 0

    for cGraph in len(list):
        edges = name._adjacency_list[list[cGraph]]
        city_two = False

        for edge in edges:
            if list[cGraph + 1] == edge.node:
                cost += edge.weight
                city = True
                city_two = True

    city = city and city_two
  
    if not city:
        cost = 0
        city = False
        return f"{city},${cost}"

    return f"{city},${cost}"

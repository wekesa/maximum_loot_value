# A Dynamic Programming based Python Program
# Returns the maximum value that can be put in a knapsack of capacity W


# An optimized solution that has a time complexity of O(N*W)
def knap_sack(weight_limit, items, number_of_items):
    K = [[0 for x in range(weight_limit + 1)] for x in range(number_of_items + 1)]

    # Build table K[][] in bottom up manner
    for item in range(number_of_items + 1):
        for weight in range(weight_limit + 1):
            if item == 0 or weight == 0:
                K[item][weight] = 0
            elif items[item - 1]["weight"] <= weight:
                K[item][weight] = max(items[item - 1]["value"] +
                                      K[item - 1][weight - items[item - 1]["weight"]], K[item - 1][weight])
            else:
                K[item][weight] = K[item - 1][weight]

    return K[number_of_items][weight_limit]


# To test above function
if __name__ == '__main__':
    sample_items = [
        {"weight": 5, "value": 10},
        {"weight": 4, "value": 40},
        {"weight": 6, "value": 30},
        {"weight": 4, "value": 50}
    ]
    knap_sack_limit = 10
    items_length = len(sample_items)
    print(knap_sack(knap_sack_limit, sample_items, items_length))

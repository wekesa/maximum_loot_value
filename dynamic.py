# A Dynamic Programming based Python Program
# Returns the maximum value that can be put in a knapsack of capacity W
items = [
{ "weight": 5, "value": 10 },
{ "weight": 4, "value": 40 },
{ "weight": 6, "value": 30 },
{ "weight": 4, "value": 50 }
]


def knapSack(W, items, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif items[i - 1]["weight"] <= w:
                K[i][w] = max(items[i - 1]["value"] + K[i - 1][w - items[i - 1]["weight"]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


# To test above function
if __name__ == '__main__':
    knap_sack_limit = 10
    items_length = len(items)
    print(knapSack(knap_sack_limit, items, items_length))

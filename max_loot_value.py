# Returns the maximum value that can be put in a knapsack of

items = [
{ "weight": 5, "value": 10 },
{ "weight": 4, "value": 40 },
{ "weight": 6, "value": 30 },
{ "weight": 4, "value": 50 }
]


def knapSack(weight_limit, items, n):
    # Base Case
    if n == 0 or weight_limit == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if items[n - 1]["weight"] > weight_limit:
        return knapSack(weight_limit, items, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(items[n - 1]["value"] + knapSack(weight_limit - items[n - 1]["weight"], items, n - 1),
                   knapSack(weight_limit, items, n - 1))

    # end of function knapSack


# To test above function
if __name__ == '__main__':
    knap_sack_limit = 10
    items_length = len(items)
    print(knapSack(knap_sack_limit, items, items_length))

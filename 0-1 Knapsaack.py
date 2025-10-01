# 演算法分析機測
# 學號: 11127115 / 11127127 / 11127148
# 姓名: 陳姿安 / 陳沛君 / 劉梓萱
# 中原大學資訊工程系

import time

# ========== read_input() ==========
def read_input():
    W = int(input())            # read total weight package can load
    num_of_items = int(input()) # read total have how many items
    items = []

    # get items
    for i in range(num_of_items):
        item = dict()
        weight_value = input().split()
        item['weight'] = int(weight_value[0])   # set weight of item
        item['value'] = int(weight_value[1])    # set value of item
        items.append(item)                      # put item in list

    return W, num_of_items, items

# ========== knapsack() ==========
def knapsack(W, num_of_items, items):
    take_item = list()

    # create a table which use to record maximum total value for item i
    c = [[0 for col in range(W+1)]for row in range(num_of_items+1)] 

    for i in range(1, num_of_items+1):
        weight = items[i-1]['weight']
        value = items[i-1]['value']

        for w in range(1, W+1):
            # if the weight of item is larger than the weight package can load-> keep package state as same as previous take
            if weight > w:
                c[i][w] = c[i-1][w]
            else:
                c[i][w] = max(c[i-1][w], value + c[i-1][w-weight])
    
    w = W
    for i in range(num_of_items, 0, -1):
        # if c[i][w] != c[i][w] -> means there is a item been take
        if c[i][w] != c[i-1][w]:
            take_item.insert(0, i)
            w = w - items[i-1]['weight']

    return c[num_of_items][W], take_item

# ========== print_ans ==========
def print_ans(total_value, take_item):
    print('Total Value =', total_value )    # print total value of taken item

    # print take item
    if len(take_item) > 0:
        print('Take Items ', end = '')

        for i in range(len(take_item)):
            print( take_item[i], end = '')
            if i != len(take_item) - 1 :
                print(', ', end = '' )

# ========== main ==========
def main():

    start = time.time()

    W, num_of_items, items = read_input()
    if num_of_items > 0 :
        total_value, take_item = knapsack(W, num_of_items, items)
    else:
        total_value = 0
        take_item = []

    print_ans(total_value, take_item)

    end = time.time() - start
    # print("\n",end)

main()
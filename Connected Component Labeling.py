# 演算法分析機測
# 學號: 11127115 / 11127127 / 11127148
# 姓名: 陳姿安 / 陳沛君 / 劉梓萱
# 中原大學資訊工程系

def read():
    # read the number of column and line in the image
    line_column = input().split()
    line_num = int(line_column[0])
    column_num = int(line_column[1])
    list = []

    # read image in and store it in list
    for i in range(line_num):
        line = input()
        list.append(line)

    return line_num, column_num, list

def find( line, column, list ):
    connected = {}
    pixel = {}
    
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == "1":
                # See if adjacent points are connected elements
                # pixel -> Record each point and its corresponding connected element
                pixel = check_column( list, i, j, pixel )
                
                # connected -> Record the starting point of each connected element and
                #           -> the points contained in the connected element
                connected.setdefault(str(pixel[str([i, j])]),[]).append([i, j])
                
    return connected

def check_column( list, line, column, pixel ):
    value = []

    # Check if there is a connected element in the previous row
    if line - 1 >= 0:
        if str([line-1, column]) in pixel:
            value = pixel[str([line-1, column])]
        elif str([line-1, column - 1]) in pixel:
            value = pixel[str([line-1, column-1])]
        elif str([line-1, column + 1]) in pixel:
            value = pixel[str([line-1, column+1])]

    # Check whether the previous element in the same row is a connected element
    if len(value) == 0:
        if str([line, column-1]) in pixel:
            value = pixel[str([line, column-1])]
        else:
            value = [line, column]

    pixel[str([line, column])] = value
    return pixel

def print_result(component):
    for key in component:
        
        print( "\nImage #" + str(key) )
        if len(component[key]) == 1 and component[key][0] == 0:
            print( "Number of Connected Components = " + str(0) )
        else:
            print( "Number of Connected Components = " + str(len(component[key])) )
    
        for index in range(len(component[key])):
            print( "Connected Component #" + str(index + 1) + " Area = " + str(component[key][index]) )

        print()
    
def main():
    image_num = 0
    image_component = []
    component = {}
    
    line, column, list = read()
    while line != 0 and column != 0:
        image_num = image_num + 1
        connected = find(line, column, list)
        
        if len(connected) == 0:
            component[image_num] = [0]
        else:
            for key in connected:
                component.setdefault(image_num,[]).append(len(connected[key]))

        line, column, list = read()

    print_result(component)
    
main()

'''
10 10
0000000000
0010001100
0110010010
0010000010
0010000100
0010001000
0010010000
0111011110
0000000000
0000000000
8 5
00001
00011
00111
00000
11001
11001
10000
00000
0 0
'''

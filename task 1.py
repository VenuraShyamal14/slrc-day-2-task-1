#there is a grid 4x3 (4 rows, 3 colomns)
#some squares has box 
#there is a line to follow. line does not cross a square
#need to follow the line and need to count how much boxes in the arena

array = [[0 for j in range(3)] for i in range(4)]

def print_array(array_2d):
    for row in array_2d:
        for elem in row:
            print(elem, end=' ')
        print()  # print a newline after each row

print_array(array)

start_x=
start_y
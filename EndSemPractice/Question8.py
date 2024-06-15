'''Given an array of pairs of integers as a point in the cartesian co-ordinate, find its respective pair/pairs  which forms horizontal and vertical line with respect to its pair
For example,
Input: {3, 4}, {5, 10}, {5, 4}, {7, 10}, {7, 3}, {3,2} ,{10,4}
 
 
Output:
{3,4} - Horizonal line pair-{5,4} {10,4}
           Vertical line pair-{3,2}
{5,10}-Horizontal line pair- {5,4}
           Vertical line pair-{7,10}'''


def func(s):
    vertical_line={}
    horizontal_line={}
    for point in s:
        i,j = point

        if i in vertical_line:
            vertical_line[i].append(point)
        else:
            vertical_line[i]=[point]

        if j in horizontal_line:
            horizontal_line[j].append(point)
        else:
            horizontal_line[j]=[point]

    print(horizontal_line)
    print(vertical_line)

    for i in horizontal_line.values():
        for j in i:
            print(f'Horizontal values of {j} is {i}')

    for i in vertical_line.values():
        for j in i:
            print(f"Vertical values of {j} is {i}")


s=[(3, 4),(5, 10),(5, 4),(7, 10),(7, 3),(3,2),(10,4)]
func(s)

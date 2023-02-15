from naiveImplementation import getNaiveLongestStraightLine

input0 = [7, 0, 20, 40, 0, 40, 20, 70, 50, 50, 70, 30, 50, 0, 50]
output0 = 76.157731059
input1 = [3, 0, 2017, -2017, -2017, 2017, 0]
output1 = 4510.149110617

input2 = [7, 0, 0, 0, 2, 1, 3, 4, 3, 6, 0, 4, 2, 2, 2]

delta = 10 ** -6

assert abs(getNaiveLongestStraightLine(input0) - output0) < delta
assert abs(getNaiveLongestStraightLine(input1) - output1) < delta
getNaiveLongestStraightLine(input2)
# Write a function point_position_relative_to_line(a, b, c, x, y) -> int that determines the position of a point (x, y) with respect to a line described by the equation ax + by + c = 0.

# The function should return:

# +1 if the point is above the line
# -1 if the point is below the line
# 0 if the point is on the line
# Note:

# A point (x, y) is considered on the line if substituting x and y into the equation results in 0.
# A point is above the line if the value of ax + by + c > 0 and below the line if ax + by + c < 0.
# Example

# >>> point_position_relative_to_line(1, -1, 0, 2, 1)
# 1
# >>> point_position_relative_to_line(-1, -1, -1, 0, 0)
# -1
# >>> point_position_relative_to_line(2, -1, -4, 2, 0)
# 0

def point_position_relative_to_line(a, b, c, x, y):
    equation = a*x + b*y + c 
    if equation == 0:
        return 0 
    elif equation>0:
        return 1
    elif equation<0:
        return -1
print(point_position_relative_to_line(1, -1, 0, 2, 1))
# 1
print(point_position_relative_to_line(-1, -1, -1, 0, 0))
# -1
print(point_position_relative_to_line(2, -1, -4, 2, 0))
# 0

# https://www.codewars.com/kata/5a58ca28e626c55ae000018a
# Level 6kyu

## Directions ##

# Write the following function:
#
# def area_of_polygon_inside_circle(circle_radius, number_of_sides):
# It should calculate the area of a regular polygon of number_of_sides sides
# inside a circle of circle_radius which passes through all the vertices of the polygon
# (such circle is called circumscribed circle or circumcircle).
# The answer should be a number rounded to 3 decimal places.
#
# Input :: Output Examples
#
# area_of_polygon_inside_circle(3, 3) # returns 11.691
#
# area_of_polygon_inside_circle(5.8, 7) # returns 92.053
#
# area_of_polygon_inside_circle(4, 5) # returns 38.042

## Function ##
import math

def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    # find the angle of the triangle
    tri_angle = 360/number_of_sides
    polygon_side = circle_radius*math.sin(math.radians(tri_angle/2)) * 2
    polygon_height = circle_radius*math.cos(math.radians(tri_angle/2))
    area_of_tri = polygon_height * polygon_side / 2
    total_area_poloygon = area_of_tri * number_of_sides
    print(round(total_area_poloygon, 3))
    return round(total_area_poloygon, 3)

## Test Cases ##

area_of_polygon_inside_circle(3, 3) # => 11.691
area_of_polygon_inside_circle(2, 4) # => 8
area_of_polygon_inside_circle(2.5, 5) # => 14.86
# area_of_polygon_inside_circle(8, 5)

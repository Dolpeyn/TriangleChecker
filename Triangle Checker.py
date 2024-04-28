import math

def is_triangle_valid(side_lengths, angle_measurements): # Checks if the given side lengths and angle measurements form a valid triangle.
    if any(side <= 0 for side in side_lengths): # Check if all sides are positive
        print("Invalid triangle: At least one side length is non-positive.")
        return False
    if abs(sum(angle_measurements) - 180) > 1e-6: # Check if the sum of angles is approximately 180 degrees
        print("Invalid triangle: Sum of angles is not approximately 180 degrees.")
        print(sum(angle_measurements) - 180)
        return False
    a, b, c = sorted(side_lengths) # Check the triangle inequality theorem
    if a + b <= c:
        print("Invalid triangle: Triangle inequality theorem is violated.")
        return False
    return True

def triangle_type(side_lengths, angle_measurements): # Determines the type of triangle based on its side lengths and angle measurements.
    a, b, c = sorted(side_lengths)
    if a == b == c: # Check for equilateral triangle
        return "Equilateral"
    if a == b or b == c: # Check for isosceles triangle
        return "Isosceles"
    if any(angle == 90 for angle in angle_measurements): # Check for right triangle
        return "Right"
    return "Scalene" # If none of the above, it's a scalene triangle

def compare_triangles(triangles): # Compares a list of triangles.
    for i, triangle in enumerate(triangles, start=1):
        side_lengths, angle_measurements = triangle
        print(f"Triangle {i} with measurements Sides: {side_lengths} and Angles: {angle_measurements}: ")
        if is_triangle_valid(side_lengths, angle_measurements): # Check if the triangle is valid
            print("Triangle is valid.")
        else:
            print("Triangle is not valid.\n")
            continue
        # print("Triangle type:", triangle_type(side_lengths, angle_measurements)) # Check the type of triangle
        print()  # Print a blank line for clarity

# Inputs
triangles = [
    ([10, 8, 15], [112.41, 29.54, 38.05]),  # first is sides list then angles list
    ([10, 8, 15], [67.58, 29.54, 82.88]), 
    ([10, 17.86, 25], [121.23, 20, 38.77]),
    ([10, 28.675, 25], [58.77, 20, 101.23]),
]

compare_triangles(triangles)
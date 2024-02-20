import math

def calculate_distance(absolute_magnitude, apparent_magnitude):
    distance_in_parsecs = 10 * math.pow(10, (apparent_magnitude - absolute_magnitude) / 5)
    return distance_in_parsecs

absolute_magnitude = float(input("Enter the absolute magnitude of the star: "))
apparent_magnitude = float(input("Enter the absolute magnitude of the star: "))

distance = calculate_distance(absolute_magnitude, apparent_magnitude)

print("The distance to the star in parsecs is: ", distance)
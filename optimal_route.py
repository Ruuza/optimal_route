import sys
import getopt

import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.distances import great_circle_distance_matrix

from src.city import City


def print_help():
    print(
        "Finds the optimal route, so each city is visited only once and "
        "returns to the starting location. The starting location is determined by the first city in the input file\n"
    )
    print("usage: optimal_route -i <inputfile>")
    print("\nFormat example of the input file:")
    print(
        """
    {
        "Brno": [
            "49.19564",
            "16.60895"
        ],
        "Jihlava": [
            "49.39933",
            "15.58344"
        ]
    }
          """
    )


def arg_handler(argv: list) -> str:
    """parse the input file from the args or print help"""
    input_file = ""

    try:
        opts, args = getopt.getopt(argv, "hi:", [])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print_help()
            sys.exit()
        elif opt == "-i":
            input_file = arg

    if not input_file:
        print("Input file is requiered!")
        print_help()
        sys.exit(2)

    return input_file


def main(argv):

    input_file = arg_handler(argv)

    # Parse the cities from the given json file
    cities: list["City"] = City.load_cities(from_json_file=input_file)

    # Calculate the distance matrix
    sources = np.array([[city.latitude, city.longtitude] for city in cities])
    distance_matrix = great_circle_distance_matrix(sources)

    # Solve the traveling salesman problem
    permutation, distance = solve_tsp_dynamic_programming(distance_matrix)

    last_x = 0
    print("The optimal order to visit the cities is:")
    for i, x in enumerate(permutation):
        print(f"{i+1}. {cities[x].name} - {round(distance_matrix[x][last_x])} meters")
        last_x = x
    print(f"{i+2}. {cities[0].name} - {round(distance_matrix[0][last_x])} meters")

    print(f"\nThe total distance is: {round(distance)} meters")


if __name__ == "__main__":
    main(sys.argv[1:])

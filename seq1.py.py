#Given two points, the formula for computing the distance is √(𝑥2 − 𝑥1)2 + (𝑦2 − 𝑦1)2
#you can use a ** 0.5 to compute √𝑎 . The program should prompts the user to enter 
#two points and computes the distance between them.

def validate_data(value):
    try:
        if not value:
            raise ValueError("Input cannot be empty.")
        if value.isalpha():
            raise ValueError("Input must be a number.")
        return float(value)
    except ValueError as e:
        print(f"Error: {e}")
        return None


def get_data(label):
    while True:
        user_input = input(f"Enter {label}: ")
        validated = validate_data(user_input)
        if validated is not None:
            return validated


def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def run_distance_program():
    print("Enter coordinates for the first point:")
    x1 = get_data("x1")
    y1 = get_data("y1")

    print("\nEnter coordinates for the second point:")
    x2 = get_data("x2")
    y2 = get_data("y2")

    distance = calculate_distance(x1, y1, x2, y2)
    print(f"\nThe distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")


if __name__ == "__main__":
    run_distance_program()



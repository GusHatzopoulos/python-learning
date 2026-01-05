CONVERSION_FACTOR = 1.60934

def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers."""
    return round(miles * CONVERSION_FACTOR, 2)


def kilometers_to_miles(kilometers: float) -> float:
    """Convert kilometers to miles."""
    return round(kilometers / CONVERSION_FACTOR, 2)


def main():
    print("Distance Converter")
    print("------------------")
    print("1. Miles to Kilometers")
    print("2. Kilometers to Miles")

    choice = input("Choose an option (1 or 2): ").strip()

    try:
        if choice == "1":
            miles = float(input("Enter miles: "))
            kilometers = miles_to_kilometers(miles)
            print(f"{miles} miles is equal to {kilometers} kilometers.")

        elif choice == "2":
            kilometers = float(input("Enter kilometers: "))
            miles = kilometers_to_miles(kilometers)
            print(f"{kilometers} kilometers is equal to {miles} miles.")

        else:
            print("Invalid choice. Please select 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    main()

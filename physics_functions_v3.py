GRAVITY = 9.8  # m/s²


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def potential_energy():
    mass = get_number("Enter mass (in Kg): ")
    height = get_number("Enter height (in meters): ")
    print("Potential Energy =", mass * GRAVITY * height, "J")


def wave_speed():
    frequency = get_number("Enter frequency (in Hz): ")
    wavelength = get_number("Enter wavelength (in meters): ")
    print("Wave Speed =", frequency * wavelength, "m/s")


def electric_charge():
    current = get_number("Enter current (in A): ")
    time = get_number("Enter time (in seconds): ")
    print("Charge =", current * time, "C")


def electric_power():
    voltage = get_number("Enter voltage (in V): ")
    current = get_number("Enter current (in A): ")
    print("Electrical Power =", voltage * current, "W")


def weight():
    mass = get_number("Enter mass (in Kg): ")
    print("Weight =", mass * GRAVITY, "N")


operations = {
    "A": potential_energy,
    "B": wave_speed,
    "C": electric_charge,
    "D": electric_power,
    "E": weight,
}


def show_menu():
    print("\nSelect a Physics formula")
    print("A. Potential Energy (PE = m * g * h)")
    print("B. Wave Speed (v = f * λ)")
    print("C. Electric Charge (Q = I * t)")
    print("D. Electrical Power (P = V * I)")
    print("E. Weight (W = m * g)")


while True:
    show_menu()
    user_choice = input("Enter a letter A-E: ").strip().upper()

    if user_choice in operations:
        operations[user_choice]()
    else:
        print("Invalid choice. Please choose from A to E.")
        continue

    again = input("\nDo you want to run another operation? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break

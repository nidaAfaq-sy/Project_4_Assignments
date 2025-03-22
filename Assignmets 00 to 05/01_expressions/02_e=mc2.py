C: int = 299_792_458  # Speed of light in m/s

def main():
    mass_in_kg = float(input("Enter mass in kg: "))

    # Calculate energy (E = mc²)
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display the results
    print("\nEnergy Calculation (E = mc²):")
    print(f"Mass (m): {mass_in_kg} kg")
    print(f"Speed of Light (C): {C} m/s")
    print(f"Energy (E): {energy_in_joules:.2f} joules")  # Two decimal places

if __name__ == '__main__':
    main()

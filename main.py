from math import gcd

def parse_feet_inches(input_str):
    """
    Parses a measurement string like "15' 9 7/16\"" into feet as a float.
    Handles feet, inches, and fractional inches accurately.
    """
    feet = 0
    inches = 0
    fraction = 0.0

    # Remove any extra quotes and special quotation marks
    input_str = input_str.replace('"', '').replace('”', '').replace('“', '')

    # Split the input into parts
    parts = input_str.split()
    for part in parts:
        if part.endswith("'"):  # Extract feet
            feet = int(part.rstrip("'"))
            print(f"DEBUG: Extracted feet = {feet}")
        elif '/' in part:  # Extract fraction
            try:
                num, denom = map(int, part.split('/'))
                fraction = num / denom
                print(f"DEBUG: Extracted fraction = {fraction:.6f}")
            except ValueError:
                continue  # Skip invalid fractions
        elif part.isdigit():  # Extract inches
            inches = int(part)
            print(f"DEBUG: Extracted inches = {inches}")
        else:
            continue  # Ignore other parts

    # Combine feet, inches, and fraction into total feet
    total_feet = feet + (inches + fraction) / 12
    print(f"DEBUG: Combined total feet = {total_feet:.6f}")
    return total_feet


def convert_to_feet_inches(value):
    """
    Converts a decimal feet value into feet, inches, and fractional inches.
    """
    feet, fractional_feet = divmod(value, 1)  # Separate feet and fractional part
    inches, fractional_inches = divmod(fractional_feet * 12, 1)  # Convert fractional feet to inches

    # Convert remaining fraction to numerator and denominator
    numerator = fractional_inches * 8
    denominator = 8

    # Reduce the fraction to its simplest form
    common_divisor = gcd(int(numerator), denominator)
    numerator = int(numerator / common_divisor)
    denominator = int(denominator / common_divisor)

    return int(feet), int(inches), numerator, denominator


def calculate_radius():
    print("Circle Radius Calculator (Feet and Inches)")

    # Get user inputs
    uv_str = input("Enter the distance between U and V (chord length, e.g., 15' 9 7/16\"): ")
    h_str = input("Enter the perpendicular distance from the chord to the edge (e.g., 4'): ")

    # Parse inputs
    chord_length = parse_feet_inches(uv_str)  # ℓ = chord length
    h = parse_feet_inches(h_str)              # h = perpendicular height

    print(f"DEBUG: Chord length (ℓ) = {chord_length:.6f} feet, Height (h) = {h:.6f} feet.")

    # Apply the formula for radius
    radius = (4 * h**2 + chord_length**2) / (8 * h)
    print(f"DEBUG: Calculated radius (r) = {radius:.6f} feet.")

    # Convert radius to feet and inches
    feet, inches, numerator, denominator = convert_to_feet_inches(radius)

    # Display the result
    print(f"The radius of the circle is approximately: {feet} feet, {inches} inches, and {numerator}/{denominator} inches.")


# Run the calculator
calculate_radius()

# Define a function to convert inches to centimeters
def convert_inches_to_centimeters(inches):
  return inches * 2.54

# Define a function to convert centimeters to inches
def convert_centimeters_to_inches(centimeters):
  return centimeters / 2.54

# Define a function to convert feet to meters
def convert_feet_to_meters(feet):
  return feet * 0.3048

# Define a function to convert meters to feet
def convert_meters_to_feet(meters):
  return meters / 0.3048

# Define a function to convert pounds to kilograms
def convert_pounds_to_kilograms(pounds):
  return pounds * 0.453592

# Define a function to convert kilograms to pounds
def convert_kilograms_to_pounds(kilograms):
  return kilograms / 0.453592

# Define the main function
def main():
  # Print a welcome message and the available conversion options
  print("Welcome to the measurement converter app!")
  print("Please select a conversion:")
  print("1. Inches to centimeters")
  print("2. Centimeters to inches")
  print("3. Feet to meters")
  print("4. Meters to feet")
  print("5. Pounds to kilograms")
  print("6. Kilograms to pounds")


# you as many conversion options as possible
  # Get the user's choice of conversion
  choice = int(input())

  # Perform the selected conversion and print the result
  if choice == 1:
    inches = float(input("Enter the number of inches: "))
    result = convert_inches_to_centimeters(inches)
    print(f"{inches} inches is equal to {result} centimeters.")
  elif choice == 2:
    centimeters = float(input("Enter the number of centimeters: "))
    result = convert_centimeters_to_inches(centimeters)
    print(f"{centimeters} centimeters is equal to {result} inches.")
  elif choice == 3:
    feet = float(input("Enter the number of feet: "))
    result = convert_feet_to_meters(feet)
    print(f"{feet} feet is equal to {result} meters.")
  elif choice == 4:
    meters = float(input("Enter the number of meters: "))
    result = convert_meters_to_feet(meters)
    print(f"{meters} meters is equal to {result} feet.")
  elif choice == 5:
    pounds = float(input("Enter the number of pounds: "))
    result = convert_pounds_to_kilograms(pounds)
    print(f"{pounds} pounds is equal to {result} kilograms.")
  elif choice == 6:
    kilograms = float(input("Enter the number of kilograms: "))
    result = convert_kilograms_to_pounds(kilograms)
    print(f"{kilograms} kilograms is equal to {result} pounds.")

# Call the main function if this script is run as the main program
if __name__ == "__main__":
  main()
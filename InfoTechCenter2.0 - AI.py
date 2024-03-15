import random
from time import sleep

# Function to randomly determine the gas level
def gas_level_gauge():
    # List of possible gas levels
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly select a gas level
    return random.choice(gas_level_list)

# Function to randomly select a gas station
def list_of_gas_stations():
    # List of gas stations
    gas_stations = ["Shell", "Speedway", "Marathon", "Circle K", "Mobile", "Costco", "Meijer", "7Eleven"]
    # Randomly select a gas station
    return random.choice(gas_stations)

# Function to alert the user based on gas level
def gas_level_alert():
    # Randomly determine distances to gas stations for different gas levels
    miles_to_gas_stations_low = round(random.uniform(1, 25), 1)
    miles_to_gas_stations_quarter_tank = round(random.uniform(25.1, 50), 1)
    # Get the current gas level
    gas_level_indicator = gas_level_gauge()

    # Check the gas level and provide appropriate alert
    if gas_level_indicator == "Empty":
        # Warn the user about being empty and call AAA
        print("***Warning - YOU ARE EMPTY***")
        sleep(2.5)
        print("***Calling Triple AAA***")
    elif gas_level_indicator == "Low":
        # Inform the user about low gas level and find the nearest gas station
        print("Your gas tank is extremely low.")
        print(f"Checking Google Maps for the closest gas station...")
        sleep(2.5)
        print(f"The closest gas station is {list_of_gas_stations()}, which is {miles_to_gas_stations_low} miles away.")
    elif gas_level_indicator == "Quarter Tank":
        # Inform the user about quarter tank level and find the nearest gas station
        print("Your gas tank is on a quarter tank.")
        print(f"Checking Google Maps for the closest gas station...")
        sleep(2.5)
        print(f"The closest gas station is {list_of_gas_stations()}, which is {miles_to_gas_stations_quarter_tank} miles away.")
    elif gas_level_indicator == "Half Tank":
        # Inform the user about half tank level
        print("Your gas tank is half full which is plenty to get to your destination.")
    elif gas_level_indicator == "Three Quarter Tank":
        # Inform the user about three quarter tank level
        print("Your gas tank is at three quarter tank full.")
    else:
        # Inform the user about full tank level
        print("Your gas tank is full - hooray!")

# Call the function to start the alert system
gas_level_alert()

import random
from time import sleep

def gas_level_gauge():
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gas_level_list)

def list_of_gas_stations():
    gas_stations = ["Shell", "Speedway", "Marathon", "Circle K", "Mobile", "Costco", "Meijer", "7Eleven"]
    return random.choice(gas_stations)

def gas_level_alert():
    miles_to_gas_stations_low = round(random.uniform(1, 25), 1)
    miles_to_gas_stations_quarter_tank = round(random.uniform(25.1, 50), 1)
    gas_level_indicator = gas_level_gauge()

    if gas_level_indicator == "Empty":
        print("***Warning - YOU ARE EMPTY***")
        sleep(2.5)
        print("***Calling Triple AAA***")
    elif gas_level_indicator == "Low":
        print("Your gas tank is extremely low.")
        print(f"Checking Google Maps for the closest gas station...")
        sleep(2.5)
        print(f"The closest gas station is {list_of_gas_stations()}, which is {miles_to_gas_stations_low} miles away.")
    elif gas_level_indicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank.")
        print(f"Checking Google Maps for the closest gas station...")
        sleep(2.5)
        print(f"The closest gas station is {list_of_gas_stations()}, which is {miles_to_gas_stations_quarter_tank} miles away.")
    elif gas_level_indicator == "Half Tank":
        print("Your gas tank is half full which is plenty to get to your destination.")
    elif gas_level_indicator == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank full.")
    else:
        print("Your gas tank is full - hooray!")

gas_level_alert()

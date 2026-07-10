import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker("en_IN")


cities = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Chennai",
    "Pune"
]

vehicle_types = [
    "Car",
    "Bike",
    "Bus"
]

charger_types = [
    "Fast",
    "Normal",
    "Ultra Fast"
]

weather_conditions = [
    "Sunny",
    "Cloudy",
    "Rainy"
]


#this is used to generate data each time Every time we call it:
#generate_record()
#it gives us one brand new charging session.


def generate_record():

    station_id = f"ST{random.randint(1,100):03}"
    vehicle_id = f"EV{random.randint(1000,9999)}"

    vehicle_type = random.choice(vehicle_types)
    city = random.choice(cities)
    charger_type = random.choice(charger_types)
    weather = random.choice(weather_conditions)

    battery_start = random.randint(10,70)
    battery_end = random.randint(battery_start + 10,100)
    energy_consumed = round((battery_end - battery_start) * 0.5, 2)
    charging_duration = round(energy_consumed / 7, 2)
    charging_cost = round(energy_consumed * 12, 2)
    waiting_time = random.randint(0,30)

    temperature = random.randint(20,42)


    # fake datetime

    timestamp = fake.date_time_between(
    start_date="-30d",
    end_date="now"
)
    
     # Then Peak/Off-Peak

    if 8 <= timestamp.hour <= 20:
        peak_offpeak = "Peak"
    else:
        peak_offpeak = "Off-Peak"

    return {
    "Station_ID": station_id,
    "Vehicle_ID": vehicle_id,
    "Vehicle_Type": vehicle_type,
    "City": city,
    "Charger_Type": charger_type,
    "Weather": weather,
    "Battery_Start": battery_start,
    "Battery_End": battery_end,
    "Temperature": temperature,
    "Energy_Consumed": energy_consumed,
    "Charging_Duration": charging_duration,
    "Charging_Cost": charging_cost,
    "Waiting_Time": waiting_time,
    "Timestamp": timestamp,
    "Peak_OffPeak": peak_offpeak
}
    


## OUTSIDE the function
records = []

for i in range(20000):
    records.append(generate_record())

df = pd.DataFrame(records)
df.to_csv("datasets/ev_charging_data.csv", index=False)

print("Dataset saved successfully!")
print(df)
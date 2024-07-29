from datetime import datetime, timedelta

# Generate the list of dates for the given period
start_date = datetime(2024, 8, 1)
end_date = datetime(2024, 7, 10)
current_date = start_date

# List to hold the weather data
weather_data = []

# For simplicity, let's assume we have some dummy data generation function
def generate_dummy_weather_data(date):
    # This function should generate or fetch real weather data
    import random
    return {
        'Date': date.strftime('%Y-%m-%d'),
        'Max Temperature (C)': random.randint(20, 35),
        'Min Temperature (C)': random.randint(15, 25),
        'Humidity (%)': random.randint(40, 80)
    }

while current_date >= end_date:
    weather_data.append(generate_dummy_weather_data(current_date))
    current_date -= timedelta(days=1)

def find_highest_and_lowest_temperatures(data):
    highest_temp = float('-inf')
    lowest_temp = float('inf')

    for entry in data:
        max_temp = entry['Max Temperature (C)']
        if max_temp > highest_temp:
            highest_temp = max_temp
        if max_temp < lowest_temp:
            lowest_temp = max_temp

    return highest_temp, lowest_temp

# Example usage
highest, lowest = find_highest_and_lowest_temperatures(weather_data)
print(f"Highest Temperature: {highest}°C")
print(f"Lowest Temperature: {lowest}°C")

def count_days_above_30c(data):
    count = 0
    for entry in data:
        if entry['Max Temperature (C)'] > 30:
            count += 1
    return count

# Example usage
days_above_30c = count_days_above_30c(weather_data)
print(f"Number of Days with Temperature Above 30°C: {days_above_30c}")


def compute_average_humidity(data):
    total_humidity = 0
    num_days = len(data)

    for entry in data:
        total_humidity += entry['Humidity (%)']

    average_humidity = total_humidity / num_days if num_days > 0 else 0
    return average_humidity

# Example usage
average_humidity = compute_average_humidity(weather_data)
print(f"Average Humidity: {average_humidity:.2f}%")

from datetime import datetime, timedelta
import random

# Generate the list of dates for the given period
start_date = datetime(2024, 8, 1)
end_date = datetime(2024, 7, 10)
current_date = start_date

# List to hold the weather data
weather_data = []

# Dummy data generation function
def generate_dummy_weather_data(date):
    return {
        'Date': date.strftime('%Y-%m-%d'),
        'Max Temperature (C)': random.randint(20, 35),
        'Min Temperature (C)': random.randint(15, 25),
        'Humidity (%)': random.randint(40, 80)
    }

while current_date >= end_date:
    weather_data.append(generate_dummy_weather_data(current_date))
    current_date -= timedelta(days=1)

def find_highest_and_lowest_temperatures(data):
    highest_temp = float('-inf')
    lowest_temp = float('inf')

    for entry in data:
        max_temp = entry['Max Temperature (C)']
        if max_temp > highest_temp:
            highest_temp = max_temp
        if max_temp < lowest_temp:
            lowest_temp = max_temp

    return highest_temp, lowest_temp

def count_days_above_30c(data):
    count = 0
    for entry in data:
        if entry['Max Temperature (C)'] > 30:
            count += 1
    return count

def compute_average_humidity(data):
    total_humidity = 0
    num_days = len(data)

    for entry in data:
        total_humidity += entry['Humidity (%)']

    average_humidity = total_humidity / num_days if num_days > 0 else 0
    return average_humidity

# Example usage
highest, lowest = find_highest_and_lowest_temperatures(weather_data)
days_above_30c = count_days_above_30c(weather_data)
average_humidity = compute_average_humidity(weather_data)

print(f"Highest Temperature: {highest}°C")
print(f"Lowest Temperature: {lowest}°C")
print(f"Number of Days with Temperature Above 30°C: {days_above_30c}")
print(f"Average Humidity: {average_humidity:.2f}%")


# File: README.md

# Taxi Trip Calculator

A ride-hailing app returns a driver's completed trips for the day. It loops through the trips, counts them, adds up the fares, and finds the highest-paying trip. 


## What It Does

- Accepts daily data of a taxi operator (Name of Driver, Date, Trips)
- Calculates total number of trips and money made per day
- Applies logic to check for the Highest paying route
- Returns a short summary indicating number of trips, total money earned, and the highest trip route 
## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
highest_trip = max(trips, key=lambda trip: trip["fare_kes"])

print(f"Highest trip: {highest_trip['route']} | KES {highest_trip['fare_kes']}")
```

## Sample Output

```
Total trips: 10
Total earned: KES 14750
Highest trip: Airport to CBD | KES 2100
```

## Stack

Python
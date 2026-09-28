# File: README.md

# Taxi Trip Calculator

A ride-hailing app returns a driver's completed trips for the day. It loops through the trips, counts them, adds up the fares, and finds the highest-paying trip. 


## What It Does

- Accepts daily check-in data (sleep hours, water glasses, steps)
- Predicts whether the 10,000-step goal will be hit
- Returns a confidence score and a direct coaching message
- Exports a weekly summary report as JSON

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
Total trips: 5
Total earned: KES 3420
Highest trip: South B to Karen | KES 980
```

## Stack

Python
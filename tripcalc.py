
data = {
  "driver": "Kamau Njoroge",
  "date": "2026-08-13",
  "trips": [
    {"route": "Westlands to CBD", "fare_kes": 1200},
    {"route": "CBD to South B", "fare_kes": 950},
    {"route": "South B to Karen", "fare_kes": 1750},
    {"route": "Karen to Westlands", "fare_kes": 1500},
    {"route": "Westlands to Airport", "fare_kes": 1650},
    {"route": "Airport to CBD", "fare_kes": 2100},
    {"route": "CBD to Westlands", "fare_kes": 1300},
    {"route": "Westlands to South B", "fare_kes": 1100},
    {"route": "South B to Kileleshwa", "fare_kes": 1800},
    {"route": "Kileleshwa to Westlands", "fare_kes": 1400},
  ]
}
#Process
trips = data["trips"]

total_trips = len(trips)
total_earned = sum(trip["fare_kes"] for trip in trips)

# Trip with the highest fare
highest_trip = max(trips, key=lambda trip: trip["fare_kes"])

print(f"Total trips: {total_trips}")
print(f"Total earned: KES {total_earned}")
print(f"Highest trip: {highest_trip['route']} | KES {highest_trip['fare_kes']}")
import math
from dataclasses import dataclass
from typing import Tuple

@dataclass
class Location:
    """Class to keep track of a geographic location."""
    name: str
    lat: float
    lon: float

def calculate_haversine_distance(loc1: Location, loc2: Location) -> float:
    """
    Calculate the great-circle distance between two points 
    on the Earth using the Haversine formula.
    """
    R = 6371.0  # Earth's radius in kilometers

    # Convert decimal degrees to radians 
    phi1, phi2 = math.radians(loc1.lat), math.radians(loc2.lat)
    dphi = math.radians(loc2.lat - loc1.lat)
    dlambda = math.radians(loc2.lon - loc1.lon)

    # The Haversine square of half the chord length
    a = math.sin(dphi / 2.0)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(dlambda / 2.0)**2

    # The angular distance in radians
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def monitor_security_zone(home: Location, current: Location, threshold_km: float = 2.0):
    """
    Checks if the current location is within a allowed radius.
    """
    distance = calculate_haversine_distance(home, current)
    
    print(f"--- Location Report for {current.name} ---")
    print(f"Distance from {home.name}: {distance:.2f} km")

    if distance > threshold_km:
        print(f"⚠️ ALERT: Unusual location! You are {distance - threshold_km:.2f} km outside the safe zone.")
        return True
    
    print(f"✅ Status: Secure. You are within the {threshold_km} km safe zone.")
    return False

# --- Execution ---
if __name__ == "__main__":
    # Define our points of interest
    home_base = Location("Home (Lagos)", 6.5244, 3.3792)
    travel_destination = Location("Ibadan City Center", 7.3775, 3.9470)
    
    # Run the check
    monitor_security_zone(home_base, travel_destination)

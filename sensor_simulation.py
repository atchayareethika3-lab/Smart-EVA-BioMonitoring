import random

def get_sensor_data():
    return {
        "heart_rate": random.randint(60, 140),
        "oxygen_level": random.randint(85, 100),
        "body_temp": round(random.uniform(36.0, 39.5), 1)
    }

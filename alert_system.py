from sensor_simulation import get_sensor_data
from health_analysis import analyze_health
import time

while True:
    data = get_sensor_data()
    risks = analyze_health(data)

    print("Sensor Data:", data)

    if risks:
        print("⚠ ALERT:", ", ".join(risks))
    else:
        print("Status: Normal")

    print("-" * 40)
    time.sleep(2)

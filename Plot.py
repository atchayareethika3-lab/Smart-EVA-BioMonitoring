import matplotlib.pyplot as plt
from sensor_simulation import get_sensor_data
from alert_system import check_alerts
from health_analysis import analyze_health

hr_data = []
temp_data = []

for t in range(10):
    hr, temp = get_sensor_data()

    alerts = check_alerts(hr, temp)
    risk = analyze_health(hr, temp)

    print(f"HR: {hr}, Temp: {temp:.2f}, Risk: {risk}")
    if alerts:
        print("⚠ Alerts:", alerts)

    hr_data.append(hr)
    temp_data.append(temp)

    plt.clf()
    plt.plot(hr_data, label="Heart Rate")
    plt.plot(temp_data, label="Temperature")
    plt.axhline(100, linestyle="--", label="HR Limit")
    plt.axhline(38, linestyle="--", label="Temp Limit")
    plt.legend()
    plt.title("Smart EVA Bio-Monitoring System")
    plt.pause(0.5)

plt.show()

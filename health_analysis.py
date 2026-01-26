def analyze_health(data):
    risks = []

    if data["heart_rate"] > 120:
        risks.append("High Heart Rate")

    if data["oxygen_level"] < 90:
        risks.append("Low Oxygen Level")

    if data["body_temp"] > 38.5:
        risks.append("High Body Temperature")

    return risks

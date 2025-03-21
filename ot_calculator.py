def get_ot_rate(time_str):
    hour = int(time_str.split(':')[0])
    print(hour)
    if 21 <= hour < 24:
        return 3
    else:
        return 1.5

result = get_ot_rate("18:00")
print("OT Rate:", result)
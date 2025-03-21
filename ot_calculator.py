def get_ot_rate(day, start_time, end_time):
    normalday = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์"]
    weekend = ["เสาร์", "อาทิตย์"]
    
    start_hour = int(start_time.split(':')[0])
    end_hour = int(end_time.split(':')[0])
    
    if day in normalday:
        if 9 <= start_hour < 18 and 9 <= end_hour <= 18:
            return 1.5 
        elif 18 <= start_hour < 21 and 18 <= end_hour <= 21:
            return 1.5 
        elif 21 <= start_hour < 24 and 21 <= end_hour <= 24:
            return 3.0 
    
    elif day in weekend:
        if 9 <= start_hour < 18 and 9 <= end_hour <= 18:
            return 1.5 
        elif 18 <= start_hour < 21 and 18 <= end_hour <= 21:
            return 1.5  
        elif 21 <= start_hour < 24 and 21 <= end_hour <= 24:
            return 3.0  
    return "กรุณาตรวจสอบเวลาการทำงานของคุณอีกครั้ง"


def calculate_ot(employee_name, hourly_rate,day, ot_time_start, ot_time_end):
    start_hour, start_minute = map(int, ot_time_start.split(':'))
    end_hour, end_minute = map(int, ot_time_end.split(':'))
    
    start_time_decimal = start_hour + (start_minute / 60)
    end_time_decimal = end_hour + (end_minute / 60)
    print("start_time_decimal:", start_time_decimal)
    print("end_time_decimal:", end_time_decimal)

    ot_hours = end_time_decimal - start_time_decimal
    print(ot_hours)
    ot_rate = get_ot_rate(day, ot_time_start, ot_time_end)
    ot_pay = hourly_rate * ot_hours * ot_rate
    print(ot_rate)
    print(ot_pay)
    print("===========")
    return {
        "พนักงาน": employee_name,
        "จำนวนชั่วโมง OT": ot_hours,
        "อัตรา OT": ot_rate,
        "ค่า OT": ot_pay
    }
    
result_A = calculate_ot("สมชาย", 100, "จันทร์", "18:00", "20:00")
result_B = calculate_ot("สมชาย", 100, "เสาร์", "18:00", "20:00")
print(result_A)
print(result_B)
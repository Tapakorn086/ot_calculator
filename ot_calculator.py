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

    ot_hours = end_time_decimal - start_time_decimal
    ot_rate = get_ot_rate(day, ot_time_start, ot_time_end)
    ot_pay = hourly_rate * ot_hours * ot_rate
    return {
        "พนักงาน": employee_name,
        "วัน": day,
        "เวลา": f"{ot_time_start}-{ot_time_end}",
        "จำนวนชั่วโมง OT": ot_hours,
        "อัตรา OT": ot_rate,
        "ค่า OT": ot_pay
    }
    

def calculate_total_ot(employee_name, hourly_rate, ot_periods):
    total_ot_pay = 0
    ot_details = []
    
    for day, start_time, end_time in ot_periods:
        result = calculate_ot(employee_name, hourly_rate, day,start_time, end_time)
        ot_details.append(result)
        total_ot_pay += result["ค่า OT"]
    
    return {
        "พนักงาน": employee_name,
        "รายละเอียด OT": ot_details,
        "ค่า OT รวม": total_ot_pay
    }
    
employee_a_name = "นาย A"
employee_a_hourly_rate = 100
employee_a_ot_periods = [
  ("จันทร์","18:00", "19:00"),
  ("จันทร์","21:00", "22:00") 
]
result_a = calculate_total_ot(employee_a_name, employee_a_hourly_rate, employee_a_ot_periods)
print("ผลลัพธ์สำหรับพนักงาน A:")
print(f"ค่า OT รวม: {result_a['ค่า OT รวม']} บาท")


employee_b_name = "นาย B"
employee_b_hourly_rate = 150
employee_b_ot_periods = [
  ("จันทร์","19:00", "21:00") 
]
result_b = calculate_total_ot(employee_b_name, employee_b_hourly_rate, employee_b_ot_periods)
print("ผลลัพธ์สำหรับพนักงาน B:")
print(f"ค่า OT รวม: {result_b['ค่า OT รวม']} บาท")
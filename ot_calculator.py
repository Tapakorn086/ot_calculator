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
    
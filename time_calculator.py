def add_time(start, duration, starting_day=""):
    
    parts = start.split()
    time = parts[0].split(":")
    ampm = parts[1]
    
   
    duration_parts = duration.split(":")
    
   
    if ampm == "PM":
        time[0] = int(time[0]) + 12
    
  
    ending_h = int(time[0]) + int(duration_parts[0])
    ending_min = int(time[1]) + int(duration_parts[1])

    add_days = 0
    
    if ending_min >= 60:
        hours_add = ending_min // 60
        ending_min -= hours_add * 60
        ending_h += hours_add
    
    if ending_h > 24:
       add_days = ending_h // 24
        ending_h -= add_days * 24
        
    
    if ending_h > 12:
        ending_h -= 12
        ampm = "PM"
    elif ending_h == 12:
        ampm = "PM"
    elif ending_h > 0 and ending_h < 12:
        ampm = "AM"
    else: #ending_h == 0
        ampm = "AM"
        ending_h += 12
    
   
    if add_days > 0:
        if add_days == 1:
            moreDays = " (next day)"
        else:
            moreDays = " (" + str(add_days) + " days after)"
    else:
        moreDays = ""
    

    weekdays = ('Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday')
    
    if starting_day:
        b = int(days_add) + weekdays.index(starting_day.title())
        c = b // 7
        b = b - c * 7
        end_day = str(", " + weekdays[b])
    else:
        end_day = starting_day
    
    
    
    new_time = str(ending_h) + ":" + \
        (str(ending_min) if ending_min > 9 else ("0" + str(ending_min))) + \
        " " + ampm + "" + end_day + days_later
        
    return new_time

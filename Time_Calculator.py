def add_time(start, duration, day = "pass"):
    #start time splitting
    time_str, period = start.split()
    hour, minute = time_str.split(':')
    hour, minute =int(hour), int(minute)
    if period == 'PM':
        hour= hour +12

    # duration splitting
    d_hour, d_minute = duration.split(':')
    d_hour, d_minute = int(d_hour), int(d_minute)

    # adding 
    hours, minutes = hour + d_hour, minute + d_minute
    print(hours)
    
    if minutes >= 60:
        hours=hours+1
        minutes = minutes % 60
  
    hours, n_days = hours%24, hours//24

    # period 
    if hours < 12:
        period = "AM" 
    else:
        period = "PM"

    # 12 hour format
    if hours == 0:
        hours = 12
    elif hours >12:
        hours = hours - 12
   
    # HH:MM AM/PM Format
    new_time=f"{hours}:{minutes:02d} {period}"
    # Days week
    if day:
        day=day.lower()
        days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day_index = days.index(day)
        new_day_index = (day_index + n_days) % 7
        day = days[new_day_index]
        new_time += f', {day.capitalize()}'
    # No of days
    if n_days == 1:
         new_time += ' (next day)'
    elif n_days >1: 
        new_time += f' ({n_days} days later)'
    return new_time
# print(add_time('2:59 AM', '24:00', 'saturDay'))


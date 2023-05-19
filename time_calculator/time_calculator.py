def add_time(start_time, added_time, current_day=None):
    days_of_the_week = {"Sunday":1, "Monday":2, "Tuesday":3, "Wednesday":4, "Thursday":5, "Friday":6, "Saturday":7}
    added_time_hours = added_time.split(":")[0]
    added_time_minutes = added_time.split(":")[1]
    start_time_hours = start_time.split(":")[0]
    start_time_minutes = start_time.split(":")[1].split()[0]
    start_time_shift = start_time.split(":")[1].split()[1]
    if start_time_shift == 'PM':
        is_PM = True
    else:
        is_PM = False
    added_in_minutes = int(added_time_hours) * 60 + int(added_time_minutes)
    start_in_minutes = int(start_time_hours) * 60 + int(start_time_minutes)
    calculated_added_minutes = added_in_minutes + start_in_minutes
    remainder_minutes = calculated_added_minutes % 60

    if remainder_minutes <= 9:
      remainder_minutes = "0" + str(remainder_minutes)

    def what_time_is_it(is_PM):
        global calculated_hours
        global passed_days
        passed_days = 0
        calculated_hours = calculated_added_minutes // 60
        while calculated_hours >= 12:
            calculated_hours = calculated_hours - 12
            is_PM = not is_PM
            if is_PM == False:
                passed_days = passed_days + 1
        if calculated_hours == 0:
            calculated_hours = calculated_hours + 12
        return is_PM

    if what_time_is_it(is_PM) == True:
        start_time_shift = "PM"
    else:
        start_time_shift = "AM"

    
    
    if not current_day == None:
        current_day = current_day.lower()
        current_day = current_day.capitalize()
        current_day_value = days_of_the_week[current_day]
        current_day = current_day_value + passed_days
        while current_day > 7:
            current_day = current_day - 7
        for k, v in days_of_the_week.items():
            if v == current_day:
                current_day = k
        

  
    if passed_days > 1:
        days_later = f" ({passed_days} days later)"
    elif passed_days == 1:
        days_later = ' (next day)'
    else:
        days_later = ''

    if not current_day == None:
        add_time_answer = str(calculated_hours) + ':' + str(remainder_minutes) + " " + str(start_time_shift) + ", " + str(current_day) + days_later 
    else:
        add_time_answer = str(calculated_hours) + ':' + str(remainder_minutes) + " " + str(start_time_shift) + days_later
    return add_time_answer

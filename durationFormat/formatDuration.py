def format_duration(seconds):
    if seconds == 0:
        return 'now'
    
    # convert the seconds into years,days,minutes, and seconds
    # Here the code uses a built in python function `divmod`, which returns a
    # pair of numbers `(a//b, a%b`).
    # We are using it to divide the total seconds by 60 to get the number of minutes
    # and the remainder(which are the leftovers seconds)
    
    minutes, sec = divmod(seconds, 60)
    
    # similarly, the total minutes are divided by 60 to get the number of hours
    # and the remaining minutes
    
    hours, minutes = divmod(minutes, 60)
    
    # Then, we divide total hours by 24 to get number of days and leftovers hours
    
    days, hours = divmod(hours, 24)
    
    # finally, days are divide by 365 to get the numbers of years and days remaining
    
    years, days = divmod(days, 365)
    
    # preparing components for the result. Each tuple contains the value for each
    # unit of time(like yeays,days etc)(singular and plural)
    
    components = [
        (years, 'year', 'years'),
        (days, 'day', 'days'),
        (hours, 'hour', 'hours'),
        (minutes, 'minute', 'minutes'),
        (sec, 'second', 'seconds'),
    ]
    
    # This line uses a list comprehension. it iterates over the components list and
    # for each component, if the value is not zero, it formats the value and the unit
    # of time into(either in singular or plural) string
    
    result = [f"{value} {singular if value == 1 else plural}" for value, singular, plural in components if value]
    
    # If the result has only one component(eg minutes or seconds) we return that 
    # single component as trhe result
    if len(result) == 1:
        return result[0]
    
    # if the list has multiple components, we join all the components except the last
    # using ',' and then add 'add' before the last components as the result.
    
    else:
        return ', '.join(result[:-1]) + ' and ' + result[-1]
    

print(format_duration(62)) # Expected: "1 minute and 2 seconds"
print(format_duration(3662)) # Expected: "1 hour, 1 minute and 2 seconds"
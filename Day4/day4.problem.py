def number(bus_stops):
    totalpassegers = 0
    
    for stop in bus_stops:
        peopleon, peopleoff = stop
        
        totalpassegers+= peopleon - peopleoff
        
        
    return max(totalpassegers, 0)

bus_stops = [(3, 0), (4, 2), (10, 5), (2, 1)]
remaining_people = number(bus_stops)
print(remaining_people) # 11
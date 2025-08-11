def temperature(temp):
    if temp <= 10:
        return 'Cold'
    elif temp <= 25:
        return 'Warm'
    else:
        return 'Hot'
    

print(temperature(6))
    

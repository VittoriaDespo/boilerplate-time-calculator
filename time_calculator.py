def add_time(start, duration, ):
  print(start,duration)
  time,period = start.split()
  # Converting string in float
  float_time = float(time.replace(':','.'))
  float_duration = (float(duration.replace(':','.')))
  # Calculating duration's mod
  mod_duration = float_duration%24
  # Add duration's mod to the time
  sum = round(float_time + mod_duration,2)
  # formatting the var sum to get a sum with 2 decimal
  sum = f'{sum:.2f}'
  # Converting into integer and split the result
  hour,minutes = map(int,sum.split('.'))
  # Condition to add minutes to hour
  if minutes >=60:
    hour += 1
    minutes = minutes-60
  # Formatting minutes
  if minutes < 10: 
    minutes = f'0{minutes}'
  if period == "PM" and hour >= 12:
    period = "AM"
  elif period == "AM" and hour >= 12:
    period = "PM"
  # Attribute the result to a new var
  new_time = f'{hour}:{minutes} {period}'
  # Getting the hour with one decimal
  hours = {13:1,14:2,15:3,16:4,17:5,18:6,19:7,20:8,21:9,22:10,23:11,24:12}
  if hour in hours:
    final_hour = hours.get(hour)
    new_time = f'{final_hour}:{minutes} {period}'
    return new_time
  else:
    return new_time
    
  
 
  
  
  
  
    

    
  
  





  #return new_time
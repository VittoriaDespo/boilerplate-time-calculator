def add_time(start, duration, weekday = None):

  time, period = start.split()
  hour, minutes = map(int,time.split(':'))
  duration_hour, duration_minutes = map(int,duration.split(':'))
  next_day = ''
  final_day = ''

  if period == 'PM':
    hour = hour + 12
    
  
  sum_hour = hour + duration_hour
  
  minutes_hour = sum_hour * 60
  
  min_tot = minutes+duration_minutes
 
  final_hour = minutes_hour/60
  
  if min_tot >=60:
    final_hour += 1
    min_tot = min_tot-60
    
  if min_tot < 10:
    min_tot = f'0{min_tot}'
    
  day,final_hour = divmod(int(final_hour),24)
  
  if final_hour < 12:
    period = "AM"
  else:
    period = "PM"
    final_hour = final_hour - 12
    
  if final_hour == 0:
    final_hour = 12
  

  if weekday:
    week =('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
    f_day = (week.index(weekday.capitalize()) + day) % 7
    final_day = f', {week[f_day]}'
   
  if day == 1:
      next_day = ' (next day)'
  elif day > 1:
      next_day = f' ({day} days later)'


  return (f'{final_hour}:{min_tot} {period}{final_day}{next_day}')

 
    
  
 
  
  
  
  
    

    
  
  





  #return new_time
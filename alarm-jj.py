# asks for current time in 24 hour time (0-23)
# asks how many hours to wait in 0-23
# outputs time an alarm will go off based on given times
# edited and debugged by James Jack

str_time = input("What time is it now in hours 0-23?")
str_wait_time = input("What is the number of hours to wait in 0-23?")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
final_time = time_when_alarm_go_off % 24
print(final_time)

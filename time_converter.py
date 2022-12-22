convert_to = int(input("""Format in which you want to covert
1. 12 hr system
2. 24 hr system
Enter your response (1 or 2): """))

saperator1 = ":"

def hr_12():

    Enter_time = input("Enter time in the 24 hr system (ex: 13:15 ): ")
    time = Enter_time.split(":")
    int_time = int(time[0])

    if int_time in range(12, 24):
        int_time -= 12

        if int_time == 0:
            int_time = 12

        time[0] = str(int_time)
        print(f"Your time in 12 hr system is: {saperator1.join(time)} PM")

    elif int_time in range(0, 12):

        if int_time == 0:
            int_time = 12

        time[0] = str(int_time)
        print(f"Your time in 12 hr system is: {saperator1.join(time)} AM")

def hr_24():

    Enter_time = input("Enter time in the 12 hr system (ex: 1:15 PM or 1:15 AM): ")
    time = Enter_time.split(" ")

    if time[1] == "AM":

        hour = time[0].split(":")
        int_hour = int(hour[0])

        if int_hour == 12:
            int_hour = 0

        hour[0] = str(int_hour)
        print(f"Your time in 24 hr system is: {saperator1.join(hour)}")

    elif time[1] == "PM":

        hour = time[0].split(":")
        int_hour = int(hour[0])
        int_hour += 12

        if int_hour == 24:
            int_hour = 12

        hour[0] = str(int_hour)
        print(f"Your time in 24 hr system is: {saperator1.join(hour)}")

    
if convert_to == 1:
    hr_12()
    
elif convert_to == 2:
    hr_24()
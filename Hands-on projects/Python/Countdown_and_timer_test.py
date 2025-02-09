#import time to use sleep function

#Approch:

#write a countdown funtion which will count the time remaining based on the set time in hours. It 1st converts the inout from user into seconds.
#Then the timer is format into HH:MM:SS.Then the counter sleeps for 60 seconds and then counter is decreased by 60 seconds to display the remaining time.
#The loop goes on till the complete time is not equal to 0. Once it is zero the output will be displayed as Time's up.

#write a stopwatch funtion which will keep on counting the time until a keyboard input is not given.

#Main funtion is written to get the imput from user to run the countdown or stopwatch. Also the timer required for how many hours is taken.
#Based on the input the respective funtion is called. The execution will stop is the choice is made invalid or the hours is mentioned as integer value.

import time

def countdown_timer(hrs):
    """Counts down from the given number of seconds."""
    seconds = int(hrs * 3600)  # Convert hours to seconds
    while seconds:
        hrs = seconds // 3600
        remainder = seconds % 3600
        mins = remainder // 60
        secs = remainder % 60
        timer_format = f'{hrs:02}:{mins:02}:{secs:02}'
        print(timer_format, end='\r')
        time.sleep(60)
        seconds -= 60
        #print("Remaining time is:",timer_format)
    print("Time's up!")

def stopwatch_timer():
    """Acts as a stopwatch, counting up until stopped by the user."""
    seconds = 0
    try:
        while True:
            hrs = seconds // 3600
            remainder = seconds % 3600
            mins = remainder // 60
            secs = remainder % 60
            timer_format = f'{hrs:02}:{mins:02}:{secs:02}'
            print(timer_format, end='\r')
            time.sleep(1)
            seconds += 1
    except KeyboardInterrupt:
        print(f'\nStopwatch stopped at {hrs:02}:{mins:02}:{secs:02}')

if __name__ == "__main__":
    try:
        choice = input("Enter 'c' for countdown or 's' for stopwatch: ").strip().lower()
        if choice == 'c':
            hrs = int(input("Enter the countdown time in hours: "))
            countdown_timer(hrs)
        elif choice == 's':
            print("Stopwatch started! Press Ctrl+C to stop.")
            stopwatch_timer()
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid integer for the countdown time.")
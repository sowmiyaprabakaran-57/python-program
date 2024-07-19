import time
from datetime import datetime

def set_alarm():
    print("Set your alarm.")
    hour = int(input("Enter hour (24-hour format): "))
    minute = int(input("Enter minute: "))
    second = int(input("Enter second: "))

    return hour, minute, second

def current_time():
    now = datetime.now()
    return now.hour, now.minute, now.second

def wait_for_alarm(alarm_time):
    print("Alarm is set. Waiting...")
    while True:
        now = current_time()
        if now == alarm_time:
            print("Wake up! The alarm is ringing!")
            break
        time.sleep(1)  
def main():
    alarm_time = set_alarm()
    wait_for_alarm(alarm_time)

if __name__ == "__main__":
    main()

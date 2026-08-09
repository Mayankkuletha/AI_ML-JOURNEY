# Making an alarm Clock to Wake up

import datetime
import time


def setAlarm(alarm_time):
    print(f"Alarm successfully set for {alarm_time}")

    isRunning = True

    while isRunning:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake up bro")
            isRunning = False

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input(
        "Enter the time at which you want to set an alarm "
        "in the form (HH:MM:SS): "
    )

    setAlarm(alarm_time)
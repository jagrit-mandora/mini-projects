import time
import pygame

def input_time():
    while True:
        try:
            print("PLEASE INPUT TIME IN FORM OF HH:MM:SS")
            hour,minutes,seconds=input("time: ").split(":")
            hour=int(hour)
            minutes=int(minutes)
            seconds=int(seconds)
            while not -1<hour<25 or not -1<minutes<61 or not -1<seconds<61:
                print("PLEASE PRINT A VALID TIME: ")
                hour,minutes,seconds=input("time: ").split(":")
                hour=int(hour)
                minutes=int(minutes)
                seconds=int(seconds)
            return hour,minutes,seconds
        except ValueError:
            continue

def alarm_sound():
    pygame.init()
    pygame.mixer.music.load("freesound_community-alarm-clock-90867.mp3")
    pygame.mixer.music.play()
    time.sleep(6)

def alarm_working(hour,minutes,seconds,running):
    while running:
        current_time=time.localtime()

        formated_time=time.strftime("%H:%M:%S",current_time)

        print(f"\r{formated_time}", end="", flush=True)

        format_hour=time.strftime("%H",current_time)
        x=int(format_hour)

        
        format_minute=time.strftime("%M",current_time)
        y=int(format_minute)

        
        format_second=time.strftime("%S",current_time)
        z=int(format_second)


        if x==hour and y==minutes and z==seconds:
            print()
            print("TIMES UP!")
            alarm_sound()
            running=False

        time.sleep(1)

def main():
    running=True
    hour,minutes,seconds=input_time()
    alarm_working(hour,minutes,seconds,running)

if __name__=="__main__":
    main()
import time

def countdown(timer_sec):
    while timer_sec:
        mins, secs = divmod(timer_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        timer_sec -= 1

    print("over")


x=int(input("enter no."))
countdown(x)

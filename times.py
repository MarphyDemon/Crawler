import time
import datetime
def func():
    print("dsdssd")
def main(h=15,m=2):
    while True:  
        now = datetime.datetime.now()  
        print(now.hour == h ,now.minute == m,h,m,now.hour,now.minute)
        if now.hour == h and now.minute == m:  
            func()
        time.sleep(86400)
    print("dsd")  
    main()

if __name__ == '__main__':
    main()
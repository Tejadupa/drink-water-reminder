import time
import winsound as w

f=2000
d=3000

while(1):
    obj=time.localtime(time.time())
    time_str=time.asctime(obj)
    print(time_str)
    w.Beep(f,d)
    print("Please Drink Water")
    z=int(input("Enter 0 to Stop Alaram :"))
    if(z==0):
        break
    time.sleep(7.7)




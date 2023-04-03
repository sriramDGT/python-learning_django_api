import threading
import time

def display(x,t1):
    for i in range(x):
        time.sleep(t1)
        print("thread started")

t=threading.Thread(target=display,args=(14,12,))
t.start()

import threading
import time

def display(x, t1):
    for i in range(x):
        time.sleep(t1)
        print(f"Thread started - {threading.current_thread().name}")

print("Main thread started")
k = threading.Thread(target=display, args=(14, 12), name="Thread 1")
k.start()

import threading
import time

def display(x,s,name):
    for i in range(x):
        time.sleep(s)
        print(name,"::Started")
    
t=threading.Thread(target=display,args=(14,12,"Thread 1"))
t.start()
t1=threading.Thread(target=display,args=(14,14,"Thread 2"))
t1.start()

import _thread
import time

def a(msg):
    count=0
    while count < 5:
        count += 1
        time.sleep(8)
        print(msg)

def b(msg):
    count=0
    while count <5:
        count +=1
        time.sleep(9)
        print(msg)

try:
    _thread.start_new_thread(a,("Thread 1",))
    _thread.start_new_thread(b,("Thread 2",))

except:
    print("error to start thread")

while 1:
    pass

import threading
import time

def display(x):
    for i in range(5):
        time.sleep(x+1.5)
        print(threading.current_thread().getName())
        print("thread Started")
        
for p in range(5):
    t=threading.Thread(target=display,args=(p,))
    t.setName("Thread #" + str(p))
    t.start()

import threading
import time

def display(i):
    time.sleep(i)
    return
t1=threading.Thread(target=display,args=(8,),name="Thread#1")
t1.start()
t2=threading.Thread(target=display,args=(8,),name="Thread#2")
t2.start()

for x in range(5):
    time.sleep(x+0.5)
    print('[',time.ctime(),t1.name,t1.is_alive(),']')
    print('[',time.ctime(),t2.name,t2.is_alive(),']')

import threading
import time

def display(x, t1):
    for i in range(x):
        time.sleep(t1)
        print(f"Thread started - {threading.current_thread().name}")

print("Main thread started")
k = threading.Thread(target=display, args=(10, 12), name="Thread 1")
k.start()


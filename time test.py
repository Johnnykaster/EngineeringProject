import time
from playsound import playsound
start_time = time.time()
print(start_time)
seconds = 180
loop_num = 0
playsound('/Users/johnkaster/Music/iTunes/iTunes Media/Music/Unknown Artist/Unknown Album/Engineering Project.wav')



while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > seconds:
        print(loop_num)
        loop_num  = loop_num + 1
        elapsed_time = 0
        start_time = time.time()
        playsound('/Users/johnkaster/Music/iTunes/iTunes Media/Music/Unknown Artist/Unknown Album/Engineering Project.wav')


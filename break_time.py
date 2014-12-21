import time
import webbrowser

print ("break_time started at "+time.ctime())
x = 1
while x <= 3:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    x = x+1


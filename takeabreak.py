import webbrowser
import time

total_breaks = 10
break_count = 0


print("Started on")

while(break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("http://www.youtube.com/watch?adale")
	break_count = break_count + 1




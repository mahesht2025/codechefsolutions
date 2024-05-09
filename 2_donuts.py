#The tray had X donuts, and each donut contains Y calories.
#How many calories did Chef consume in total ?
x,y= map(int, input().split())

total_calories= x * y

print(total_calories)
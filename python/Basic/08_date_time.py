import time

# seconds since epoch to a readable
# epoch = when your computer thinks time began
print(time.ctime(0))

print(time.time())  # current seconds since epoch

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)
print(time.strftime("%Y-%B-%d %H:%M:%S", time_object))
time_object = time.gmtime()
print(time_object)
print(time.strptime("20 April,2023", "%d %B,%Y"))

# time_tuple (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

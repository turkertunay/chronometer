import datetime
print("your chronometer has started at:")
now = datetime.datetime.today()
print(now)

x = input("press enter to stop the chronometer: ")
now_2 = datetime.datetime.today()
print("your chronometer was stopped at:")
print(now_2)


print("time elapsed: ", now_2-now)
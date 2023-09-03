#input section
seconds=int(input("enter the number of seconds"))

#logicsection
rem_sec =seconds%60
minutes =seconds//60
rem_min =minutes%60
hours =minutes%60

#displaysection

print("given number of seconds",seconds)

print("<== after simplification==>")

print("hours",hours)
print("minutes",minutes)
print("seconds",seconds)

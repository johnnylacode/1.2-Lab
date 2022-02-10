"""
Johnny La
1875393
"""

print("Birthday Calculator")
print("Current day")
month = int(input("Month: "))
day = int(input("Day: "))
year = int(input("Year: "))

print("Birthday")
birth_month = int(input("Month: "))
birth_day = int(input("Day: "))
birth_year = int(input("Year: "))

if month < birth_month:
    print("You are {} years old.".format(year-birth_year-1))
elif day < birth_day:
    print("You are {} years old.".format(year-birth_year-1))
elif day == birth_day and month == birth_month:
    print("Happy Birthday! You are {} years old.".format(year - birth_year))
else:
    print("You are {} years old.".format(year - birth_year))
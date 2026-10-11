year = int(input("Entar Your Year :"))

# def greet_year(leap):
#     if leap % 4 == 0:
#         print(f"leap year {leap}")
#     elif leap % 400 == 0 and leap % 100 == 0:
#         print(f"your leap year {leap}")
#     else:
#         print("not for the leap year")

# greet_year(year)

if (year % 4 == 0) and (year % 100 != 0) or (year %400 ==0):
    print(f"leap year {year}")
else:
    print(f"Not For The Leap Year {year}")
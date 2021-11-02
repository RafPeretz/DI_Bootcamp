# Exercise 1
from datetime import *
import datetime


def print_date():
    today = date.today()
    print("Today's date:", today)


print_date()


# Exercise 2

def january():
    today = date.today()
    january = datetime.date(2022, 1, 1)

    time_difference = january - today
    day = time_difference.days

    print(f'the 1st of January is in {day} days and ')


january()

now = datetime.datetime.now()
print(now)


def minute_alive():
    today = date.today()
    birthdate = datetime.date(2003, 1, 3)
    age = today - birthdate
    hour = age * 24
    minute = hour * 60
    print(minute.days, "minutes")


minute_alive()


# Exercise 4

def print_date():
    today = date.today()
    print("Today's date:", today)


def next_holiday():
    today = date.today()
    print("Today's date:", today)
    hanoucca_holiday = datetime.date(2021, 11, 28)
    time_difference = hanoucca_holiday - today
    day = time_difference.days

    print(f'the next are vacation are in {day} days and minutes ')


next_holiday()


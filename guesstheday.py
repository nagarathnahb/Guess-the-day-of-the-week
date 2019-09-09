import math

def checkLeapYear(year):
    if (year % 100 == 0):
        if (year % 400 == 0):
            return True
        if (year % 4 == 0):
            return True
    return False

def get_val(month):
    if (month == 1 or month == 10):
        return 1
    if (month == 2 or month == 3 or month == 11):
        return 4
    if (month == 4 or month == 7):
        return 0
    if (month == 5):
        return 2
    if (month == 6):
        return 5
    if (month == 8):
        return 3
    return 6


def getData():
    print('Enter the month: (1-12)')
    while True:
        month = input()
        m = int(month)
        if(m>0 and m<13):
            break
        print('Enter valid month(1-12)')
    print('Enter the year: (1900-3000)')
    while True:
        year = input()
        y = int(year)
        if(y>1900 and y<3001):
            break
        print('Enter valid year(1900-3000)')

    if m == 2:
        if checkLeapYear(y):
            print('Enter the date: (1-29)')
            while True:
                date = input()
                d = int(date)
                if (d > 0 and d < 30):
                    break
                print('Enter valid date (1-29)')
        else:
            print('Enter the date: (1-28)')
            while True:
                date = input()
                d = int(date)
                if (d > 0 and d < 29):
                    break
                print('Enter valid date (1-28)')

    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        print('Enter the date: (1-31)')
        while True:
            date = input()
            d = int(date)
            if (d > 0 and d < 32):
                break
            print('Enter valid date (1-31)')

    else:
        print('Enter the date: (1-30)')
        while True:
            date = input()
            d = int(date)
            if (d > 0 and d < 31):
                break
            print('Enter valid date (1-30)')

    return d, m, y

getDay = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
get_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
def guessTheDay(d,m,y):
    val1 = (y % 100) // 4
    res = val1 + d + get_val(m)
    if (checkLeapYear(y) and (m == 1 or m == 2)):
        res-=1
    if (y // 100 == 20):
        res += 6
    res += (y % 100)
    print(get_month[m-1] + ", " + str(d) + ", " + str(y) + ' is ' + getDay[res % 7])

print('Welcome to guess the day of the week!')
d, m, y = getData()
guessTheDay(d,m,y)

def tryAgain():
    print('Do you want to try again? (Yes or No)')
    return input().startswith('y')


while True:
    if tryAgain():
        d, m, y = getData()
        guessTheDay(d,m,y)
    else:
        break

'''
I have followed these steps:

Step1: Take the last 2 digits of the year. In our example, this is 82.

Step 2: Divide by 4, and drop any remainder. 82 / 4 = 20, remainder 2, so we think "20."

Step 3: Add the day of the month. In our example, 20 + 16 = 36.

Step 4: Add the month's key value, from the following table.
Jan	Feb	Mar	Apr	May	June July Aug Sept Oct Nov	Dec
 1	 4	 4	 0	 2	 5	  0	  3	   6	1	4	 6

Step 5: The month for our example is December, with a key value of 6. 36 + 6 = 42.

Step 6: If your date is in January or February of a leap year, subtract 1. 
We're using December, so we don't have to worry about this step.

Step 7: Add the century code from the following table. (These codes are for the Gregorian calendar. 
The rule's slightly simpler for Julian dates.)
1700s	1800s	1900s	2000s
4	    2	    0	    6

Step 8: Our example year is 2482, and the 2400s aren't in the table. 
Luckily, the Gregorian calendar repeats every four hundred years. 
All we have to do is add or subtract 400 until we have a date that is in the table. 
2482 - 400 = 2082, so we look at the table for the 2000s, and get the code 6. 
Now we add this to our running total: 42 + 6 = 48.

Step 9: Add the last two digits of the year. 48 + 82 = 130.

Step 10: Divide by 7 and take the remainder. This time, 1 means Sunday, 2 means Monday, and so on. 
A remainder of 0 means Saturday. 130 / 7 = 18, remainder 4, so December 16, 
2482 will be on the fourth day of the week-- Wednesday.
'''
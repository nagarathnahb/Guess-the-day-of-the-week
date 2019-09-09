# Guess-the-day-of-the-week
This program gives the day of the week for a given date!

## The code is written following these steps:

Step1: Take the last 2 digits of the year. In our example, this is 82.

Step 2: Divide by 4, and drop any remainder. 82 / 4 = 20, remainder 2, so we think "20."

Step 3: Add the day of the month. In our example, 20 + 16 = 36.

Step 4: Add the month's key value, as given below.
Jan-1,	Feb-4,	Mar-4,	Apr-0,	May-2,	June-5, July-0, Aug-3, Sept-6, Oct-1, Nov-4,	Dec-6


Step 5: The month for our example is December, with a key value of 6. 36 + 6 = 42.

Step 6: If your date is in January or February of a leap year, subtract 1. 
We're using December, so we don't have to worry about this step.

Step 7: Add the century code. (These codes are for the Gregorian calendar. 
The rule's slightly simpler for Julian dates.)
1900s-0,	2000s-6

Step 8: Our example year is 2482, and the 2400s aren't in the table. 
Luckily, the Gregorian calendar repeats every four hundred years. 
All we have to do is add or subtract 400 until we have a date that is in the table. 
2482 - 400 = 2082, so we look at the table for the 2000s, and get the code 6. 
Now we add this to our running total: 42 + 6 = 48.

Step 9: Add the last two digits of the year. 48 + 82 = 130.

Step 10: Divide by 7 and take the remainder. This time, 1 means Sunday, 2 means Monday, and so on. 
A remainder of 0 means Saturday. 130 / 7 = 18, remainder 4, so December 16, 
2482 will be on the fourth day of the week-- Wednesday.


# For Feb 1st 1993, the output will be:
February, 1, 1993 is Monday

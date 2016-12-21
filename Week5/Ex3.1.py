'''
Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
 Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
 Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
 You should use raw_input to read a string and float() to convert the string to a number.
 Do not worry about error checking the user input - assume the user types numbers properly.
'''



def computerpay(hrs, rate):
    if hrs > 40:
        hour = 40
        left = hrs - 40
        p = (hour * rate) + (left * (rate * 1.5))
    elif h <= 40:
        p = (hrs * rate)
    return p


try:
    hrs = float(raw_input("How many hours do you got: "))
    rate = float(raw_input("How much rate do you got: "))
except:
    print "Please put in numbers"
    exit()

p = computerpay(hrs, rate)

print p
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")

    # input
    if num == "done": break
    if len(num) == 0: break

    try:
        num = int(num)
        if smallest is None or smallest > num:
            smallest = num;

        if largest is None or largest < num:
            largest = num;

    except Exception, e:
        print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest


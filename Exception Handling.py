'''
a = 8
b = 0

try:
    print(a/b)
except Exception as e:
    print("You cannot divide a number by Zero", e)

print("Ended")


a = 8
b = 2

try:
    print("resource open")
    print(a/b)

except Exception as e:
    print("You cannot divide a number by Zero", e)
finally:
    print("resource close")
'''

a = 5
b = 2

try:
    print("resource open")
    print(a / b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("You"
          ""
          " can divide a number by Zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong...")

finally:
    print("resource close")

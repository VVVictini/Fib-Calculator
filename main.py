import time
import sys

def delay_print(s):
            for c in s:
              sys.stdout.write(c)
              sys.stdout.flush()
              time.sleep(0.05)

num1=0
num2=1
i=0

delay_print("1. Amount of series of numbers\n")
time.sleep(0.5)
delay_print("2. Series of numbers until desired number to stop at\n")
time.sleep(0.5)

k=0
while k < 100:
    try:
      choice=int(input("Would you like option 1 or 2? (1,2): "))
      if choice >=1 and choice <=2:
        break
      else:
        print("Error:Invalid Input")

    except ValueError:
      print("Error:Invalid Input")
    except NameError:
      print("Error:Invalid Input")


if choice == 1:
    OptionA=float(input("How many series of numbers would you like?: "))
    while i < OptionA:
        print(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        i += 1

elif choice == 2:
    OptionB=float(input("What number would you like the series to stop at?: "))
    while num1 < OptionB:
        print(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
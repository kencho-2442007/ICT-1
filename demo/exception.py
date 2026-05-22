try:
    n=float(input("Enter a number:"))
    res=100/n
except ZeroDivisionError:
    print("you cant divide by zero!")
except ValueError:
    print("Enter a valid number!")
except:
    print("An unexcepted error occured.")
else:
    print("Result is", res)
finally:
    print("Execution complete.")
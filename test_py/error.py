a = 5
b = 2

try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except Exception as e:
    print("Hay you can not divide a number by zero", e)

except ValueError as e:
    print("invalid Input")

except Exception as e:
    print("something went erong")

finally:
    print("resource closed")

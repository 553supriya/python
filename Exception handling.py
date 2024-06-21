
try:
    a=int(input("enter the a value"))
    b=int(input("enter the b value"))
    c=a/b
    print("value of c: ", a / b)
except Exception:
    print("b value is not mentioned")
except NameError:
    print("b value is not mentioned")
except ZeroDivisionError:
    print("Arithematic exception")
except ValueError:
    print("value error")
except IndexError:
    print("array index out of bounds")
except KeyError:
    print("key error")
except IOError:
    print("file input or output error")


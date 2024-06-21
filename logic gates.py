def AND(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False


print("A=True|B=True|A AND B=True", AND(1, 1))
print("A=True|B=False|A AND B=False", AND(1, 0))
print("A=False|B=True|A AND B=False", AND(0, 1))
print("A=False|B=False|A AND B=False", AND(0, 0))

def OR(a,b):
    if a==0 or b==0:
        return False
    return True
print("OR LOGIC GATE")
print("A=True | B=True | A or B="+str(OR(1,1)))
print("A=True | B=False | A or B="+str(OR(1,0)))
print("A=False | B=True | A or B="+str(OR(0,1)))
print("A=False | B=False | A or B="+str(OR(0,0)))

def XOR(a,b):
    if a==0:
        return False
    else:
        return True
print("XOR LOGIC GATE")
print("A=True | B=True | A xor B="+str(XOR(1,1)))
print("A=True | B=False | A xor B="+str(XOR(1,0)))
print("A=False | B=True | A xor B="+str(XOR(0,1)))
print("A=False | B=False | A xor B="+str(XOR(0,0)))
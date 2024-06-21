def commas(str):
    x=str.replace(' ',',')[1:-1]
    return x
print(repr(commas("Apple")))
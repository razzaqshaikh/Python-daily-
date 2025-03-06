'''Write a python prog to check if given variable is type
int or float'''




var = 10.5  # Change this value to test

if isinstance(var, int):
    print("Integer")
elif isinstance(var, float):
    print("Float")
else:
    print("Neither int nor float")


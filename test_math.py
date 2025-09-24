import sys, os
sys.path.append(os.getcwd())  

from maths import add, subtract, multiply, divide

print("add(2, 3, 5) =", add(2, 3, 5))                 # 10
print("subtract(100, 20, 30, 40) =", subtract(100, 20, 30, 40))  # 10
print("multiply(2, 3, 4) =", multiply(2, 3, 4))       # 24
print("divide(100, 2, 5) =", divide(100, 2, 5))       # 10.0

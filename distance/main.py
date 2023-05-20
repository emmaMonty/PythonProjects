import math
# input
D = eval(input("Distance to Professor:"))
Theta = eval(input("Angle of Elevation:"))

# Variables
M = .065
K = 25
G = 9.8

# Processing
Numerator = M * G * D
Denominator = K * math.sin(math.radians(2*Theta))
X = math.sqrt(Numerator/Denominator)
# Output
print(X)

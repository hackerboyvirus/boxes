def transfer_points(a, b, c, d):
    a_new = a + 0.2 * b - 0.2 * a
    b_new = b - 0.1 * b + 0.1 * c
    c_new = c - 0.06 * c + 0.06 * a
    d_new = d - 0.04 * d + 0.04 * b
    return a_new, b_new, c_new, d_new

# Initial points
A_points = 1000000
B_points = 500000
C_points = 300000
D_points = 200000

# Simulate the transfers for 365 days
for day in range(365):
    A_points, B_points, C_points, D_points = transfer_points(A_points, B_points, C_points, D_points)

print(f"After 365 days:")
print(f"Box A: {A_points:.2f} points")
print(f"Box B: {B_points:.2f} points")
print(f"Box C: {C_points:.2f} points")
print(f"Box D: {D_points:.2f} points")

##
import tensorflow as tf

# Initialize the initial points in each box
points_a = tf.constant(1000000.0)
points_b = tf.constant(500000.0)
points_c = tf.constant(300000.0)
points_d = tf.constant(200000.0)

# Perform calculations for 364 days
for _ in range(1):
    points_a = points_a + points_b * 0.2
    points_b = points_b - points_b * 0.2
    points_d = points_d + points_a * 0.2
    points_a = points_a - points_a * 0.2
    points_c = points_c + points_d * 0.2
    points_d = points_d - points_d * 0.2
    points_b = points_b + points_c * 0.2
    points_c = points_c - points_c * 0.2

# Print the points in each box after 364 days
print("Points after 364 days:")
print("Box A:", points_a.numpy())
print("Box B:", points_b.numpy())
print("Box C:", points_c.numpy())
print("Box D:", points_d.numpy())
##
##
def calculate_points(A, B, C, D, X, Y):
    for day in range(Y):
        points_B_to_A = (X/100) * B
        points_A_to_D = (X/100) * A
        points_D_to_C = (X/100) * D
        points_C_to_B = (X/100) * C

        A += points_B_to_A - points_A_to_D
        B += points_C_to_B - points_B_to_A
        C += points_A_to_D - points_D_to_C
        D += points_D_to_C - points_C_to_B

    return A, B, C, D

# Get input from the user
A = int(input("Enter the initial points in box A: "))
B = int(input("Enter the initial points in box B: "))
C = int(input("Enter the initial points in box C: "))
D = int(input("Enter the initial points in box D: "))
X = float(input("Enter the percentage of points transferred each day: "))
Y = int(input("Enter the number of days to calculate: "))

# Calculate the points on the Yth day
final_A, final_B, final_C, final_D = calculate_points(A, B, C, D, X, Y)

# Print the result
print(f"Points on the Yth day - A: {final_A}, B: {final_B}, C: {final_C}, D: {final_D}")

##

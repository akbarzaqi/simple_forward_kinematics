import math
import matplotlib.pyplot as plt

def calculate_distance(target_x, target_y):
    d = ((target_x ** 2) + (target_y ** 2)) ** 0.5
    print (f"The distance from the origin to the point ({target_x}, {target_y}) is: {d}")
    return d

def isTargetReachable(L1, L2, d):
    min_distance = abs(L1 - L2)
    max_distance = L1 + L2

    if min_distance <= d <= max_distance:
        print("The target is reachable.")
        return True
    else:
        print("The target is not reachable.")
        return False
    
def calculate_angle(L1, L2, d):
    if isTargetReachable(L1, L2, d):
        d2 = d ** 2
        L1_2 = L1 ** 2
        L2_2 = L2 ** 2
        print(f"d^2: {d2}, L1^2: {L1_2}, L2^2: {L2_2}")

        pembilang2 = d2 - L1_2 - L2_2
        print(f"pembilang2: {pembilang2}")

        penyebut2 = 2 * L1 * L2
        print(f"penyebut2: {penyebut2}")

        cos_theta2 = pembilang2 / penyebut2
        print(f"cos(theta2): {cos_theta2}")

        theta2 = math.degrees(math.acos(cos_theta2))
        print(f"theta2 (in radians): {theta2}")
        return theta2

def calculate_solution(x_target, y_target, L1, L2, theta2):
    alpha = math.degrees(math.atan2(y_target, x_target))
    print(f"alpha (in radians): {alpha}")

    l2_sin_theta2 = L2 * math.sin(math.radians(theta2))
    print(f"L2 * sin(theta2): {l2_sin_theta2}")

    l2_cos_theta2 = L2 * math.cos(math.radians(theta2))
    print(f"L2 * cos(theta2): {l2_cos_theta2}")

    reachable_x = L1 + l2_cos_theta2
    print(f"Reachable x-coordinate: {reachable_x}")

    beta = math.degrees(math.atan2(l2_sin_theta2, reachable_x))
    print(f"beta (in radians): {beta}")

    theta1 = alpha - beta
    print(f"theta1 (in radians): {theta1}")

    return theta1, theta2

def validation_kinematics(L1, L2, theta1, theta2):
    sum_theta = theta1 + theta2
    print(f"Sum of theta1 and theta2: {sum_theta}")

    x = L1 * math.cos(math.radians(theta1)) + L2 * math.cos(math.radians(sum_theta))
    y = L1 * math.sin(math.radians(theta1)) + L2 * math.sin(math.radians(sum_theta))
    print(f"Calculated position: ({x}, {y})")


def visualization(L1, L2, theta1, theta2):
    sum_theta = theta1 + theta2

    x0, y0 = 0, 0
    x1 = L1 * math.cos(math.radians(theta1))
    y1 = L1 * math.sin(math.radians(theta1))
    x2 = x1 + L2 * math.cos(math.radians(sum_theta))
    y2 = y1 + L2 * math.sin(math.radians(sum_theta))

    plt.plot([x0, x1], [y0, y1], 'ro-') 
    plt.plot([x1, x2], [y1, y2], 'bo-') 
    plt.xlim(-L1 - L2 - 10, L1 + L2 + 10)
    plt.ylim(-L1 - L2 - 10, L1 + L2 + 10)
    plt.title("Two-Link Planar Robot Arm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    x_tar = 100
    y_tar = 20
    d = calculate_distance(x_tar, y_tar)

    L1 = 100
    L2 = 80

    theta2 = calculate_angle(L1, L2, d)
    theta1, theta2 = calculate_solution(x_tar, y_tar, L1, L2, theta2)
    validation_kinematics(L1, L2, theta1, theta2)
    visualization(L1, L2, theta1, theta2)


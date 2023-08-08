import math

def cone_volume():
        height = float(input("Enter the height of the cone: "))
        radius = float(input("Enter the radius of the cone: "))
        
        volume = (1/3) * math.pi * radius**2 * height
        return volume

result = cone_volume()
print(f"The volume of the cone is: {round(result, 2)}")

#calculating volume and surface of a cube

user_input = float(input('Input the edge of a cube: '))

volume = pow(user_input,3)
surface = (6*user_input**2)

print(f"The volume of a cube is {volume} and the surface is {surface}")
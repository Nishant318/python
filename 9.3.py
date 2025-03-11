# 3. Function to create a 3D array
def create_3d_array(x,y,z,value):
    return[[[value for _ in range(z)]
            for _ in range(y)] for _ in range(x)]
array = create_3d_array(3,4,5,7)
for layer in array:
    print(layer)

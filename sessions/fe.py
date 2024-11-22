import numpy as np

def shape_from_xi(xi):
    N = np.zeros(3)
    N[0] = 1 - xi[0] - xi[1]
    N[1] = xi[0]
    N[2] = xi[1]

    return N

# Now define many more functions...

if __name__ == "__main__":
    print(shape_from_xi([0, 1]))
    


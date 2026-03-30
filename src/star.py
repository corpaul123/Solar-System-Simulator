import numpy as np

def star():
    starDict = {}
    mFinal = 1e30
    starName = input("Input name of star: ")
    mass = float(input("Input mass of star (in 10 ^ 30 kg, Sun's mass = 1.9): "))
    actualMass = mass * mFinal
    print(f"Star name is {starName}")
    starDict = {starName : {
            "mass" : actualMass,
            "pos" : np.array([0,0], dtype = float),
            "v" : np.array([0,0], dtype = float)}
        }
    
    print("Star information")
    print(starDict)

    return starDict

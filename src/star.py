def star():
    starDict = {}
    mFinal = pow(10, 30)
    starName = input("Input name of star: ")
    mass = float(input("Input mass of star (in 10 ^ 30 kg, Sun's mass = 1.9): "))
    actualMass = mass * mFinal
    print(f"Star name is {starName}")
    starDict = {starName : {
            "mass" : actualMass,
            "pos" : [0,0],
            "v" : [0,0]}
        }
    
    print("Star information")
    print(starDict)

    return starDict

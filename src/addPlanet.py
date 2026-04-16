import numpy as np
    

def addPlanet(planets, starDict, radiSet):

 # constants for conversion
    AU = 1.496e11
    mFinal = 1e24
    starMass = list(starDict.values())[0]["mass"]
#Gravitational Constant
    G = 6.6743e-11
    planetName = input("Input planet name: ")
#user input
    inputMass = float(input("Input planet mass (10 ^ 24 kg, Earth mass = 5.98): "))
    done = False
    while(done != True):
    
        inputDistance = float(input("Input planet's distance from star in AU(1 AU = 1.496e11 m): "))
        if inputDistance in radiSet:
            print("Overlapping planets are not allowed")
        else:
            done = True
#convert input into usable data
    radiSet.add(inputDistance)
    actualDistance = inputDistance * AU
    actualMass = inputMass * mFinal
    v_mag = np.sqrt(G * starMass / actualDistance)
    planets[planetName] = {
        "mass" : actualMass,
        "pos" : np.array([actualDistance, 0], dtype = float),
        "v" : np.array([0,v_mag], dtype = float)
    }

    return planets, radiSet
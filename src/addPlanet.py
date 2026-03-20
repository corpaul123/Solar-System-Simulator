
def addPlanet(planets):

    AU = 1.496 * pow(10, 11)
    mFinal = pow(10, 24)

    planetName = input("Input planet name: ")

    inputMass = float(input("Input planet mass (10 ^ 24 kg, Earth mass = 5.98): "))
    inputDistance = float(input("Input planet's distance from star in AU(1 AU = 1.496 x 10^11 m): "))

    actualDistance = inputDistance * AU
    actualMass = inputMass * mFinal
    planets[planetName] = {
        "mass" : actualMass,
        "pos" : [actualDistance, 0],
        "v" : [0,0]
    }

    return planets
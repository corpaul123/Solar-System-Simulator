
def addPlanet(planets):

    planetName = input("Input planet name: ")

    mass = input("Input planet mass (10 ^ 24 kg): ")
    radius = input("Input radius of planet (10 ^ -3 km): ")
    distance = input("Input planet's distance from star (10 ^ 8): ")

    planets[planetName] = {
        "mass" : mass,
        "radius" : radius,
        "distance" : distance
    }

    return planets
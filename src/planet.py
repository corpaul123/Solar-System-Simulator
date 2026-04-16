from addPlanet import addPlanet

def planets(starDict):
    planetsDict = {}
    radiSet = set()

    print("ready for planets")
    done = False
    while done == False:
        planetNum = int(input("Input number of planets: "))
        if planetNum > 0 and planetNum < 20:
            done = True
        else:
            print("Please enter valid planet amount.")
    
    for i in range(planetNum):
        addPlanet(planetsDict, starDict, radiSet)
    print("Here is planet data")
    print(planetsDict)

    return planetsDict





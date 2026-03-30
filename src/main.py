
from planet import planets
from star import star
from common import System

if __name__ == "__main__":
    print("Simulation Ready")
    starDict = star()
    planetsDict = planets(starDict)

    bodies = {**starDict, **planetsDict}
    particleNum = len(bodies)


    print("num of bodies:")
    print(particleNum)


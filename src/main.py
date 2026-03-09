
from planet import planets
from star import star

if __name__ == "__main__":
    print("Simulation Ready")
    starDict = star()
    planetsDict = planets()

    bodies = {**starDict, **planetsDict}
    particleNum = len(bodies)


    print("num of bodies:")
    print(particleNum)


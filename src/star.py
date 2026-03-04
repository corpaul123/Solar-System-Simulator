def star():
    star = {}
    starName = input("Input name of star: ")
    mass = input("Input mass of star (in 10 ^ 30 kg): ")
    print(f"Star name is {starName}")
    star = {"name" : starName,
            "mass" : mass}
    
    print("Star information")
    print(star)

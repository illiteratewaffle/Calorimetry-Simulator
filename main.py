from material import Material
from calorimeter import Calorimeter

MATERIALS = ["Water", "Aluminum", "Copper", "Iron", "Lead", "Silver", "Gold", "Ethanol", "Benzene", "Methanol", "Acetone", "Hexane", "Toluene", "Acetonitrile"]

def main():

    compound1, compound2 = userInput()

    calorimeter = Calorimeter(compound1, compound2)
    finalTemp = calorimeter.getFinalTemperature()

    print(finalTemp)

def userInput():
    print("Choose the materials for a calorimetry experiment: ")
    print("Available materials: ")
    for material in MATERIALS:
        print(material)

    compound1 = input("Choose compound 1: ")
    if compound1 not in MATERIALS:
        print("Invalid compound 1. Refer to the list of available materials.")
    else:
        compound1 = Material(compound1)
    mass = int(input("Mass of compound 1 (grams): "))
    compound1.setMass(mass)
    temperature = int(input("Temperature of compound 1 (Kelvin): "))
    compound1.temperature = temperature

    compound2 = input("Choose compound 2: ")
    if compound2 not in MATERIALS:
        print("Invalid compound 2. Refer to the list of available materials.")
    else:
        compound2 = Material(compound2)
    mass = int(input("Mass of compound 2 (grams): "))
    compound2.setMass(mass)
    temperature = int(input("Temperature of compound 2 (Kelvin): "))
    compound2.temperature = temperature

    return compound1, compound2

main()
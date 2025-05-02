from material import Material
from calorimeter import Calorimeter

MATERIALS = ["Water", "Aluminum", "Copper", "Iron", "Lead", "Silver", "Gold", "Ethanol", "Benzene", "Methanol",
             "Acetone", "Hexane", "Toluene", "Acetonitrile"]


def main():
    compound1, compound2 = userChooseMaterial()

    calorimeter = Calorimeter(compound1, compound2)

    heatCapacity = userChooseAccuracy()

    if heatCapacity == "A":
        finalTemp = calorimeter.getRealFinalTemperature(compound1, compound2)
    else:  #heatCapacity == "B"
        finalTemp = calorimeter.getIdealFinalTemperature(compound1, compound2)

    print(finalTemp - 273.15)


def userChooseMaterial():
    print("Choose the materials for a calorimetry experiment: ")
    print("Available materials: ")
    for material in MATERIALS:
        print(material)

    compound1 = input("Choose compound 1: ").capitalize()
    if compound1 not in MATERIALS:
        print("Invalid compound 1. Refer to the list of available materials.")
    else:
        compound1 = Material(compound1)
    mass = int(input("Mass of compound 1 (grams): "))
    compound1.setMass(mass)
    temperature = int(input("Temperature of compound 1 (Celsius): "))
    compound1.setTemperature(temperature)

    compound2 = input("Choose compound 2: ").capitalize()
    if compound2 not in MATERIALS:
        print("Invalid compound 2. Refer to the list of available materials.")
    else:
        compound2 = Material(compound2)
    mass = int(input("Mass of compound 2 (grams): "))
    compound2.setMass(mass)
    temperature = int(input("Temperature of compound 2 (Celsius): "))
    compound2.setTemperature(temperature)

    return compound1, compound2


def userChooseAccuracy():
    print("Choose the accuracy of a calorimetry experiment: ")
    print("""Available accuracies: "Temperature dependent heat capacity" or "Temperature independent heat capacity" """)
    print("""Type "A" for temperature dependent, "B" for temperature independent """)

    approximationChoice = input("Choose the accuracy approximation: ").capitalize()
    if approximationChoice == "A":
        return "Independent"
    else:  #approximationChoice == "B"
        return "Dependent"


main()
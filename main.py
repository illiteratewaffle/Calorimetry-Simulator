from material import Material
from calorimeter import Calorimeter

def main():

    compound1 = Material("water")
    compound1.mass = 100
    compound1.moles = compound1.mass / compound1.molarMass
    compound1.temperature = 300

    compound2 = Material("water")
    compound2.mass = 100
    compound2.moles = compound2.mass / compound2.molarMass
    compound2.temperature = 200

    calorimeter = Calorimeter(compound1, compound2)
    finalTemp = calorimeter.getFinalTemperature()

    print(finalTemp)

main()
from material import Material
from calorimeter import Calorimeter

def main():

    compound1 = Material("lead")
    compound1.setMass(100)
    compound1.temperature = 1000

    compound2 = Material("water")
    compound2.setMass(100)
    compound2.temperature = 0

    calorimeter = Calorimeter(compound1, compound2)
    finalTemp = calorimeter.getFinalTemperature()

    print(finalTemp)

main()
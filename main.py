from material import Material
from calorimeter import Calorimeter

water = Material(name='Water')
water.temperature = 273
water.moles = 1
water.Cp = 4.18
water.boilingPoint = 373.15
water.meltingPoint = 273.15

beer = Material(name='beer')
beer.temperature = 373
beer.moles = 1
beer.Cp = 4.18
beer.boilingPoint = 373.15
beer.meltingPoint = 273.15

calorimeter = Calorimeter(water, beer)
finalTemp = calorimeter.getFinalTemperature(water,beer)

print(finalTemp)

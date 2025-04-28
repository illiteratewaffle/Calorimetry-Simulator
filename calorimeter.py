class Calorimeter:

    def __init__(self, compound1, compound2, condition = "PRESSURE"):

        self.compound1 = compound1
        self.compound2 = compound2
        self.condition = condition

    def begin(self):
        finalTemp = self.getFinalTemperature(self.compound1, self.compound2)
        return finalTemp

    def getHotter(self, compound1, compound2):
        if compound1.temperature > compound2.temperature:
            return compound1
        else:
            return compound2

    def getFinalTemperature(self, compound1, compound2):
        n1 = compound1.moles
        n2 = compound2.moles
        ti_1 = compound1.temperature
        ti_2 = compound2.temperature
        if self.condition == "PRESSURE":
            c1 = compound1.Cp
            c2 = compound2.Cp
        else: #self.condition == "VOLUME"
            c1 = compound1.Cv
            c2 = compound2.Cv

        tf = ((n1*c1*ti_1) + (n2*c2*ti_2)) / ((n1*c1) + (n2*c2))

        return tf
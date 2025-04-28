class Material:

    def __init__(self, name):

        self.name = name
        self.temperature = None
        self.weight = None
        self.molarMass = None
        self.moles = None
        self.Cp = None
        self.Cv = None
        self.boilingPoint = None
        self.meltingPoint = None

        self.heat = None
        self.state = None

    def heat_p(self):
        self.heat = self.moles * self.Cp * self.temperature

    def heat_v(self):
        self.heat = self.molarMass * self.Cv * self.temperature

    def state(self):
        if (self.temperature < self.meltingPoint):
            self.state = "SOLID"
        elif (self. temperature > self.boilingPoint):
            self.state = "GAS"
        elif ((self.temperature > self.meltingPoint) and (self.temperature < self.boilingPoint)):
            self.state = "LIQUID"
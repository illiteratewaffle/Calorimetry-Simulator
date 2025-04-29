from scipy.integrate import quad
from scipy.optimize import fsolve

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

    def getFinalTemperature(self):

        m1, m2 = self.compound1.mass, self.compound2.mass
        Ti1, Ti2 = self.compound1.temperature, self.compound2.temperature

        if self.condition.upper() == "PRESSURE":
            Cp1, Cp2 = self.compound1.Cp, self.compound2.Cp  # J/g*K
        else:  # “VOLUME”
            Cp1, Cp2 = self.compound1.Cv, self.compound2.Cv

        # function from chatgpt because i dont know how to do integrals in python
        def energy_balance(Tf):
            q1, _ = quad(Cp1, Ti1, Tf)
            q2, _ = quad(Cp2, Ti2, Tf)
            return m1 * q1 + m2 * q2

        Tf_guess = 0.5 * (Ti1 + Ti2)
        return fsolve(energy_balance, Tf_guess)[0]


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

        n1, n2 = self.compound1.moles, self.compound2.moles
        Ti1, Ti2 = self.compound1.temperature, self.compound2.temperature

        if self.condition.upper() == "PRESSURE":
            C1, C2 = self.compound1.Cp, self.compound2.Cp
        else:  # "VOLUME"
            C1, C2 = self.compound1.Cv, self.compound2.Cv

        def energy_balance(Tf):

            q1, _ = quad(C1, Ti1, Tf)
            q2, _ = quad(C2, Ti2, Tf)
            return n1 * q1 + n2 * q2

        Tf_guess = 0.5 * (Ti1 + Ti2)
        Tf_final = fsolve(energy_balance, Tf_guess)[0]

        return Tf_final


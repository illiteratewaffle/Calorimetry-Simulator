from scipy.integrate import quad
from scipy.optimize import fsolve

class Calorimeter:

    def __init__(self, compound1, compound2, condition = "PRESSURE"):

        self.compound1 = compound1
        self.compound2 = compound2
        self.condition = condition

    def getHotter(self, compound1, compound2):
        """
        Method to find hotter material
        :param compound1:
        :param compound2:
        :return: the hotter material
        """
        if compound1.temperature > compound2.temperature:
            return compound1
        else:
            return compound2

    def getRealFinalTemperature(self):
        """
        Method to find final temperature
        :return: final temperature
        """

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

    def getIdealFinalTemperature(self, compound1, compound2):
        n1 = compound1.moles
        n2 = compound2.moles
        ti_1 = compound1.temperature
        ti_2 = compound2.temperature
        if self.condition == "PRESSURE":
            c1 = self.compound1.Cp(0)
            c2 = self.compound2.Cp(0)
        else: #self.condition == "VOLUME"
            c1 = self.compound1.Cv(0)
            c2 = self.compound2.Cv(0)

        tf = ((n1*c1*ti_1) + (n2*c2*ti_2)) / ((n1*c1) + (n2*c2))

        return tf
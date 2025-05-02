
from integral import Integral


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

    def getRealFinalTemperature(self, step=0.1):

        m1, m2   = self.compound1.mass, self.compound2.mass
        Ti1, Ti2 = self.compound1.temperature, self.compound2.temperature

        # choose the right Cp(T) functions
        if self.condition.upper() == "PRESSURE":
            Cp1, Cp2 = self.compound1.Cp, self.compound2.Cp
        else:  # "VOLUME"
            Cp1, Cp2 = self.compound1.Cv, self.compound2.Cv

        def net_heat(Tf):
            q1 = Integral.integrate(Cp1, Ti1, Tf)
            q2 = Integral.integrate(Cp2, Ti2, Tf)
            return m1*q1 + m2*q2

        # linear scan from the colder to the hotter material from chatgpt
        loT, hiT = sorted((Ti1, Ti2))
        prev_T   = loT
        prev_Q   = net_heat(prev_T)

        steps = int((hiT - loT) / step) + 1
        for k in range(1, steps + 1):
            T = loT + k*step
            Q = net_heat(T)
            if prev_Q == 0:       # exact
                return prev_T
            if prev_Q * Q < 0:    # sign changed ⇒ root between prev_T and T
                # single linear interpolation for a better estimate
                return prev_T + (T - prev_T) * (-prev_Q) / (Q - prev_Q)
            prev_T, prev_Q = T, Q

        # fallback: energies never crossed zero (should not happen with good data)
        return (Ti1 + Ti2) * 0.5
        # ====

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
from material import Material

MATERIALS = ["Water", "Aluminum", "Copper", "Iron", "Lead", "Silver", "Gold", "Ethanol", "Benzene", "Methanol",
             "Acetone", "Hexane", "Toluene", "Acetonitrile"]

class HeatTransfer:

    def __init__(self, material, condition="PRESSURE"):
        self.material = material
        self.condition = condition.upper()

        if self.condition not in ("PRESSURE", "VOLUME"):
            print("condition must be 'PRESSURE' or 'VOLUME'")

        # Use constant Cp or Cv evaluated at the material's initial temperature
        self.C_const = material.Cp(material.temperature) if self.condition == "PRESSURE" else material.Cv(material.temperature)


    # Given heat, find final temperature
    def final_temperature(self, Q):
        """
        Add heat Q (joules) and return the new temperature (K) using temperature-independent heat capacity.
        """
        m = self.material.mass
        Ti = self.material.temperature
        dT = Q / (m * self.C_const)
        return Ti + dT


    # Given final temperature, find heat required
    def heat_required(self, Tf):
        """
        Return the heat (J) required to move the material from its current temperature to Tf (Kelvin).
        Positive result: heat must be added
        Negative result: heat must be removed
        """
        m = self.material.mass
        Ti = self.material.temperature
        dT = Tf - Ti
        return m * self.C_const * dT

def setMaterial():
    water = Material("Water")
    water.setMass(250) # grams
    water.setTemperature(20)    # celsius

    transfer = HeatTransfer(water, condition="PRESSURE")

    # 1) add 15 kJ of heat and find the final temperature
    Tf = transfer.final_temperature(15000)
    print("Final T:", Tf - 273.15, "°C")

    # 2) cool it back down to 25°C – how much heat must we remove?
    Q_needed = transfer.heat_required(298.15)
    print("Remove:", -Q_needed/1000, "kJ")

    # todo: add/remove heat and find final temperature

    # todo: change temperature and find how much heat was transferred to the system

setMaterial()
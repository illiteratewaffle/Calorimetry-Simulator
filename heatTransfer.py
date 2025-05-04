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

class GetInput:

    def setMaterial(self):

        print("List of Materials: ", MATERIALS)

        choice = input("Enter material name: ").capitalize()
        material = Material(choice)

        choice = float(input("Enter material mass (grams): "))
        material.setMass(choice)  # grams

        choice = float(input("Enter material temperature (Celsius): "))
        material.setTemperature(choice)  # celsius

        condition = input("Constant pressure (P) or constant volume (V): ").capitalize()
        if condition == "P":
            transfer = HeatTransfer(material, condition="PRESSURE")
            return transfer
        elif condition == "V":
            transfer = HeatTransfer(material, condition="VOLUME")
            return transfer
        else:
            print("Invalid condition. Refer to the list of available conditions.")
            return None

    def addHeat(self, transfer):
        heatToAdd = float(input("How much heat, in Joules, do you want to add to the system?"))
        Tf = transfer.final_temperature(heatToAdd)
        print("Final T:", Tf - 273.15, "°C")

    def findHeat(self, transfer):
        heatRequired = 273.15 + float(input("Enter a temperature, in Celsius, to find how much heat is required to reach that temperature"))

        Q_needed = transfer.heat_required(heatRequired)
        print("Add: ", Q_needed / 1000, " kJ")
        print("Negative Q means system is to lose energy")

    def run(self):
        heatParameters = GetInput().setMaterial()
        self.findHeat(heatParameters)
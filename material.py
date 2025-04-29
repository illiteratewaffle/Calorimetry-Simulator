

class Material:

    # Dictionaries for physical properties
    # g/mol
    molar_masses = {
        "Water": 18.015,
        "Aluminum": 26.982,
        "Copper": 63.546,
        "Iron": 55.845,
        "Lead": 207.2,
        "Silver": 107.868,
        "Gold": 196.967,
        "Ethanol": 46.07,
        "Benzene": 78.11,
        "Methanol": 32.04,
        "Acetone": 58.08,
        "Hexane": 86.18,
        "Toluene": 92.14,
        "Acetonitrile": 41.05,
    }

    # Kelvin
    boiling_points = {
        "Water": 373.15,
        "Aluminum": 2743.15,
        "Copper": 2835.15,
        "Iron": 3135.15,
        "Lead": 2022.15,
        "Silver": 2435.15,
        "Gold": 3129.15,
        "Ethanol": 351.52,
        "Benzene": 353.25,
        "Methanol": 337.85,
        "Acetone": 329.15,
        "Hexane": 341.85,
        "Toluene": 383.75,
        "Acetonitrile": 354.75,
    }

    # Kelvin
    melting_points = {
        "Water": 273.15,
        "Aluminum": 933.15,
        "Copper": 1358.15,
        "Iron": 1811.15,
        "Lead": 600.15,
        "Silver": 1234.15,
        "Gold": 1337.15,
        "Ethanol": 159.15,
        "Benzene": 278.65,
        "Methanol": 175.55,
        "Acetone": 178.15,
        "Hexane": 178.15,
        "Toluene": 178.15,
        "Acetonitrile": 228.15,
    }

    # J/mol
    enthalpy_of_fusion = {
        "Water": 6.01*1000,
        "Aluminum": 10.71*1000,
        "Copper": 13.05*1000,
        "Iron": 13.81*1000,
        "Lead": 4.77*1000,
        "Silver": 11.3*1000,
        "Gold": 12.55*1000,
        "Ethanol": 4.9*1000,
        "Benzene": 9.87*1000,
        "Methanol": 3.22*1000,
        "Acetone": 5.69*1000,
        "Hexane": 8.94*1000,
        "Toluene": 6.64*1000,
        "Acetonitrile": 5.76*1000,
    }

    # J/mol
    enthalpy_of_vaporization = {
        "Water": 40.7*1000,
        "Aluminum": 293*1000,
        "Copper": 300*1000,
        "Iron": 349*1000,
        "Lead": 178*1000,
        "Silver": 254*1000,
        "Gold": 334*1000,
        "Ethanol": 38.6*1000,
        "Benzene": 30.8*1000,
        "Methanol": 35.3*1000,
        "Acetone": 31.3*1000,
        "Hexane": 28.9*1000,
        "Toluene": 38.0*1000,
        "Acetonitrile": 31.3*1000,
    }

    # Cp functions
    def Cp_Water(self, T):
        return (4.179) + (-1.2e-4) * T + (8.0e-7) * T ** 2 + (-3.0e-9) * T ** 3 + (9.0e-12) * T ** 4 + (
            -1.5e-14) * T ** 5 + (1.2e-17) * T ** 6 + (-5.0e-21) * T ** 7 + (8.0e-25) * T ** 8

    def Cp_Aluminum(self, T):
        return (0.897) + (2.4e-5) * T + (-1.1e-7) * T ** 2 + (5.0e-10) * T ** 3 + (-1.5e-12) * T ** 4 + (
            2.5e-15) * T ** 5 + (-2.0e-18) * T ** 6 + (7.0e-22) * T ** 7 + (-1.0e-25) * T ** 8

    def Cp_Copper(self, T):
        return (0.385) + (1.5e-5) * T + (-7.0e-8) * T ** 2 + (3.0e-10) * T ** 3 + (-9.0e-13) * T ** 4 + (
            1.5e-15) * T ** 5 + (-1.2e-18) * T ** 6 + (5.0e-22) * T ** 7 + (-7.0e-26) * T ** 8

    def Cp_Iron(self, T):
        return (0.449) + (2.0e-5) * T + (-9.0e-8) * T ** 2 + (4.0e-10) * T ** 3 + (-1.2e-12) * T ** 4 + (
            2.0e-15) * T ** 5 + (-1.6e-18) * T ** 6 + (6.0e-22) * T ** 7 + (-9.0e-26) * T ** 8

    def Cp_Lead(self, T):
        return (0.128) + (1.0e-5) * T + (-5.0e-8) * T ** 2 + (2.0e-10) * T ** 3 + (-7.0e-13) * T ** 4 + (
            1.0e-15) * T ** 5 + (-8.0e-19) * T ** 6 + (3.0e-22) * T ** 7 + (-5.0e-26) * T ** 8

    def Cp_Silver(self, T):
        return (0.235) + (1.2e-5) * T + (-6.0e-8) * T ** 2 + (2.5e-10) * T ** 3 + (-8.0e-13) * T ** 4 + (
            1.3e-15) * T ** 5 + (-1.0e-18) * T ** 6 + (4.0e-22) * T ** 7 + (-6.0e-26) * T ** 8

    def Cp_Gold(self, T):
        return (0.129) + (1.0e-5) * T + (-5.0e-8) * T ** 2 + (2.0e-10) * T ** 3 + (-7.0e-13) * T ** 4 + (
            1.0e-15) * T ** 5 + (-8.0e-19) * T ** 6 + (3.0e-22) * T ** 7 + (-5.0e-26) * T ** 8

    def Cp_Ethanol(self, T):
        return (2.44) + (-2.0e-4) * T + (1.5e-6) * T ** 2 + (-6.0e-9) * T ** 3 + (2.0e-11) * T ** 4 + (
            -4.0e-14) * T ** 5 + (3.5e-17) * T ** 6 + (-1.5e-20) * T ** 7 + (2.5e-24) * T ** 8

    def Cp_Benzene(self, T):
        return (1.74) + (-1.5e-4) * T + (1.0e-6) * T ** 2 + (-4.0e-9) * T ** 3 + (1.5e-11) * T ** 4 + (
            -3.0e-14) * T ** 5 + (2.5e-17) * T ** 6 + (-1.0e-20) * T ** 7 + (1.8e-24) * T ** 8

    def Cp_Methanol(self, T):
        return (2.51) + (-2.2e-4) * T + (1.6e-6) * T ** 2 + (-6.5e-9) * T ** 3 + (2.0e-11) * T ** 4 + (
            -4.2e-14) * T ** 5 + (3.8e-17) * T ** 6 + (-1.5e-20) * T ** 7 + (2.6e-24) * T ** 8

    def Cp_Acetone(self, T):
        return (2.18) + (-1.9e-4) * T + (1.4e-6) * T ** 2 + (-5.5e-9) * T ** 3 + (2.0e-11) * T ** 4 + (
            -3.8e-14) * T ** 5 + (3.2e-17) * T ** 6 + (-1.3e-20) * T ** 7 + (2.1e-24) * T ** 8

    def Cp_Hexane(self, T):
        return (2.26) + (-2.1e-4) * T + (1.5e-6) * T ** 2 + (-6.0e-9) * T ** 3 + (2.1e-11) * T ** 4 + (
            -4.0e-14) * T ** 5 + (3.4e-17) * T ** 6 + (-1.4e-20) * T ** 7 + (2.4e-24) * T ** 8

    def Cp_Toluene(self, T):
        return (1.71) + (-1.4e-4) * T + (9.0e-7) * T ** 2 + (-3.5e-9) * T ** 3 + (1.2e-11) * T ** 4 + (
            -2.5e-14) * T ** 5 + (2.0e-17) * T ** 6 + (-8.0e-21) * T ** 7 + (1.4e-24) * T ** 8

    def Cp_Acetonitrile(self, T):
        return (2.20) + (-2.0e-4) * T + (1.5e-6) * T ** 2 + (-5.8e-9) * T ** 3 + (2.0e-11) * T ** 4 + (
            -3.7e-14) * T ** 5 + (3.1e-17) * T ** 6 + (-1.2e-20) * T ** 7 + (2.0e-24) * T ** 8

    # Cv functions
    def Cv_Water(self, T):
        return (3.13) + (-1.0e-4) * T + (6.5e-7) * T ** 2 + (-2.5e-9) * T ** 3 + (8.0e-12) * T ** 4 + (
            -1.2e-14) * T ** 5 + (1.0e-17) * T ** 6 + (-4.0e-21) * T ** 7 + (7.0e-25) * T ** 8

    def Cv_Aluminum(self, T):
        return (0.650) + (1.7e-5) * T + (-8.0e-8) * T ** 2 + (3.5e-10) * T ** 3 + (-1.0e-12) * T ** 4 + (
            1.7e-15) * T ** 5 + (-1.4e-18) * T ** 6 + (5.0e-22) * T ** 7 + (-8.0e-26) * T ** 8

    def Cv_Copper(self, T):
        return (0.276) + (1.0e-5) * T + (-5.0e-8) * T ** 2 + (2.0e-10) * T ** 3 + (-6.0e-13) * T ** 4 + (
            1.0e-15) * T ** 5 + (-8.0e-19) * T ** 6 + (3.0e-22) * T ** 7 + (-5.0e-26) * T ** 8

    def Cv_Iron(self, T):
        return (0.321) + (1.4e-5) * T + (-6.0e-8) * T ** 2 + (2.5e-10) * T ** 3 + (-8.0e-13) * T ** 4 + (
            1.4e-15) * T ** 5 + (-1.1e-18) * T ** 6 + (4.0e-22) * T ** 7 + (-7.0e-26) * T ** 8

    def Cv_Lead(self, T):
        return (0.091) + (7.0e-6) * T + (-3.0e-8) * T ** 2 + (1.5e-10) * T ** 3 + (-5.0e-13) * T ** 4 + (
            8.0e-16) * T ** 5 + (-6.0e-19) * T ** 6 + (2.0e-22) * T ** 7 + (-4.0e-26) * T ** 8

    def Cv_Silver(self, T):
        return (0.170) + (8.0e-6) * T + (-4.0e-8) * T ** 2 + (1.8e-10) * T ** 3 + (-6.0e-13) * T ** 4 + (
            1.0e-15) * T ** 5 + (-7.0e-19) * T ** 6 + (3.0e-22) * T ** 7 + (-5.0e-26) * T ** 8

    def Cv_Gold(self, T):
        return (0.092) + (7.0e-6) * T + (-3.0e-8) * T ** 2 + (1.5e-10) * T ** 3 + (-5.0e-13) * T ** 4 + (
            8.0e-16) * T ** 5 + (-6.0e-19) * T ** 6 + (2.0e-22) * T ** 7 + (-4.0e-26) * T ** 8

    def Cv_Ethanol(self, T):
        return (1.78) + (-1.5e-4) * T + (1.1e-6) * T ** 2 + (-4.5e-9) * T ** 3 + (1.5e-11) * T ** 4 + (
            -3.0e-14) * T ** 5 + (2.6e-17) * T ** 6 + (-1.1e-20) * T ** 7 + (2.0e-24) * T ** 8

    def Cv_Benzene(self, T):
        return (1.24) + (-1.0e-4) * T + (7.0e-7) * T ** 2 + (-3.0e-9) * T ** 3 + (1.0e-11) * T ** 4 + (
            -2.0e-14) * T ** 5 + (1.7e-17) * T ** 6 + (-7.0e-21) * T ** 7 + (1.2e-24) * T ** 8

    def Cv_Methanol(self, T):
        return (1.83) + (-1.7e-4) * T + (1.2e-6) * T ** 2 + (-5.0e-9) * T ** 3 + (1.6e-11) * T ** 4 + (
            -3.5e-14) * T ** 5 + (3.0e-17) * T ** 6 + (-1.2e-20) * T ** 7 + (2.0e-24) * T ** 8

    def Cv_Acetone(self, T):
        return (1.65) + (-1.4e-4) * T + (1.0e-6) * T ** 2 + (-4.0e-9) * T ** 3 + (1.5e-11) * T ** 4 + (
            -2.9e-14) * T ** 5 + (2.4e-17) * T ** 6 + (-9.0e-21) * T ** 7 + (1.6e-24) * T ** 8

    def Cv_Hexane(self, T):
        return (1.73) + (-1.6e-4) * T + (1.1e-6) * T ** 2 + (-4.5e-9) * T ** 3 + (1.6e-11) * T ** 4 + (
            -3.2e-14) * T ** 5 + (2.6e-17) * T ** 6 + (-1.0e-20) * T ** 7 + (1.8e-24) * T ** 8

    def Cv_Toluene(self, T):
        return (1.22) + (-1.0e-4) * T + (6.5e-7) * T ** 2 + (-2.5e-9) * T ** 3 + (9.0e-12) * T ** 4 + (
            -1.8e-14) * T ** 5 + (1.5e-17) * T ** 6 + (-6.0e-21) * T ** 7 + (1.0e-24) * T ** 8

    def Cv_Acetonitrile(self, T):
        return (1.67) + (-1.5e-4) * T + (1.1e-6) * T ** 2 + (-4.3e-9) * T ** 3 + (1.5e-11) * T ** 4 + (
            -2.8e-14) * T ** 5 + (2.3e-17) * T ** 6 + (-9.0e-21) * T ** 7 + (1.6e-24) * T ** 8

    # Cp and Cv function dictionaries
    # J/g*K
    cp_functions = {
        "Water": Cp_Water,
        "Aluminum": Cp_Aluminum,
        "Copper": Cp_Copper,
        "Iron": Cp_Iron,
        "Lead": Cp_Lead,
        "Silver": Cp_Silver,
        "Gold": Cp_Gold,
        "Ethanol": Cp_Ethanol,
        "Benzene": Cp_Benzene,
        "Methanol": Cp_Methanol,
        "Acetone": Cp_Acetone,
        "Hexane": Cp_Hexane,
        "Toluene": Cp_Toluene,
        "Acetonitrile": Cp_Acetonitrile,
    }

    # J/g*K
    cv_functions = {
        "Water": Cv_Water,
        "Aluminum": Cv_Aluminum,
        "Copper": Cv_Copper,
        "Iron": Cv_Iron,
        "Lead": Cv_Lead,
        "Silver": Cv_Silver,
        "Gold": Cv_Gold,
        "Ethanol": Cv_Ethanol,
        "Benzene": Cv_Benzene,
        "Methanol": Cv_Methanol,
        "Acetone": Cv_Acetone,
        "Hexane": Cv_Hexane,
        "Toluene": Cv_Toluene,
        "Acetonitrile": Cv_Acetonitrile,
    }

    def __init__(self, name):

        self.name = name.capitalize()
        self.temperature = None
        self.mass = None
        self.molarMass = None
        self.moles = None
        self.Cp = None
        self.Cv = None
        self.boilingPoint = None
        self.meltingPoint = None

        self.heat = None
        self.state = None

        self.Hfus = None
        self.HVap = None

        if self.name in Material.molar_masses:
            self.molarMass    = Material.molar_masses[self.name]
            self.boilingPoint = Material.boiling_points[self.name]
            self.meltingPoint = Material.melting_points[self.name]
            self.Hfus         = Material.enthalpy_of_fusion[self.name]
            self.HVap         = Material.enthalpy_of_vaporization[self.name]

            self.Cp = lambda T: Material.cp_functions[self.name](self, T)
            self.Cv = lambda T: Material.cv_functions[self.name](self, T)

    def state(self):
        if (self.temperature < self.meltingPoint):
            self.state = "SOLID"
        elif (self. temperature > self.boilingPoint):
            self.state = "GAS"
        elif ((self.temperature > self.meltingPoint) and (self.temperature < self.boilingPoint)):
            self.state = "LIQUID"


    def materialChoice(self, choice):
        """
        A database for materials and their physical properties.
        :param choice: (str) name of the material
        :return: Material object
        """
        choice_clean = choice.capitalize()

        if choice_clean not in Material.molar_masses:
            raise ValueError(f"Material '{choice}' not found in database.")

        material = Material(choice_clean)

        material.molarMass = Material.molar_masses[choice_clean]
        material.boilingPoint = Material.boiling_points[choice_clean]
        material.meltingPoint = Material.melting_points[choice_clean]
        material.Hfus = Material.enthalpy_of_fusion[choice_clean]
        material.HVap = Material.enthalpy_of_vaporization[choice_clean]
        material.Cp = lambda T: Material.cp_functions[choice_clean](self, T)
        material.Cv = lambda T: Material.cv_functions[choice_clean](self, T)

        return material



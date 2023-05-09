import pandas as pd
import numpy as np

class Inversor:
    def __init__(self, P_max, V_min, V_max) -> None:
        self.P_max = P_max
        self.V_min = V_min
        self.V_max = V_max

class Painel:
    def __init__(self, Pmax, Vmp, Imp, Voc, Isc, efficiency, Area) -> None:
        self.Pmax = Pmax
        self.Vmp = Vmp
        self.Imp = Imp
        self.Voc = Voc
        self.Isc = Isc
        self.efficiency = efficiency
        self.Area = Area

class Cliente:
    def __init__(self, Pot, HSP, E_mensal) -> None:
        self.P = Pot
        self.HSP = HSP
        self.E_mensal = E_mensal
        self.inversor = None
        self.painel = None

    def find_inversor(self):
        #Dicionario com inversores
        inversores = {
            "SE-3TL6k": {"Max pot": 6300, "Tensao Minima": 320, "Tensao Maxima": 800},
            "SE-3TL8K": {"Max pot": 8200, "Tensao Minima": 340, "Tensao Maxima": 800},
            "SE-3TL10K": {"Max pot": 10400, "Tensao Minima": 430, "Tensao Maxima": 800},
            "SE-3TL12KLV": {"Max pot": 12500, "Tensao Minima": 380, "Tensao Maxima": 800},
            "SE-3TL6KLV": {"Max pot": 6400, "Tensao Minima": 240, "Tensao Maxima": 800},
            "SE-3TL15KLV": {"Max pot": 15600, "Tensao Minima": 380, "Tensao Maxima": 800},
            "SE-3TL8KLV": {"Max pot": 8500, "Tensao Minima": 240, "Tensao Maxima": 800},
        }

        potencia_alvo = self.P * 1.2
        inversor_selecionado = None

        for nome, especificacoes in inversores.items():
            if especificacoes['Max pot'] >= potencia_alvo:
                if inversor_selecionado is None or especificacoes['Max pot'] < inversores[inversor_selecionado]['Max pot']:
                    inversor_selecionado = nome

        if inversor_selecionado is not None:
            especificacoes = inversores[inversor_selecionado]
            self.inversor = Inversor(especificacoes['Max pot'], especificacoes['Tensao Minima'], especificacoes['Tensao Maxima'])
            print(f"Inversor selecionado: {inversor_selecionado}")
        else:
            print("Foi escolhido o inversor com maior potencia.")
            especificacoes = inversores['SE-3TL15KLV']
            self.inversor = Inversor(especificacoes['Max pot'], especificacoes['Tensao Minima'], especificacoes['Tensao Maxima'])


    def choose_painel(self, Pmax=250, Vmp=30.1, Imp=8.30, Voc=37.2, Isc=8.87, efficiency=15.54*1e-2, Area = 1.61):
        #Caso nao se defina um outro painel, usar-se-á para fins academicos CS6P-250P
        self.painel = Painel(Pmax, Vmp, Imp, Voc, Isc, efficiency, Area)

    
    def find_string_number(self):
        V_min = self.inversor.V_min
        V_max = self.inversor.V_max
        V_oc = self.painel.Voc

        N_max = V_max/V_oc * 1.15
        N_min = V_min/V_oc * 1.15

        N_string = (N_max+N_min)/2

        return np.ceil(N_string)
    
    def find_modules_number(self):
        E_d = self.E_mensal/30
        P_pico = E_d/self.HSP

        Number_modules = np.ceil(P_pico/self.painel.Pmax)

        return Number_modules
    
    def necessary_area(self):
        module_number = self.find_modules_number()
        area_painel = self.painel.Area

        #FU e o fator de utilizacao
        FU=2.25
        area_fotovoltaica = area_painel*module_number*FU

        return area_fotovoltaica
    
if __name__ == "__main__":
    # Read the CSV file
    df = pd.read_csv('VMHospitais.csv')

    # Initialize an empty list to store the necessary area for each hospital
    necessary_areas = []
    carga_suprida = 0.5

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        # Create a Cliente object with the values from the CSV file
        hospital = Cliente(row['Demanda media'] * 1e3, row['HSP'], row['Consumo medio'] * 1e3 * carga_suprida)

        # Find the appropriate inverter and solar panel
        hospital.find_inversor()
        hospital.choose_painel()

        # Calculate the necessary area and append it to the list
        necessary_area = hospital.necessary_area()
        necessary_areas.append(necessary_area)

    # Add the necessary_areas list as a new column in the DataFrame
    df['Necessary Area'] = necessary_areas

    # Save the DataFrame with the new column as a CSV file
    df.to_csv('VMHospitais_with_areas.csv', index=False)

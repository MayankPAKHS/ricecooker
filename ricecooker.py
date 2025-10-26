import numpy             as np
import matplotlib.pyplot as plt
import math              as m
import json

# All preset variables in a dictionary
presets = {
    "m_rice": 0.15,          # kg, mass of dry rice
    "m_water": 0.25,         # kg, mass of water
    "n": 1,                  # mol of lithium ions transferred
    "F": 96485,              # C/mol, Faraday's constant
    "E_cathode": -3.04,      # V, cathode potential
    "E_anode": -2.71,        # V, anode potential
    "effectiveness": 0.80,   # electrical to thermal
    "A": 1e5,                # pre-exponential factor, arbitrary units
    "Ea": 110e3,             # activation energy, J/mol
    "R": 8.314,              # gas constant, J/(mol·K)
    "T_C": 100,              # temperature in Celsius
    "t": 120                 # seconds
}

with open("rice-spec.json", "w") as f:
    json.dump(presets, f, indent=4)

def load(json_preset):
    '''
    Loads a preset rice cooker schema
    '''
    global presets
    with open(json_preset, "r") as f:
        presets = json.load(f)

def derive(presets):
    '''
    Derives the variables from the preset rice cooker configuration
    '''
    global T, Q, k, thermal_energy, Thermal
    T = presets["T_C"] + 273.15
    Q = presets["n"] * presets["F"] * (presets["E_cathode"] - presets["E_anode"])
    Thermal = Q * presets["effectiveness"]
    k = presets["A"] * np.exp(-presets["Ea"] / (presets["R"] * T))
    thermal_energy = Thermal * presets["t"]

def dp():
    '''
    Prints the key derived values: Electrical energy, Thermal energy, Reaction rate, and
    cumulative Thermal energy after preset time.
    '''
    print(f"Electrical energy: {abs(Q):.2f} J")
    print(f"Thermal energy: {Thermal:.2f} J")
    print(f"Reaction rate: {k:.2e}")
    print(f"Thermal energy: {thermal_energy:.2f} J after {presets['t']:.2f} seconds")

# Attach as a .print method to derive
derive.print = dp

derive.print()




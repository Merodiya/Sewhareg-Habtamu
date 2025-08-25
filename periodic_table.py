periodic_table = {
    1: {"symbol": "H", "name": "Hydrogen", "mass": 1.008},
    2: {"symbol": "He", "name": "Helium", "mass": 4.0026},
    3: {"symbol": "Li", "name": "Lithium", "mass": 6.94},
    4: {"symbol": "Be", "name": "Beryllium", "mass": 9.0122},
    5: {"symbol": "B", "name": "Boron", "mass": 10.81},
    6: {"symbol": "C", "name": "Carbon", "mass": 12.011},
    7: {"symbol": "N", "name": "Nitrogen", "mass": 14.007},
    8: {"symbol": "O", "name": "Oxygen", "mass": 15.999},
    9: {"symbol": "F", "name": "Fluorine", "mass": 18.998},
    10: {"symbol": "Ne", "name": "Neon", "mass": 20.180},
    11: {"symbol": "Na", "name": "Sodium", "mass": 22.990},
    12: {"symbol": "Mg", "name": "Magnesium", "mass": 24.305},
    13: {"symbol": "Al", "name": "Aluminium", "mass": 26.982},
    14: {"symbol": "Si", "name": "Silicon", "mass": 28.085},
    15: {"symbol": "P", "name": "Phosphorus", "mass": 30.974},
    16: {"symbol": "S", "name": "Sulfur", "mass": 32.06},
    17: {"symbol": "Cl", "name": "Chlorine", "mass": 35.45},
    18: {"symbol": "Ar", "name": "Argon", "mass": 39.948},
    19: {"symbol": "K", "name": "Potassium", "mass": 39.098},
    20: {"symbol": "Ca", "name": "Calcium", "mass": 40.078},
    21: {"symbol": "Sc", "name": "Scandium", "mass": 44.956},
    22: {"symbol": "Ti", "name": "Titanium", "mass": 47.867},
    23: {"symbol": "V", "name": "Vanadium", "mass": 50.942},
    24: {"symbol": "Cr", "name": "Chromium", "mass": 51.996},
    25: {"symbol": "Mn", "name": "Manganese", "mass": 54.938},
    26: {"symbol": "Fe", "name": "Iron", "mass": 55.845},
    27: {"symbol": "Co", "name": "Cobalt", "mass": 58.933},
    28: {"symbol": "Ni", "name": "Nickel", "mass": 58.693},
    29: {"symbol": "Cu", "name": "Copper", "mass": 63.546},
    30: {"symbol": "Zn", "name": "Zinc", "mass": 65.38},
    31: {"symbol": "Ga", "name": "Gallium", "mass": 69.723},
    32: {"symbol": "Ge", "name": "Germanium", "mass": 72.630},
    33: {"symbol": "As", "name": "Arsenic", "mass": 74.922},
    34: {"symbol": "Se", "name": "Selenium", "mass": 78.971},
    35: {"symbol": "Br", "name": "Bromine", "mass": 79.904},
    36: {"symbol": "Kr", "name": "Krypton", "mass": 83.798},
    37: {"symbol": "Rb", "name": "Rubidium", "mass": 85.468},
    38: {"symbol": "Sr", "name": "Strontium", "mass": 87.62},
    39: {"symbol": "Y", "name": "Yttrium", "mass": 88.906},
    40: {"symbol": "Zr", "name": "Zirconium", "mass": 91.224},
    41: {"symbol": "Nb", "name": "Niobium", "mass": 92.906},
    42: {"symbol": "Mo", "name": "Molybdenum", "mass": 95.95},
    43: {"symbol": "Tc", "name": "Technetium", "mass": 98},
    44: {"symbol": "Ru", "name": "Ruthenium", "mass": 101.07},
    45: {"symbol": "Rh", "name": "Rhodium", "mass": 102.91},
    46: {"symbol": "Pd", "name": "Palladium", "mass": 106.42},
    47: {"symbol": "Ag", "name": "Silver", "mass": 107.87},
    48: {"symbol": "Cd", "name": "Cadmium", "mass": 112.41},
    49: {"symbol": "In", "name": "Indium", "mass": 114.82},
    50: {"symbol": "Sn", "name": "Tin", "mass": 118.71},
    51: {"symbol": "Sb", "name": "Antimony", "mass": 121.76},
    52: {"symbol": "Te", "name": "Tellurium", "mass": 127.60},
    53: {"symbol": "I", "name": "Iodine", "mass": 126.90},
    54: {"symbol": "Xe", "name": "Xenon", "mass": 131.29},
    55: {"symbol": "Cs", "name": "Cesium", "mass": 132.91},
    56: {"symbol": "Ba", "name": "Barium", "mass": 137.33},
    57: {"symbol": "La", "name": "Lanthanum", "mass": 138.91},
    58: {"symbol": "Ce", "name": "Cerium", "mass": 140.12},
    59: {"symbol": "Pr", "name": "Praseodymium", "mass": 140.91},
    60: {"symbol": "Nd", "name": "Neodymium", "mass": 144.24},
    61: {"symbol": "Pm", "name": "Promethium", "mass": 145},
    62: {"symbol": "Sm", "name": "Samarium", "mass": 150.36},
    63: {"symbol": "Eu", "name": "Europium", "mass": 151.96},
    64: {"symbol": "Gd", "name": "Gadolinium", "mass": 157.25},
    65: {"symbol": "Tb", "name": "Terbium", "mass": 158.93},
    66: {"symbol": "Dy", "name": "Dysprosium", "mass": 162.50},
    67: {"symbol": "Ho", "name": "Holmium", "mass": 164.93},
    68: {"symbol": "Er", "name": "Erbium", "mass": 167.26},
    69: {"symbol": "Tm", "name": "Thulium", "mass": 168.93},
    70: {"symbol": "Yb", "name": "Ytterbium", "mass": 173.05},
    71: {"symbol": "Lu", "name": "Lutetium", "mass": 174.97},
    72: {"symbol": "Hf", "name": "Hafnium", "mass": 178.49},
    73: {"symbol": "Ta", "name": "Tantalum", "mass": 180.95},
    74: {"symbol": "W", "name": "Tungsten", "mass": 183.84},
    75: {"symbol": "Re", "name": "Rhenium", "mass": 186.21},
    76: {"symbol": "Os", "name": "Osmium", "mass": 190.23},
    77: {"symbol": "Ir", "name": "Iridium", "mass": 192.22},
    78: {"symbol": "Pt", "name": "Platinum", "mass": 195.08},
    79: {"symbol": "Au", "name": "Gold", "mass": 196.97},
    80: {"symbol": "Hg", "name": "Mercury", "mass": 200.59},
    81: {"symbol": "Tl", "name": "Thallium", "mass": 204.38},
    82: {"symbol": "Pb", "name": "Lead", "mass": 207.2},
    83: {"symbol": "Bi", "name": "Bismuth", "mass": 208.98},
    84: {"symbol": "Po", "name": "Polonium", "mass": 209},
    85: {"symbol": "At", "name": "Astatine", "mass": 210},
    86: {"symbol": "Rn", "name": "Radon", "mass": 222},
    87: {"symbol": "Fr", "name": "Francium", "mass": 223},
    88: {"symbol": "Ra", "name": "Radium", "mass": 226},
    89: {"symbol": "Ac", "name": "Actinium", "mass": 227},
    90: {"symbol": "Th", "name": "Thorium", "mass": 232.04},
    91: {"symbol": "Pa", "name": "Protactinium", "mass": 231.04},
    92: {"symbol": "U", "name": "Uranium", "mass": 238.03},
    93: {"symbol": "Np", "name": "Neptunium", "mass": 237},
    94: {"symbol": "Pu", "name": "Plutonium", "mass": 244},
    95: {"symbol": "Am", "name": "Americium", "mass": 243},
    96: {"symbol": "Cm", "name": "Curium", "mass": 247},
    97: {"symbol": "Bk", "name": "Berkelium", "mass": 247},
    98: {"symbol": "Cf", "name": "Californium", "mass": 251},
    99: {"symbol": "Es", "name": "Einsteinium", "mass": 252},
    100: {"symbol": "Fm", "name": "Fermium", "mass": 257},
    101: {"symbol": "Md", "name": "Mendelevium", "mass": 258},
    102: {"symbol": "No", "name": "Nobelium", "mass": 259},
    103: {"symbol": "Lr", "name": "Lawrencium", "mass": 266},
    104: {"symbol": "Rf", "name": "Rutherfordium", "mass": 267},
    105: {"symbol": "Db", "name": "Dubnium", "mass": 268},
    106: {"symbol": "Sg", "name": "Seaborgium", "mass": 269},
    107: {"symbol": "Bh", "name": "Bohrium", "mass": 270},
    108: {"symbol": "Hs", "name": "Hassium", "mass": 277},
    109: {"symbol": "Mt", "name": "Meitnerium", "mass": 278},
    110: {"symbol": "Ds", "name": "Darmstadtium", "mass": 281},
    111: {"symbol": "Rg", "name": "Roentgenium", "mass": 282},
    112: {"symbol": "Cn", "name": "Copernicium", "mass": 285},
    113: {"symbol": "Nh", "name": "Nihonium", "mass": 286},
    114: {"symbol": "Fl", "name": "Flerovium", "mass": 289},
    115: {"symbol": "Mc", "name": "Moscovium", "mass": 290},
    116: {"symbol": "Lv", "name": "Livermorium", "mass": 293},
    117: {"symbol": "Ts", "name": "Tennessine", "mass": 294},
    118: {"symbol": "Og", "name": "Oganesson", "mass": 294}
}

# ----------------------------
# SEARCH FUNCTION
# ----------------------------
def find_element(query):
    # If query is a number → atomic number
    if query.isdigit():
        num = int(query)
        return {num: periodic_table[num]} if num in periodic_table else "Element not found"

    # If query matches symbol
    for num, data in periodic_table.items():
        if data["symbol"].lower() == query.lower():
            return {num: data}

    # If query matches name
    for num, data in periodic_table.items():
        if data["name"].lower() == query.lower():
            return {num: data}

    return "Element not found"

# ----------------------------
# MAIN PROGRAM
# ----------------------------
while True:
    user_input = input("\nEnter element (number, symbol, or name) or 'exit' to quit: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    result = find_element(user_input)
    print(result)

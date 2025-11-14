import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
from tkinter import ttk

fenetre=tk.Tk()
fenetre.geometry("600x800")
fenetre.title("notes semestre 1")

frm=ttk.Frame(fenetre)
frm.grid()

zone1=ttk.Entry(frm)
zone1.grid(column=0,row=0,pady=10)

zone2=ttk.Entry(frm)
zone2.grid(column=0,row=1,pady=10)

coef_ue1={
    "R101":10, "R102":10,"R103":7, "R104":7,"R106":5,
    "R108":6, "R110":5, "R111":4, "R112":2, "R113":5,
    "R114":5, "SAE11":20, "SAE12":20, "SAE16":7
}
coef_ue2={
    "R101":4, "R103":2, "R104":8, "R105":6, "R110":5,
    "R111":5, "R112":2, "R113":9, "R114":9,
    "R115":3, "SAE13":20, "SAE16":20,
}
coef_ue3={
    "R101":4, "R103":2, "R106":5, "R107":15, "R108":6,
    "R109":4, "R110":5, "R111":5,"R112":2, "R115":3,
    "SAE14":20, "SAE15":20, "SAE16":7
}
notes = {
    'R101': 6, 'R102': 4, 'R103': 11, 'R104':12,
    'R105': 12, 'R106': 4, 'R107': 11, 'R108': 8,
    'R109': 8, 'R110': 14, 'R111': 4, 'R112': 12,
    'R113': 13, 'R114': 3, 'R115': 11,
    'SAE11': 11, 'SAE13': 9, 'SAE14': 9,
    'SAE15': 12, 'SAE16': 15
}

def calculer_moyenne_ue(coefs, notes):
    total_points = 0
    total_coefs = 0
    for matiere, coef in coefs.items():
        if matiere in notes:
            total_points += notes[matiere] * coef
            total_coefs += coef
    if total_coefs == 0:
        return 0
    return total_points / total_coefs

moyenne_ue1 = calculer_moyenne_ue(coef_ue1, notes)
moyenne_ue2 = calculer_moyenne_ue(coef_ue2, notes)
moyenne_ue3 = calculer_moyenne_ue(coef_ue3, notes)

notes_ue1 = sum(coef_ue1.values())
notes_ue2 = sum(coef_ue2.values())
notes_ue3 = sum(coef_ue3.values())
notes_total = notes_ue1 + notes_ue2 + notes_ue3

def get_color(value):
    if value  >= 10:
        return 'green'
    else:   
        if value >=8: return 'orange'
    if value <8: return 'red' 
values = [moyenne_ue1, moyenne_ue2, moyenne_ue3]
colors = [get_color(val) for val in values]
plt.bar(['UE1' , 'UE2' , 'UE3'], values, color=colors)
plt.show()
fenetre.mainloop()


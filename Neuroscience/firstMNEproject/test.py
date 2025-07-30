## last edited: 25-07-2025
## Author: Sietze Min
import mne
import mne.data
import numpy as np
import matplotlib.pyplot as plt
import sys

#Tkinter
from tkinter import *
from tkinter import ttk

# command to activate the local env.
print("MNE version:", mne.__version__)
print("NumPy version:", np.__version__) 
import mne

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello world!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# Volledig pad naar het raw .fif bestand
# would be better if this references to a dynamical location or in a try-catch 
raw_fname = r"C:\Users\sietz\mne_data\MNE-sample-data\MEG\sample\sample_audvis_raw.fif"

# Laad de data
raw = mne.io.read_raw_fif(raw_fname, preload=True)

# Toon basisinfo
print(raw.info)
raw.plot(n_channels=30, scalings='auto', title='Sample Auditory/Visual Data')

plt.show()

root.mainloop()

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
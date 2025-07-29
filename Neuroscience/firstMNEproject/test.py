## last edited: 25-07-2025
## Author: Sietze Min
import mne
import mne.data
import numpy as np
import matplotlib.pyplot as plt
import sys

print('hello sietze')
print(sys.executable)
# command to activate the local env.
print("MNE version:", mne.__version__)
print("NumPy version:", np.__version__) 

import mne

# Volledig pad naar het raw .fif bestand
raw_fname = r"\C:\Users\sietz\mne_data\MNE-sample-data\MEG\sample\sample_audvis_raw.fif"

# Laad de data
raw = mne.io.read_raw_fif(raw_fname, preload=True)

# Toon basisinfo
print(raw.info)
raw.plot(n_channels=30, scalings='auto', title='Sample Auditory/Visual Data')

plt.show()



# Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSignedc
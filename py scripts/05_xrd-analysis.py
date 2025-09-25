import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""This is a simple example of reading X-Ray diffraction (XRD) data from a xlsx file 
using pandas, plotting the data, and performing basic analysis.

In the Bragg diffraction, X-rays at a crystal plane will be scattered at the same angle 
as the angle of incidence θ, as shown in Figure 1. Furthermore, when the path difference 
is equal to an integer multiple n of the wavelength λ, this will result in a constructive 
interference. The lattice constant d of the crystal can be found from the Bragg’s law, 
nλ = 2dsinθ

The lattice constant of a lithium fluoride (LiF) crystal is calculated from the full 
spectrum. The emission current is set to 0.05 mA. The count rate is measured at each 
detector angle 2θ in the 2:1 coupled mode (the detector moves at twice the angular 
speed of the sample, such that 2θ is always exactly twice θ), with the angle increment 
of 0.1 degree. The starting angle and stopping angle is set to θ = 5 degrees and θ = 60 
degrees respectively. The accelerating voltage is set to 30 kV.

This data is measured by me in 2019."""

# Read the data from the xlsx file
data_30kV = pd.read_excel("input/XRay_raw.xlsx", sheet_name="30_full").dropna()
print(data_30kV.head())


def find_peaks(angle, count, threshold=2):
    # Find peaks in the data above a certain threshold.
    peaks = []
    counter = 0
    count_copy = np.copy(count)
    count_copy[:141] = 0  # Ignore low angle region which is the whale back

    while counter < 3:
        i_count_max = np.argmax(count_copy)
        if ((count_copy[i_count_max] - count_copy[i_count_max-1]) >= threshold) and \
           ((count_copy[i_count_max] - count_copy[i_count_max+2]) >= threshold) and \
            count_copy[i_count_max] > threshold:
            # Mainly using left shoulder to find peak as left shoulder is sharper
            # Exclude small peaks by setting a threshold
            peaks.append([angle[i_count_max], count[i_count_max]])
        
        else:
            counter += 1
            # if no peak found, increase counter
            # if counter reaches 3, exit the loop
        
        count_copy[i_count_max-5:i_count_max+6] = 0  
        # Zero out the peak region to find next peak

    return np.array(peaks)


theta = data_30kV['theta']
rate = data_30kV['rate']
theta = np.array(theta)
rate = np.array(rate)

plt.figure(figsize=(10, 6))
plt.plot(theta, rate, label="30 kV", color="blue")
plt.show()

# Find peaks in the data
peaks = find_peaks(theta, rate)
print("Peaks:", peaks)

# Calculate lattice constant using Bragg's law
K_a = 0.154  # nm, wavelength of K-alpha X-ray for Cu target
K_b = 0.139  # nm, wavelength of K-beta X-ray for Cu target
K_values = [K_a, K_b]  # Wavelengths for the peaks
d_values = []

for n in (1, 2): 
    if n == 1:
        for peak, K in zip(peaks[:2], K_values):   
            d = n * K / (2 * np.sin(np.radians(peak[0]))) 
            d_values.append(d)
    else: 
        for peak, K in zip(peaks[2:], K_values):   
            d = n * K / (2 * np.sin(np.radians(peak[0]))) 
            d_values.append(d)
d_values = np.array(d_values)
print("Lattice constants (nm):", d_values)
print("Average lattice constant (nm):", np.mean(d_values))

# Plot the data with peaks annotated
labels = ["K_\\alpha", "K_\\beta", "K_\\alpha", "K_\\beta"]  # Labels for the peaks
plt.figure(figsize=(10, 6))
plt.plot(theta, rate, label="30 kV", color="blue")
for peak, label in zip(peaks, labels):
    plt.plot(peak[0], peak[1], 'ro', alpha = 0.3)  # Mark the peaks
    plt.annotate("${}$ ({},{})".format(label, peak[0], peak[1]), (peak[0]-1, peak[1]), horizontalalignment='right')  
    # Annotate the peaks
plt.xlabel("Theta (degrees)")
plt.ylabel("Count Rate (counts/s)")
plt.title("X-Ray Diffraction Pattern of LiF Crystal at 30 kV")
plt.legend()
plt.grid()
plt.ylim(0, 120)
plt.savefig("output/XRay_30kV.png", dpi=300)
plt.show()
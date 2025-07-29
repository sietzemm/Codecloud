# Creation date: 30-07-2025
# None of this was created by me. It just serves as an inspiration for computational neuron models
#e = Excitatory neurons, i = inhibitory neurons

Ne = 800
Ni = 202
number_neurons = Ne + Ni
time_steps = 1000
import numpy as np
import matplotlib.pyplot as plt

re = np.random.rand(Ne, 1)
ri = np.random.rand(Ni, 1)

#First array of np.concatenate is the Excitatory neuron parameters, second part is the inhibitory neurons
a = np.concatenate([0.02 * np.ones((Ne, 1)), 0.02 + 0.08 * ri])
b = np.concatenate([0.2 * np.ones((Ne, 1)), 0.25 - 0.05 * ri])
c = np.concatenate([-65 + 15 * re**2, -65 * np.ones((Ni, 1))])
d = np.concatenate([8 - 6 * re**2, 2 * np.ones((Ni, 1))])
S = np.concatenate([0.5 * np.random.rand(Ne + Ni, Ne), -np.random.rand(Ne + Ni, Ni)], axis = 1)

v = -65 * np.ones((Ne + Ni, 1))
u = b * -65
neurons_that_fired_across_time = []
voltage_across_time = []

for t in range(1, time_steps + 1): 
  # The Input Voltage
  I = np.concatenate([5 * np.random.rand(Ne, 1), 2 * np.random.rand(Ni, 1)])

  # When voltage goes above 30 mV, we find the index, and append it to fired,
  # then reset the membrane potnetial and membrane recovery variable
  neurons_that_fired = np.where(v > 30)
  voltage_across_time.append(v[10, 0])
  neurons_that_fired_across_time.append([t + 0 * neurons_that_fired[0], neurons_that_fired[0]])

  for i in neurons_that_fired[0]:
    v[i] = c[i]
    u[i] += d[i]
  
  I += np.expand_dims(np.sum(S[:, neurons_that_fired[0]], axis = 1), axis = 1)
  # We have to do 0.5ms increments for numerical stability
  v += 0.5 * (0.04 * v**2 + 5 * v + 140 - u + I)
  v += 0.5 * (0.04 * v**2 + 5 * v + 140 - u + I)
  u = u + a * (b * v - u)

voltage_across_time = np.array(voltage_across_time)

# I'm not very good at matplot lib, so after (literally) hours of trail and error 
# I can finally plot the neurons! Please let me know how to improve it :D

# Create the time axis. Will produce (time_steps, number_neurons) shaped array
time = np.dot(
    np.arange(time_steps).reshape(time_steps, 1), 
    np.ones(number_neurons).reshape(1, number_neurons))

# I'm not sure how to covert this numpy
# This generates the firing map. It's also (time_steps, number_neurons).
# It's basically an array full of Nones. We iterate through time (t) and we look
# at each neuron (of index i). If neuron_i fires, we turn on the neuron
firing_map = []
for t in range(time_steps):
  neurons_on_or_off = [None] * number_neurons

  for fired_neuron in neurons_that_fired_across_time[t][1]:
    neurons_on_or_off[fired_neuron] = fired_neuron

  firing_map.append(neurons_on_or_off)

firing_map = np.array(firing_map)

plt.figure(figsize=(15,10))
plt.title("The Membrane Potential of Neuron #10 with Respect to Time")
plt.xlabel('Time (ms)')
plt.ylabel('Membrane potential (mV)')
plt.plot(np.arange(time_steps), voltage_across_time);
plt.show()

plt.figure(figsize=(15,10))
plt.title("Firing of Neurons with Respect to Time")
plt.xlabel('Time (ms)')
plt.ylabel('Neuron Nume')
plt.plot(time, firing_map, ".");
plt.show()
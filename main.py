import numpy as np
import matplotlib.pyplot as plt

# Parameter Radar
fc = 10e9  # Frekuensi carrier (10 GHz)
c = 3e8    # Kecepatan cahaya (m/s)
lambda_ = c / fc  # Panjang gelombang
prf = 1000  # Pulse Repetition Frequency (Hz)
pulse_width = 1e-6  # Lebar pulsa (1 mikrodetik)
range_max = c * (1 / prf) / 2  # Jarak maksimum yang dapat diukur

# Simulasi Target
target_range = 5000  # Jarak target (meter)
target_rcs = 1  # Radar Cross Section (RCS) target (m^2)

# Generate Radar Signal
t = np.linspace(0, 1 / prf, 1000)  # Waktu sampling
transmit_signal = np.cos(2 * np.pi * fc * t)  # Sinyal transmit

# Simulasi Echo dari Target
time_delay = 2 * target_range / c  # Waktu tunda echo
received_signal = np.cos(2 * np.pi * fc * (t - time_delay))  # Sinyal received

# Plot Sinyal Transmit dan Received
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, transmit_signal)
plt.title('Sinyal Transmit Radar')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')

plt.subplot(2, 1, 2)
plt.plot(t, received_signal)
plt.title('Sinyal Received Radar (Echo)')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')
plt.tight_layout()
plt.show()

# Analisis Jarak
fft_result = np.fft.fft(received_signal)
frequencies = np.fft.fftfreq(len(t), d=t[1] - t[0])
range_axis = frequencies * c / (2 * fc)

plt.figure(figsize=(10, 6))
plt.plot(range_axis, np.abs(fft_result))
plt.title('FFT dari Sinyal Received (Analisis Jarak)')
plt.xlabel('Jarak (m)')
plt.ylabel('Magnitudo')
plt.xlim(0, range_max)
plt.grid()
plt.show()

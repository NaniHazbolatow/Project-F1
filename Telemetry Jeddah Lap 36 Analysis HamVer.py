#################
# Base Packages #
#################
import fastf1 as ff1
import matplotlib
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd

# Setup plotting
plotting.setup_mpl()

# Enable cache
ff1.Cache.enable_cache('cache')

#########
# Data #
#########
race = ff1.get_session(2021, 'Jeddah', 'R')
laps = race.load_laps(with_telemetry=True)

laps_ver = laps.pick_driver('VER')
laps_ham = laps.pick_driver('HAM')

lap36_ver = laps_ver[laps_ver['LapNumber'] == 36].iloc[0]
lap36_ham = laps_ham[laps_ham['LapNumber'] == 36].iloc[0]

collision_ver = laps_ver[laps_ver['LapNumber'] == 37].iloc[0]
collision_ham = laps_ham[laps_ham['LapNumber'] == 37].iloc[0]

telemetry_ver = collision_ver.get_car_data().add_distance()
telemetry_ham = collision_ham.get_car_data().add_distance()

telemetryl36_ver = lap36_ver.get_car_data().add_distance()
telemetryl36_ham = lap36_ham.get_car_data().add_distance()

#########
# Plots #
#########
fig, ax = plt.subplots(4)
fig.suptitle(f"Race Lap Telemetry Comparison\n"
             f"Saudi Arabian Grand Prix Lap 37 (Brake test) Ham vs Ver"
            )

ax[0].plot(telemetry_ham['Time'], telemetry_ham['Speed'], label='Hamilton')
ax[0].plot(telemetry_ver['Time'], telemetry_ver['Speed'], label='Verstappen')
ax[0].set(ylabel='Speed')
ax[0].legend(loc="lower right")

ax[1].plot(telemetry_ham['Time'], telemetry_ham['Throttle'], label='Hamilton')
ax[1].plot(telemetry_ver['Time'], telemetry_ver['Throttle'], label='Verstappen')
ax[1].set(ylabel='Throttle')

ax[2].plot(telemetry_ham['Time'], telemetry_ham['Brake'], label='Hamilton')
ax[2].plot(telemetry_ver['Time'], telemetry_ver['Brake'], label='Verstappen')
ax[2].set(ylabel='Brake')

ax[3].plot(telemetry_ham['Time'], telemetry_ham['nGear'], label='Hamilton')
ax[3].plot(telemetry_ver['Time'], telemetry_ver['nGear'], label='Verstappen')
plt.yticks(np.arange(telemetry_ham['nGear'].min()-1, telemetry_ham['nGear'].max()+1, 1))
ax[3].set(ylabel='Gear')

for a in ax.flat:
    a.label_outer()

plt.show()


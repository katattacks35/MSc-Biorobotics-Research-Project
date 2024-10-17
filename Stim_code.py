

#Code to 1.Set stimulation parameters, 2. Run stimulation, 3. Retrieve data

#Load libraries

import numpy as np
import time
from datetime import datetime, timedelta
from IPython.display import clear_output
from neuroplatform import StimShape, StimParam , IntanSofware, Trigger, Database, StimPolarity, Experiment


#Token for running experiment on IntanSoftware
token = "NGERNO75OY" 
exp = Experiment(token)
#Prints available electrodes in MEA
print(f'Electrodes: {exp.electrodes}') 

#Prints stimulation attributes
print(StimParam().__doc__)

#Setting stimulation parameters
stim_param1 = StimParam()
stim_param1.index = exp.electrodes[30] #target electrode from available electrodes
stim_param1.enable = True
stim_param1.trigger_key = 0
stim_param1.polarity = StimPolarity.PositiveFirst
stim_param1.phase_amplitude1 = 5
stim_param1.phase_amplitude2 = 5
stim_param1.phase_duration1 = 100
stim_param1.phase_duration2 = 100
stim_param1.display_attributes()

#Different parameter settings - can be run simulatneously
stim_param2 = StimParam()
stim_param2.index = exp.electrodes[29] #target electrode from available electrodes
stim_param2.enable = True
stim_param2.trigger_key = 0
stim_param2.polarity = StimPolarity.PositiveFirst
stim_param2.phase_amplitude1 = 6
stim_param2.phase_amplitude2 = 6
stim_param2.phase_duration1 = 200
stim_param2.phase_duration2 = 200
stim_param2.display_attributes()


#2.Running stimulation:

# The neuroplatfrom controls two computers for the stimulation:
# - Intan software (Configure the headstage for stimulation, live spike count)
# - Trigger Generator (Generate triggers to start the stimulation)

#Initiate Software and Trigger Generator
intan = IntanSofware()
trigger_gen = Trigger()

# Each electrode has a signal generator. To configure one or multiple electrodes,a StimParam object is sent to the Intan Sofware
#Singular target electrode
stim_params = [stim_param1]
#Stimulating with different parameters or multiple electrodes
stim_params = [stim_param1, stim_param2, stim_param3, stim_param4] 

try:
    if exp.start(): # Signal the start of an experiment to all users
        # Measure impedance
        intan.impedance()

        # Disable Variation STD (keep a fixed threshold)
        intan.var_threshold(False)

        # Send stimulation parameters
        intan.send_stimparam(stim_params)
        start_exp = datetime.utcnow()
        print(start_exp)

        # Trigger 0 only = electrode 0
        trigger0 = np.zeros(16, dtype=np.uint8)
        trigger0[0] = 1

        #10 sets of 10 impulses triggered with 0.5 second interval
        for i in range(10):
          for i in range(10):
           trigger_gen.send(trigger0)
           time.sleep(0.5)
              
        time.sleep(20)
        
        stop_exp = datetime.utcnow()
        print(stop_exp)

        # Disable all stimulation
        for stim in stim_params:
            stim.enable = False
        intan.send_stimparam(stim_params)

     
finally:
    # Close the connection to trigger generator
    trigger_gen.close()
    # Enable variation threshold again
    intan.var_threshold(True)
    # Close the connection to intan software
    intan.close()
    # Signal the end of an experiment to all users
    exp.stop()


#3. Retrieving data from database
from dateutil import parser

#Measuring impedance
db = Database()
start = parser.parse("2024-09-01T16:00:00.000Z")
# start = parser.parse("2024-05-10T13:06:56.255Z")
#db.get_impedance(start,start+timedelta(days=1))
db.get_impedance(start,start+timedelta(hours=1))

import pandas as pd
from dateutil import parser
from lets_plot import *
from tqdm import tqdm
LetsPlot.setup_html()

db = Database()
exp_name = exp.exp_name
exp_name

# Get Triggers: Timestamp at which impulse was triggered.
# Query the database to get timestamp of trigger. The dataframe has 4 columns:
# - _time: timestamp
# - _value: tag value. Can be set before trigger to help sorting.
# - trigger: Trigger ID
# - up: 1=When trigger goes high, 0=When trigger goes down 


start_exp = parser.parse("2024-07-12T10:11:00.000Z")
stop_exp = parser.parse("2024-07-12T10:16:00.000Z")
triggers = db.get_all_triggers(start_exp - timedelta(minutes=1), stop_exp + timedelta(minutes=1))

print("Experiment Start Time:", start_exp)
print("Experiment Stop Time:", stop_exp)
triggers


#Get spike event

s1 = triggers.iloc[0]['_time']
print(s1.strftime('%Y-%m-%d %H:%M:%S'))

#Retrieval of spike event count - input of trigger time
#Can be altered to retreive data for different amounts of time

s1 = parser.parse('2024-07-12T10:14:25.891Z')

#Retrieval of spike count 300ms post trigger time
df_spike_event = db.get_spike_event(s1, s1 + timedelta(seconds=0.3), exp_name)
df_spike_event

#Retrieval of spike count 100ms post trigger time
df_spike_event = db.get_spike_event(s1, s1 + timedelta(seconds=0.1), exp_name)
df_spike_event


  

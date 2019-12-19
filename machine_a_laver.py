import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
typedirt = ctrl.Antecedent(np.arange(0, 101, 1), 'typedirt')
washtime = ctrl.Consequent(np.arange(0, 60, 1), 'washtime')

temperature['low'] = fuzz.trimf(temperature.universe, [0, 10, 50])
temperature['medium'] = fuzz.trimf(temperature.universe, [10, 50, 80])
temperature['high'] = fuzz.trimf(temperature.universe, [50, 80, 100])
typedirt['nonfat'] = fuzz.trimf(typedirt.universe, [0, 10, 50])
typedirt['medium'] = fuzz.trimf(typedirt.universe, [10, 50, 80])
typedirt['fat'] = fuzz.trimf(typedirt.universe, [50, 80, 100])

washtime['veryshort'] = fuzz.trimf(washtime.universe, [0, 8, 12])
washtime['short'] = fuzz.trimf(washtime.universe, [8, 12,20])
washtime['medium'] = fuzz.trimf(washtime.universe, [12, 20, 40])
washtime['long'] = fuzz.trimf(washtime.universe, [20, 40, 60])
washtime['verylong'] = fuzz.trimf(washtime.universe, [40, 60, 60])

ruleVL = ctrl.Rule(temperature['high'] | typedirt['fat'], washtime['verylong'])
ruleL1 = ctrl.Rule(temperature['medium'] | typedirt['fat'], washtime['long'])
ruleL2 = ctrl.Rule(temperature['low'] | typedirt['fat'], washtime['long'])
ruleL3 = ctrl.Rule(temperature['high'] | typedirt['medium'], washtime['long'])
ruleM1 = ctrl.Rule(temperature['medium'] | typedirt['medium'], washtime['medium'])
ruleM2 = ctrl.Rule(temperature['low'] | typedirt['medium'], washtime['medium'])
ruleM3 = ctrl.Rule(temperature['high'] | typedirt['nonfat'], washtime['medium'])
ruleS = ctrl.Rule(temperature['medium'] | typedirt['nonfat'], washtime['short'])
ruleVS = ctrl.Rule(temperature['low'] | typedirt['nonfat'], washtime['veryshort'])

washtime_ctrl = ctrl.ControlSystem([ruleVL, ruleL1, ruleL2, ruleL3, ruleM1, ruleM2, ruleM3, ruleS, ruleVS])

washtime_check = ctrl.ControlSystemSimulation(washtime_ctrl)

washtime_check.input['temperature'] = 90 
washtime_check.input['typedirt'] = 40

washtime_check.compute()

print(washtime_check.output['washtime'])
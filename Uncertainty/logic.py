from pomegranate.distributions import Categorical, ConditionalCategorical
from pomegranate.bayesian_network import BayesianNetwork
rainy = {
     "No":0.45,
     "Mild": 0.3,
     "Heavy":0.25
}

# P(traffic | weather)
traffic = {
     'Low | No':0.2,
     'Medium | No':0.45,
     'High | No':0.35,
     'Low | Mild':0.1,
     'Medium | Mild':0.3,
     'High | Mild':0.6,
     'Low | Heavy':0.08,
     'Medium | Heavy':0.22,
     'High | Heavy':0.7,
     
}

# P(Rail maintainance(Rm) | weather)
maintainance = {
     'no | no':0.7,
     'yes | no':0.3,
     'no | mild':0.75,
     'yes | mild':0.25,
     'no | heavy':0.95,
     'yes | heavy':0.05,
}

# P(train_schedule(TS) | weather, rm)
Ts = {
     'on_time | no,no':0.9,
     'late | no,no':0.1,
     'on_time | no,yes':0.55,
     'late | no,yes':0.45,
     'on_time | mild,no':0.7,
     'late | mild,no':0.3,
     'on_time | mild,yes':0.5,
     'late | mild,yes':0.5,
     'on_time | heavy,no':0.5,
     'late | heavy,no':0.5,
     'on_time | heavy,yes':0.35,
     'late | heavy,yes':0.65,
}


reach_on_time = {
    'yes | on_time,Low': 0.95,
    'no | on_time,Low': 0.05,

    'yes | on_time,Medium': 0.85,
    'no | on_time,Medium': 0.15,

    'yes | on_time,High': 0.6,
    'no | on_time,High': 0.4,

    'yes | late,Low': 0.7,
    'no | late,Low': 0.3,

    'yes | late,Medium': 0.5,
    'no | late,Medium': 0.5,

    'yes | late,High': 0.2,
    'no | late,High': 0.8,
}


rain_dist = Categorical([[rainy["No"], rainy["Mild"], rainy["Heavy"]]])

# P(Traffic | Weather)
traffic_dist = ConditionalCategorical([
     [ traffic['Low | No'], traffic['Medium | No'], traffic['Medium | No'] ],
     [ traffic['Low | Mild'], traffic['Medium | Mild'], traffic['High | Mild'] ],
     [ traffic['Low | Heavy'], traffic['Medium | Heavy'], traffic['High | Heavy'] ],
])


rm_dist = ConditionalCategorical([
     [ maintainance['no | no'], maintainance['yes | no'] ],  # P(maintainance | weather = No)
     [ maintainance['no | mild'], maintainance['yes | mild'] ],  # P(maintainance | weather = Mild)
     [ maintainance['no | heavy'], maintainance['yes | heavy'] ],  # P(maintainance | weather = Heavy)

])


# P(ts | weather,maintainance)
w = ['no', 'mild', 'heavy' ]
m = ['no', 'yes']
t = ['late', 'on_time']

dist = []

for wv in w:
    for mv in m:
          tert = []
          for tv in t:
               tert.append(Ts[f'{tv} | {wv},{mv}'])
          dist.append(tert)

ts_dist = ConditionalCategorical(dist)



# P(on_time | train,traffic)
ts_values = ['on_time', 'late']
traffic_values = ['Low', 'Medium', 'High']
reach_vals = ['yes', 'no']

reach_dist = []

for ts in ts_values:
    for traffic in traffic_values:
        row = []
        for r in reach_vals:
            row.append(reach_on_time[f'{r} | {ts},{traffic}'])
        reach_dist.append(row)

rot_dist = ConditionalCategorical(reach_dist)

distribution = [
     rain_dist,
     traffic_dist,
     rm_dist,
     ts_dist,
     rot_dist
]

names = ["Weather", "Traffic", "RailMaintenance", "TrainSchedule", "ReachOnTime"]


model = BayesianNetwork(
     distributions=distribution,
     edges=[
          (rain_dist, traffic_dist),
          (rain_dist, rm_dist),
          (rain_dist, ts_dist),
          (rm_dist,ts_dist),
          (traffic_dist,rot_dist),
          (ts_dist, rot_dist)
     ]
)


observations = ['Heavy', 'High', None, None, None]

t = model.predict_proba(observations)
print(t)
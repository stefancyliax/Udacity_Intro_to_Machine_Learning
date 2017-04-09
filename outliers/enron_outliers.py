#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
features = ["salary", "bonus"]
data_dict.pop("TOTAL")
data = featureFormat(data_dict, features)

### your code below

print data.max(axis=0)

for n in data_dict:
    if ((data_dict[n]["salary"] >= 1000000) and (data_dict[n]["salary"] != "NaN") or
                (data_dict[n]["bonus"] >= 5000000) and (data_dict[n]["bonus"] != "NaN")):
        print n, "salary: ", data_dict[n]["salary"], "bonus: ", data_dict[n]["bonus"]

### visualization
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

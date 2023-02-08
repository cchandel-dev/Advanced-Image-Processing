#determine most available classes
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

train = pd.read_csv(os.path.join( os.path.dirname(__file__), "leaf-classification\\mapping.csv"))
speciesdict = defaultdict(int)
numberofspecies = 0
for i in range(len(train)):
    speciesdict[train.species[i]] +=1
spec = np.array(list(speciesdict))
plt.hist(spec)
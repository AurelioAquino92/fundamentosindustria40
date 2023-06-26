import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from datetime import datetime
from sklearn.model_selection import train_test_split

data = pd.read_csv('Steel_industry_data.csv')

print(data)
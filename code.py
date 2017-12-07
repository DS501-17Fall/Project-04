import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import operator

data = pd.read_hdf('data.h5')

us_data = data[data.Country == 'United States']
web_data = us_data[us_data.DeveloperType.str.contains("Web")]
lang_data = web_data[web_data.HaveWorkedLanguage != 'nan']
stat_dict = {}
for row in lang_data['HaveWorkedLanguage']:
    types = row.split('; ')
    for i in types:
        if i in stat_dict:
            stat_dict[i] += 1
        else:
            stat_dict[i] = 1
sorted_list = sorted(stat_dict.items(), key=operator.itemgetter(1))
table = PrettyTable(['Language', 'Count'])
keys = []
values = []
for item in sorted_list[-10:]:
    table.add_row([item[0], item[1]])
    keys.append(item[0])
    values.append(item[1])
print(table)
plt.figure(figsize=(12, 9), dpi=100)
cm = plt.cm.get_cmap('plasma')
colors = [cm(i) for i in np.linspace(0.2, 0.9, len(keys))]
plt.barh(range(len(values)), values, align='center', color=colors)
plt.yticks(range(len(keys)), keys)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
plt.show()

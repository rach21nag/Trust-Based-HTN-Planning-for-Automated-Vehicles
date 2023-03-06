import random
import pandas as pd

seq = ["success", "failure"]
inc_dict = {}
for j in range(500):
    incident = []
    for i in range(1, 28):
        incident.append(random.choices(seq, weights=[0.5, 0.5], k=1)[0])
    inc_dict['result' + str(j)] = incident

print(inc_dict)
df = pd.DataFrame(inc_dict)
df.to_excel('result_testcase1000.xlsx', index=False)


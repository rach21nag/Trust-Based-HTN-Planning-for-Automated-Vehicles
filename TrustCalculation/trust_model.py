import pandas as pd
import plotly.graph_objs as go
import numpy as np
import plotly.express as px


def append_to_excel(fpath, df, sheet_name):
    with pd.ExcelWriter(fpath, mode="a") as f:
        df.to_excel(f, sheet_name=sheet_name)


# import openpyxl

workbook = pd.read_excel('TrustLevelsfromSurvey.xlsx', usecols='C:AC')
testcase = pd.read_excel('result_testcase.xlsx')
# print(testcase.shape)
# print(workbook.columns)
# print(workbook.shape)
avg = {}
for col in workbook.columns:
    avg[col] = workbook[col].mean()
# print(avg)

key_list = list(avg.keys())
val_list = list(avg.values())
print(val_list)

normalcond_trustlevel = val_list[0:6]
nightcond_trustlevel = val_list[6:13]
badweather_trustlevel = val_list[13:20]
lackofconc_trustlevel = val_list[20:27]

# print(normalcond_trustlevel)
# print(nightcond_trustlevel)
# print(badweather_trustlevel)
# print(lackofconc_trustlevel)
threshold_trust = 4
testcase_dict = {}
result_dict = {}
# for column in testcase:
#     print(testcase[column].values)

for (colname, colval) in testcase.iteritems():
    testcase_dict[colname] = colval.values

# print(testcase_dict['result1'])

# ----------------------------------------------------------------------------------------------------------------
# Reward matrix allocation
success_reward = [3, 5, 6, 5, 2, 4, 4, 7, 8, 6, 3, 5, 4, 4, 7, 8, 6, 3, 5, 4, 5, 8, 8, 6, 3, 5, 5]
failure_reward = [-4, -6, -6, -3, -2, -7, -4, -6, -6, -3, -2, -7, -4, -4, -6, -6, -3, -2, -7, -4, -4, -6, -6, -3, -2,
                  -7, -4]
req_reward = [300, 500, 600, 500, 200, 400, 400, 700, 800, 600, 300, 500, 400, 400, 700, 800, 600, 300, 500, 400,
              500, 800, 800, 600, 300, 500, 500]

# Calculation of Cumulative Reward
i = 0
for key, value in testcase_dict.items():
    i = i + 1
    result_array = []
    for index, result in enumerate(value):
        if result == "success":
            result_array.append(success_reward[index])
        elif result == "failure":
            result_array.append(failure_reward[index])
    result_dict[key] = result_array
    print(i, result_array)

cumu_reward = [0 for k in range(testcase.shape[0])]
for key, value in result_dict.items():
    for index, result in enumerate(value):
        cumu_reward[index] += result

print("Cumulative Reward", cumu_reward)
print("Required Reward", req_reward)

# -------------------------------------------------------------------------------------------------------------
# Calculation of Reward Level
reward_level = [0 for k in range(testcase.shape[0])]
for index in range(len(cumu_reward)):
    reward_level[index] = (cumu_reward[index] / req_reward[index]) * 100
print("Reward level in %", reward_level)

# --------------------------------------------------------------------------------------------------------------
# Translation into Trust Levels
trust_level = []
for i, reward in enumerate(reward_level):
    if 0 < reward <= 30:
        trust_level.append(1)
    elif 30 < reward <= 50:
        trust_level.append(2)
    elif 50 < reward <= 84:
        trust_level.append(3)
    elif 85 < reward <= 94:
        trust_level.append(4)
    elif 95 < reward <= 100:
        trust_level.append(5)
    else:
        trust_level.append(0)
print("Trust level (1-5)", trust_level)
# -------------------------------------------------------------------------------------------------------------
# Plot of Reward Distribution
normalcond_reward = reward_level[0:6]
normalcond_reward.append(0)
nightcond_reward = reward_level[6:13]
badweather_reward = reward_level[13:20]
normal_situation = key_list[6:13]
night_situation = key_list[6:13]
badweather_situation = key_list[6:13]
normalcond_trustlevel = trust_level[0:6]
normalcond_trustlevel.append(0)
nightcond_trustlevel = trust_level[6:13]
badweather_trustlevel = trust_level[13:20]
reward_norm_df = pd.DataFrame({'Normal Condition Situations': normal_situation,
                               'Reward Level in percentage': normalcond_reward,
                               'Trust Level': normalcond_trustlevel})
reward_night_df = pd.DataFrame({'Night Condition Situations': night_situation,
                                'Reward Level in percentage': nightcond_reward,
                                'Trust Level': badweather_trustlevel})
reward_badweather_df = pd.DataFrame({'Bad Weather Situations': badweather_situation,
                                     'Reward Level in percentage': badweather_reward,
                                     'Trust Level': nightcond_trustlevel})

fig = go.Figure()
fig.add_trace(go.Scatter(x=reward_norm_df["Normal Condition Situations"], y=reward_norm_df["Trust Level"],
                         name="Normal Conditions", mode="lines"))
fig.add_trace(go.Scatter(x=reward_night_df["Night Condition Situations"], y=reward_night_df["Trust Level"],
                         name="Night Conditions", mode="lines"))
fig.add_trace(go.Scatter(x=reward_badweather_df["Bad Weather Situations"], y=reward_badweather_df["Trust Level"],
                         name="Bad Weather Conditions", mode="lines"))
fig.update_layout(
    title="Trust Level Translation", xaxis_title="Situations", yaxis_title="Trust Level"
)
fig.show()

fig1 = px.line(reward_norm_df, x="Normal Condition Situations", y="Reward Level in percentage",
               title='Reward Attainment Distribution', markers=True)
fig2 = px.line(reward_night_df, x="Night Condition Situations", y="Reward Level in percentage",
               title='Reward Attainment Distribution', markers=True)
fig3 = px.line(reward_badweather_df, x="Bad Weather Situations", y="Reward Level in percentage",
               title='Reward Attainment Distribution', markers=True)
fig1.show()
fig2.show()
fig3.show()
# -------------------------------------------------------------------------------------------------------------
relative = np.isclose(val_list, trust_level, atol=1, equal_nan=False)
print("Relative array", relative)

# Transfer of Data into Excel Sheet
# reward_df = pd.DataFrame(cumu_reward).T
# reward_df.to_excel(excel_writer="creward.xlsx", index=False, header=False)

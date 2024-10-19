import numpy as np
import pandas as pd
graphs = {}

def get_data(current):
    df = pd.read_csv(current)
    recent = df.tail(1)
    values = ['GoalThink', 'GoalSatis', 'GoalEfficacy', 'GoalIntrinsic', 'GoalApproach', 'GoalGrowth', 'GoalConflict', # Goal graphs
              'StandardThink', 'StandardSatis', 'StandardEfficacy', 'Standardintrinsic', 'StandardApproach', 'StandardGrowth', 'StandardConflict',# Moral Standard Graphs
              'RssmRelateSatis', 'RssmControlSatis', 'RssmEsteemFrus', 'RssmAutoFrus' , 'RSSMName1', 'RSSMName2', 'RSSMName3', 'RSSMName4'# RSSM graphs
              ]
    add_goals(recent, values[:7])
    add_morals(recent, values[7:])
    add_rssm(recent, values[14:])
    add_temperament(recent)
    add_descriptions(recent)
    add_comparison(recent)
    add_personal_data(recent)
    add_radar(recent)

    return graphs

def add_goals(data, values):
    temp = {}
    checker = 0

    # Goal Think
   # for x in range(4):
    temp = {'GoalThink': [], 'GoalSatis': [], 'GoalEfficacy': [], 'GoalIntrinsic': [], 'GoalApproach': [], 'GoalGrowth': [], 'GoalConflict': []}
    column_indices = [38, 49, 60, 71]
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
        #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['GoalThink'].append(data.iloc[0][column_name])
        else:
            temp['GoalThink'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['43_1', '54_1', '66_1', '76_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['GoalSatis'].append(data.iloc[0][column_name])
        else:
            temp['GoalSatis'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['42_1', '53_1', '64_1', '75_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['GoalEfficacy'].append(data.iloc[0][column_name])
        else:
            temp['GoalEfficacy'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['41_1', '52_1', '63_1', '74_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['GoalIntrinsic'].append(data.iloc[0][column_name])
        else:
            temp['GoalIntrinsic'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['39_1', '50_1', '61_1', '72_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['GoalApproach'].append(data.iloc[0][column_name])
        else:
            temp['GoalApproach'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['40_1', '51_1', '62_1', '73_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['GoalGrowth'].append(data.iloc[0][column_name])
        else:
            temp['GoalGrowth'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['40_1', '51_1', '62_1', '73_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['GoalConflict'].append(data.iloc[0][column_name])
        else:
            temp['GoalConflict'] = [data.iloc[0][column_name]]
            checker = 1


    # handle if any values are nan
    temp['GoalThink'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['GoalThink']]
    temp['GoalSatis'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['GoalThink']]
    temp['GoalEfficacy'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['GoalThink']]
    temp['GoalIntrinsic'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['GoalThink']]
    temp['GoalApproach'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['GoalThink']]
    temp['GoalGrowth'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['GoalThink']]
    temp['GoalConflict'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['GoalThink']]


    # # Convert values to integers for calculation
    values = [int(val) for val in temp['GoalThink']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['GoalThink'].insert(0, average)

    values = [int(val) for val in temp['GoalSatis']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['GoalSatis'].insert(0, average)

    values = [int(val) for val in temp['GoalEfficacy']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['GoalEfficacy'].insert(0, average)

    values = [int(val) for val in temp['GoalIntrinsic']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['GoalIntrinsic'].insert(0, average)

    values = [int(val) for val in temp['GoalApproach']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['GoalApproach'].insert(0, average)

    values = [int(val) for val in temp['GoalGrowth']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['GoalGrowth'].insert(0, average)

    values = [int(val) for val in temp['GoalConflict']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['GoalConflict'].insert(0, average)

    graphs['Goals'] = temp
    print("goals graph: ", graphs['Goals'])

def add_morals(data, values):
    temp = {}
    temp = {'StandardThink': [], 'StandardSatis': [], 'StandardEfficacy': [], 'Standardintrinsic': [], 'StandardApproach': [], 'StandardGrowth': [], 'StandardConflict': []}
    checker = 0

    column_indices = [481, 829, 836, 843]
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['StandardThink'].append(data.iloc[0][column_name])
        else:
            temp['StandardThink'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['486_1', '834_1', '841_1', '848_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['StandardSatis'].append(data.iloc[0][column_name])
        else:
            temp['StandardSatis'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['485_1', '833_1', '840_1', '847_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['StandardEfficacy'].append(data.iloc[0][column_name])
        else:
            temp['StandardEfficacy'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['484_1', '832_1', '839_1', '846_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['Standardintrinsic'].append(data.iloc[0][column_name])
        else:
            temp['Standardintrinsic'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['482_1', '830_1', '837_1', '844_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['StandardApproach'].append(data.iloc[0][column_name])
        else:
            temp['StandardApproach'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['483_1', '831_1', '838_1', '845_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['StandardGrowth'].append(data.iloc[0][column_name])
        else:
            temp['StandardGrowth'] = [data.iloc[0][column_name]]
            checker = 1

    column_indices = ['483_1', '831_1', '838_1', '845_1']
    for column_index in column_indices:
        column_name = f'Q{column_index}'
        if checker == 1:
            #temp[values[i]].append(data.iloc[0][f'{values[i]}{x+1}'])
            temp['StandardConflict'].append(data.iloc[0][column_name])
        else:
            temp['StandardConflict'] = [data.iloc[0][column_name]]
            checker = 1


    # Handle if nan values
    temp['StandardThink'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['StandardThink']]
    temp['StandardSatis'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['StandardSatis']]
    temp['StandardEfficacy'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['StandardEfficacy']]
    temp['Standardintrinsic'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['Standardintrinsic']]
    temp['StandardApproach'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['StandardApproach']]
    temp['StandardGrowth'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['StandardGrowth']]
    temp['StandardConflict'] = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp['StandardConflict']]


    values = [int(val) for val in temp['StandardThink']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['StandardThink'].insert(0, average)

    values = [int(val) for val in temp['StandardSatis']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['StandardSatis'].insert(0, average)

    values = [int(val) for val in temp['StandardEfficacy']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['StandardEfficacy'].insert(0, average)

    values = [int(val) for val in temp['Standardintrinsic']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['Standardintrinsic'].insert(0, average)

    values = [int(val) for val in temp['StandardApproach']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['StandardApproach'].insert(0, average)

    values = [int(val) for val in temp['StandardGrowth']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['StandardGrowth'].insert(0, average)

    values = [int(val) for val in temp['StandardConflict']]
    # Calculate the average
    average = sum(values) / len(values)
    temp['StandardConflict'].insert(0, average)

    graphs['Morals'] = temp
    print("morals: ", graphs['Morals'])

def add_comparison(data):

    labels = ['Money', 'JobCareer', 'EducLearning', 'LeisureRecrea', 'SelfGrowth', 'IntimateRel', 'FriendsFamily',
              'SpiritReligion', 'PhysicalHealth']
    values = {}
    column_index = ['81_1', '81_2', '81_3', '81_4', '81_5', '81_6', '81_7', '81_8', '81_10']

    temp_values = []

    for index in column_index:
        column_name = f'Q{index}'
        temp_values.append(data.iloc[0][column_name])
        print("temp val", temp_values)

    # check if nan
    temp_values = [0 if isinstance(val, float) and np.isnan(val) else val for val in temp_values]

    # if all values are now 0 set to original values
    if all(val == 0 for val in temp_values):
        # Set values to be 1-9
        temp_values = list(range(1, 10))

    label_values = dict(zip(labels, temp_values))

    sorted_label_values = dict(sorted(label_values.items(), key=lambda item: int(item[1])))
    graphs['Comparison'] = sorted_label_values

    print("comparison: ", graphs['Comparison'])

def add_personal_data(data):
    temp = {}
    temp['First'] = data.iloc[0]['Q1']
    temp['Last'] = data.iloc[0]['RecipientLastName']
    temp['Email'] = data.iloc[0]['Q3']
    graphs['Personal'] = temp


def add_rssm(data, values):
    temp = {}
    # average = {}
    # average = {'RssmRelateSatisAverage': [], 'RssmControlSatisAverage': []}
    temp = {'RssmRelateSatis': [], 'RssmControlSatis': [], 'RssmEsteemFrus': [], 'RssmAutoFrus': []}

    # relatedness satisfaction
    indices = ['RSSM Relatedness Satisfaction-weightedAvg', 'Person 1 Relatedness Satisfaction-weightedAvg', 'Person 2 Relatedness Satisfaction-weightedAvg', 'Person 3 Relatedness Satisfaction-weightedAvg', 'Person 4 Relatedness Satisfaction-weightedAvg']
    for index in indices:
        temp['RssmRelateSatis'].append(data.iloc[0][index])

    # control satis
    indices = ['RSSM Control Satisfaction-weightedAvg', 'Person 1 Control Satisfaction-weightedAvg', 'Person 2 Control Satisfaction-weightedAvg', 'Person 3 Control Satisfaction-weightedAvg', 'Person 4 Control Satisfaction-weightedAvg']
    for index in indices:
        temp['RssmControlSatis'].append(data.iloc[0][index])

    # esteem frus
    indices = ['RSSM Self-Esteem Frustration-weightedAvg', 'Person 1 Self-Esteem Frustration-weightedAvg', 'Person 2 Self-Esteem Frustration-weightedAvg', 'Person 3 Self-Esteem Frustration-weightedAvg', 'Person 4 Self-Esteem Frustration-weightedAvg']
    for index in indices:
        temp['RssmEsteemFrus'].append(data.iloc[0][index])

    #auto frus
    indices = ['RSSM Autonomy Frustration-weightedAvg', 'Person 1 Autonomy Frustration-weightedAvg', 'Person 2 Autonomy Frustration-weightedAvg', 'Person 3 Autonomy Frustration-weightedAvg', 'Person 4 Autonomy Frustration-weightedAvg']
    for index in indices:
        temp['RssmAutoFrus'].append(data.iloc[0][index])

    graphs['RSSM'] = temp
    print("RSSM graph", graphs['RSSM'])
    temp = {}
    temp['Overall'] = 'Overall'

    column_index = ['11_4_TEXT', '11_5_TEXT', '11_6_TEXT', '11_9_TEXT']
    name = ['RSSMName1', 'RSSMName2', 'RSSMName3', 'RSSMName4']
    for index in column_index:
        column_name = f'Q{index}'
        names = name.pop(0)
        temp[names] = data.iloc[0][column_name]

    graphs['RSSMNames'] = temp
    print("RSSMnames", graphs['RSSMNames'])


def add_temperament(data):
    labels = ['FFFS', 'BIS', 'BAS-Total', 'BAS-RI', 'BAS-GDP', 'BAS-RR', 'BAS-I']
    temp = {}
    temp['FFFS'] = data.iloc[0]['FFFS-weightedAvg']
    temp['BIS'] = data.iloc[0]['BIS-weightedAvg']
    temp['BAS-Total'] = data.iloc[0]['BAS-weightedAvg']
    temp['BAS-RI'] = data.iloc[0]['BAS-RI-weightedAvg']
    temp['BAS-GDP'] = data.iloc[0]['BAS-GDP-weightedAvg']
    temp['BAS-RR'] = data.iloc[0]['BAS-RR-weightedAvg']
    temp['BAS-I'] = data.iloc[0]['BAS-I-weightedAvg']

    graphs['Temperament'] = temp

def add_descriptions(data):
    for i in range(4):
        if i == 0:
           # graphs['GoalDescription'] = [data.iloc[0][f'GoalDescrip{i+1}']]
            graphs['GoalDescription'] = [data.iloc[0]['Q33'], data.iloc[0]['Q34'], data.iloc[0]['Q35'], data.iloc[0]['Q36']]
            print("goal descrip", graphs['GoalDescription'])
            #graphs['StandardDescription'] = [data.iloc[0][f'StandardDescrip{i+1}']]
            graphs['StandardDescription'] = [data.iloc[0]['Q486_4_TEXT'], data.iloc[0]['Q486_5_TEXT'], data.iloc[0]['Q486_6_TEXT'], data.iloc[0]['Q486_7_TEXT']]
            print("standard descrip: ", graphs['StandardDescription'])

        else:
            graphs['GoalDescription'].append(data.iloc[0][f'GoalDescrip{i+1}'])
            graphs['StandardDescription'].append(data.iloc[0][f'StandardDescrip{i+1}'])


def add_radar(data):

    temp = {}
    temp = {'RadarRSSMDominantIPS': [], 'RadarRSSMDominDistantIPS': [], 'RadarRSSMDistantIPS': [], 'RadarRSSMYieldDistantIPS': [], 'RadarRSSMYieldIPS': [], 'RadarRSSMYieldFriendIPS': [], 'RadarRSSMFriendIPS': [], 'RadarRSSMDominFriendIPS': [], 'RadarRSSMName': [], 'RSSM_YVector': [], 'RSSM_XVector': []}

    domineeringLabel = ['CSIPP1 Domineering-weightedAvg','CSIPP2 Domineering-weightedAvg', 'CSIPP3 Domineering-weightedAvg', 'CSIPP4 Domineering-weightedAvg']
    socInhibitLabel = ['CSIPP1 Socially Inhibited-weightedAvg', 'CSIPP2 Socially Inhibited-weightedAvg', 'CSIPP3 Socially Inhibited-weightedAvg', 'CSIPP4 Socially Inhibited-weightedAvg']
    intrusiveLabel = ['CSIPP1 Intrusive-weightedAvg', 'CSIPP2 Intrusive-weightedAvg', 'CSIPP3 Intrusive-weightedAvg', 'CSIPP4 Intrusive-weightedAvg']
    SelfSacLabel = ['CSIPP1 Self-Sacrificing-weightedAvg', 'CSIPP2 Self-Sacrificing-weightedAvg', 'CSIPP3 Self-Sacrificing-weightedAvg', 'CSIPP4 Self-Sacrificing-weightedAvg']
    exploitableLabel = ['CSIPP1 Exploitable-weightedAvg', 'CSIPP2 Exploitable-weightedAvg', 'CSIPP3 Exploitable-weightedAvg', 'CSIPP4 Exploitable-weightedAvg']
    nonassertLabel = ['CSIPP1 Nonassertive-weightedAvg',  'CSIPP2 Nonassertive-weightedAvg',  'CSIPP3 Nonassertive-weightedAvg',  'CSIPP4 Nonassertive-weightedAvg']
    distantLabel = ['CSIPP1 Distant-weightedAvg', 'CSIPP2 Distant-weightedAvg', 'CSIPP3 Distant-weightedAvg', 'CSIPP4 Distant-weightedAvg']
    selfCentLabel = ['CSIPP1 Self-Centered-weightedAvg', 'CSIPP2 Self-Centered-weightedAvg', 'CSIPP3 Self-Centered-weightedAvg', 'CSIPP4 Self-Centered-weightedAvg']

    # domineering - dominant
    for index in domineeringLabel:
        temp['RadarRSSMDominantIPS'].append(data.iloc[0][index])

    #self centered - dominant distant
    for index2 in selfCentLabel:
        temp['RadarRSSMDominDistantIPS'].append(data.iloc[0][index2])

    # distant - distant
    for indexDistant in distantLabel:
        temp['RadarRSSMDistantIPS'].append(data.iloc[0][indexDistant])

    # yield distant - socially inhibited
    for index3 in socInhibitLabel:
        temp['RadarRSSMYieldDistantIPS'].append(data.iloc[0][index3])

    #nonassertive - yield
    for index4 in nonassertLabel:
        temp['RadarRSSMYieldIPS'].append(data.iloc[0][index4])

    # exploitable - yield friendly
    for index5 in exploitableLabel:
        temp['RadarRSSMYieldFriendIPS'].append(data.iloc[0][index5])

    # self-sacrificing - friendly
    for index6 in SelfSacLabel:
        temp['RadarRSSMFriendIPS'].append(data.iloc[0][index6])

    #intrusive - dominant friendly
    for index7 in intrusiveLabel:
        temp['RadarRSSMDominFriendIPS'].append(data.iloc[0][index7])

    graphs['RadarRSSM'] = temp
    temp = {}


    column_index = ['11_4_TEXT', '11_5_TEXT', '11_6_TEXT', '11_9_TEXT']
    name = ['RSSMName1', 'RSSMName2', 'RSSMName3', 'RSSMName4']
    for index in column_index:
        column_name = f'Q{index}'
        names = name.pop(0)
        temp[names] = data.iloc[0][column_name]

    graphs['RadarRSSMName'] = temp

    graphs['RSSM_YVector'] = [1]
    graphs['RSSM_XVector'] = [0.5]


"""
 This is executed after a model is successfully generated.
 With random data inputs, the model is tested.

 The expected intents are classified as expected with sample data
"""
import pandas as pd
from rasa_nlu.model import Interpreter
import json
import xlrd
import xlsxwriter
from tqdm import tqdm
interpreter = Interpreter.load("./models/current/intentClassifier")
df_dict = {}
'''
# Test with sample data
print(json.dumps(interpreter.parse("Your Thoughts Appreciated Sirji,  Impossible is nothing, we can possible all things as a Good Citizen.  We all Support Your Decision. ")["intent"], indent=1))
print(json.dumps(interpreter.parse("Sir please look after the other patient than corona as no opd in hospitals or specialist drs not available ")["intent"], indent=2))
print(json.dumps(interpreter.parse("Happy you shifted from old agenda of dividing people .Please focus on growth of amchi maharatra and people of Maharashtra .Please be strong 💪we are with you  ")["intent"], indent=2))
print(json.dumps(interpreter.parse("willing to help")["intent"], indent=2))
print(json.dumps(interpreter.pars("Sir we are with you in all your decisions. Proud of you, CM of the people, by the people and for the people. ")["intent"], indent=2))
'''
#result = interpreter.parse("best")['intent']['name']
#print(df['intent'].value_counts())
#df.to_csv('d_254663352342290.csv')
# read data
filename = 'data_check.xlsx'
xls = xlrd.open_workbook(filename, on_demand=True)
sheets = xls.sheet_names()

# reading the data
for i in sheets:
    df_dict.update({i.split('.', 1)[0]: pd.read_excel(filename, sheet_name=i)})


#creating intent
writer = pd.ExcelWriter('vdo_intent_all.xlsx', engine='xlsxwriter')
for k, v in tqdm(df_dict.items()):
    df_dict[k]['intent'] = df_dict[k]['message'].apply(lambda x: interpreter.parse(x)['intent']['name'])
    df_dict[k].to_excel(writer, sheet_name=k)
writer.save()




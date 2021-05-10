import pandas as pd

df = pd.read_csv('reference_securities.csv')
print(len(df))
ref_set = set(df["ID_BB_GLOBAL_COMPANY"])

print(len(ref_set))
data = pd.read_csv('corp_pfd.dif', header=None, skiprows=241, sep='|', nrows=2896)
data = data[df.columns]

print(len(data))
rows_to_keep = []
for i in range(len(data)):
    temp_id = data.iloc[i,200]
    # print("temp_id = " + temp_id)
        
    if temp_id in ref_set:
        #print("they're the same!")
        rows_to_keep.append(i)

data = data.iloc[rows_to_keep]         
print(data)
           
 

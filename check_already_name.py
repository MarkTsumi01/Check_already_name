import time

import pandas as pd


df = pd.read_excel('sa.xlsx')
data = pd.read_excel('แก้ล่าสุด.xlsx')
processed_places = data['place'].tolist()



no_data = []
same_data = []
round = 0
success = 0

for i in range(len(df)):
    # create variable to collect critilia place and point to loop
    place = df.iloc[i, 0]

    if place not in processed_places :
        print(f"Dont have {place} in data")
        no_data.append(place)

    else :
        print(f"Same name = {place}")
        same_data.append(place)
    round += 1

len_data = len(no_data)
len_has = len(same_data)
print(no_data)
print(same_data)
print(f"Total round = : {round}")
print(f"Total no data = : {len_data}")
print(f"All same name = : {len_has}")
print(f"Success = {success}")

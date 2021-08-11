from collections import Counter
import csv
with open('SOCR-HeightWeight.csv', newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(n_num)

data = Counter(new_data)
mode_data_for_range = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for Weight, occurrence in data.items():
    if 75 < float(Weight) < 85:
        mode_data_for_range["75-85"] += occurrence
    elif 85 < float(Weight) < 95:
        mode_data_for_range["85-95"] += occurrence
    elif 95 < float(Weight) < 105:
        mode_data_for_range["95-105"] += occurrence
    elif 105 < float(Weight) < 115:
        mode_data_for_range["105-115"] += occurrence
    elif 115 < float(Weight) < 125:
        mode_data_for_range["115-125"] += occurrence
    elif 125 < float(Weight) < 135:
        mode_data_for_range["95-105"] += occurrence
    elif 135 < float(Weight) < 145:
        mode_data_for_range["135-145"] += occurrence
    elif 145 < float(Weight) < 155:
        mode_data_for_range["145-155"] += occurrence
    elif 155 < float(Weight) < 165:
        mode_data_for_range["155-165"] += occurrence
    elif 165 < float(Weight) < 175:
        mode_data_for_range["165-175"] += occurrence
mode_range,mode_occurrence = 0,0
for range, occurrence in mode_data_for_range.items():
    if occurrence > mode_occurrence:
        mode_range, mode_occurrence = [int(range.split("-")[0]),int(range.split("-")[1])], occurrence
mode = float((mode_range[0]+mode_range[1])/2)
print(f"mode is->{mode: 2f}")
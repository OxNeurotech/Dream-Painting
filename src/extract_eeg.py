# This script extracts just the EEG data from the .pth dataset
# and moves this into a new dataset file (.csv extension)
import os
import torch
from typing import List
from tqdm import tqdm

# Access the .pth dataset (original file)
data_dir = os.path.join(os.path.dirname(__file__), "../data/")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
data_path = os.path.join(data_dir, "eeg_55_95_std.pth")
model = torch.load(data_path)

# According to the paper, EEG samples are standardized by the following
def standardize_eeg_sample(eeg: List[float]) -> List[float]:
    if len(eeg) < 460:
        print("This array has too few samples!")
        return eeg
    return eeg[20:460]

# Field names need to be
# Subject Number
# Image Number
# Channel Numbers

# get the channel numbers in order
file = open("../data/channel_names.txt")
channel_names = file.read().splitlines()
file.close()

fieldnames = ["subject", "label"]
fieldnames.extend(channel_names)

eeg_data = {key: [] for key in dict.fromkeys(fieldnames)}

# load data into dictionaries

print("Loading data...")
for i in tqdm(range(len(model['dataset']))):
    eeg_data['subject'].append(model['dataset'][i]['subject'])
    eeg_data['label'].append(model['dataset'][i]['label'])
    for j in range(128):
        eeg_data[channel_names[j]].append(standardize_eeg_sample(model['dataset'][i]['eeg'][j]))
print("Data loaded!")

torch.save(eeg_data, os.path.join(data_dir, "data.pt"))

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
file = open(os.path.join(data_dir, "channel_names.txt"))
channel_names = file.read().splitlines()
file.close()

fieldnames = ["image"]
fieldnames.extend(channel_names)

subj_1 = dict.fromkeys(fieldnames, [])
subj_2 = dict.fromkeys(fieldnames, [])
subj_3 = dict.fromkeys(fieldnames, [])
subj_4 = dict.fromkeys(fieldnames, [])
subj_5 = dict.fromkeys(fieldnames, [])
subj_6 = dict.fromkeys(fieldnames, [])

subj_choices = {1: subj_1, 2: subj_2, 3: subj_3, 4: subj_4, 5: subj_5, 6: subj_6}
electrode_pos = dict(zip(range(128), channel_names))

# load data into dictionaries
print("Loading data...")
for i in tqdm(range(len(model['dataset']))):
    subj = subj_choices[model['dataset'][i]['subject']]
    subj['image'].append(model['dataset'][i]['image'])
    for j in range(len(model['dataset'][i]['eeg'])):
        subj[electrode_pos[j]].append(standardize_eeg_sample(model['dataset'][i]['eeg'][j]))
print("Data loaded!")

torch.save(subj_choices, os.path.join(data_dir, "data.pth"))
# This script extracts just the EEG data from the .pth dataset
# and moves this into a new dataset file (.csv extension)

import os
import torch

# Access the .pth dataset (original file)
data_dir = os.path.join(os.path.dirname(__file__), "../data/")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
data_path = os.path.join(data_dir, "eeg_55_95_std.pth")
model = torch.load(data_path)


# Create the .csv ready for writing
save_path = os.path.join(data_dir, "eeg_data.csv")


# Field names need to be
# Subject Number
# Image Number
# Channel Numbers

# get the channel numbers in order
file = open("../data/channel_names.txt")
channel_names = file.read().splitlines()
file.close()

# print(len(model['dataset'][1]['eeg'][0]))
with open(save_path, 'w') as csvfile:
    fieldnames = ["subject", "image"]
    fieldnames.extend(channel_names)    # to include the channel numbers


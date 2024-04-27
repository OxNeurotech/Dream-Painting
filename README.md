# Dream-Painting
g.tec SPRING SCHOOL BR41N.io Hackathon - Dream Painting category
Project: Using 16-channel EEG recording positions to generate images from sleep signals.

## Strategy
[DreamDiffusion](https://github.com/bbaaii/DreamDiffusion) is a "framework for generating high-quality images from brain EEG signals". The model created in this framework relies on a 128-channel EEG dataset.

Our device is the OPENBCI CYTON + DAISY Chip. Together, they combine to 16 EEG channels. The aim is to either:

1. Analyze and extract the 16 most crucial channels in the EEG dataset used to train the model in DreamDiffusion, and generate images using these 16 channels

2. Choose 16 EEG positions to generate the other 112 signals generatively, making up the 128 channel size for input to the DreamDiffusion model

Then, we will test our strategy with actual data collected from our own setup.

## Data
The input data to analyze is found in [eeg_visual_classification](https://github.com/perceivelab/eeg_visual_classification?tab=readme-ov-file). This is **NOT** included in the repo, and needs to be downloaded (only `eeg_55_95_std.pth` is necessary). The channel order is recorded in a ` channel_names.txt ` file in the `data` directory. 

import librosa

# Create a list of durations
old_durations_list = []

# Loop over the dataset
for row in dataset["path"]:
    duration = librosa.get_duration(filename=row)
    old_durations_list.append(duration)

# Create a new column
dataset = dataset.add_column("duration", old_durations_list)

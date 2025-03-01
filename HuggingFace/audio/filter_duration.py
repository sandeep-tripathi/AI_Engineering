import librosa

# Create a list of durations
old_durations_list = []

# Loop over the dataset
for row in dataset["path"]:
    old_durations_list.append(librosa.get_duration(path=row))

# Create a new column
dataset = dataset.add_column("duration", old_durations_list)

# Filter the dataset for sound under 6 sec
filtered_dataset = dataset.filter(lambda d: d < 6.0, input_columns=["duration"], keep_in_memory=True)

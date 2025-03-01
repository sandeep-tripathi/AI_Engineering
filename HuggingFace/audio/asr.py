from transformers import pipeline

# Create an ASR pipeline using Meta's wav2vec model
meta_asr = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

# Predict the text from the example audio
example_audio = example["audio"]["path_to_audio_file"]  # Change this to the appropriate key and path for the audio file
meta_pred = meta_asr(example_audio)["text"].lower()

# Repeat for OpenAI's Whisper model
open_asr = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")
open_pred = open_asr(example_audio)["text"].lower()

# Print the prediction from both models
print("META:", meta_pred)
print("OPENAI:", open_pred)

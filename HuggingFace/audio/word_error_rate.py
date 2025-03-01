from transformers import pipeline
import evaluate

# Create an ASR pipeline using Meta's wav2vec model
meta_asr = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

# Predict the text from the example audio
example_audio = example["audio"]["path_to_audio_file"]  # Adjust the key to your data structure
meta_pred = meta_asr(example_audio)["text"].lower()

# Repeat for OpenAI's Whisper model
open_asr = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")
open_pred = open_asr(example_audio)["text"].lower()

# Create the word error rate metric
wer = evaluate.load("wer")

# Save the true sentence of the example
true_sentence = example["sentence"].lower()  # Adjust the key to your data structure

# Compute the wer for each model prediction
meta_wer = wer.compute(predictions=[meta_pred], references=[true_sentence])
open_wer = wer.compute(predictions=[open_pred], references=[true_sentence])

# Print the WER for both models
print(f"The WER for the Meta model is {meta_wer} and for the OpenAI model is {open_wer}")

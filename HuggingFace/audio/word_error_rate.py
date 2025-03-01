import pandas as pd
from transformers import pipeline
import evaluate

# Create an ASR pipeline using Meta's wav2vec2-base-960h model
meta_asr = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

# Repeat for OpenAI's whisper-tiny model
open_asr = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")

# Create the data function
def data(n=3):
    for i in range(n):
        yield english[i]["audio"]["array"], english[i]["sentence"].lower()

# Predict the text for the audio file with both models
output = []
for audio, sentence in data():
    meta_pred = meta_asr(audio)["text"].lower()
    open_pred = open_asr(audio)["text"].lower()
    # Append to the output list
    output.append({"sentence": sentence, "metaPred": meta_pred, "openPred": open_pred})

output_df = pd.DataFrame(output)

# Create the word error rate metric
wer = evaluate.load("wer")

# Compute the WER for both models
metaWER = wer.compute(predictions=output_df["metaPred"], references=output_df["sentence"])
openWER = wer.compute(predictions=output_df["openPred"], references=output_df["sentence"])

# Print the WER
print(f"The WER for the Meta model is {metaWER} and for the OpenAI model is {openWER}")

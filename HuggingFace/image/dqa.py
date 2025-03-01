from transformers import pipeline

# Create the pipeline
dqa = pipeline(task="document-question-answering", 
               model="naver-clova-ix/donut-base-finetuned-docvqa")

# Set the image and question
image = "document.png"
question = "Which meeting is this document about?"

# Get the answer
results = dqa(image=image, question=question)

print(results)

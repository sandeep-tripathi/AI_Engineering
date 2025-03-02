# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_3ZCPFh_9+++Ro1UvTStRiXGYe")
index = pc.Index('pinecone-datacamp')

# Takes the documents retrieved from the Pinecone index, and integrates them into a prompt that the question-answering model can ingest:
def prompt_with_context_builder(query, docs):
    delim = '\n\n---\n\n'
    prompt_start = 'Answer the question based on the context below.\n\nContext:\n'
    prompt_end = f'\n\nQuestion: {query}\nAnswer:'

    prompt = prompt_start + delim.join(docs) + prompt_end
    return prompt


# Query
query = "How to build next-level Q&A with OpenAI"

# Retrieve the top three most similar documents and their sources
documents, sources = retrieve(query, top_k=3, namespace='youtube_rag_dataset', emb_model="text-embedding-3-small")

prompt_with_context = prompt_with_context_builder(query, documents)
print(prompt_with_context)

def question_answering(prompt, sources, chat_model):
    sys_prompt = "You are a helpful assistant that always answers questions."
    
    # Use OpenAI chat completions to generate a response
    res = client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    answer = res.choices[0].message.content.strip()
    answer += "\n\nSources:"
    for source in sources:
        answer += "\n" + source[0] + ": " + source[1]
    
    return answer

answer = question_answering(
  prompt=prompt_with_context,
  sources=sources,
  chat_model='gpt-4o-mini')
print(answer)


####Output
"""
Answer the question based on the context below.

Context:
and our model into a pipeline, into a Q&A pipeline. So again, we get this pipeline from the Transformers library. So we come down here, do from Transformers, import pipeline. And now what we want to do is just initialize a pipeline object. So to do that, we just write pipeline. And then in here, what we need to add is a model type. So obviously, you can see up here, we have all of these different tasks. So summarization, text generation and so on. The Transformers library needs to understand, or this pipeline object needs to understand which one of those pipelines or functions we are intending to use. So to tell it that we want to do question answering, we just write question answering. And that basically sets the wrapper of the pipeline to handle question answering formats. So we'll see our input and for our input, we will be passing a context and a question. So we'll see that it will convert into the right structure that we need for question answering, which is the CLS context separator, question separator and padding. It will convert into that, feed it into our tokenizer.

---

and our model into a pipeline, into a Q&A pipeline. So again, we get this pipeline from the Transformers library. So we come down here, do from Transformers, import pipeline. And now what we want to do is just initialize a pipeline object. So to do that, we just write pipeline. And then in here, what we need to add is a model type. So obviously, you can see up here, we have all of these different tasks. So summarization, text generation and so on. The Transformers library needs to understand, or this pipeline object needs to understand which one of those pipelines or functions we are intending to use. So to tell it that we want to do question answering, we just write question answering. And that basically sets the wrapper of the pipeline to handle question answering formats. So we'll see our input and for our input, we will be passing a context and a question. So we'll see that it will convert into the right structure that we need for question answering, which is the CLS context separator, question separator and padding. It will convert into that, feed it into our tokenizer.

---

And on the Hugging Face website, we just want to go over to the Models page. So it's here. Okay and on this Models page, the thing that we want to be looking at is this question and answering task. So here we have all these tasks because when you're working with transformers, they can work with a lot of different things. Text summarization, text classification, generation, loads of different things. But what we want to do is question answering. So we click on here and this filters all of the models that are available to us just purely for question and answering. So this is the sort of power of using the Hugging Face Transformers library. It already has all these pre-trained models that we can just download and start using. Now, when you want to go and apply these to specific use cases, you probably want to fine tune it, which means you want to train it a little bit more than what it is already trained. But for actually getting used to how all of this works, all you need to do is download this model and start asking questions and understanding how everything is actually functioning. So obviously there's a lot of models here. We've got 262 models for question answering,

Question: How to build next-level Q&A with OpenAI
Answer:
The context provided does not specifically address building a next-level Q&A system with OpenAI. However, it does describe how to set up a question-answering pipeline using the Transformers library, which can be a foundational step in creating a Q&A system. To build a more advanced Q&A system with OpenAI, you might consider the following steps:

1. **Choose a Model**: Select a suitable pre-trained model from the Hugging Face Models page that is designed for question answering.

2. **Initialize the Pipeline**: Use the Transformers library to create a Q&A pipeline by importing the pipeline function and specifying the model type as "question answering".

3. **Prepare Input**: Structure your input data by providing a context and a question. The pipeline will handle the formatting required for question answering.

4. **Fine-tuning**: If necessary, fine-tune the model on your specific dataset to improve its performance for your particular use case.

5. **Integration**: Integrate the Q&A pipeline into your application, allowing users to input questions and receive answers based on the provided context.

6. **Enhancements**: Consider adding features such as user feedback loops, context retrieval from databases, or multi-turn conversations to enhance the Q&A experience.

By following these steps and leveraging the capabilities of the Transformers library and OpenAI models, you can build a sophisticated Q&A system.

Sources:
How to Build Q&A Models in Python (Transformers): https://youtu.be/scJsty_DR3o
How to Build Q&A Models in Python (Transformers): https://youtu.be/scJsty_DR3o
How to Build Q&A Models in Python (Transformers): https://youtu.be/scJsty_DR3o

<script.py> output:
    Answer the question based on the context below.
    
    Context:
    and our model into a pipeline, into a Q&A pipeline. So again, we get this pipeline from the Transformers library. So we come down here, do from Transformers, import pipeline. And now what we want to do is just initialize a pipeline object. So to do that, we just write pipeline. And then in here, what we need to add is a model type. So obviously, you can see up here, we have all of these different tasks. So summarization, text generation and so on. The Transformers library needs to understand, or this pipeline object needs to understand which one of those pipelines or functions we are intending to use. So to tell it that we want to do question answering, we just write question answering. And that basically sets the wrapper of the pipeline to handle question answering formats. So we'll see our input and for our input, we will be passing a context and a question. So we'll see that it will convert into the right structure that we need for question answering, which is the CLS context separator, question separator and padding. It will convert into that, feed it into our tokenizer.
    
    ---
    
    and our model into a pipeline, into a Q&A pipeline. So again, we get this pipeline from the Transformers library. So we come down here, do from Transformers, import pipeline. And now what we want to do is just initialize a pipeline object. So to do that, we just write pipeline. And then in here, what we need to add is a model type. So obviously, you can see up here, we have all of these different tasks. So summarization, text generation and so on. The Transformers library needs to understand, or this pipeline object needs to understand which one of those pipelines or functions we are intending to use. So to tell it that we want to do question answering, we just write question answering. And that basically sets the wrapper of the pipeline to handle question answering formats. So we'll see our input and for our input, we will be passing a context and a question. So we'll see that it will convert into the right structure that we need for question answering, which is the CLS context separator, question separator and padding. It will convert into that, feed it into our tokenizer.
    
    ---
    
    And on the Hugging Face website, we just want to go over to the Models page. So it's here. Okay and on this Models page, the thing that we want to be looking at is this question and answering task. So here we have all these tasks because when you're working with transformers, they can work with a lot of different things. Text summarization, text classification, generation, loads of different things. But what we want to do is question answering. So we click on here and this filters all of the models that are available to us just purely for question and answering. So this is the sort of power of using the Hugging Face Transformers library. It already has all these pre-trained models that we can just download and start using. Now, when you want to go and apply these to specific use cases, you probably want to fine tune it, which means you want to train it a little bit more than what it is already trained. But for actually getting used to how all of this works, all you need to do is download this model and start asking questions and understanding how everything is actually functioning. So obviously there's a lot of models here. We've got 262 models for question answering,
    
    Question: How to build next-level Q&A with OpenAI
    Answer:
    The context provided does not specifically address building a next-level Q&A system with OpenAI. However, it does describe how to set up a question-answering pipeline using the Transformers library, which can be a foundational step in creating a Q&A system. To build a more advanced Q&A system with OpenAI, you might consider the following steps:
    
    1. **Choose the Right Model**: Start by selecting a suitable pre-trained model from the Hugging Face Models page that is specifically designed for question answering.
    
    2. **Fine-Tuning**: Depending on your specific use case, you may want to fine-tune the model on a dataset that is relevant to your domain to improve its performance.
    
    3. **Pipeline Initialization**: Use the Transformers library to initialize a Q&A pipeline by importing the necessary components and specifying the model type as "question answering".
    
    4. **Input Preparation**: Prepare your input by providing a context and a question. The pipeline will handle the formatting required for question answering.
    
    5. **Integration with OpenAI**: If you want to leverage OpenAI's capabilities, you could integrate their API to enhance the Q&A system, possibly by using their language models for generating more nuanced responses or handling complex queries.
    
    6. **Testing and Iteration**: Continuously test the system with various questions and contexts, iterating on the model and its parameters to improve accuracy and relevance.
    
    7. **User Interface**: Consider building a user-friendly interface that allows users to easily input their questions and view the answers generated by the model.
    
    By following these steps, you can create a more sophisticated Q&A system that leverages both the Transformers library and OpenAI's models.
    
    Sources:
    How to Build Q&A Models in Python (Transformers): https://youtu.be/scJsty_DR3o
    How to Build Q&A Models in Python (Transformers): https://youtu.be/scJsty_DR3o
    How to Build Q&A Models in Python (Transformers): https://youtu.be/scJsty_DR3o
"""

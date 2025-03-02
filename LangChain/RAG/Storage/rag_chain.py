vectorstore = Chroma.from_documents(
    docs,
    embedding=OpenAIEmbeddings(api_key='<OPENAI_API_TOKEN>', model='text-embedding-3-small'),
    persist_directory=os.getcwd()
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Create a chain to link retriever, prompt_template, and llm
rag_chain = ({"context": retriever, "question": RunnablePassthrough()}
            | prompt_template
            | llm)

# Invoke the chain
response = rag_chain.invoke("Which popular LLMs were considered in the paper?")
print(response.content)

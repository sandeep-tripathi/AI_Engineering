# Import the character splitter
from langchain_text_splitters import CharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = CharacterTextSplitter(
    separator='\n',
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap)

# Split the string and print the chunks
docs = splitter.split_text(quote) 
print(docs)
print([len(doc) for doc in docs])


import tiktoken

# Load the encoder for the OpenAI text-embedding-3-small model
enc = tiktoken.encoding_for_model("text-embedding-3-small")

# Encode each text in documents and calculate the total tokens
total_tokens = sum(len(enc.encode(doc)) for doc in documents)

cost_per_1k_tokens = 0.00002

# Display number of tokens and cost
print('Total tokens:', total_tokens)
print('Cost:', (total_tokens / 1000) * cost_per_1k_tokens)

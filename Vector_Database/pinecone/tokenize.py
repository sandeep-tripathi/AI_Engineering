from collections import Counter

def tokenize(text):
    # Assuming this is a function that splits text into tokens
    return text.split()

class Document:
    def __init__(self, text):
        self.text = text
        # Pre-tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # Tally the document's word counts with non-public count_words method
        self.word_counts = self._count_words()

    def _tokenize(self):
        # Non-public method to tokenize the document's text
        return tokenize(self.text)
	
    def _count_words(self):
        # Non-public method to tally document's word counts with Counter
        return Counter(self.tokens)

# Example usage
document = Document("This is a test. This test is quite simple.")
print(document.tokens)
print(document.word_counts)


# Output
#['This', 'is', 'a', 'test.', 'This', 'test', 'is', 'quite', 'simple.']
#Counter({'This': 2, 'is': 2, 'test.': 1, 'test': 1, 'a': 1, 'quite': 1, 'simple.': 1})

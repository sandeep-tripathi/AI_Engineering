import itertools
def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable into an iterator
    it = iter(iterable)
    # Slice the iterator into chunks of size batch_size
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        # Yield the chunk
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))


# Example Usage:
# all_vectors = [...]  # Assume this is your list of vectors
# for chunk in chunks(all_vectors, batch_size=100):
#     print(chunk)  # Process each chunk

from scipy.spatial import distance

# Assuming vectors A, B, C, and D are defined as follows
A = [1, 2, 3]
B = [4, 5, 6]
C = [1, 1, 1]
D = [2, 2, 2]

# Compute cosine distances
dist_A_B = distance.cosine(A, B)
dist_A_C = distance.cosine(A, C)
dist_A_D = distance.cosine(A, D)

# Print the distances
print(f"Cosine distance between A and B: {dist_A_B}")
print(f"Cosine distance between A and C: {dist_A_C}")
print(f"Cosine distance between A and D: {dist_A_D}")

# Determine the vector most similar to A
distances = {
    "B": dist_A_B,
    "C": dist_A_C,
    "D": dist_A_D
}

# Find the vector with the minimum distance
most_similar_vector = min(distances, key=distances.get)
print(f"The vector most similar to A is: {most_similar_vector}")

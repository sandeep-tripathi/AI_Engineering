"""Connect to your Index



Install Pinecone
If you haven’t already, install the Python client on the command line:

pip install pinecone
Initialize
"Next, initialize the client and target the “quickstart” index:
"""

from pinecone import Pinecone

pc = Pinecone(api_key="********-****-****-****-************")
index = pc.Index("quickstart")
Upsert
Then write vectors into a namespace in your index. You use namespaces to help speed up queries and comply with multi-tenancy requirements.

index.upsert(
    vectors=[
        {
            "id": "vec1", 
            "values": [1.0, 1.5], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec2", 
            "values": [2.0, 1.0], 
            "metadata": {"genre": "action"}
        }, {
            "id": "vec3", 
            "values": [0.1, 0.3], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec4", 
            "values": [1.0, -2.5], 
            "metadata": {"genre": "action"}
        }
    ],
    namespace= "ns1"
)
Query
Search the "ns1" namespace in your index for the 2 vectors that are most similar to an example vector, filtering for results that match a specific metadata value:

response = index.query(
    namespace="ns1",
    vector=[0.1, 0.3],
    top_k=2,
    include_values=True,
    include_metadata=True,
    filter={"genre": {"$eq": "action"}}
)
    
print(response)

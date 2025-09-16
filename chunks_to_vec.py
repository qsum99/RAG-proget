from google import genai
import os
import json
import pandas as pd
import joblib 
from google.genai import types
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# using googal gemini
def creting_embedding(text):
    client = genai.Client(api_key="AIzaSyBQXVAajLzVJFOJMWpp90u_qMLh0tlF80Q")

    texts = [text]

    result = [
        np.array(e.values) for e in client.models.embed_content(
            model="gemini-embedding-001",
            contents=texts,
            config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")).embeddings
    ]
    return result
# let's pass all chunks
json_file=os.listdir("jsons")
my_list=[]
chunk_id=0
# reading all json_files
for jsons in json_file:
    with open(f"jsons/{jsons}") as f:
        data=json.load(f)
    print(f"creting embedding for this file:{jsons}")
    embeddings=creting_embedding([d['text'] for d in data['chunks']]) # passing all text to convert in embeddings
    for i , chunk in enumerate(data["chunks"]):
        chunk["chunk_id"]=chunk_id # adding a chunk_id
        chunk["embedding"]=embeddings # adding a embeddings in df
        chunk_id=+1
        my_list.append(chunk)
df=pd.DataFrame.from_records(my_list)# conveting in to a Dataframe
joblib.dump(df,"embeddings.joblib")#saving in joblib

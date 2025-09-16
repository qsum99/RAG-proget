import joblib
from google import genai
from google.genai import types
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
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
#lets lode the data
data=joblib.load("embeddings.joblib")

# taking input form user and convert into the embeddings
user_input=input("Ask a Question:")
input_embedding=creting_embedding(user_input)
# finding a cosine_similarity embeddings
similarity= cosine_similarity(np.vstack(input_embedding),np.vstack(data["embedding"])).flatten()
top_elemant=15
max_ind=similarity.argsort()[::-1][0:top_elemant]
similarity_df=data.loc[max_ind]
prompt=f""" i am teaching quantum infromation and communition using coursera's introduction quantum infromation,
here are the video subtitle chunks containing video title ,video number,module , start time in secondes,end time in secondes
and the text at that time
{similarity_df[["title","number","module","start","end","text"]].to_json()}
--------------------------------------------------------------------------
"{user_input}"
user asked this question related to the video chunks ,you have to answer in human way (dont mention the above format,
it is just for you) where and how much content is taught in which video (in which video and which module at what timestamp) and guide the user to go 
to that particular video. if user asks unrelated questions ,tell him that you can only answer questiona
related to the course
"""
for index ,item in similarity_df.iterrows():
    print(index, item['title'],item['module'],item['number'],item['text'],item['start'],item['end'])
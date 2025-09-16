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
#creting modle
def inference(prompt):
    client= genai.Client(api_key="AIzaSyBQXVAajLzVJFOJMWpp90u_qMLh0tlF80Q")
    response = client.models.generate_content(
                model="models/gemini-2.5-flash",
               contents=prompt
               )
    return response.text

#lets load the data
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
and the output shoude be in this fromat
Your response should have the following structure:
(do not use this type of sentenes Based on the provided video subtitles this all are there for you )
1.  A heading or introductory sentence stating where quantum teleportation is taught (e.g., "Based on the provided video subtitles ").
2.  A list of key video details:
    * **Video:** [Video Title and Number]
    * **Module:** [Module Number]
3.  A brief summary of what is discussed in the video, referencing specific concepts like CNOT gates or the one-time pad.
4.  A bulleted list of specific timestamp ranges and a short description of the content within that range.(only conseder 4 to 5 timestamp and convet seconds in to a minute)
5.  A concluding sentence guiding the user to the correct video.

Do not include any information that is not present in the provided text.if what to include place include relevant to that specific topic"
in end ask user can hellp moor about that or releted sentens
"""
response=inference(prompt)
print(response)

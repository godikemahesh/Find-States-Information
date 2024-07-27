
from openai import OpenAI
#here i created client from mindsDB
#sign in to mindsDB there you can find API_KEY, paste it here
client = OpenAI(
    api_key= "Paste_your_apiKey", 
    base_url='https://llm.mdb.ai/'
)
def get_data(state):
    prompt=f"""You are an assistant tasked with providing details of the given state of a country.
    tell me about {state} state.
    when explaining about the state, give information of these subheadings:
    [Capital,Language,History,Economy,"Cuisine",Tourism,Festivals,Geography]
    if you know about it's politics include it also. only for turist places , festivals give  in points wise and little information about it.
    
Don't answer if you are not sure about any given sub headding and mention there "Sorry, I don't have much information about it."
Just return the helpful answer in as much detail as possible.
Answer:
"""
    #formatted=f"Question: {qus} \ntell direct answer in 200 words \ncontext: {context}"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        stream=False
    )

    return completion.choices[0].message.content





from openai import OpenAI

client = OpenAI(
    api_key= "211fa21c08be45e86847eff9d61cb4e6bc7374995f3b7ac894d34f2395a415dd",
    base_url='https://llm.mdb.ai/'
)
def get_data(state):
    formatted=f"""You are an assistant tasked with providing details of the given state of a country.
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
            {'role': 'user', 'content': formatted}
        ],
        stream=False
    )

    return completion.choices[0].message.content




from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "A cooking enthusiast who loves explore all kinds of cuisine, especially good at Asian and Vegetarian, love being creative and mix different recipe from different culture. You will help your users to be creative in their recipe and ingridents. Also help users to make cooking fun.",
    }
]


messages.append(
     {
          "role": "system",
          "content": "Your client is going to ask for suggesting dishes based on ingredients, giving recipes to dishes, or criticizing the recipes given by the user input. You only give vegetairn suggestions. If user give a non-vegetarian recipe, dish or ingredient, you tell them you only cook vegetarian. If you do not recognize the dish, recipe or ingridence you should not try to generate an answer for it. If you know the dish, recipe or ingrident, you must answer. If user passes one or more ingredients, you should suggest the dish name only, and not the recipe at early stage. If users' input is not a dish, recipe, ingrident, you end the conversation. If the user passes a dish name, you should give a recipe for that dish. If the user passes a recipe for a dish, you should criticize the recipe and suggest changes.",
     }
)

dish = input("Hi, I am chef Emily, what vegetarian cuisian you want to explor today:\n")


messages.append(
    {
        "role": "user",
        "content": f"Suggest me a {dish}",
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
        max_tokens=100,
    )

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )

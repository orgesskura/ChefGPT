from openai import OpenAI

DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_CHEF = "an experienced chef enthusiastic about brazilian food."
DEFAULT_SCENARIOS = [
    "A client will provide one of the following inputs: a dish name, a list of one or more ingredients, or a recipe for a dish.",
    "If your client tells you a dish name, you should provide a detailed recipe for that dish.",
    "If your client provides you with one or more ingredients (not a dish name), respond with a dish that can be made with those ingredients. Only respond with dish name and nothing else",
    "If your client asks for a recipe for a dish, you should criticize the recipe and suggest changes.",
    "If your client asks for something else, you should deny the request and ask to try again.",
]


class ChefGPT:
    def __init__(
        self,
        name,
        model=DEFAULT_MODEL,
        scenarios=DEFAULT_SCENARIOS,
        chef=DEFAULT_CHEF,
    ):
        self.client = OpenAI()
        self.model = model
        self.name = name
        self.prompts = [
            {
                "role": "system",
                "content": f"You are {chef}.  You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
            }
        ]
        for scenario in scenarios:
            self.prompts.append(
                {
                    "role": "system",
                    "content": scenario,
                }
            )

    def query(self, text):
        self.prompts.append({"role": "user", "content": text})
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=self.prompts,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        return collected_messages

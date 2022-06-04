import settings
import openai


openai.api_key = settings.API['KEY']
response = openai.Completion.create(engine="davinci",
                                    prompt="There is a house in New Orleans",
                                    max_tokens=100)

print(response['choices'][0]['text'])
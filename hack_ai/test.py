
from openai import OpenAI

def main():

    client = OpenAI(
        api_key='呱',  
    )

    completion = client.images.generate(
        model="dall-e-3",
        prompt="A cute baby sea otter",
        n=1,
        size="1024x1024"
    )
    # ans = completion.choices[0].message
    # print(completion)
    url = completion.data[0].url
    print(url)

main()

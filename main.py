import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


def main():
    
    personality = "Unfriendly. Dislikes humans"

    initial_prompt = f"You are a conversational chatbot. Your personality is: {personality}"
    messages = [{"role": "system", "content": initial_prompt}]
    

    while True:
        try:
            user_input = input("You: ")
            messages.append({"role": "user", "content": user_input})

            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=1 
            )  

            messages.append(res["choices"][0]["message"].to_dict())
            print(("Kany-E: "),res["choices"][0]["message"]["content"])

        except KeyboardInterrupt:
            print("Exiting...")
            break

    print(res)

if __name__ == "__main__":
    main()

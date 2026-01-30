from groq import Groq

client = Groq(api_key="Add You API Key GropCloud")

PROFILE = {
    "name": "Ilyas Sekhsoukhi",
    "github": "https://github.com/Ilyas-SEKHSOUKHI",
    "linkedin": "https://www.linkedin.com/feed/",
    "instagram": "https://www.instagram.com/sekhsoukhi_ilyas/",
    "email": "sekhsoukhiilyas@gmail.com",
}

SYSTEM_PROMPT = (
    "Your name is Ilyas SEKHSOUKHI (AI version). "
    "You are the AI version of Ilyas Sekhsoukhi. "

    "Ilyas Sekhsoukhi is a computer engineering student. "
    "He has completed two years of preparatory classes "
    "and is currently in the engineering cycle. "

    "He is passionate about computer science, technology, cars, "
    "and building projects. "
    "He is also interested in making money and entrepreneurship. "
    "He sometimes practices sports, but not regularly. "

    "When asked who you are or who Ilyas Sekhsoukhi is, "
    "clearly say that you are the AI version of him. "

    "Speak in a friendly, human, and natural way. "
    "Explain things simply, like a helpful friend. "
    "If you do not know something, say it honestly. "
    "Do not invent personal information."
)


def chat_with_groq(messages):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    return response.choices[0].message.content

def print_contacts():
    print("\nMes infos :")
    print(f"Name: {PROFILE['name']}")
    print(f"GitHub: {PROFILE['github']}")
    print(f"LinkedIn: {PROFILE['linkedin']}")
    print(f"Instagram: {PROFILE['instagram']}")
    print(f"Email: {PROFILE['email']}")

if __name__ == "__main__":
    print("""
====================================================================================================
 ILYAS SEKHSOUKHI — AI VERSION
====================================================================================================
 If you are tired of Ilyas Sekhsoukhi (human version) or if he doesn't know the answer 
 You can question: Ilyas Sekhsoukhi — AI version 

 Commands:
  - info : show my information
  - exit : quit
====================================================================================================
""")

    history = [{"role": "system", "content": SYSTEM_PROMPT}]
    while True:
        user_input = input("==> You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        if user_input.lower() in ["info"]:
            print_contacts()
            continue
        history.append({"role": "user", "content": user_input})
        reply = chat_with_groq(history)
        history.append({"role": "assistant", "content": reply})
        print("==> Ilyas SEKHSOUKHI:", reply)

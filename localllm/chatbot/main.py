    """
    
    _summary_ : Ollama llama3 from Ollama.com
    
    https://realpython.com/python-gui-tkinter/
    
    """

from langchain_ollama OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

import tkinter as tk


template = '''
Answer below.

Conversation history: {context}

Question: {question}

Answer: 
'''



model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)


chain = prompt | model


window = tk.Tk()

context = ""
greeting = tk.Label(text=context)

entry = tk.Entry(fg="yellow", bg="blue", width=50)   

user_input = ""

def get_entry_text():
    user_input = entry.get()
    
    return user_input

MyButton1 = tk.Button(text="Submit", width=10, command=entry.get())


def run_chat_ai_gui():
    greeting.pack()
    while True:
        if user_input.lower() == "exit":
            window.destroy()
            break
            
        

        result = chain.invoke({"context": context, "question": "hey how are you"})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"
        
if __name__ == "__main__":
    
    run_chat_ai_gui()
    

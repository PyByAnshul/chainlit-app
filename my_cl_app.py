import chainlit as cl
from langchain_ollama import OllamaLLM

@cl.on_chat_start
async def main():
    await cl.Message(content="Hello World").send()

@cl.on_message
async def handle_message(message):
    try:
        ollama = OllamaLLM(base_url='http://ollama:11434', model='llama3.2:3b')
        response = ollama.invoke(message.content)
        if response:
            await cl.Message(content=response).send()
        else:
            await cl.Message(content="Error: Could not get a response from Llama.").send()
    except Exception as e:
        await cl.Message(content=f"An error occurred: {str(e)}").send()

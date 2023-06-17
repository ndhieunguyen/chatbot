import poe
import logging


def query_from_API(query: str, token: str, bot_name: str = "chinchilla") -> str:
    response = ""
    try:
        poe.logger.setLevel(logging.INFO)
        client = poe.Client(token)

        for chunk in client.send_message(bot_name, query, with_chat_break=True):
            word = chunk["text_new"]
            response += word

        client.purge_conversation(bot_name, count=3)
    except Exception as e:
        print(e)
        pass
    return response

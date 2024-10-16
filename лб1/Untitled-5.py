from telethon import TelegramClient

api_id = 'id'  
api_hash = 'hash_id'  
phone_number = 'number'    

client = TelegramClient('session_name', api_id, api_hash)

async def send_message_to_chat(chat_id, message_text):
    try:
        await client.send_message(chat_id, message_text)
        print(f"Повідомлення відправлено до чату {chat_id}")
    except Exception as e:
        print(f"Помилка: {e}")

async def main():
    await client.start(phone_number)
    
    await send_message_to_chat('@test6385385385375', 'шо вы лохи')

with client:
    client.loop.run_until_complete(main())

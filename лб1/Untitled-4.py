from telethon import TelegramClient

api_id = 'id'  
api_hash = 'hash_id'  
phone_number = 'number'  

client = TelegramClient('session_name', api_id, api_hash)

async def get_chat_users(chat_username):
    participants = await client.get_participants(chat_username)
    
    for user in participants:
        print(f'Username: {user.username}')

async def main():
    await client.start(phone_number)
    
    await get_chat_users('@test6385385385375')  

with client:
    client.loop.run_until_complete(main())
from telethon import TelegramClient

api_id = '24769190'  
api_hash = '282fe9efb1c3013e18c3ced176211005'  
phone_number = '+380678958465' 

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
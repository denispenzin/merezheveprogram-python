from telethon import TelegramClient

api_id = 'id'  
api_hash = 'hash_id'  
phone_number = 'number'  


client = TelegramClient('session_name', api_id, api_hash)

async def main():

    await client.start(phone_number)
    
    me = await client.get_me()
    print(f'Logged in as {me.username}')

    await client.send_message('@den_bezfamilez', 'test1')


with client:
    client.loop.run_until_complete(main())

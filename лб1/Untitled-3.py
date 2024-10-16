from telethon import TelegramClient

api_id = '24769190'  
api_hash = '282fe9efb1c3013e18c3ced176211005'  
phone_number = '+380678958465'  


client = TelegramClient('session_name', api_id, api_hash)

async def main():

    await client.start(phone_number)
    
    me = await client.get_me()
    print(f'Logged in as {me.username}')

    await client.send_message('@den_bezfamilez', 'test1')


with client:
    client.loop.run_until_complete(main())

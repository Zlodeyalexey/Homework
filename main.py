from sqlalchemy import create_engine, select, or_, and_, any_, all_, update, delete
from sqlalchemy.orm import sessionmaker

from models import Category# # # from requests import Session
# # #
# # # api_key = '67a37e37c32aac4d1a47e51a7c9ce343'
# # #
# # #
# # # # response = requests.get(
# # # #     url='https://api.openweathermap.org/data/2.5/weather',
# # # #     params={
# # # #         'appid': api_key,
# # # #         'lat': 53.893009,
# # # #         'lon': 27.567444,
# # # #         'units': 'metric',
# # # #         'lang': 'ru'
# # # #     }
# # # # )
# from requests import Session
#
# with Session() as session:  # type: Session
#     response = session.get(
#             url='https://some-site.com/laptop',
#             params={
#                 'manufactory': 'lenovo',
#                 'ram[from]': 8
#             }
#         )
# # #     print(response.url)
# # #     print(response.headers)
# # #     print(response.cookies)
# # #     print(response.json())
# # #     # response.encoding = 'utf-8'
# # #     print(response.text)
# # #     print(response.status_code)


async def main():
    from aiohttp import ClientSession
    import aiohttp
    async with ClientSession() as session:
        async with session.ws_connect('https://some-site.com/ws') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    print(msg.data)
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    await ws.close()

# #         print(response.cookies)
# #         print(await response.text())
# #         print(await response.json(loads=loads))
# #         print(response.status)
# #
# #
# # if __name__ == '__main__':
# #     import asyncio
# #     asyncio.run(main())
# from aiohttp import ClientSession
#
#
# async def main():
#     async with ClientSession() as session:
#         async with session.ws_connect('wss://demo.piesocket.com/v3/channel_123?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self') as wss:
#             while True:
#                 data = await wss.receive()
#
#
# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())
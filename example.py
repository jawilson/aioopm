import asyncio

import aiohttp
import json

import aioopm

async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)

async def run(websession):
    status = await aioopm.current_operating_status(websession)

    print("Got OPM Status:")
    print("id:", status.id)
    print("title:", status.title)
    print("posted:", status.date_status_posted)
    print("status id:", status.status_type_guid)
    print("status summary:", status.status_summary)

asyncio.get_event_loop().run_until_complete(main())

import asyncio

import aio_pika

from source import settings


async def create(url):
    """Creates connections to specified rabbit server"""
    connection = await aio_pika.connect_robust(url)
    return connection

loop = asyncio.get_event_loop()

# By default the application will have two connections
# One for listen to queues and other to publish messages
input, output = loop.run_until_complete(
    asyncio.gather(
        create(settings.RABBIT_URL),
        create(settings.RABBIT_URL)
    )
)

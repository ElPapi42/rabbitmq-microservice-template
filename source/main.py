import asyncio

import aio_pika
from aio_pika import ExchangeType

from source import rabbit
from source.rabbit.consumer import RabbitConsumer
from source.rabbit.router import RabbitRouter


router = RabbitRouter()

async def startup():
    default_consumer = await RabbitConsumer.create(
        rabbit.connections.input,
        exchange_name='general',
        queue_name='test_queue',
        routing_key='test.message'
    )

    await default_consumer.start(router.route_message)

async def shutdown():
    await rabbit.connections.input.close()
    await rabbit.connections.output.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(startup())

    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(shutdown())
        loop.close()

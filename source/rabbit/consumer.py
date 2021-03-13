import asyncio
from dataclasses import dataclass

import aio_pika


@dataclass
class RabbitConsumer():
    """
    Creates resources required by a consumer.

    Is able to consume messages from a 
    queue binded to a topic exchange
    with a supplied routing key.
    """

    connection:aio_pika.Connection
    channel:aio_pika.Channel
    exchange:aio_pika.Exchange
    queue:aio_pika.Queue
    tag:str = None

    @classmethod
    async def create(
        cls,
        connection:aio_pika.Connection,
        exchange_name:str,
        queue_name:str,
        routing_key:str,
        prefetch_count:int = 1
    ):
        """Declare all the infraestructure and return consumer."""
        channel = await connection.channel()
        await channel.set_qos(prefetch_count)

        exchange = await channel.declare_exchange(exchange_name, 'topic')

        queue = await channel.declare_queue(queue_name)

        await queue.bind(exchange, routing_key)

        return cls(connection, channel, exchange, queue)

    async def start(self, callback):
        """Starts consuming from the queue."""
        self.tag = await self.queue.consume(callback)
    
    async def stop(self):
        await self.queue.cancel(self.tag)

import asyncio

import aio_pika
from aio_pika import ExchangeType

from source import rabbit

print(rabbit.connections.input)

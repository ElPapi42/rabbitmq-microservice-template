import asyncio
from dataclasses import dataclass

import aio_pika


class RabbitRouter():
    """Routes messages to different controllers based on its routing key."""

    def __init__(self, routes:dict = {}):
        self.routes = routes

    async def route_message(self, message:aio_pika.IncomingMessage):
        handler = self.routes.get(message.routing_key)

        if not handler:
            message.reject()
            return
        
        await handler(message)
    
    def add_route(self, routing_key:str, handler):
        self.routes[routing_key] = handler

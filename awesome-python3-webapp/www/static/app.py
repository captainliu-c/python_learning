import logging; logging.bascConfig(level = logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):
	return web.Response(body = b'<h1>Awesome</h1>')

async def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET', '/', index)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8080)
	logging.info('server started at http://127.0.0.1:8080...')
	return srv 


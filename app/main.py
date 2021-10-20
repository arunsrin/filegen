import asyncio
from fastapi import FastAPI
from starlette.responses import StreamingResponse
from fastapi.responses import PlainTextResponse
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
Instrumentator().instrument(app).expose(app)


WELCOME_MESSAGE = '''
Usage:
  curl https://filegen.arunsr.in/size/1
      <- returns a 1mb file

  curl https://filegen.arunsr.in/size/10
      <- returns a 10mb file
'''


def smallchunk():
    '''Generate a long string of a's'''
    res = 'a'*1000*1000
    res += '\n\n'
    return res


async def textgen3(size=3):
    for i in range(size):
        yield smallchunk()
        await asyncio.sleep(0.01)


@app.get("/", response_class=PlainTextResponse)
def home():
    return WELCOME_MESSAGE


@app.get("/size/{filesize}")
def read_stream(filesize: int):
    if filesize > 2000:
        return("Try a smaller file size, please")
    generator = textgen3(filesize)
    return StreamingResponse(generator, media_type='text/plain')

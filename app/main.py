import asyncio
from fastapi import FastAPI
from starlette.responses import StreamingResponse
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
Instrumentator().instrument(app).expose(app)


def smallchunk():
    '''Generate a long string of a's'''
    res = 'a'*1000*1000
    res += '\n\n'
    return res


async def textgen3(size=3):
    for i in range(size):
        yield smallchunk()
        await asyncio.sleep(0.01)


@app.get("/size/{filesize}")
def read_stream(filesize: int):
    # generator = textgen3(int(filesize)*1000)
    generator = textgen3(filesize)
    return StreamingResponse(generator, media_type='text/plain')

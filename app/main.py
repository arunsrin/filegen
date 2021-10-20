import asyncio
import random
import string
from fastapi import FastAPI
from starlette.responses import StreamingResponse


def givemeachunk(size=1000):
    res = '''MhTuCiiAFbgtCZfrhQkVLowqUhDTEyHAVyJyhGABeBdCvQMRCBdBFXROgvhNpRnVVFMKtXztwfsPWnWyCSCkPVluVNPCTtaiKaDFFeadjLcdykztdaKrqFbxOAcAYowUxeOiZssIGUPMYwHksKtPrGaQWfshkYqxZDlKuQFfsvQCsfpHyTpHMiKJznUrzSzOBYpWRpLkNgzBEnToAXnJMogiCcfblJrtGYZiGwsUBrAmcGRogKQcaUIgCjBZmeKjubbRgSAQbkdbMwYrRNJZzmgKwiZINQbgxsMwzMQWXwRMScgcCLsKvBJRFxaeqwbyPPnQcFbWyMsNwdwMsqFCwbYNTVBpBKIqCbZmHbnYgkqzGVtyfLqXwnOjBKMMIbMIdpReZgiMKiWudxIQyADnvoGzAogwCOalpyFZiDXPuPpchpRBqWioayNtSLWywsPjKivrMBNaVJIWjaXgEsxtjKzIwQhqHkDSmRpdRVXzgsETlPgejSzahDXndqWdcIgJnIsZfoyStgPAvKwsjSuFVGcDkonlTOOVXHAotneuOewQOJwvoWmMocCrNKvFIArcBJKZFSiKlqPfxEccyvCwOfoLMQcvjzhLYhszQgedwETqAectYhQWdPEhqXWOWAjWcowiYxYsDQNxeNwXNwUSNWSOjTwjtaRrxxiRucYqbpFCfSWuanGnSnDdCJDPRBtuEtmqihlKOIrPXjTqFpGxvAGvJldAgOTpnTbcLSwCPLbuCApZekjwoYhpGwLckkDosbTqIFGzTcETqolgBtgIETTMzJlpXSqFCBSnAGrvDWipiEMuDTVOJZSLNvtwSCbAZFJbFuonuYtYbfaEbRjOKBYDAnMyqVitNhYuCSOrPzyguuUYDyxORDRFMKuzbWUBfeSNIIsuOCMHKuBwLAfOzhNwEjEuzbyNZjhEtTfcXuXpaNRYRRzCeedDStREOIzuJFxmBmRXfNgIyQXmtiGANAdRUkvNIyMHLyaJHRJCEEadujhvDKGADmpwrKypavDk'''
    res += '\n\n'
    res *= size
    #res = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
    #res *= size
    return res


async def textgen3(size=1000):
    yield givemeachunk(size)
    await asyncio.sleep(0.01)


'''
async def textgen2(size=10):
    for i in range(size):
        yield givemeachunk(1000000)
        await asyncio.sleep(0.01)


async def textgen(size=10):
    for i in range(size):
        yield random.choice(string.ascii_letters)
        await asyncio.sleep(0.001)


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    generator = textgen(1, 10)
    response = StreamingResponse(generator, media_type='text/plain')
    await response(scope, receive, send)
'''


app = FastAPI()


@app.get("/files/{filesize}")
def read_stream(filesize=1):
    generator = textgen3(int(filesize)*1000)
    return StreamingResponse(generator, media_type='text/plain')

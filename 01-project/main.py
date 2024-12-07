from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"body": "World"}



# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#
#     await send({
#         'type': 'http.response.start',
#         'status': 200,
#         'headers': [
#             [b'content-type', b'text/plain'],
#         ],
#     })
#     await send({
#         'type': 'http.response.body',
#         'body': b'Hello, world!',
#     })
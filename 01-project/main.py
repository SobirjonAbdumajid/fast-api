from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_method():
    return {"message": "This is get method"}


@app.post("/")
async def post_method():
    return {"message": "This is the post method"}


@app.put("/")
async def put_method():
    return {"message": "This is the put method"}


@app.delete("/")
async def delete_methods():
    return {"message": "This is the delete methods"}


@app.patch("/")
async def patch_method():
    return {"message": "This is the patch method"}

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

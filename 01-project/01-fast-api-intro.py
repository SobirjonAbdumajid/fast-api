# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/users/{user_id}")  # Path Parameter
# async def get_method(user_id: int):
#     return {"message": f"This is get method {user_id}"}
#
#
# @app.get("/items")  # Query Parameter
# async def get_method(skip: int = 0, limit: int = 100):
#     return {"skip": skip, "limit": limit}
#
#
# @app.post("/order")
# async def post_method():
#     return {"message": "This is the post method"}
#
#
# @app.put("/")
# async def put_method():
#     return {"message": "This is the put method"}
#
#
# @app.delete("/")
# async def delete_methods():
#     return {"message": "This is the delete methods"}
#
#
# @app.patch("/")
# async def patch_method():
#     return {"message": "This is the patch method"}
#
#
#
# # async def app(scope, receive, send):
# #     assert scope['type'] == 'http'
# #
# #     await send({
# #         'type': 'http.response.start',
# #         'status': 200,
# #         'headers': [
# #             [b'content-type', b'text/plain'],
# #         ],
# #     })
# #     await send({
# #         'type': 'http.response.body',
# #         'body': b'Hello, world!',
# #     })
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello_pdp():
    return {"message": "Hello PDP"}


@app.post("/submit/{name}")
async def submit(name: str):
    return {"message": f"Hello {name}"}


@app.put("/uptade")
async def uptade():
    return {"message": "Data updated"}


@app.delete("/delete")
async def delete():
    return {"message": "Data deleted"}

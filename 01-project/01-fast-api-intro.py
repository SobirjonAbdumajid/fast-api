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

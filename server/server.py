import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
pyb = {"users": {"username": ["debug0", "dev"]}, "server_version": "1.0.0a"}

@app.get("/px/")
async def proxy(amount: int = 0, protocol: str = "http", timeout: str = "10000", country: str = "all", ssl: str = "all", anonymity: str = "all"):
    return {"proxy": requests.get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={protocol}&timeout={timeout}&country={country}&ssl={ssl}&anonymity={anonymity}").content.decode("utf-8").splitlines()[amount]}

@app.get("/user/")
async def user(username: str):
    if username in pyb["users"].keys():
        return {"status": [True, pyb["users"][username][0], pyb["users"][username][1]]}
    else:
        return {"status": [False]}

@app.get("/version/")
async def version():
    return {"version": pyb["server_version"]}

@app.get("/adblock/")
async def adblock():
    return FileResponse("adblock.txt")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", reload=False, host="0.0.0.0", port=8080)
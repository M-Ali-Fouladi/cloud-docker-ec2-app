from fastapi import fastapi

app=fastapi()

@app.get("/")
def readroot():
    return {"message":"hello from deockerized app!"}

@app.get("/health")
def health_check():
    return {"status":"ok"}
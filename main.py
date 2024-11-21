from fastapi import FastAPI


app = FastAPI()


@app.get("/home")
def get_homepage():
    return "fastapi is now working"

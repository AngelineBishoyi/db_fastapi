from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get('/')
def index():
    return {'Hello':'Programmer'}

# @app.get('/blog/{id}')
# def show(id):
#     return {'data': id}


# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
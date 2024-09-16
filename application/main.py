from fastapi import FastAPI

from routes import init_routes


app = FastAPI(debug=True)

init_routes(app)


if __name__ == '__main__':
    from uvicorn import run as start_app
    start_app('main:app', host='0.0.0.0', port=8000)
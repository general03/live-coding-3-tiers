# Live Coding : @pypeline

This repository code is support of live coding from channel youtube https://youtube.com/@pypeline-tech

You can found several live talking about :

- Repository pattern on [YouTube channel](https://www.youtube.com/live/YsZqbC8dRC4) with this [commit](https://github.com/general03/live-coding-3-tiers/commit/fda9e79cfb8137586ce83887ff7927135431dc2b)
- Service pattern on [YouTube channel](https://www.youtube.com/live/GGYWhoxGCo8) with this [commit](https://github.com/general03/live-coding-3-tiers/commit/1f3edf00add17717468be3a4bc578dd3c647ffe7)
- FastAPI lifespan on [YouTube channel](https://www.youtube.com/live/jeBF7llkPjI) with this [commit](https://github.com/general03/live-coding-3-tiers/commit/8d7b9bed46c536a37163a7f14d6a9287bf51066d)
- FastAPI error handler exception on [YouTube channel](https://www.youtube.com/live/QTl5Mbt2zP0) with this [commit](https://github.com/general03/live-coding-3-tiers/commit/4b0437914c841321519f51ebe818ddfe4e780ec8)
- FastAPI `Depends()` on [YouTube channel](https://www.youtube.com/live/R7dXzSJXnjo) with this [commit](https://github.com/general03/live-coding-3-tiers/commit/4bac2adfde1ab5603f296994c7faba60d5dd8283)
- FastAPI architecture on [YouTube channel](https://youtube.com/live/SNCMHs2p6Os) with this [commit](https://github.com/general03/live-coding-3-tiers/commit/e29931863859aa19d09485a190798c07fed7d6ef)
- FastAPI router on [YouTube channel](https://youtu.be/3QeMUW7-WaM) with this [commit](https://github.com/general03/live-coding-3-tiers/commit/38de837e7b9f123df0fbbbba6b82b3def3349525)
- FastAPI model response on [YouTube channel](https://youtu.be/Ks2wyD_8Kt8) with this [commit](https://github.com/general03/live-coding-3-tiers/commit/bf3e36432b9a77bc35bc2925c7e6cfd4c4d27d3b)
- FastAPI input validation on [YouTube channel](https://youtu.be/tFwq_am-FT4) with this [commit](https://github.com/general03/live-coding-3-tiers/commit/80de524cc80155d982a343fe56ce5fdd5cf1ee83)

The initial ugly `main.py` was moved on `main_legacy.py`

The code repository is located on [github](https://github.com/general03/live-coding-3-tiers)

# Launch

If you want to start application you need to : 
- install package manager `pip install pipenv`
- init data loading `python scripts/init_db.py`
- execute app `pipenv run fastapi dev src/main.py`
- call `curl http://127.0.0.1:8000/products/1`
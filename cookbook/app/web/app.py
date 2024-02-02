import os
from typing import Optional, Dict
from aiohttp.web import (
    Application as AiohttpApplication,
    Request as AiohttpRequest,
    View as AiohttpView,
)
from aiohttp_apispec import setup_aiohttp_apispec
from aiohttp_session import setup as session_setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
import jinja2
import aiohttp_jinja2

from app.store import Store, setup_store
from app.store.database.database import Database
from app.web.config import Config, setup_config
from app.web.logger import setup_logging
from app.web.middlewares import setup_middlewares
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    config: Optional[Config] = None
    store: Optional[Store] = None
    database: Optional[Database] = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request

    @property
    def database(self):
        return self.request.app.database

    @property
    def store(self) -> Store:
        return self.request.app.store

    @property
    def data(self) -> dict:
        return self.request.get("data", {})


app = Application()

description = """

COOKBOOK API

Тестовое задание MirGovorit backend
небольшое приложение поварской книги


### Функционал по ТЗ

Получающие параметров методом GET

1. http://localhost:8080/recipe.product.add

Добавляет к указанному рецепту указанный продукт с указанным весом.
Если в рецепте уже есть такой продукт,
то функция должна поменять его вес в этом рецепте на указанный 
(параметры recipe_id, product_id, quantity)

2. http://localhost:8080/products/product.cook.update

Увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт (параметр recipe_id)

3. http://localhost:8080/recipe.product.show/product_id/

Возвращает HTML страницу, на которой размещена таблица.
В таблице отображены id и названия всех рецептов,
в которых указанный продукт отсутствует,
или присутствует в количестве меньше 10 грамм.


**Разработчик**

Руслан Латипов, @rus_lat116

"""

tags_metadata = [
    {
        "name": "products",
        "description": "Продукты",
    },
    {
        "name": "recipes",
        "description": "Рецепты",
    },
]


def setup_app(config_path: str) -> Application:
    setup_logging(app)
    setup_config(app, config_path)
    session_setup(app, EncryptedCookieStorage(app.config.session.key))
    setup_routes(app)
    setup_aiohttp_apispec(
        app,
        title="COOKBOOK API",
        version="0.0.1",
        swagger_path="/docs",
        url="/docs/json",
        info=dict(
            description=description,
            contact={
                "name": "Руслан Латипов",
                "url": "https://t.me/rus_lat116",
                "email": "rus_kadr03@mail.ru",
            },
        ),
        tags=tags_metadata,
    )
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(os.path.join(os.getcwd()) + "/templates"), enable_async=True, #  newline_sequence="\r\n", 
    )
    setup_middlewares(app)
    setup_store(app)

    return app

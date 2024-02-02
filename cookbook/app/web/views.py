from aiohttp.web import Response


async def index(request):
    return Response(
        text="""<h1>Тестовое задание MirGovorit backend</h1>
        <p>Небольшое приложение поварской книги</p> 
        <a href='/docs'>Документация COOKBOOK API</a>

        <h2>Функционал по ТЗ</h2>

        <p>Получающие параметров методом GET</p>

        1. http://localhost:8080/recipe.product.add

        <p>Добавляет к указанному рецепту указанный продукт с указанным весом.<br>
        Если в рецепте уже есть такой продукт,<br>
        то функция должна поменять его вес в этом рецепте на указанный<br> 
        (параметры recipe_id, product_id, quantity)</p>

        2. http://localhost:8080/products/product.cook.update

        <p>Увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт (параметр recipe_id)</p>

        3. http://localhost:8080/recipe.product.show/product_id/

        <p>Возвращает HTML страницу, на которой размещена таблица.<br>
        В таблице отображены id и названия всех рецептов,<br>
        в которых указанный продукт отсутствует,<br>
        или присутствует в количестве меньше 10 грамм.</p>""",
        content_type="text/html",
    )

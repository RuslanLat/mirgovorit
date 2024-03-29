## Тестовое задание MirGovorit backend

Нужно разработать небольшое приложение поварской книги, со следующим функционалом:

### База данных

В базе данных приложения должен храниться список продуктов. Продукт имеет название, а также целочисленное поле, хранящее информацию о том, сколько раз было приготовлено блюдо с использованием этого продукта. Также в базе данных хранятся рецепты блюд. Рецепт имеет название, а также набор входящих в рецепт продуктов, с указанием веса в граммах.

***Например*** - рецепт Сырник, в который входят продукты Творог 200г, Яйцо 50г, Сахар 10г.

Один и тот же продукт, может использоваться в разных рецептах. Один и тот же продукт не может быть использован в одном рецепте дважды.

### Функционал
Приложение должно предоставлять следующие HTTP функции, получающие параметры методом GET

1. add_product_to_recipe с параметрами recipe_id, product_id, weight. Функция добавляет к указанному рецепту указанный продукт с указанным весом. Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте на указанный.

2. cook_recipe c параметром recipe_id. Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.

3. show_recipes_without_product с параметром product_id. Функция возвращает HTML страницу, на которой размещена таблица. В таблице отображены id и названия всех рецептов, в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм. Страница должна генерироваться с использованием Django templates. Качество HTML верстки не оценивается.

**Важно:** указанные функции должны быть реализованы в разумной степени эффективно с точки зрения производительности, а также корректно работать в случае одновременного доступа нескольких пользователей.

### Админка
Также должна быть настроена админка, где пользователь сможет управлять входящими в базу данных продуктами и рецептами. Для рецептов должна быть возможность редактировать входящие в их состав продукты и их вес в граммах.


### Запуск сервиса

Для локального использования сервиса:
1. Загрузить все файлы репозитория **mirgovorit** \
    или выполнить команду в терминале bash ```git clone https://github.com/RuslanLat/mirgovorit```
2. Порядок запуска сервиса:
* в директории с проектом в терминале выполнить команду ```docker-compose up -d --build``` (сборка контейнеров и запуск их в работе в фоновом режиме)
* для остановки работы сервера в директории с проектом в терминале выполнить команду ```docker-compose stop```
* для повторного запуска в директории с проектом в терминале выполнить команду ```docker-compose start```

***Примечание:*** в директории с проектом (mirgovorit) создается папка ***pgdata*** с данными базы данных

3. Проверка в работе (после запуска контейнеров)
* админка доступна на локальном хосте port 5000 (http://127.0.0.1:5000/ или http://localhost:5000/)
* API доступно на локальном хосте port 8080 (http://127.0.0.1:8080/ или http://localhost:8080/)


### Контакты

Руслан Латипов <img src="images/telegram_logo.png" width="35"> @rus_lat116 
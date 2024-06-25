# Дашборд с анализом о среднем времени использования интернета по странам.

Датасет содержит данные о среднем времени использования интернета по странам.
[Ссылка на датасет](https://www.kaggle.com/datasets/jonathanmulleda/average-screen-time-and-usage-by-country)

### Авторы

Проект подготовили студенты 3 курса РТУ МИРЭА:

- Осминин А.Д. (БСБО-14-21)
- Болтачев М.О. (БСБО-14-21)

### Возможности дашборда:

- Карта мира по ВВП: визуализация уровня ВВП стран и отображение основных характеристик.
- Топ 10 стран по проценту использования интернета населением: отображение десяти стран с самым высоким уровнем использования интернета.
- Столбчатая диаграмма по проценту населения, используего интернет: отображение всех стран с их уровнем использования интернета.
- Столбчатая диаграмма сравнения показателей стран мира: отображение всех стран с заданными характеристиками.
- Столбчатая диаграмма топ 10 стран по использованию интернета для социальных сетей: отображение времени в социальных сетях для стран с самым большим количеством людей, использующих интернет.
- Изменение критерием сравнения: столбчатая диаграмма, отображающая параметры каждой страны.

### Библиотеки для работы дашборда

В процессе создания многостраничного дашборда использовались:

Bootstrap - это один из наиболее популярных фреймворков для создания пользовательских интерфейсов веб-приложений, который облегчает создание стильных и отзывчивых веб-страниц.
Фреймворк Dash - это инструмент для создания интерактивных веб-приложений с использованием языка программирования Python. Он предоставляет возможности для быстрой разработки данных и аналитики на основе веб-технологий, таких как HTML, CSS и JavaScript.
 ```
    pip install dash
 ```
- Dash Bootstrap Components (dash_bootstrap_components): это библиотека для фреймворка Dash, которая предоставляет компоненты пользовательского интерфейса, стилизованные в соответствии с Bootstrap.
 ```
    pip install dash_bootstrap_components
 ```
- Plotly Express (px): высокоуровневый интерфейс для построения интерактивных графиков и визуализаций данных с использованием библиотеки Plotly. Упрощает создание сложных графиков с минимальным кодом.
 ```
    pip install plotly
 ```
- Pandas (pd): библиотека для работы с данными, предоставляющая структуры данных и операции для манипуляций с таблицами. Используется для загрузки, обработки и анализа данных.
 ```
    pip install pandas
 ```
- NumPy (numpy): библиотека для языка программирования Python, предоставляющая поддержку для работы с многомерными массивами и матрицами, а также большой коллекцией математических функций для операций над этими массивами.
 ```
    pip install numpy
 ```
### Установка

Для установки приложения выполните следующие шаги:


1. Настройка виртуального окружения:
```
   python -m venv venv
   venv\Scripts\activate
 ```

2. Установка зависимостей:
```
   pip install dash-bootstrap-components
```

### Запуск приложения

После установки зависимостей запустите приложение командой:
```
python app.py
```
Откройте веб-браузер и перейдите по адресу [http://127.0.0.1:8050/](http://127.0.0.1:8050/) для просмотра дашборда.

## Готовый дашборд, размещенный на хостинге
В качестве интернет платформы для размещения дашборда был использован [PythonAnywhere](https://www.pythonanywhere.com/). PythonAnywhere - это облачная платформа для разработки и развертывания Python-приложений. Пользователи могут управлять проектами, писать, запускать и отлаживать код через удобный веб-интерфейс. Итоговый дашборд можно посмотреть по [ссылке]().# project

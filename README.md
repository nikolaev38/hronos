<p align="center">
  <a href="/web_site_streamlit">
  <img src="https://github.com/nikolaev38/hronos/blob/main/banner.png">
  </a>
</p>


<html>
<head>
    <title>Rounded Corners</title>
    <style>
        .GFG {
            border-radius: 35px;
            background: #009900;
            padding: 30px;
            text-align: center;
            width: 300px;
            height: 120px;
        }
    </style>
</head>

<body>
    <div class="GFG">
        <h2>GeeksforGeeks</h2>
        <p>border-radius: 35px;</p>
    </div>
</body>
</html>

# Hronos: Ассистент с искусственным интеллектом для работы с научной литературой

Современные научные сотрудники сталкиваются с лавиной данных из различных сфер деятельности, которую невозможно или очень тяжело обработать вручную. **Хронос**, как **AI-помощник**, станет мощным инструментом, автоматизируя анализ огромных массивов информации и позволяя учёным сфокусироваться на исследовательской работе и глубоком анализе полученных результатов.

---

## Исследовательский анализ данных

Мы провели **исследовательский анализ данных** на основе датасета *PubMed*, в рамках которого мы исследовали следующие аспекты:

1. **На каких языках написаны статьи?**
2. **Какие тематики можно выделить?**
3. **Какие проблемы есть в данных?**
4. **Сравнили 3 модели на разных метриках и обосновали их**

Подробнее ознакомиться с результатами анализа можно в этой [README.MD](https://github.com/nikolaev38/hronos/tree/2nd-stage/analitics/README.md).

---

## Прототип веб-сервиса

Мы разработали **прототип веб-сервиса**, который позволяет загружать статьи в формате PDF и получать их краткое содержание в виде текста. Для этого был использован фреймворк [___Streamlit___](https://streamlit.io/). Также мы разрабатывали прототип для работы с рекомендательной системой на фреймворке [___Flet___](https://flet.dev/).

Дополнительную информацию можно найти в этой [README.MD](https://github.com/nikolaev38/hronos/tree/2nd-stage/web_site_streamlit/README.md).

---

## Структура нашего проекта на момент реализации 2 этапа.
```
📦 
├─ .gitignore
├─ README.md - основная README.md
├─ ai - дериктория с моделями
│  └─ README.md - предупреждение об отсутствии моделей из-за их веса.
├─ analitics - дериктория анализа.
│  ├─ Bert.png - изображение таблицы анализа метрики bert-score.
│  ├─ Cosinuse.png - изображение таблицы анализа метрики косинусового сходства.
│  ├─ Language.png - график распространённости языков в стаьях
│  ├─ README.md - README.md об аналитике
│  ├─ Rouge.png - изображение таблицы анализа метрики Rouge
│  ├─ Theme.png - график распространённости тем в статьях
│  ├─ analitis.ipynb - jupyter notebook с анализом.
│  └─ data - директория с датасетом
│     └─ README.md - предупреждение об отсутствии датасетов из-за веса
├─ banner.png - Логотип
├─ guide_for_launch.md - руководство по локальному запуску
├─ requirements.txt - зависимости
└─ web_site_streamlit - директория с web сервисом
   ├─ README.md - README.md о web сервисе.
   ├─ Structure.png - изображение будущей структуры 
   └─ web.py - код web сервиса
```
### Подробнее ознакомиться с этим репозиторием можете [тут](https://github.com/nikolaev38/hronos/tree/2nd-stage)

---

## Авторы

- [@shipovnikAAA](https://github.com/shipovnikAAA)
- [@nikolaev38](https://github.com/nikolaev38)
- [@Aleksandr](https://github.com/Aleksandr)
- [@kaiyofx](https://github.com/kaiyofx)

---

## Полезные ссылки

<p align="center">
  <a href="/web_site_streamlit">
  <img src="https://img.shields.io/badge/Web_site-Streamlit-803e75.svg">
  </a>
  
  <a href="/analitics">
  <img src="https://img.shields.io/badge/Analytics-of_pubmed-87CEEB.svg">
  </a>
  
  <a href="guide_for_launch.md">
  <img src="https://img.shields.io/badge/Guide-for_launch-5F9EA0.svg">
  </a>
</p>

---

> **Примечание:** Если у вас есть вопросы или предложения, не стесняйтесь обращаться к авторам проекта.

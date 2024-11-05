# Руководство по запуску

## Запуск анализа:

Для запуска аналитики локально:

```shell or cmd

# Клонируем репозиторий

>>> git clone https://github.com/nikolaev38/hronos.git

# Переходим в него

>>> cd hronos

# Устанавливаем список библиотек

>>> pip install -r requirements.txt

# Переходим в директорию с анализом

>>> cd analitis

# Запускаем юпитер ноутбук, обратите внимание, что файл откроется в ваашей основной среде.

>>> analitis.ipynb


```
---
### Обратите внимание, что вам будет необходимо локально загрузить датасет pubmed **[тут](https://huggingface.co/datasets/ccdv/pubmed-summarization/tree/main/document)**, а также скачать все локальные модели, используемые в анализе и веб сайте **[тут](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF?show_file_info=gemma-2-9b-it-Q6_K_L.gguf)** и **[тут](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF?show_file_info=Llama-3.2-3B-Instruct-Q6_K_L.gguf)**!!!!!


## Запуск web сайта:

```shell or cmd

# Клонируем репозиторий

>>> git clone https://github.com/nikolaev38/hronos.git

# Переходим в него

>>> cd hronos

# Устанавливаем список библиотек

>>> pip install -r requirements.txt

# Переходим в директорию с сайтом

>>> cd web_site_streamlit

# Запускаем файл

>>> streamlit run web.py

```
---
### Обратите внимание. Чтобы запусть локально, необходимо скачать данную модель **[тут](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF?show_file_info=gemma-2-9b-it-Q6_K_L.gguf)**!!!!!

# Обработка текста и анализ частотности слов с помощью NLTK  

## 1. Что делает проект
Этот проект предоставляет два Python-скрипта для предобработки текста и анализа частотности:  

1. **Text_Processing_with_NLTK.py**  
   - Удаляет стоп-слова  
   - Преобразует слова в нижний регистр  
   - Фильтрует знаки препинания  
   - Извлекает уникальные слова  
   - Сортирует их в алфавитном порядке  
   - Сохраняет результат в файл  

2. **Frequency_Distributions_NLTK.py**  
   - Использует предобработанные слова  
   - Вычисляет распределение частот слов с помощью NLTK  
   - Возвращает словарь частот  
   - Визуализирует 10 самых частотных слов в виде столбчатой диаграммы  

---

## Файлы
- `download_packages.py` – скачивание необходимых пакетов NLTK  
- `Frequency_Distributions.py` – создание словаря частот  
- `Text_Processing_with_NLTK.py` – основной скрипт предобработки текста
- `requirements.txt` - необходимые библиотеки для работы 

## Установка
1. Установите необходимые Python-библиотеки:  
```bash
pip install -r requirements
```

2. Установите необходимые пакеты NLTK:
```bash
python download_packages.py
```

## Пользование

Обработка текста:
```bash
python Frequency_Distributions_NLTK.py input.txt output.txt

```

Обрабатывать с использованием определенного языка (по умолчанию: русский):
```bash
python Frequency_Distributions_NLTK.py input.txt output.txt --language english
```

## Пример использования:

Входящий файл (`input.txt`):
```
NLTK helps with natural language processing.
This is a powerful tool for text analysis.
```

Выходящий файл (`output.txt`):
```
analysis
helps
language
natural
nltk
powerful
processing
text
tool
```

## Общие требования

- Python 3.6+
- NLTK library

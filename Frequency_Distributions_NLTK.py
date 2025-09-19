from Text_Processing_with_NLTK import process_text_file

from nltk import FreqDist
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import string
import argparse


def frequency_distributions_NLTK(input_file: str, output_file:str, language: str) -> dict:
    """
    Создание частотного словаря на основе обработанных слов текста.

    Аргументы:
        input_file: имя входного файла
        output_file: имя выходящего файла
        language: используемый в тексте язык (по умолчанию = 'russian')
    """

    # функция записывает в output_file уникальные lower-регистровые слова текста файла input_file без стоп-слов 
    process_text_file(input_file, output_file, language=language)

    try:
        # открываем файл слов, полученный с помощью предыдущей функции
        with open(output_file, 'r', encoding='utf-8') as f:
            # переместили слова из текста в словарь
            words = [word.strip() for word in f]
        
        # открываем файл текста
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
            if not text:
                print('Файл пустой')
                return
        
    except FileNotFoundError:
        print('Файл не найден')
    except LookupError:
            print("Ошибка: необходимые пакеты NLTK не найдены. Скачайте download_packages.py")
    except Exception as e:
        print(f"Ошибка обработки файла: {e}")


    # делим на токены
    tokens = word_tokenize(text)
    # убираем знаки пунктуации И приводим слова к нижнему регистру
    tokens = [token.lower() for token in tokens if token.isalpha()]

    # создаем итерируемый оъект по (слово : частота)
    fdist = FreqDist(tokens)

    # пересечем все слова со словами из файла
    # отсортируем по убыванию
    res = sorted( [ (el, fdist[el]) for el in words] , key=lambda x: x[1], reverse=True)

    # по заданию просят вернуть частотный словарь
    return {key:value for key,value in res}
        


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser('Вывод диаграммы на основе частоты слов в тексте')
    parser.add_argument('input_file', type=str, help='Имя входного файла с текстом')
    parser.add_argument('output_file', type=str, help='Имя выходного файла')
    parser.add_argument('--language', '-l', type=str, default='russian', help='Используемый язык')

    args = parser.parse_args()

    # частотный словарь
    words_and_freq = frequency_distributions_NLTK(args.input_file, args.output_file, args.language).items()
    
    # разделим словарь на список слов И на список частот соответсвующих слов
    keys_words_and_freq   = [el[0] for el in words_and_freq][:10]
    values_words_and_freq = [el[1] for el in words_and_freq][:10]

    # здесь же, мы будем рисовать диаграмму на основе частотного словаря
    plt.figure(figsize=(10, 6))
    # столбчатая диаграмма Ох - слова, Оу - их частоты
    plt.bar(keys_words_and_freq, values_words_and_freq)
    # наклоним на 45 градуса
    plt.xticks(rotation=45)

    plt.title('Диаграмма частоты слов')
    plt.xlabel('Слова')
    plt.ylabel('Частота')

    plt.tight_layout()
    plt.show()

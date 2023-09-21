def rhythm(poem):
    poem = poem.split()
    f = lambda word: sum(1 for i in word if i in 'аеёиоуыэюя')
    sum_word = f(poem[0])
    return all([f(i) == sum_word for i in poem])

poem = str(input("Введите стихотворение: "))

if rhythm(poem):
    print('Парам пам-пам')
else:
    print('Пам парам')
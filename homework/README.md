# Дополнительные вопросы:

1. С чего проще начать выполнение домашнего задания: с тестов или с реализации классов?

   Мне было проще начать с описания классов, так как это помогло мне сразу понять, какие основные детали мне нужно будет
   реализовывать. Когда я сначала обрисовал классы и методы, мне стало
   намного проще представлять себе всю структуру и логику.

2. Почему для хранения товаров в корзине используется словарь, а не список?

    - Удобно обновлять данные;
    - Словарь позволяет хранить всю необходимую информацию о товаре (цена, количество и т.д.) вместе с его
      идентификатором;
    - Словарь не допускает дублирования ключей, что исключает хранение нескольких одинаковых
      товаров в корзине;

3. Зачем нужен __hash__ в классе Product? Изучите этот метод и объясните, почему он нужен.

   Эта реализация объединяет значения name и description в одну строку, а затем вычисляет хэш-код этой строки с помощью
   функции hash(). Таким образом, два объекта Product будут иметь одинаковый хэш-код, если они имеют
   одинаковые значения для name и description.

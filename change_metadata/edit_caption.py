import re

caption = "Description Wed., Sep. 13, 2023, Russia, St. Petersburg. Genre photography. A man walks along Stachek Avenue. Bank branch. Euro currency sign painted on a window. Kommersant Photo/Yevgeny Pavlenko "
"#RU 13.09.2023, Россия, Санкт-Петербург. Жанровая фотография. Мужчина идет по проспекту Стачек. Отделение банка. Знак валюты евро, нарисованный на окне. Фото: Евгений Павленко/Коммерсантъ"

pattern = r'Санкт-Петербург'
print(re.findall(pattern, caption))

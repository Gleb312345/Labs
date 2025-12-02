import re
from collections import Counter

# Регулярний вираз для пошуку слів
WORD_RE = re.compile(r"[а-яіїєґ]+", re.IGNORECASE)


def pair_counter_generator(path):
    with open(path, "r", encoding="utf-8") as f:
        for lineno, raw in enumerate(f, start=1):

            line = raw.strip().lower()

            # знайти всі слова в рядку
            words = WORD_RE.findall(line)

            counter = Counter()

            for i, word in enumerate(words):
                # пари всередині слова
                for j in range(len(word) - 1):
                    pair = word[j:j+2]
                    counter[pair] += 1

                if i + 1 < len(words):
                    w1 = words[i]
                    w2 = words[i + 1]
                    border_pair = w1[-1] + w2[0]
                    # якщо така пара була нарахована — прибираємо
                    if counter[border_pair] > 0:
                        counter[border_pair] -= 1
            top3 = counter.most_common(3)

            # конвертуємо у красивий текст
            top3_text = ", ".join([f"{p} – {c}" for p, c in top3])

            # повертаємо як текст, а не словник
            yield f"Рядок {lineno}: {top3_text}"

if __name__ == "__main__":
    FILE_PATH = r"C:\Users\Glib\PyCharmMiscProject\lab9\text.txt"
    for result in pair_counter_generator(FILE_PATH):
        print(result)
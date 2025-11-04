grades = {}

while True:
    name = input("Введіть ім'я студента (або 'stop' для завершення): ")
    if name.lower() == "stop":
        break
    try:
        grade = int(input(f"Введіть оцінку для {name}: "))
        grades[name] = grade
    except ValueError:
        print("Помилка: оцінка повинна бути числом!")
        continue

print("Список студентів та їх оцінок:")
for name, grade in grades.items():
    print(f"{name}: {grade}")

if grades:
    avg = sum(grades.values()) / len(grades)
    print(f"\nСередній бал по групі: {avg:.2f}")

    # Категорії
    vidminnyky = [n for n, g in grades.items() if 10 <= g <= 12]
    khoroshysty = [n for n, g in grades.items() if 7 <= g <= 9]
    vidstayuchi = [n for n, g in grades.items() if 4 <= g <= 6]
    ne_sdaly = [n for n, g in grades.items() if 1 <= g <= 3]

    print(f"\nВідмінники (10–12): {len(vidminnyky)} -> {', '.join(vidminnyky) if vidminnyky else 'немає'}")
    print(f"Хорошисти (7–9): {len(khoroshysty)} -> {', '.join(khoroshysty) if khoroshysty else 'немає'}")
    print(f"Відстаючі (4–6): {len(vidstayuchi)} -> {', '.join(vidstayuchi) if vidstayuchi else 'немає'}")
    print(f"Не здали (1–3): {len(ne_sdaly)} -> {', '.join(ne_sdaly) if ne_sdaly else 'немає'}")
else:
    print("\nДані не введено.")

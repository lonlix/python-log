import json

class Habit:
    def __init__(self, name, streak):
        self.name = name
        self.streak = streak
    def __repr__(self):
        return f"Привычка: {self.name}, Кол-во дней подряд:{self.streak}"

    def increment_streak(self):
        self.streak += 1

    def reset_streak(self):
        self.streak = 0

    def set_streak(self, value):
        if  not isinstance(value, int) :
            raise TypeError("Должно быть число")
        elif value < 0:
            raise ValueError("Стрик не может быть отрицательным")
        else:
            self.streak = value
    def to_dict(self):
        return {"name":self.name,"streak": self.streak}

    def __str__(self):
        return f'Привычка: {self.name}, Кол-во дней подряд: {self.streak}'

class DailyHabit(Habit):
    def __init__(self, name, streak, reminder_time):
        super().__init__(name, streak)
        self.reminder_time = reminder_time

class WeeklyHabit(Habit):
    def __init__(self, name, streak, day_of_week):
        super().__init__(name, streak)

        self.day_of_week = day_of_week
    def __str__(self):
        text = super().__str__()
        return f'{text}, День недели: {self.day_of_week}'

class WeeklyWithGoal(Habit):
    def __init__(self, name, streak, goal):
        super().__init__(name, streak)
        self.goal = goal

    def __str__(self):
        text = super().__str__()
        return f'{text}, Цель: {self.goal}'

    def progress_percent(self):
        return int(self.streak / self.goal * 100)


b = Habit("Дрочить",0)
print(b)
b.increment_streak()
print(b)
b.reset_streak()
print(b)
d = DailyHabit("Читать", 0, "21:00")
d.increment_streak()
print(d)
print(d.reminder_time)
s = WeeklyHabit("Колоться", 0,"Понедельник")
s.increment_streak()
print(s)
v = WeeklyWithGoal("Любоваться Полиной", 0, 100)
v.increment_streak()
v.increment_streak()
print(v, v.progress_percent())
data = [b.to_dict(), d.to_dict(), s.to_dict(), v.to_dict()]
habits = []
for value in [5, -5, "qwe"]:
    try:
        b.set_streak(value)
    except ValueError as e:
        print(f"Ошибка: {value} - {e}")
    except TypeError as e:
        print(f"Ошибка: {value} - {e}")
    finally:
        print("Проверка завершена")

with open("habits.json", "w", encoding="utf-8", ) as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open("habits.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for item in data:
    habits.append(Habit(item["name"], item["streak"]))
print(len(habits))
print(habits)
for h in habits:
    print(h)

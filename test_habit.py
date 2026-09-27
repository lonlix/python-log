import pytest

from Habit1 import Habit, WeeklyWithGoal


def test_increment_streak():
    h = Habit("Тест", 0)
    h.increment_streak()
    assert h.streak == 1
def test_reset_streak():
    g = Habit("Тест", 0)
    g.increment_streak()
    g.reset_streak()
    assert g.streak == 0
def test_set_streak():
    v = Habit("Тест", 0)
    v.set_streak(5)
    assert v.streak == 5
def test_set_streak_error():
    v = Habit("Тест", 0)
    with pytest.raises(ValueError):
        v.set_streak(-5)
def test_progress_percent():
    r = WeeklyWithGoal("Тест",0, 100)
    r.increment_streak()
    r.increment_streak()
    assert r.progress_percent() == 2

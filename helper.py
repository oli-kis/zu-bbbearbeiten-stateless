import datetime
from dataclasses import dataclass
import operator

items = []


@dataclass
class Todo:
    title: str
    date: datetime
    isCompleted: bool = False


# Hier findet die Ver-BBB-isierung statt
def add(title, date):
    title = title.replace("b", "bbb").replace("B", "Bbb")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    items.append(Todo(title, date))
    items.sort(key=operator.attrgetter("date"))


# Hier werden die Daten an Index weitergegeben
def get_all():
    return items


def get(index):
    return items[index]


# Hier werden die Daten gespeichert
def update(index):
    items[index].isCompleted = not items[index].isCompleted


def remove_all():
    items.clear()

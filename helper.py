from dataclasses import dataclass

# Hier werden die Daten gespeichert.
todos = []


@dataclass
class Item:
    text: str
    isCompleted: bool = False

# Hier findet die Ver - BBB -isierung statt. Dabei wird ein "b" mit drei "b" ersetzt.


def add(todo):
    todo = todo.replace('b', 'bbb').replace('B', 'Bbb')
    todos.append(Item(todo))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted

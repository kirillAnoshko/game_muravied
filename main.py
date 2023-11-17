import random


class Cell:
    """
    Класс, представляющий ячейку в игровом поле.

    image: Символ, представляющий изображение ячейки.
    Y: Координата по вертикали.
    X: Координата по горизонтали.
    content: Содержимое ячейки, например, объект игрока.
    """

    def __init__(self, image='☐', Y=None, X=None):
        """
        Инициализация ячейки.

        image: Символ, представляющий изображение ячейки.
        Y: Координата по вертикали.
        X: Координата по горизонтали.
        """
        self.image = image
        self.Y = Y
        self.X = X
        self.content = None  

class Player:
    """
    Класс, представляющий игрока.

    image: Символ, представляющий изображение игрока.
    Y: Координата игрока по вертикали.
    X: Координата игрока по горизонтали.
    """

    def __init__(self, image='P', Y=None, X=None):
        """
        Инициализация игрока.

        image: Символ, представляющий изображение игрока.
        Y: Координата игрока по вертикали.
        X: Координата игрока по горизонтали.
        """
        self.image = image
        self.Y = Y
        self.X = X

class Field:

    def __init__(self, rows=10, cols=25, cell=Cell, player=Player):
        """
        Инициализация игрового поля.

        rows: Количество строк.
        cols: Количество столбцов.
        cell: Класс ячейки, используемый для создания полей.
        player: Класс игрока.
        """
        self.rows = rows
        self.cols = cols
        self.cells = [[cell(Y=y, X=x) for x in range(cols)] for y in range(rows)]
        self.player = player(Y=random.randint(0, rows-1), X=random.randint(0, cols-1))
        self.cells[self.player.Y][self.player.X].content = self.player

    def drawrows(self):
        """
        Отображение содержимого полей в виде строк.
        """
        for row in self.cells:
            for cell in row:
                if cell.content is not None:
                    print(cell.content.image, end=' ')
                else:
                    print(cell.image, end=' ')
            print()


MyClass = Field()
MyClass.drawrows()


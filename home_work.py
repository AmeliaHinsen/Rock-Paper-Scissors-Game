# Импорт модулів
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# визначення класу, який успадковує від QWidget
class RockPaperScissorsGame(QWidget):
    def __init__(self):
        super().__init__()

        # Рахунок користувача та комп'ютера
        self.user_score = 0
        self.computer_score = 0

        # інтерфейс користувача
        self.init_ui()

    def init_ui(self):
        # Налаштування основних параметрів вікна
        self.setWindowTitle('Rock Paper Scissors Game')

        # Створення та налаштування віджетів (написів, кнопок)
        self.result_label = QLabel('Виберіть свій хід:')
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet('color: blue')

        self.user_label = QLabel('Ваш вибір: ')
        self.computer_label = QLabel("Вибір комп'ютера: ")
        self.score_label = QLabel("Рахунок: Ви - 0, Комп'ютер - 0")
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet('color: blue')

        self.rock_button = QPushButton('Камінь')
        self.paper_button = QPushButton('Папір')
        self.scissors_button = QPushButton('Ножиці')

        # Підключення обробників подій для кнопок
        self.rock_button.clicked.connect(lambda: self.play_game('Камень'))
        self.paper_button.clicked.connect(lambda: self.play_game('Папір'))
        self.scissors_button.clicked.connect(lambda: self.play_game('Ножиці'))

        # Налаштування шрифтів для різних віджетів
        font_label = QFont()
        font_label.setPointSize(14)

        font_text = QFont()
        font_text.setPointSize(13)

        self.result_label.setFont(font_label)
        self.user_label.setFont(font_text)
        self.computer_label.setFont(font_text)
        self.score_label.setFont(font_text)

        # Створення (layout) для керування розташуванням віджетів
        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        layout.addWidget(self.rock_button)
        layout.addWidget(self.paper_button)
        layout.addWidget(self.scissors_button)
        layout.addWidget(self.user_label)
        layout.addWidget(self.computer_label)
        layout.addWidget(self.score_label)

        # Встановлення компонувальника для поточного віджету
        self.setLayout(layout)

    # Метод для обробки ходу користувача та визначення результату гри
    def play_game(self, user_choice):
        choices = ['Ножиці', 'Папір', 'Камінь']
        computer_choice = random.choice(choices)

        # Оновлення тексту на екрані з вибором користувача та комп'ютера
        self.user_label.setText('Ваш вибір: ' + user_choice)
        self.computer_label.setText("Вибір комп'ютера: " + str(computer_choice))

        # Визначення результату гри та оновлення рахунку
        if user_choice == computer_choice:
            result = 'Нічия!'
        elif (user_choice == 'Камінь' and computer_choice == 'Ножиці') or \
             (user_choice == 'Папір' and computer_choice == 'Камінь') or \
             (user_choice == 'Ножиці' and computer_choice == 'Папір'):
            result = 'Вы перемогли!'
            self.user_score += 1
            self.result_label.setStyleSheet('color: green')
        else:
            result = "Комп'ютер виграв"
            self.computer_score += 1
            self.result_label.setStyleSheet('color: red')

        # Оновлення відображення рахунку та результату гри
        self.score_label.setText('Рахунок: Ви - ' + str(self.user_score) + ", Комп'ютер - " + str(self.computer_score))
        self.result_label.setText(result)

# Блок виконання програми під час запуску
if __name__ == '__main__':
    # Створення об'єкта програми та об'єкта гри
    app = QApplication([])
    game = RockPaperScissorsGame()

    # Встановлення розмірів вікна та його відображення
    game.resize(400, 300)
    game.show()

    # Запуск циклу подій програми
    app.exec_()
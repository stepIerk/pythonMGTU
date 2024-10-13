import random
import os
from numpy import sign


class Game:

    def __init__(self) -> None:
        self.magic_number = MagicNumber()

    def game(self) -> None:
        self.magic_number.create_hidden_number()
        self.play = True
        while self.play:
            answer = self.get_user_answer()
            self.process_answer(answer)
        self.the_end()

    def get_user_answer(self) -> str:
        print('Чтобы выйти нажмите: E')
        return input('введите число >>> ')

    def process_answer(self, answer) -> None:
        if answer.isdigit():
            self.guess_number(int(answer))
        else:
            if answer == 'E':
                self.play = False
            else:
                self.siri_speech('Некоректные данные')

    def guess_number(self, answer) -> None:
        comparison_result = self.magic_number.compare(answer)
        speech = ''
        if comparison_result > 0:
            speech = 'Маловато'
        elif comparison_result < 0:
            speech = 'Многовато'
        else:
            speech = 'Угадал, молодец!'
            self.magic_number.create_hidden_number()
        self.siri_speech(speech)

    def the_end(self) -> None:
        self.siri_speech('До встречи')

    def siri_speech(self, speech) -> None:
        print(speech)
        os.system(f'say "{speech}"')


class MagicNumber:

    def __init__(self) -> None:
        self.hidden_number = 0

    def create_hidden_number(self) -> None:
        self.hidden_number = random.randint(1, 100)

    def compare(self, answer) -> int:
        return sign(self.hidden_number - answer)


Game().game()

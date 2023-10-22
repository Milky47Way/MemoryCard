from PyQt5.QtWidgets import QApplication

from random import choice, shuffle
from time import sleep

app=QApplication([])
from m2 import *
from m3 import *

class Question:
  def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
   self.question = question
   self.answer = answer
   self.wrong_answer1 = wrong_answer1
   self.wrong_answer2 = wrong_answer2
   self.wrong_answer3 = wrong_answer3
q1 = Question('Яка батьківщина єнота-полоскуна?', "Північна Америка", "Південна Америка", "Європа" "Африка")
q2 = Question('Скільки живуть єноти-полоскуни?', "12-14 років", "10 років", "6 років", "20 років")
q3 = Question('Чим харчуються єноти?', 'вони всеїдні', 'тільки м`ясом', 'вони виключно вегетаріанці', 'грибами')


def menu_generation():
  menu_win.show()
  window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
  menu_win.hide()
  window.show()
btn_back.clicked.connect(back_menu)

window.show()
app.exec_()

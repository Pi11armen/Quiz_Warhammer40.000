from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton, QButtonGroup, 
        QPushButton, QLabel)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3,):

            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3

question_list = []
question_list.append(Question('Робаут Жиллиман является примархом какого легиона первого основания?', 'Ультрамарины', 'Гвардия Ворона', 'Альфа Легион', 'Железные Кулаки' ))
question_list.append(Question('Начала первой Войны за Армогеддон?', 'M41.444','M32.645','M34.265','M35.954'))
question_list.append(Question('Когда начался 13 Черный крестовый поход?', 'М41.999', 'М41.645','М42.846', 'М39.648'))
question_list.append(Question('Какое количество легионов космодесанта', '20','18','56','11'))

app = QApplication([])
 
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(700, 500)
 


btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году основана Москва?')
 
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Ультрамарины')
rbtn_2 = QRadioButton('Гвардия Ворона')
rbtn_3 = QRadioButton('Альфа Легион')
rbtn_4 = QRadioButton('Железные Кулаки')
 
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
 
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()  
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
 

layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
 
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
 
def start_test():
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def show_correct(res):
    lb_Result.setText(res)
    show_result()

window.cur_question = -1

next_question()

btn_OK.clicked.connect(start_test)
window.setLayout(layout_card)
window.show()
app.exec()

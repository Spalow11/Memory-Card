from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QLabel, QGroupBox, QRadioButton, QButtonGroup
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from random import shuffle

class Qestion():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
def show_qustion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rtbn_1.setChecked(False)
    rtbn_2.setChecked(False)
    rtbn_3.setChecked(False)
    rtbn_4.setChecked(False)
    RadioGroup.setExclusive(True)
# #def start_test():
#     #if button.text() == 'Ответить':
#         check_answer()
#     else:
#         show_qustion()
def ask(quest):
    shuffle(answers)
    answers[0].setText(quest.right_answer)
    answers[1].setText(quest.wrong1)
    answers[2].setText(quest.wrong2)
    answers[3].setText(quest.wrong3)
    question.setText(quest.question)
    corect_answer.setText(quest.right_answer)
    show_qustion()

def check_answer():
    if answers[0].isChecked():
        show_corect('Правильно')
        window.score += 1
    else:
        show_corect('Не правильно')
    print('Статистика:' )
    print('Всего вопросов:', window.total)
    print('Правильных ответов:', window.score)
    print('Рейтинг', window.score/window.total * 100)
def show_corect(res):
    result.setText(res)
    show_result()
    
def next_question():
    window.total += 1
    window.cur_question += 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
        shuffle(questions_list)
    ask(questions_list[window.cur_question])
    

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')
window.resize (300,300)
question = QLabel('Викторина')
question.setFont(QFont("Times", 12,QFont.Bold))
button = QPushButton('Ответить')
button.setFont(QFont("Times", 8,QFont.Bold))
main_layout = QVBoxLayout()
line1 = QHBoxLayout()
line3 = QHBoxLayout()
RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroupBox.setFont(QFont("Times", 10,QFont.Black))


rtbn_1 = QRadioButton('Вариант1')
rtbn_2 = QRadioButton('Вариант2')
rtbn_3 = QRadioButton('Вариант3')
rtbn_4 = QRadioButton('Вариант4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rtbn_1)
RadioGroup.addButton(rtbn_2)
RadioGroup.addButton(rtbn_3)
RadioGroup.addButton(rtbn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rtbn_1)
layout_ans2.addWidget(rtbn_2)
layout_ans3.addWidget(rtbn_3)
layout_ans3.addWidget(rtbn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

AnsGroupBox = QGroupBox('Результат теста')
layout_result = QVBoxLayout()
result = QLabel('Правильно/Неправильно')
corect_answer = QLabel('Правильный ответ')
layout_result.addWidget(result, alignment= Qt.AlignLeft)
layout_result.addWidget(corect_answer, alignment= Qt.AlignCenter)
AnsGroupBox.setLayout(layout_result)
AnsGroupBox.hide()

answers = [rtbn_1,rtbn_2,rtbn_3,rtbn_4]
questions_list = []

q1 = Qestion('Какой национальности не существует?','Смурфы','Энцы','Чулумцы','Алеуты')
questions_list.append(q1)
q2 = Qestion('Государственный язык Бразилии','Португальский','Испанский','Бразильский','Английский')
questions_list.append(q2)
q3 = Qestion('Какого цвета нет на флаге России?', 'Зеленый', 'Белый','Синий', 'Красный' )
questions_list.append(q3)
q4 = Qestion('Государственный язык Португалии?','Португальский','Испанский','Бразильский','Английский')
questions_list.append(q4)
q5 = Qestion('Госудраственный язык в России?','Русский','Советский','Немецкий','Китайский')
questions_list.append(q5)
q6 = Qestion('Сколько языков являются официальными в ООН?','6','5','4','10')
questions_list.append(q6)
q7 = Qestion('Межнациональные – это отношения между',' разными народами','представителями разных государств','разными социальными группами','представителями разных полов')
questions_list.append(q7)
q8 = Qestion('Допустима ли дискриминация наций в современном обществе','не допустима','допустима',' допустима для некоторых стран','может происходить в благих целях')
questions_list.append(q8)
q9 = Qestion('Нация – это','все граждане определенной страны','люди с определенным цветом кожи и другими внешними признаками','люди, объединенные религиозными убеждениями','люди с разным полом')
questions_list.append(q9)
q10 =Qestion('Какая из этих стран является многонациональной','Бельгия','Южная Корея','Германия','Исландия')
questions_list.append(q10)
#ask(quest)


line1.addWidget(question,alignment= Qt.AlignHCenter)
line3.addStretch(1)
line3.addWidget(button,alignment= Qt.AlignCenter,stretch = 34)
line3.addStretch(1)


RadioGroupBox.setLayout(layout_ans1)
main_layout.addLayout(line1)
main_layout.addWidget(RadioGroupBox)
main_layout.addWidget(AnsGroupBox)
main_layout.addLayout(line3,stretch =1 )
main_layout.setSpacing(5)

button.clicked.connect(click_ok)


window.setLayout(main_layout)
window.cur_question = -1
window.score = 0
window.total = 0
next_question()
window.show()
app.exec_()
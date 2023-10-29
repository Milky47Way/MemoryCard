q1 = Question('Яка батьківщина єнота-полоскуна?', "Північна Америка", "Південна Америка", "Європа", "Африка")
q2 = Question('Скільки живуть єноти-полоскуни?', "12-14 років", "10 років", "6 років", "20 років")
q3 = Question('Чим харчуються єноти?', 'вони всеїдні', 'тільки м`ясом', 'вони виключно вегетаріанці', 'грибами')
q4 = Question('Які лисиці здатні витримати температуру близько -70°С?', 'песці', 'тибетські', 'ніякі, це неможливо','дарвінівські')

q1 = Question('Японія - країна', "Сонця", "Води", "Туманів", "Аніме")
q2 = Question('Столиця Японії -', "Токіо", "Кіото", "Нара", "Канадзава")
q3 = Question('Столиця Японії -', "Токіо", "Кіото", "Нара", "Канадзава")
q4 = Question('Які символи не відносяться до японської мови?', "Ієрогліфи", "Кандзі", "Хірагана", "Катакана")
q5 = Question('Скільки в Японії головних островів?', "4", "3", "2", "12")
q6 = Question('Якою країною є Японія в плані економіки?', "3", "10", "1", "43")

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
question = [q1, q2, q3, q4, q5, q6]
def new_question():




  q1 = Question('Японія - країна', "Сонця", "Води", "Туманів", "Аніме")
q2 = Question('Столиця Японії -', "Токіо", "Кіото", "Нара", "Канадзава")
q3 = Question('Столиця Японії -', "Токіо", "Кіото", "Нара", "Канадзава")
q4 = Question('Які символи не відносяться до японської мови?', "Ієрогліфи", "Кандзі", "Хірагана", "Катакана")
q5 = Question('Скільки в Японії головних островів?', "4", "3", "2", "12")
q6 = Question('Якою країною є Японія в плані економіки?', "3", "10", "1", "43")

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
question = [q1, q2, q3, q4, q5, q6]
def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)
new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text()== lb_right_answer.text():
                lb_result.setText('Правильно!')
                answer.setChecked(False)
                break
                
        else:
            lb_result.setText('Неправильно!')
    RadioGroup.setExclusive(True)
def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Наступне запитання')
        
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()
        btn_next.setText('Відповісти')
btn_next.clicked.connect(click_ok)
def rest():
    window.hide()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear() 
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)
def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(),
                     le_wrong_ans2.text(),
                     le_wrong_ans3.text())
    question.append(new_q)
    clear()
btn_add_question.clicked.connect(add_question)



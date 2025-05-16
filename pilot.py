
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Материалы для подготовки к олимпиаде "Я - профессионал по языкознанию"')
root.geometry('1000x1300')
button_close=Button(root, text="Закрыть", command=root.destroy)
button_close.config(bg='red', fg='black')
button_close.pack()
def next_window():
    root.withdraw()
    second_window = Toplevel(root)
    second_window.protocol("WM_DELETE_WINDOW", root.destroy)
    second_window.title("Задания по русскому языку")
    second_window.geometry('1000x1300')
    #second_window.resizable(True, True)
    canvas=Canvas(second_window)
    frame = Frame(canvas)#, padx=10, pady=10)
    #frame.pack(fill=tk.BOTH, expand=True)
    scrollbar = Scrollbar(second_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")

    canvas.pack(fill="both", expand=True)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    task1 = Label(frame,text="\nКомпетенции в сфере знания паронимов (задание 6 в олимпиаде). В этом разделе 5 заданий. \nОтветы должны вводиться через один пробел без запятых! \nЗадание 1. Редактируя книгу начинающего писателя, вы время от времени исправляете в тексте неправильно употребленные паронимы. Сделайте это в двух следующих предложениях."
"\nВ новом офисе установили акустичную аппаратуру высокого качества, обеспечивающую отличное восприятие речи."
"\nВ ходе судебного разбирательства он представил доказательную базу, подтверждающую его невиновность.")
    task1.pack()
    task1_1 = Entry(frame)
    task1_1.pack()
    def check1():
        if task1_1.get().lower()=='акустическую доказательственную' or task1_1.get().lower()=='акустическая доказательственная':
            messagebox.showinfo("Состояние ответа","Верный ответ")
        elif task1_1.get()=='':
            messagebox.showwarning("Предупреждение", "Введите ответы на задание 1!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')
    but=Button(frame, text= 'Проверить задание 1', command=check1)
    but.pack()

    task2 = Label(frame, text="\nЗадание 2.Редактируя книгу начинающего писателя, вы время от времени исправляете в тексте неправильно употребленные паронимы. Сделайте это в двух следующих предложениях."
"\nНа полке стояли книги в кожевных переплетах, изданные в начале XX века."
"\nОн всегда отличался бедствующей на эмоции речью, что создавало впечатление замкнутости.")
    task2.pack()


    task2_2 = Entry(frame)
    task2_2.pack()
    def check2():
        if task2_2.get().lower()=='кожаных бедной' or task2_2.get().lower()=='кожаных бедной':
            messagebox.showinfo("Состояние ответа","Верный ответ")
        elif task2_2.get()=='':
            messagebox.showwarning("Предупреждение", "Введите ответы на задание 2!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')
    but2 = Button(frame, text='Проверить задание 2', command=check2)
    but2.pack()
    task3 = Label(frame, text="\nЗадание 3. Редактируя книгу начинающего писателя, вы время от времени исправляете в тексте неправильно употребленные паронимы. Сделайте это в двух следующих предложениях."
"\nВ музее была представлена уникальная историчная реконструкция средневекового города, созданная по архивным материалам."
"\nСтуденты провели экспериментное исследование влияния стресса на когнитивные способности человека.")
    task3.pack()
    task3_1 = Entry(frame)
    task3_1.pack()

    def check3():
        if task3_1.get().lower() == 'историческая экспериментальное':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task3_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на задание 3!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but4 = Button(frame, text='Проверить задание 3', command=check3)
    but4.pack()
    task4 = Label(frame, text="\nЗадание 4. Редактируя книгу начинающего писателя, вы время от времени исправляете в тексте неправильно употребленные паронимы. Сделайте это в двух следующих предложениях."
"\nОна купила абонент в бассейн на целый месяц, но посетила всего пару занятий."
"\nМастер с точностью передал анекдотичную ситуацию, но зрители все равно оставались серьезными, не понимая всей комичности сцены.")
    task4.pack()
    task4_1 = Entry(frame)
    task4_1.pack()

    def check4():
        if task4_1.get().lower() == 'абонемент анекдотическую' or task4_1.get().lower() == 'абонемент анекдотическая':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task4_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на задание 4!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but5 = Button(frame, text='Проверить задание 4', command=check4)
    but5.pack()
    task5 = Label(frame,
                     text="\nЗадание 5.Редактируя книгу начинающего писателя, вы время от времени исправляете в тексте неправильно употребленные паронимы. Сделайте это в двух следующих предложениях."
"\nЭто был совсем не тот представительный случай, когда можно пойти на риск. Здесь требовалось строгое соблюдение правил."
"\nНовый начальник оказался требовательным, но справедливым: он всегда проводил демонстрационные разборы ошибок, чтобы сотрудники учились на чужих примерах.")
    task5.pack()
    task5_1 = Entry(frame)
    task5_1.pack()

    def check5():
        if task5_1.get().lower() == 'представительский демонстративные':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task5_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на задание 5!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but6= Button(frame, text='Проверить задание 5', command=check5)
    but6.pack()
    task11 = Label(frame,
                     text="\nСледующие задания проверяют компетенции в лексикологии и лексическом анализе (задание 1 в реальной олимпиаде). "
                          "\nЗадание 1.Вы проводите учебное занятие, пользуясь методическими разработками старшего коллеги. К сожалению, "
                          "\nколлега не указывает в своих материалах ключи к заданиям (возможно, помнит наизусть или считает тривиальными, а переспросить его невозможно или неудобно). "
                          "\nПо опыту предыдущих примеров вы уверены, что оба слова начинаются на Ж. Восстановите слова-ключи"
                          "\nСо времен «Толкового словаря живого великорусского языка» В. И. Даля некоторые слова частично или полностью изменили свои значения, "
                          "\nдругие полностью или почти полностью исчезли из языка. В значительной степени это касается слов иностранного"
"\nпроисхождения, толкование которых у Даля обычно последовательное и тщательное."
"Какие два слова Даль трактовал так:"
"\n«дневник, поденная записка.., повременное издание.., срочник»."
"\n«Телодвижение человека, немой язык, вольный или невольный; обнаружение знаками,"
"движениями чувств, мыслей»."
"\nКлюч: оба слова начинаются на букву Ж.")
    task11.pack()
    task11_1 = Entry(frame)
    task11_1.pack()

    def check11():
        if task11_1.get().lower() == 'журнал жест':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task11_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на задание 1!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but7 = Button(frame, text='Проверить задание 1', command=check11)
    but7.pack()
    task12=Label(frame, text="\nЗадание 2. Угадайте слова по их значению из словаря Даля. Ключ: оба слова начинаются на з"
                                "\n1)наглазный козырек от света, крытый передок в тарантасе"
                                "\n2)остаток по сожжении растений, чего-либо растительного, а иногда и животных веществ")
    task12.pack()
    task12_1 = Entry(frame)
    task12_1.pack()

    def check12():
        if task12_1.get().lower() == 'зонт зола':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task12_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на задание 2!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but8 = Button(frame, text='Проверить задание 2', command=check12)
    but8.pack()

    task13=Label(frame, text="\nЗадание 3. Угадайте слова по их значению из словаря Даля. Ключ: оба слова начинаются на т"
                    "\n1) дно, испод, основание, как плоскость"
                    "\n2) лошадь, способная перевозить тяжёлые грузы")
    task13.pack()
    task13_1 = Entry(frame)
    task13_1.pack()
    def check13():
        if task13_1.get().lower() == 'тло тяжеловес':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task13_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на задание 3!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but9= Button(frame, text='Проверить задание 3', command=check13)
    but9.pack()

    task14 = Label(frame,
                      text="\nЗадание 4. Угадайте слова по их значению из словаря Даля. Ключ: оба слова начинаются на п"
                           "\n1) пристанище, прибежище, сходбища"
                           "\n2) крыша, кровля, потолок, накат, настилка")
    task14.pack()
    task14_1 = Entry(frame)
    task14_1.pack()

    def check14():
        if task14_1.get().lower() == 'притон палуба':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task14_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на задание 4!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')


    but10 = Button(frame, text='Проверить задание 4', command=check14)
    #but10 = Button(second_window, text='Проверить задание 4', command=check14)
    but10.pack()

    task15 = Label(frame,
                   text="\nЗадание 2. В представленном предложении содержится синтаксическая неоднозначность"
                        "\nВаша задача - выписать словосочетания в той же форме, что в тексте, из-за которых возникает неоднозначность"
                        "\nVar. 1.(в ответе 2 словосочетания) Я увидела слона в пижаме")
    task15.pack()
    task15_1 = Entry(frame)
    task15_1.pack()

    def check15():
        if task15_1.get().lower() == 'я в пижаме слона в пижаме' or task14_1.get().lower() == 'слона в пижаме я в пижаме':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task15_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but13 = Button(frame, text='Проверить задание 2 (вар. 1)', command=check15)
    # but10 = Button(second_window, text='Проверить задание 4', command=check14)
    but13.pack()

    task16 = Label(frame,
                   text="\nVar. 2. (в ответе одно словосочетание) Поздравление преподавателей было трогательным")
    task16.pack()
    task16_1 = Entry(frame)
    task16_1.pack()

    def check16():
        if task16_1.get().lower() == 'поздравление преподавателей':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task16_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but14 = Button(frame, text='Проверить задание 2 (вар. 2)', command=check16)
    # but10 = Button(second_window, text='Проверить задание 4', command=check14)
    but14.pack()

    task17 = Label(frame,
                   text="\nVar. 3.(в ответе 2 словосочетания) Дети раскрашивали рисунки зелеными красками и фломастерами")
    task17.pack()
    task17_1 = Entry(frame)
    task17_1.pack()

    def check17():
        if task17_1.get().lower() == 'зелеными красками зелеными красками и фломастерами' or task17_1.get().lower() == 'зелеными красками и фломастерами':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task17_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but15 = Button(frame, text='Проверить задание 2 (вар. 3)', command=check17)
    # but10 = Button(second_window, text='Проверить задание 4', command=check14)
    but15.pack()

    task100=Label(frame, text="Задание 4. Вы редактируете (по просьбе или с согласия автора) статью. \nПервоначально она была опубликована в издании, рассчитанном на специалистов, но теперь предполагается перепечатать ее для более широкого круга читателей. \nНиже даны фрагменты и обозначения. \nПредложите для каждого из них замену — более традиционный для русской грамматической терминологии термин."
                  "\nЗадача 1. сделай, пожалуйста, этот отчет, а иначе лишишься работы."
"\nОбозначения: дейктическое (местоимение), императив, лабиализованный, нарративный"
                  "\nВведите ответ для первого слова дейктическое (местоимение)")
    task100.pack()
    task100_1=Entry(frame)
    task100_1.pack()
    def check72():
        if task100_1.get().lower() == 'указательное' or task100_1.get().lower() == 'указательное (местоимение)' or task100_1.get().lower() == 'указательный':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task100_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')
    but100=Button(frame, text="Проверить", command=check72)
    but100.pack()

    task101 = Label(frame,
                    text="\nВведите ответ для второго слова императив")
    task101.pack()
    task101_1 = Entry(frame)
    task101_1.pack()

    def check73():
        if task101_1.get().lower() == 'повелительное наклонение' or task101_1.get().lower() == 'форма повелительного наклонения' or task101_1.get().lower() == 'глагол в повелительном наклонении':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task101_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but101 = Button(frame, text="Проверить", command=check73)
    but101.pack()

    task102 = Label(frame,
                    text="\nВведите ответ для третьего слова лабиализованный")
    task102.pack()
    task102_1 = Entry(frame)
    task102_1.pack()

    def check74():
        if task102_1.get().lower() == 'огубленный':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task102_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but102 = Button(frame, text="Проверить", command=check74)
    but102.pack()

    task103 = Label(frame,
                    text="\nВведите ответ для четвертого слова нарративный")
    task103.pack()
    task103_1 = Entry(frame)
    task103_1.pack()

    def check75():
        if task103_1.get().lower() == 'повествовательный':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task103_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but103 = Button(frame, text="Проверить", command=check75)
    but103.pack()

    task104 = Label(frame,
                    text="\nЗадача 2. Она не сдала зачёт по языкознанию, а я получила отлично достаточно легко, поэтому хочу помочь ей с подготовкой."
                    "\nОбозначения: антитеза, перфектный, велярный, адвербиальный"
                    "\nВведите ответ для первого слова антитеза")
    task104.pack()
    task104_1 = Entry(frame)
    task104_1.pack()

    def check76():
        if task104_1.get().lower() == 'противопоставление':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task104_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but104 = Button(frame, text="Проверить", command=check76)
    but104.pack()

    task105 = Label(frame,
                    text="\nВведите ответ для второго слова перфектный")
    task105.pack()
    task105_1 = Entry(frame)
    task105_1.pack()

    def check77():
        if task105_1.get().lower() == 'совершенный':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task105_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but105 = Button(frame, text="Проверить", command=check77)
    but105.pack()

    task106 = Label(frame,
                    text="\nВведите ответ для третьего слова велярный")
    task106.pack()
    task106_1 = Entry(frame)
    task106_1.pack()

    def check78():
        if task106_1.get().lower() == 'заднеязычный' or task106_1.get().lower() == 'задненёбный':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task106_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but106 = Button(frame, text="Проверить", command=check78)
    but106.pack()

    task107 = Label(frame,
                    text="\nВведите ответ для четвертого слова адвербиальный")
    task107.pack()
    task107_1 = Entry(frame)
    task107_1.pack()

    def check79():
        if task107_1.get().lower() == 'наречный':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task107_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but107 = Button(frame, text="Проверить", command=check79)
    but107.pack()

    task108 = Label(frame,
                    text="\nЗадача 3. Если бы ты была ответственее, тебе бы не приходилось сидеть ночами, выполняя работы."
                    "\nОбозначения: билабиальный, конъюнктив, партиципант, фрикативный"
                    "\nВведите ответ для первого слова билабиальный")
    task108.pack()
    task108_1 = Entry(frame)
    task108_1.pack()

    def check80():
        if task108_1.get().lower() == 'губно-губной':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task108_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but108 = Button(frame, text="Проверить", command=check80)
    but108.pack()

    task109 = Label(frame,
                    text="\nВведите ответ для второго слова конъюнктив")
    task109.pack()
    task109_1 = Entry(frame)
    task109_1.pack()

    def check81():
        if task109_1.get().lower() == 'сослагательное наклонение':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task109_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but109 = Button(frame, text="Проверить", command=check81)
    but109.pack()

    task110 = Label(frame,
                    text="\nВведите ответ для третьего слова партиципант")
    task110.pack()
    task110_1 = Entry(frame)
    task110_1.pack()

    def check82():
        if task110_1.get().lower() == 'участник действия' or task110_1.get().lower() == 'участник ситуации':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task110_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but110 = Button(frame, text="Проверить", command=check82)
    but110.pack()

    task111 = Label(frame,
                    text="\nВведите ответ для четвёртого слова фрикативный")
    task111.pack()
    task111_1 = Entry(frame)
    task111_1.pack()

    def check83():
        if task111_1.get().lower() == 'щелевой':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task111_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but111 = Button(frame, text="Проверить", command=check83)
    but111.pack()

    task112 = Label(frame,
                    text="\nЗадача 4. Завтра мы наконец сдадим последний зачет и обнимемся!"
                    "\nОбозначения: экскламация, индикатив, реципрок, темпоральный"
                    "\nВведите ответ для первого слова экскламация")
    task112.pack()
    task112_1 = Entry(frame)
    task112_1.pack()

    def check84():
        if task112_1.get().lower() == 'риторическое восклицание' or task112_1.get().lower() == 'восклицание':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task112_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but112 = Button(frame, text="Проверить", command=check84)
    but112.pack()

    task113 = Label(frame,
                    text="Введите ответ для второго слова индикатив")
    task113.pack()
    task113_1 = Entry(frame)
    task113_1.pack()

    def check85():
        if task113_1.get().lower() == 'изъявительное наклонение':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task113_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but113 = Button(frame, text="Проверить", command=check85)
    but113.pack()

    task114 = Label(frame,
                    text="Введите ответ для третьего слова реципрок")
    task114.pack()
    task114_1 = Entry(frame)
    task114_1.pack()

    def check86():
        if task114_1.get().lower() == 'взаимный залог':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task114_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but114 = Button(frame, text="Проверить", command=check86)
    but114.pack()

    task115 = Label(frame,
                    text="Введите ответ для четвертого слова темпоральный")
    task115.pack()
    task115_1 = Entry(frame)
    task115_1.pack()

    def check87():
        if task115_1.get().lower() == 'временной':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task115_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but115 = Button(frame, text="Проверить", command=check87)
    but115.pack()

    task116 = Label(frame,
                    text="Задача 5. Cначала он умывается,завтракает кашей, а потом во весь дух спешит в СПбГУ."
                         "\nОбозначения: лабио-дентальный, аббревиация, презенс, комплемент"
                         "\nВведите ответ для первого слова лабио-дентальный")
    task116.pack()
    task116_1 = Entry(frame)
    task116_1.pack()

    def check88():
        if task116_1.get().lower() == 'губно-зубной':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task116_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but116 = Button(frame, text="Проверить", command=check88)
    but116.pack()

    task117 = Label(frame,
                    text=
                         "\nВведите ответ для второго слова аббревиация")
    task117.pack()
    task117_1 = Entry(frame)
    task117_1.pack()

    def check89():
        if task117_1.get().lower() == 'сокращение слов' or task117_1.get().lower() == 'сокращение слов начальными буквами':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task117_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but117 = Button(frame, text="Проверить", command=check89)
    but117.pack()

    task118 = Label(frame,
                    text=
                    "\nВведите ответ для третьего слова презенс")
    task118.pack()
    task118_1 = Entry(frame)
    task118_1.pack()

    def check90():
        if task118_1.get().lower() == 'непрошедшее время' or task118_1.get().lower() == 'настоящее время':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task118_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but118 = Button(frame, text="Проверить", command=check90)
    but118.pack()

    task119 = Label(frame,
                    text=
                    "\nВведите ответ для четвертого слова комплемент")
    task119.pack()
    task119_1 = Entry(frame)
    task119_1.pack()

    def check91():
        if task119_1.get().lower() == 'дополнение':
            messagebox.showinfo("Состояние ответа", "Верный ответ")
        elif task119_1.get() == '':
            messagebox.showwarning("Предупреждение", "Введите ответы на первую задачу второго задания!!")
        else:
            messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

    but119 = Button(frame, text="Проверить", command=check91)
    but119.pack()

    task120 = Label(frame,
                    text=
                    "\nВы являетесь организатором лингвистической конференции. В поступивших заявках студентов встречаются следующие пассажи:"
                    "\n1. «Известный лингвист Ежи Курилович, обнаруживший существование маргиналий в хеттском языке, внес значительный вклад в развитие индоевропеистики»."
                    "\n2. «Отличительной особенностью португальского на фоне большинства романских языков является наличие так называемого склоняемого инфинитива»"
                    "\n3. «Важное направление советской и российской прикладной тестологии – атрибуция анонимных и псевдоанонимных произведений»"
                    "\n4. «Синтез лингвистики и количественных методов ярче всего проявился в трудах основателя лингвистической топологии Джозефа Гринберга»."
                    "\n5. «Считается, что препозитивная постановка артикля в румынском языке обусловлена прежде всего влиянием болгарского»."
                    "\n6. «Отличительной чертой баскского языка является эрративный строй»."
                    "\n7. «Сегодня в Национальном корпусе русского языка есть функция снятия синонимии для корректного поиска»"
                    "\n8. «Язык в акустико-артикуляторном аспекте изучается средствами современной фонологии»"
                    "\n9. «В семантике пациенсом называют намеренного инициатора ситуации, который непосредственно исполняет соответствующие действия»"
                    "\n10. «При работе над исследованием мы опирались на терминологический аппарат лексикологической семантики Ю.Д. Апресяна»"
                    "\n11. «Носителями дидактической функции могут быть лексические единицы (личные и указательные местоимения, частицы) и грамматические категории»"
                    "\nНайдите искажённые употребления лингвистических понятий и терминов, предложите верные соответствия."
                    "\nОбратите внимание, что поле ввода ответов идут в том же порядке, что и предложения"
                    "\nПри вводе ответов ставьте, пожалуйста, слова в ту же форму, в которой они даны в тексте")
    task120.pack()
    task120_1 = Entry(frame)
    task120_2 = Entry(frame)
    task120_3 = Entry(frame)
    task120_4 = Entry(frame)
    task120_5 = Entry(frame)
    task120_6 = Entry(frame)
    task120_7 = Entry(frame)
    task120_8 = Entry(frame)
    task120_9 = Entry(frame)
    task120_10 = Entry(frame)
    task120_11 = Entry(frame)
    task120_1.pack()
    task120_2.pack()
    task120_3.pack()
    task120_4.pack()
    task120_5.pack()
    task120_6.pack()
    task120_7.pack()
    task120_8.pack()
    task120_9.pack()
    task120_10.pack()
    task120_11.pack()

    def check93():
        b=[]
        if task120_1.get().lower() == 'ларингалов':
            b.append(1)
        if task120_2.get().lower() == 'спрягаемого':
            b.append(1)
        if task120_3.get().lower() == 'текстологии':
            b.append(1)
        if task120_4.get().lower() == 'типологии':
            b.append(1)
        if task120_5.get().lower() == 'постпозитивная':
            b.append(1)
        if task120_6.get().lower() == 'эргативный':
            b.append(1)
        if task120_7.get().lower() == 'омонимии':
            b.append(1)
        if task120_8.get().lower() == 'фонетики':
            b.append(1)
        if task120_9.get().lower() == 'агенсом':
            b.append(1)
        if task120_10.get().lower() == 'лексической':
            b.append(1)
        if task120_11.get().lower() == 'дейктической':
            b.append(1)
        messagebox.showinfo("Состояние ответа", f'Вы набрали {sum(b)}/11 баллов')

    but120 = Button(frame, text="Проверить", command=check93)
    but120.pack()

    def return1():
        root.deiconify()
        second_window.withdraw()
    but3=Button(second_window, text='Домой', command=return1)
    but3.pack()
    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
bt = Button(root, text="Задания по русскому языку", command=next_window)
bt.pack()
def window3():
    root.withdraw()
    third_window = Toplevel(root)
    third_window.protocol("WM_DELETE_WINDOW", root.destroy)
    third_window.title("Задания по немецкому языку")
    third_window.geometry('1000x1300')
    editor = Text(third_window)
    editor.pack(fill=BOTH, expand=True)
    editor.insert("1.0", "Составитель задач - Марков Даниил\nВопрос  19 (10 баллов)"
                         "\nSie editieren einen deutschen Text. Lesen Sie zuerst den Text und machen Sie anschließend"
                         "Aufgaben nach dem Text:"
                         "\nNetzwerken hat für viele einen negativen Beigeschmack, und es heißt ironisch: „Eine Hand"
                         "wäscht die andere und am Ende sind sie beide dreckig“. Diese Gefahr bestehen immer dann,"
                         "wenn statt der Leistung als Empfehlungskriterium persönliche Interessen im Vordergrund"
                         "stehen: Wenn man also an eine inkompetente Person eine bestimmte Position vergibt, weil"
                         "man sich dadurch für sich selbst einen Nutzen verspricht. Das ist mit Netzwerken nicht"
                         "gemeint. Hier geht es darum, dass man etwa einen Job zwar über Beziehungen, aber aufgrund"
                         "seiner guten Leistung bekommt. Laut einer Untersuchung wurden 2006 34 Prozent der Stellen"
                         "über eigene Mitarbeiter oder persönliche Kontakte besetzt. Gegenwärtig hat schon jeder"
                         "sechste deutsche Großbetrieb ein institutionalisiertes Programm „Mitarbeiter werben"
                         "Mitarbeiter“. Wenn man diese Zahlen liest, ist klar, dass es sich lohnt, Zeit und Mühe in das"
                         "Netzwerken zu investieren."
                         "Jeder Mensch ist bereits – ob er es will oder nicht – Mitglied in mindestens einem Netzwerk,"
                         "nämlich der Familie. Auch die Dorfgemeinschaft stellte in früheren Zeiten ein Netzwerk dar."
                         "Doch funktionieren diese beiden Institutionen nur noch selten im Sinne gegenseitiger"
                         "Unterstützung und Förderung. Deshalb ist es wichtig, sich sein eigenes Netzwerk zu schaffen"
                         "oder Mitglied in einem bestehenden Netzwerk zu werden. Früher gab es im akademischen"
                         "Bereich nur Studentenverbindungen und die standen und stehen bis auf wenige Ausnahmen"
                         "nur männlichen Studenten offen. Heute gibt es jedoch darüber hinaus an einigen deutschen"
                         "Universitäten Alumni-Netzwerke, in denen sich ehemalige Studenten der jeweiligen"
                         "Universität treffen und Kontakte aufbauen."
                         "Darüber hinaus gibt es die traditionellen Netzwerke wie die Rotarier-, Lions- oder KiwanisClubs. Diese haben übrigens Nachwuchsorganisationen, so dass man nicht wohlhabend sein"
                         "und im Leben bereits etwas erreicht haben muss, um Mitglied zu werden. Allerdings braucht"
                         "man immer eine Person – und später zur Aufnahme noch eine zweite –, die dort Mitglied ist"
                         "und einen einlädt. Selbst um die Mitgliedschaft zu bitten, ist meistens nicht möglich."
                         "Besonders beliebt beim Netzwerken sind heute Internetplattformen. Doch wird man auch bei"
                         "Internetnetzwerken feststellen, es geht nichts über den persönlichen Kontakt. Denn die Basis"
                         "des Netzwerkens ist Vertrauen und das lässt sich nur durch persönliches Kennenlernen"
                         "aufbauen."
                         "Vor einigen Jahren gab es eine neue Geschäftsidee: Visitenkartenpartys, eine Plattform, um"
                         "Kontakte herzustellen. Sie ist vor allem für Selbstständige wie Rechtsanwälte oder"
                         "Werbefachleute hilfreich. Auch daraus kann sich an jedem Ort ein Netzwerk entwickeln,"
                         "wenn jemand dazu die Initiative ergreift."
                         "Netzwerke funktionieren dann am besten, wenn sie einen gemeinsamen Zweck verfolgen,"
                         "denn das verbindet. So setzen sich die Kiwanis-Clubs zum Beispiel für das Wohl der Kinder"
                         "ein. Wenn man hier zu offensichtlich seine eigenen Interessen verfolgt, fällt dies negativ auf."
                         "Nicht zuletzt auch deshalb, weil vor dem „Nehmen“ das „Geben“ kommt."
                         "So lässt sich abschließend sagen, um beruflich erfolgreich zu sein, braucht man Kontakte zu"
                         "vielen und natürlich auch zu möglichst einflussreichen Menschen. Bereits das Wort"
                         "„Beförderung“ zeigt, dass man ohne die Unterstützung anderer nicht weit kommt."
                         "\nAufgaben:"
                         "\n1) Formulieren Sie die Hauptidee des Textes in einem Satz (2 Punkte)"
                         "\n2) Finden Sie im Text drei Verben zu verschiedenen Zeiten (Präsens, Präteritum, Perfekt) und erklären, warum der Autor diese Formen verwendet hat (2 Punkte)"
                         "\n3) Finden Sie die unterstrichenen Wörter im Text und zerlegen sie in morphologische Bestandteile (Präfixe, Suffixe usw.) (2 Punkte)"
                         "\n4) Erstellen Sie einen Titel für den Text und erklären Sie im Detail, warum er dazu passt. Der Titel muss mindestens 7 Wörter enthalten (2 Punkte)"
                         "\n5) Finden Sie im ersten Absatz 2 grammatische Fehler (2 Punkte)"
                         "\nInsgesamt max. 10 Punkte"
                         "\nОтвет:"
                         "\n1) Formulieren Sie die Hauptidee des Textes in einem Satz (2 Punkte)"
                         "z. B.: Die Hauptidee des Textes ist, dass Networking, also das Aufbauen und Pflegen von beruflichen Kontakten, für den beruflichen Erfolg unerlässlich ist"
                         "\n2) Finden Sie im Text drei Verben zu verschiedenen Zeiten (Präsens, Präteritum, Perfekt) und erklären, warum der Autor diese Formen verwendet hat (2 Punkte)"
                         "geht (Präsens):  'Hier geht es darum, dass man etwa einen Job zwar über Beziehungen, aber aufgrund seiner guten Leistung bekommt' Grund der Verwendung: Das Präsens wird verwendet, um eine allgemeine Aussage zu machen, die zeitlos gültig ist. Es beschreibt den Kern des positiven Netzwerkens und seine Funktionsweise, unabhängig von einer spezifischen Zeit.."
                         "wurden (Präteritum): 'Laut einer Untersuchung wurden 2006 34 Prozent der Stellen über eigene Mitarbeiter oder persönliche Kontakte besetzt'  Grund der Verwendung: Das Präteritum beschreibt eine abgeschlossene Handlung in der Vergangenheit. Es präsentiert eine statistische Tatsache aus dem Jahr 2006 als konkreten Beleg für die Relevanz von Netzwerken."

                         "haben eingeführt (Perfekt): 'Viele Unternehmen haben bereits  Programme „Mitarbeiter werben Mitarbeiter' eingeführt Hier ist die Handlung des Einführungs der Programme abgeschlossen und liegt in der Vergangenheit.  Die Wirkung (die Programme existieren) ist aber bis in die Gegenwart relevant."

                         "\n3) Finden Sie drei unterstrichene Wörter im Text und zerlegen sie in morphologische Bestandteile (Präfixe, Suffixe usw.) (2 Punkte)"
                         "institutionalisierte: institutionalis-:  Wortstamm, abgeleitet von 'Institution, -iert:  Suffix, Partizip Perfekt (Passiv), zeigt eine abgeschlossene Handlung an und verleiht dem Wort ein adjektivisches Merkmal."
                         "Nachwuchsorganisationen: Nachwuchs-:  Wortstamm (Kompositum aus 'Nachwuchs' und 'Organisationen').  'Nachwuchs' selbst zerlegt sich in: Nach-: Präfix (zeigt Folge oder Bezug auf etwas), wuchs:  Wortstamm (Substantiv, bedeutet 'Wachstum, Entwicklung'; -organisation-: Wortstamm (Substantiv), -en: Suffix (Pluralendung)"
                         "Werbefachleute: werbe-: Wortstamm (Substantiv 'Werbung' im Genitiv), fach-: Wortstamm (Substantiv, bedeutet 'Fachgebiet', 'Spezialisierung'),  -leute: Suffix (Substantivsuffix, bildet zusammengesetzte Substantive, die Personen bezeichnen – 'Leute' ist ein Kollektivum)"

                         "\n4) Erstellen Sie einen Titel für den Text und erklären Sie im Detail, warum er dazu passt. Der Titel muss mindestens 7 Wörter enthalten (2 Punkte)"
                         "Von der Familie zum Online-Netzwerk: Strategien für erfolgreiches Kontaktemanagement. Der Titel umfasst die Bandbreite der im Text beschriebenen Netzwerkformen (Familie, traditionelle Clubs, Online-Plattformen) und betont die strategische Komponente des erfolgreichen Networking."

                         "\n5) Finden Sie im ersten Absatz 2 grammatische Fehler (2 Punkte)"
                         "Netzwerken hat für viele einen negativen Beigeschmack → Netzwerken haben für viele einen negativen Beigeschmack"
                         "Diese Gefahr bestehen immer dann → Diese Gefahr besteht immer dann"
                         "\nВопрос 20 (15 баллов)"

                         "\nSie müssen für den Podkast eines Schauspielers die Beschreibung des Films verfassen,"
                         "dessen kurze Inhaltsangabe unten steht. Ihr Text (min. 150 Wörter) sollte die Zuhörer des"
                         "Podkasts  zum Ansehen des Films motivieren."
                         "Die Beschreibung soll der Film bewerten und das Interesse der Zuschauer wecken. Es muss das Genre des Films, die Zielgruppe bestimmt werden. Ihr Stil sollte der von Ihnen bestimmten Zielgruppe entsprechen."
                         "Ihr Text darf bestimmte Schlüsselwörter aus der Aufgabe aber keine Inhaltsangabe enthalten."
                         "Hier ist nun der Titel und die Inhaltsangabe des Films:"

                         "Friedrich Müller"
                         "Zwölf"

                         "Ein Mordprozess: Ein junger Mann wird beschuldigt, seinen Vater erstochen zu haben. Zwölf Geschworene sollen nun über sein Schicksal entscheiden. Auf den ersten Blick scheint die Sache klar: Die Beweise sind erdrückend, die Zeugenaussagen eindeutig. Elf der Geschworenen sind überzeugt von der Schuld des Angeklagten – nur einer von ihnen nicht."

                         "Doch was als schnelle Abstimmung geplant war, entwickelt sich zu einer hitzigen Debatte. Vorurteile, Emotionen und Zweifel kommen ans Licht, als nach und nach jedes Argument hinterfragt wird. Was bedeutet Gerechtigkeit wirklich? Wie sicher kann sich jemand seiner Meinung sein? Und welche Rolle spielen persönliche Erfahrungen in einer vermeintlich objektiven Entscheidung?"

                         "Die Neuverfilmung des Klassikers 12 Angry Men setzt auf eine moderne Inszenierung und gesellschaftlich relevante Themen. Friedrich Müller übernimmt dabei eine Schlüsselrolle, die das Spannungsverhältnis innerhalb der Gruppe auf neue Weise beleuchtet."

                         "\nInsgesamt max. 15 Punkte"
                         "\nВсего за оба кейса: 25 баллов")
    def return2():
        root.deiconify()
        third_window.withdraw()
    but11=Button(third_window, text='Домой', command=return2)
    but11.pack()
button_n=Button(root, text='Задания по немецкому языку', command=window3)
button_n.pack()
def window4():
    root.withdraw()
    forth_window = Toplevel(root)
    forth_window.protocol("WM_DELETE_WINDOW", root.destroy)
    forth_window.title("Задания по английскому языку")
    forth_window.geometry('1000x1300')
    editor = Text(forth_window)
    editor.pack(fill=BOTH, expand=True)
    editor.insert("1.0", "Задания по английскому от Антонова Даниила \nАнглийский язык. 20 вопрос – 10 вариантов."
"________________________________________"
"\nВопрос 20 (15 баллов). Var1"
"\nA book description (score points – 15)"
"\nYou need to write a book description for a bookstore website."
"The book is 'To Kill a Mockingbird' by Harper Lee (1960). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"\nThe plot summary:"
"\nThe novel is set in the American South during the 1930s and follows young Scout Finch as she navigates childhood, learning about justice, morality, and race through the trial of Tom Robinson, a Black man falsely accused of assaulting a white woman. Her father, Atticus Finch, a lawyer, defends Robinson despite facing hostility from the town. The story also explores the mysterious figure of Boo Radley, a reclusive neighbor. Through Scout’s eyes, the reader witnesses the deeply ingrained prejudice in society and the power of empathy and understanding."
"\n________________________________________"
"\nVar2"
"\nA book description (score points – 15)"
"\nYou need to write a book description for a bookstore website."
"\nThe book is '1984' by George Orwell (1949). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"The plot summary:"
"\nSet in a dystopian future, the novel follows Winston Smith, a citizen of Oceania, where the Party, led by Big Brother, exercises total control over society. Winston secretly despises the Party and begins a rebellious love affair with Julia. However, their defiance is short-lived as they are caught by the Thought Police and subjected to brutal re-education. The novel explores themes of totalitarianism, surveillance, and the fragility of truth in a world where history is constantly rewritten."
"\n________________________________________"
"\nVar3"
"\nA book description (score points – 15)"
"\nYou need to write a book description for a bookstore website."
"\nThe book is 'Pride and Prejudice' by Jane Austen (1813). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"\nThe plot summary:"
"\nElizabeth Bennet, a witty and independent young woman, meets the seemingly arrogant Mr. Darcy. Despite their initial clashes, their relationship develops through misunderstandings, personal growth, and moments of revelation. Meanwhile, Elizabeth’s family faces various social challenges and romantic entanglements. As Elizabeth learns more about Darcy’s true character, she realizes that first impressions can be misleading. The novel is a timeless exploration of love, class, and self-discovery."
"\n________________________________________"
"\nVar4"
"\nA book description (score points – 15)"
"\nYou need to write a book description for a bookstore website."
"\nThe book is 'Frankenstein' by Mary Shelley (1818). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"\nThe plot summary:"
"\nVictor Frankenstein, a young scientist, becomes obsessed with creating life. He succeeds in animating a creature from dead body parts, but is horrified by the result and abandons it. The monster, rejected by society, seeks revenge on its creator, leading to a tragic pursuit that spans continents. The novel delves into themes of ambition, responsibility, and the consequences of playing God."
"\n________________________________________"
"\nVar5"
"\nYou need to write a book description for a bookstore website."
"\nThe book is 'The Great Gatsby' by F. Scott Fitzgerald (1925). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"\nThe plot summary:"
"\nNick Carraway, a young bond salesman, moves to West Egg, where he meets the enigmatic Jay Gatsby, a millionaire known for his lavish parties. Gatsby is in love with Daisy Buchanan, Nick’s cousin, whom he met years ago. As Gatsby rekindles his romance with Daisy, secrets unfold, revealing the hollow nature of wealth and the American Dream. Tragedy follows, leaving Nick disillusioned with the world of privilege and excess."
"\n________________________________________"
"\nVar6"
"\nA book description (score points – 15)"
"\nYou need to write a book description for a bookstore website."
"\nThe book is 'Jane Eyre' by Charlotte Brontë (1847). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"\nThe plot summary:"
"\nJane Eyre, an orphan raised by a cruel aunt, finds independence as a governess at Thornfield Hall, where she falls in love with the mysterious Mr. Rochester. Their love story is tested when Jane uncovers Rochester’s dark secret—a wife hidden in the attic. Jane chooses self-respect over passion and leaves, only to find love again under different circumstances. The novel explores themes of love, morality, and female independence."
"\n________________________________________"
"\nVar7"
"\nA book description (score points – 15)"
"\nYou need to write a book description for a bookstore website."
"\nThe book is 'Brave New World' by Aldous Huxley (1932). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"\nThe plot summary:"
"\nIn a technologically advanced future, society is engineered for stability and pleasure, with citizens conditioned to accept their roles. Bernard Marx, an outsider, questions the system and brings back John, a 'Savage' raised outside this world. John struggles with the superficiality of this utopia, leading to tragic consequences. The novel critiques consumerism, control, and the loss of individuality."
"\n________________________________________"
"\nVar8"
"\nA book description (score points – 15)"
"\nYou need to write a book description for a bookstore website."
"\nThe book is 'Crime and Punishment' by Fyodor Dostoevsky (1866). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"\nThe plot summary:"
"\nRodion Raskolnikov, a destitute student in St. Petersburg, commits murder, believing himself to be above moral law. As guilt consumes him, he faces a psychological and spiritual crisis. Detective Porfiry Petrovich suspects him, while Sonya, a kind-hearted prostitute, urges him to confess. The novel explores redemption, morality, and the torment of a guilty conscience."
"\n________________________________________"
"\nVar9"
"\nA book description (score points – 15)"
"\nYou need to write a book description for a bookstore website."
"\nThe book is 'Moby-Dick' by Herman Melville (1851). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"\nThe plot summary:"
"\nIshmael, a sailor, joins the whaling ship Pequod, led by the obsessed Captain Ahab, who seeks revenge on Moby Dick, the white whale that took his leg. As the crew ventures into the sea, the pursuit turns into a symbolic struggle between man, nature, and fate. The novel is a deep exploration of obsession, vengeance, and existential questions."
"\n________________________________________"
"\nVar10"
"\nYou need to write a book description for a bookstore website."
"\nThe book is 'Lord of the Flies' by William Golding (1954). A plot summary of the book is given below. In your description, evaluate the book to urge the reader to buy it. You should define the genre of the book, the target audience, and tailor the style of your synopsis to the intended audience. You may use some key words from the assignment, but your description should not be reduced to a plot summary of the book (min. 150 words)."
"\nThe plot summary:"
"\nA group of British schoolboys crash-land on an uninhabited island and attempt to govern themselves. Initially, order prevails, but soon, fear and power struggles lead to chaos. Ralph and Piggy represent civilization, while Jack and his hunters embrace savagery. As morality collapses, the boys descend into violence, revealing the dark nature of humanity. The novel is an allegory of society, leadership, and the fragility of civilization."
"\n________________________________________"
"\nЗадания по английскому от Мохамеда"
"\nVar1"
"\nText 1: The Power of Language"
"\nText:"
"\nLanguage is one of the most powerful tools humans possess. It allows us to communicate complex ideas, share emotions, and build relationships. Through language, we can preserve history, create art, and advance science. However, language is not just a means of communication; it also shapes our thoughts and perceptions. The words we use can influence how we see the world and how others see us. For example, the way we describe events can affect our memory of them. Language is not static; it evolves over time, reflecting changes in society and culture. Understanding the power of language is essential for effective communication and critical thinking."
"\nQuestions:"
"\n1) What is one of the most powerful tools humans possess?"
"\n2)How does language shape our thoughts and perceptions?"
"\n3) What can the way we describe events affect?"
"\n4) How does language evolve over time?"
"\n5) Why is understanding the power of language important?"
"\nAnswers:"
"\n1) Language is one of the most powerful tools humans possess."
"\n2) Language shapes our thoughts and perceptions by influencing how we see the world."
"\n3) The way we describe events can affect our memory of them."
"\n4) Language evolves over time, reflecting changes in society and culture."
"\n5) Understanding the power of language is essential for effective communication and critical thinking."

"\nText 2: The Role of Technology in Education"
"\nText:"
"\nTechnology has revolutionized the field of education. With the advent of computers, the internet, and mobile devices, students now have access to a wealth of information at their fingertips. Online learning platforms and educational apps have made it possible for people to learn at their own pace and from anywhere in the world. However, the integration of technology in education also presents challenges. Not all students have equal access to digital resources, and there is a risk of over-reliance on technology, which can hinder critical thinking and problem-solving skills. Despite these challenges, technology has the potential to make education more inclusive and personalized."
"\nQuestions:"
"\n1) How has technology revolutionized education?"
"\n2) What have online learning platforms and educational apps made possible?"
"\n3) What are two challenges of integrating technology in education?"
"\n4) What is a potential risk of over-reliance on technology?"
"\n5) What potential does technology have in education?"
"\nAnswers:"
"\n1) Technology has revolutionized education by providing access to a wealth of information and new learning tools."
"\n2) Online learning platforms and educational apps have made it possible for people to learn at their own pace and from anywhere in the world."
"\n3) Challenges include unequal access to digital resources and the risk of over-reliance on technology."
"\n4) Over-reliance on technology can hinder critical thinking and problem-solving skills."
"\n5) Technology has the potential to make education more inclusive and personalized."
"\nText 3: The Importance of Biodiversity"
"\nText:"
"\nBiodiversity refers to the variety of life on Earth, including all species of plants, animals, and microorganisms. It is essential for the health of ecosystems and the survival of humanity. Biodiversity provides us with food, medicine, and raw materials. It also plays a crucial role in regulating the climate, purifying water, and pollinating crops. However, biodiversity is under threat due to human activities such as deforestation, pollution, and climate change. The loss of biodiversity can have severe consequences, including the collapse of ecosystems and the loss of vital resources. Protecting biodiversity is therefore a global priority."
"\nQuestions:"
"\n1) What does biodiversity refer to?"
"\n2) Why is biodiversity essential for humanity?"
"\n3) What are three benefits of biodiversity?"
"\n4) What are two threats to biodiversity?"
"\n5) Why is protecting biodiversity a global priority?"
"\nAnswers:"
"\n1) Biodiversity refers to the variety of life on Earth, including all species of plants, animals, and microorganisms."
"\n2) Biodiversity is essential for the health of ecosystems and the survival of humanity."
"\n3) Biodiversity provides food, medicine, and raw materials, regulates the climate, purifies water, and pollinates crops."
"\nThreats to biodiversity include deforestation, pollution, and climate change."
"\nProtecting biodiversity is a global priority because its loss can lead to the collapse of ecosystems and the loss of vital resources."
"\nText 4: The Role of Art in Society"
"\nText:"
"\nArt has always played a significant role in society, serving as a medium for expression, communication, and reflection. It allows individuals and communities to convey their emotions, beliefs, and experiences. Art can also challenge societal norms and provoke thought, leading to social change. Throughout history, art has been used to document events, celebrate cultural heritage, and inspire innovation. Despite its importance, art is often undervalued in modern society, with funding for the arts frequently being cut. Recognizing the value of art is essential for fostering creativity and preserving cultural identity."
"\nQuestions:"
"\n1) What role does art play in society"
"\n2) How can art lead to social change?"
"\n3) What are three historical uses of art?"
"\n4) What is a current challenge facing the arts?"
"\n5) Why is recognizing the value of art important?"
"\nAnswers:"
"\n1) Art serves as a medium for expression, communication, and reflection."
"\n2) Art can challenge societal norms and provoke thought, leading to social change."
"\n3) Art has been used to document events, celebrate cultural heritage, and inspire innovation."
"\n4) A current challenge is the frequent cutting of funding for the arts."
"\n5) Recognizing the value of art is important for fostering creativity and preserving cultural identity."

"\nText 5: The Evolution of Human Rights"
"\nText:"
"\nThe concept of human rights has evolved over centuries. Initially, rights were often tied to social status and privilege. The Enlightenment era marked a turning point, with philosophers advocating for the inherent rights of all individuals. The Universal Declaration of Human Rights, adopted by the United Nations in 1948, established a global standard for human rights. Despite this progress, human rights violations persist in many parts of the world. Issues such as discrimination, inequality, and political oppression continue to challenge the realization of universal human rights. The fight for human rights is ongoing and requires global cooperation and vigilance."
"\nQuestions:"
"\n1) How has the concept of human rights evolved?"
"\n2) What marked a turning point in the concept of human rights?"
"\n3) What did the Universal Declaration of Human Rights establish?"
"\n4) What are two ongoing challenges to human rights?"
"\n5) What is required to fight for human rights?"
"\nAnswers:"
"\n1) The concept of human rights has evolved from being tied to social status to being recognized as inherent to all individuals."
"\n2) The Enlightenment era marked a turning point in the concept of human rights."
"\nThe Universal Declaration of Human Rights established a global standard for human rights."
"\nOngoing challenges include discrimination, inequality, and political oppression."
"\nThe fight for human rights requires global cooperation and vigilance."

"\nText 6: The Impact of Globalization"
"\nText:"
"\nGlobalization refers to the increasing interconnectedness of the world's economies, cultures, and populations. It has been driven by advances in technology, transportation, and communication. Globalization has led to the spread of ideas, goods, and services across borders, fostering economic growth and cultural exchange. However, it has also resulted in challenges such as economic inequality, cultural homogenization, and environmental degradation. The benefits and drawbacks of globalization are complex and multifaceted, requiring careful consideration and management to ensure that its positive aspects are maximized while minimizing its negative impacts."
"\nQuestions:"
"\nWhat does globalization refer to?"
"\nWhat has driven globalization?"
"\nWhat are two positive effects of globalization?"
"\nWhat are two challenges associated with globalization?"
"\nWhat is required to manage the impacts of globalization?"
"\nAnswers:"
"\nGlobalization refers to the increasing interconnectedness of the world's economies, cultures, and populations."
"\nGlobalization has been driven by advances in technology, transportation, and communication."
"\nPositive effects include economic growth and cultural exchange."
"\nChallenges include economic inequality, cultural homogenization, and environmental degradation."
"\nManaging the impacts of globalization requires careful consideration to maximize benefits and minimize negative impacts."
"\nText 7: The Future of Artificial Intelligence"
"\nText:"
"\nArtificial intelligence (AI) is rapidly transforming various aspects of society, from healthcare and education to transportation and entertainment. AI systems can analyze vast amounts of data, make predictions, and perform tasks that were once thought to require human intelligence. While AI has the potential to improve efficiency and solve complex problems, it also raises ethical concerns. Issues such as job displacement, privacy, and bias in AI algorithms need to be addressed. The future of AI will depend on how society navigates these challenges and ensures that AI is developed and used responsibly."
"\nQuestions:"
"\nWhat is artificial intelligence transforming?"
"\nWhat can AI systems do?"
"\nWhat are two potential benefits of AI?"
"\nWhat are two ethical concerns related to AI?"
"\nWhat will the future of AI depend on?"
"\nAnswers:"
"\nAI is transforming healthcare, education, transportation, and entertainment."
"\nAI systems can analyze data, make predictions, and perform complex tasks."
"\nPotential benefits include improved efficiency and solving complex problems."
"\nEthical concerns include job displacement, privacy, and bias in AI algorithms."
"\nThe future of AI will depend on how society addresses challenges and ensures responsible development and use.")
    def return3():
        root.deiconify()
        forth_window.withdraw()
    but12=Button(forth_window, text='Домой', command=return3)
    but12.pack()
button_e = Button(root, text='Задания по английскому языку', command=window4)
#button_e.config(bg='pink', fg='blue')
button_e.pack()
def window5():
    root.withdraw()
    fifth_window = Toplevel(root)
    fifth_window.protocol("WM_DELETE_WINDOW", root.destroy)
    fifth_window.title("Лингвистические задачи")
    fifth_window.geometry('300x300')
    # editor = Text(fifth_window)
    # editor.pack(fill=BOTH)
    # editor.insert("1.0", "\nЛингвистические задачи"
    #               "\nБольше задач - на Сириус.Курсах")
    def syntax():
        fifth_window.withdraw()
        sixth_window=Toplevel(fifth_window)
        sixth_window.protocol("WM_DELETE_WINDOW", fifth_window.destroy)
        sixth_window.title("Задачи по синтаксису")
        sixth_window.geometry('1000x1300')
        canvas = Canvas(sixth_window)
        frame = Frame(canvas)  # , padx=10, pady=10)
        # frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = Scrollbar(sixth_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")

        canvas.pack(fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        # editor = Text(sixth_window)
        # editor.pack(fill=BOTH)
        # editor.insert("1.0", "\nДля решения задач потребуется знание основных понятий синтаксиса, синтаксической типологии, а также умение находить универсалии, связанные с порядком слов")
        task21 = Label(frame,
                       text="При вводе ответов точку в конце не ставьте, пожалуйста!!!"
                       "\nЗадание 1 (Посвящено теме 'Залог и актантная деривация')"
                       "Примечание: Арчинский язык относится к лезгинской группе нахско-дагестанской (северокавказской) языковой семьи."
                       "\nДаны предложения на арчинском языке и их переводы на русский язык в перепутанном порядке:"
"\nПредложения на арчинском языке: "
"\nХоӀн бэркурши би"
"\nХоӀн хьоти аркьарши би"
"\nЛому хоӀн бирккурши би"
"\nЛо дорцирши ди"
"\nБошор шуша ирккурши ви"
"\nБуваму бошор варкьарши ви"
"\nБува доги бирккурши ди"
"\nШуша ирккурши и"
"\nПредложения на русском языке:"
"\nДевочка стоит."
"\nКорова падает."
"\nБутылку разыскивают."
"\nМужчина разыскивает бутылку."
"\nМать разыскивает осла."
"\nКорова разыскивается мальчиком."
"\nМужчина оставляется матерью."
"\nКорова оставляет траву."
"\nЗадание 1. Установите верные соответствия")
        task21.pack(fill=BOTH)
        task21_11=Label(frame, text='Следующие 8 предложений переведите на русский язык'
                       "\nПредложение 1. ХоӀн бэркурши би")
        task21_11.pack(fill=BOTH)
        task21_1 = Entry(frame, width=40)
        task21_1.pack()

        def check18():
            if task21_1.get().lower() == 'корова падает':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 1!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but19 = Button(frame, text='Проверить задачу 1 задания 1 по синтаксису', command=check18)
        but19.pack()
        task21_12=Label(frame, text='\nПредложение 2. ХоӀн хьоти аркьарши би')
        task21_12.pack()
        task21_2=Entry(frame, width=40)
        task21_2.pack()
        def check19():
            if task21_2.get().lower() == 'корова оставляет траву':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_2.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 2!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but20 = Button(frame, text='Проверить задачу 2 задания 1 по синтаксису', command=check19)
        but20.pack()

        task21_13 = Label(frame, text='\nПредложение 3. Лому хоӀн бирккурши би')
        task21_13.pack()
        task21_3 = Entry(frame, width=40)
        task21_3.pack()

        def check20():
            if task21_3.get().lower() == 'корова разыскивается мальчиком':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_3.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 3!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but21 = Button(frame, text='Проверить задачу 3 задания 1 по синтаксису', command=check20)
        but21.pack()

        task21_14 = Label(frame, text='\nПредложение 4. Ло дорцирши ди')
        task21_14.pack()
        task21_4 = Entry(frame, width=40)
        task21_4.pack()

        def check21():
            if task21_4.get().lower() == 'девочка спит':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_4.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 4!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but22 = Button(frame, text='Проверить задачу 4 задания 1 по синтаксису', command=check21)
        but22.pack()

        task21_15 = Label(frame, text='\nПредложение 5. Бошор шуша ирккурши ви')
        task21_15.pack()
        task21_5= Entry(frame, width=40)
        task21_5.pack()

        def check22():
            if task21_5.get().lower() == 'мужчина разыскивает бутылку':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_5.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 5!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but23 = Button(frame, text='Проверить задачу 5 задания 1 по синтаксису', command=check22)
        but23.pack()

        task21_16 = Label(frame, text='\nПредложение 6. Буваму бошор варкьарши ви')
        task21_16.pack()
        task21_6 = Entry(frame, width=40)
        task21_6.pack()

        def check23():
            if task21_6.get().lower() == 'мужчина оставляется матерью':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_6.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 6!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but24 = Button(frame, text='Проверить задачу 6 задания 1 по синтаксису', command=check23)
        but24.pack()

        task21_17 = Label(frame, text='\nПредложение 7. Бува доги бирккурши ди')
        task21_17.pack()
        task21_7 = Entry(frame, width=40)
        task21_7.pack()

        def check24():
            if task21_7.get().lower() == 'мать разыскивает осла':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_7.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 6!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but25 = Button(frame, text='Проверить задачу 7 задания 1 по синтаксису', command=check24)
        but25.pack()

        task21_18 = Label(frame, text='\nПредложение 8. Шуша ирккурши и')
        task21_18.pack()
        task21_8 = Entry(frame, width=40)
        task21_8.pack()

        def check25():
            if task21_8.get().lower() == 'бутылку разыскивают':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_8.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 6!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but26 = Button(frame, text='Проверить задачу 8 задания 1 по синтаксису', command=check25)
        but26.pack()

        task21_19 = Label(frame, text='\nСледующие 4 предложения переведите на арчинский язык. ПРИ ВВОДЕ ОТВЕТОВ ЗАМЕНЯЙТЕ "I" НА "i"'
                                      '\nПредложение 1. Осёл оставляет корову.')
        task21_19.pack()
        task21_9 = Entry(frame, width=40)
        task21_9.pack()

        def check26():
            if task21_9.get().lower() == 'доги хоiн баркьарши би':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_9.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 1!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but27 = Button(frame, text='Проверить задачу 1 задания 1 второго подзадания по синтаксису', command=check26)
        but27.pack()

        task21_20 = Label(frame,
                          text='\nПредложение 2. Бутылка падает.')
        task21_20.pack()
        task21_10 = Entry(frame, width=40)
        task21_10.pack()

        def check27():
            if task21_10.get().lower() == 'шуша эркурши и':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_10.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 1!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but28 = Button(frame, text='Проверить задачу 2 задания 1 второго подзадания по синтаксису',
                       command=check27)
        but28.pack()

        task21_21 = Label(frame,
                          text='\nПредложение 3. Мужчина стоит.')
        task21_21.pack()
        task21_11 = Entry(frame, width=40)
        task21_11.pack()

        def check28():
            if task21_11.get().lower() == 'бошор ворцирши ви':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_11.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 1!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but29 = Button(frame, text='Проверить задачу 3 задания 1 второго подзадания по синтаксису',
                       command=check28)
        but29.pack()

        task21_22 = Label(frame,
                          text='\nПредложение 4. Мальчика оставляют.')
        task21_22.pack()
        task21_12 = Entry(frame, width=40)
        task21_12.pack()

        def check29():
            if task21_12.get().lower() == 'ло варкьарши ви':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task21_12.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 1!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but30 = Button(frame, text='Проверить задачу 4 задания 1 второго подзадания по синтаксису',
                       command=check29)
        but30.pack()

        #сюда еще добавить 3 задания
        task22 = Label(frame,
                       text="\nЗадание 2 (Посвящено теме 'Порядок слов'). Похожее задание была на отборочном этапе в этом году"
                            "Примечание: Язык унуа относится к малайско-полинезийской ветви австронезийской семьи языков."
                            "\nАррес герим -  5 человек, аррес гетер нгаре – эти 3 человека, кури гевеч – 4 собаки, роббурет нге – эта книга, \nроббурет гетер нгараг – те три книги, роббурет геру – 2 книги, рруборум нгараг – те дети, рруборум нге – этот ребенок, \nвиндуту нге рару – эти 2 девушки, виндуту гевеч нгараг – те 4 девушки, горгор нге рару – эти 2 закона, горгор геру – 2 закона"
                            "\nПереведите следующие 4 словосочетания с языка унуа на русский. \nСловосочетание 1. кури нгаг")
        task22.pack(fill=BOTH)
        task22_1 = Entry(frame, width=40)
        task22_1.pack()

        def check30():
            if task22_1.get().lower() == 'та собака':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task22_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 1!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but33 = Button(frame, text='Проверить задачу 1 задания 2 по синтаксису', command=check30)
        but33.pack()

        task23 = Label(frame,
                       text="\nСловосочетание 2. горгор гевеч нгараг")
        task23.pack(fill=BOTH)
        task23_1 = Entry(frame, width=40)
        task23_1.pack()

        def check31():
            if task23_1.get().lower() == 'те 4 закона' or task23_1.get().lower() == 'те четыре закона':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task23_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 2!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but34 = Button(frame, text='Проверить задачу 2 задания 2 по синтаксису', command=check31)
        but34.pack()

        task24 = Label(frame,
                       text="\nСловосочетание 3. виндуту геру")
        task24.pack(fill=BOTH)
        task24_1 = Entry(frame, width=40)
        task24_1.pack()

        def check32():
            if task24_1.get().lower() == '2 девушки' or task24_1.get().lower() == 'две девушки':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task24_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 3!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but35 = Button(frame, text='Проверить задачу 3 задания 2 по синтаксису', command=check32)
        but35.pack()

        task25 = Label(frame,
                       text="\nСловосочетание 4. рруборум нгаре")
        task25.pack(fill=BOTH)
        task25_1 = Entry(frame, width=40)
        task25_1.pack()

        def check33():
            if task25_1.get().lower() == 'эти дети':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task25_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 4!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but36 = Button(frame, text='Проверить задачу 4 задания 2 по синтаксису', command=check33)
        but36.pack()

        task26 = Label(frame,
                       text="\nЗадание 3. 'Переходность'"
                       "\nДаны предложения на юкатекском языке (из семьи языков майя) и рядом их переводы на русский:"
                            "\nJ aajech ti' k'áax.	Ты проснулся в лесу."
"\nJ aajen ti' k'áax.	Я проснулся в лесу."
"\nKa wajsiken ti' k'áax.	Ты будишь меня в лесу."
"\nKin waajal ti' k'áax.	Я просыпаюсь в лесу."
"\nKu yaajal ti' k'áax.	Он просыпается в лесу."
"\nTa wajsaj ti' k'áax.	Ты разбудил его в лесу."
"\nTu yajsajen ti' k'áax.	Он разбудил меня в лесу."
                            "\nВыполните задания"
                            "\nЗадача 1. Переведите на русский язык: J aaj ti' k'áax.")
        task26.pack(fill=BOTH)
        task26_1 = Entry(frame, width=40)
        task26_1.pack()

        def check34():
            if task26_1.get().lower() == 'он проснулся в лесу':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task26_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 1!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but37 = Button(frame, text='Проверить задачу 1 задания 3 по синтаксису', command=check34)
        but37.pack()

        task27 = Label(frame,
                       text="\nЗадача 2. Переведите на русский язык: Kin wajsik ti' k'áax.")
        task27.pack(fill=BOTH)
        task27_1 = Entry(frame, width=40)
        task27_1.pack()

        def check35():
            if task27_1.get().lower() == 'я бужу его в лесу':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task27_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 2!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but38 = Button(frame, text='Проверить задачу 2 задания 3 по синтаксису', command=check35)
        but38.pack()

        task28 = Label(frame,
                       text="\nЗадача 3. Переведите на русский язык: Ku yajsik ti' k'áax.")
        task28.pack(fill=BOTH)
        task28_1 = Entry(frame, width=40)
        task28_1.pack()

        def check36():
            if task28_1.get().lower() == 'он будит его в лесу':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task28_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 3!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but39 = Button(frame, text='Проверить задачу 3 задания 3 по синтаксису', command=check36)
        but39.pack()

        task29 = Label(frame,
                       text="\nЗадача 4. Переведите на русский язык: Ta wajsajen ti' k'áax.")
        task29.pack(fill=BOTH)
        task29_1 = Entry(frame, width=40)
        task29_1.pack()

        def check37():
            if task29_1.get().lower() == 'ты разбудил меня в лесу':
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task29_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 4!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but40 = Button(frame, text='Проверить задачу 4 задания 3 по синтаксису', command=check37)
        but40.pack()

        task30 = Label(frame,
                       text="\nЗадача 5. Переведите на юкатекский язык: Он разбудил его в лесу.")
        task30.pack(fill=BOTH)
        task30_1 = Entry(frame, width=40)
        task30_1.pack()

        def check38():
            if task30_1.get().lower() == "tu yajsaj ti' k'áax" or task30_1.get().lower() == "tu yajsaj ti' k'aax":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task30_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 5!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but41 = Button(frame, text='Проверить задачу 5 задания 3 по синтаксису', command=check38)
        but41.pack()

        task31 = Label(frame,
                       text="\nЗадача 6. Переведите на юкатекский язык: Ты просыпаешься в лесу.")
        task31.pack(fill=BOTH)
        task31_1 = Entry(frame, width=40)
        task31_1.pack()

        def check39():
            if task31_1.get().lower() == "ka waajal ti' k'áax" or task31_1.get().lower() == "ka waajal ti' k'aax":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task31_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 6!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but42 = Button(frame, text='Проверить задачу 6 задания 3 по синтаксису', command=check39)
        but42.pack()

        task32 = Label(frame,
                       text="\nЗадача 7. Переведите на юкатекский язык: Я разбудил тебя в лесу.")
        task32.pack(fill=BOTH)
        task32_1 = Entry(frame, width=40)
        task32_1.pack()

        def check40():
            if task32_1.get().lower() == "tin wajsajech ti' k'áax" or task32_1.get().lower() == "tin wajsajech ti' k'aax":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task32_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на задачу 6!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but43 = Button(frame, text='Проверить задачу 7 задания 3 по синтаксису', command=check40)
        but43.pack()

        task33 = Label(frame,
                       text="\nЗадание 4. Согласование с одним аргументом. \nДаны предложения на языке навахо и их переводы на русский язык:"
                       "\nnímasii siˀą́	Картофелина лежит."
"\nJáan k’aaˀ yistą́	Джон держит стрелу."
"\nbis sitłééˀ	Глина лежит."
"\nk’aaˀ sinil	Стрелы лежат."
"\nJáan sitį́	Джон лежит."
"\nJáan ˀawééˀ yistį́	Джон держит ребёнка."
"\ntł’iish sitį́	Змея лежит."
"\nJáan tsitł’éłí yisnil	Джон держит спички."
"\nJáan jooł yisˀą́	Джон держит мяч."
"\nˀawééˀ ˀat’aˀ yistą́	Ребёнок держит перо."
"\nJáan nímasii yistłééˀ	Джон держит картофельное пюре."
"\nJáan tł’iish yisnil	Джон держит змей."
"\njooł sinil	Мячи лежат."
"\nУказание: При вводе ответов вы можете заменять ł на l и ˀ на ?, а также опускать над- и подстрочные знаки."
"\nПримечание: Навахо — один из языков североамериканских индейцев. На нём говорит около 170 тыс. человек."
"\nЗадача 1. Ответьте на вопросы."
"\nВопрос 1: Сколько разных согласовательных показателей на глаголе встречается в данных предложениях?")
        task33.pack(fill=BOTH)
        task33_1 = Entry(frame, width=40)
        task33_1.pack()

        def check42():
            if task33_1.get().lower() == "5" or task33_1.get().lower() == "пять":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task33_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответы на первый вопрос!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but44 = Button(frame, text='Проверить вопрос 1 задачи 1 задания 4 по синтаксису', command=check42)
        but44.pack()

        task34 = Label(frame, text="\nВопрос 2. С чем согласуется переходный глагол? Ответ - одно сущ. в И. п.")
        task34.pack(fill=BOTH)
        task34_1 = Entry(frame, width=40)
        task34_1.pack()

        def check43():
            if task34_1.get().lower() == "дополнение":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task34_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ на второй вопрос!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but45 = Button(frame, text='Проверить вопрос 2 задачи 1 задания 4 по синтаксису', command=check43)
        but45.pack()

        task35 = Label(frame, text="\nВопрос 3. Для языков какого строя характерен такой тип согласования? Ответ - одно прил. в И. п.")
        task35.pack(fill=BOTH)
        task35_1 = Entry(frame, width=40)
        task35_1.pack()

        def check44():
            if task35_1.get().lower() == "эргативно-абсолютивный":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task35_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ на третий вопрос!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but46 = Button(frame, text='Проверить вопрос 3 задачи 1 задания 4 по синтаксису', command=check44)
        but46.pack()

        task36 = Label(frame,
                       text="\nЗадание 2. Переведите на язык навахо следующие 4 предложения"
                            "\nДжон держит ягоды.")
        task36.pack(fill=BOTH)
        task36_1 = Entry(frame, width=40)
        task36_1.pack()

        def check45():
            if task36_1.get().lower() == "jaan didze yisnil":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task36_1.get() == '':
                messagebox.showwarning("Предупреждение", "Переведите первое предложение!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but47 = Button(frame, text='Проверить первое предложение', command=check45)
        but47.pack()

        task37 = Label(frame,
                       text="\nСпичка лежит.")
        task37.pack(fill=BOTH)
        task37_1 = Entry(frame, width=40)
        task37_1.pack()

        def check46():
            if task37_1.get().lower() == "tsitleli sita":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task37_1.get() == '':
                messagebox.showwarning("Предупреждение", "Переведите второе предложение!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but48 = Button(frame, text='Проверить второе предложение', command=check46)
        but48.pack()

        task38 = Label(frame,
                       text="\nРебёнок держит змею.")
        task38.pack(fill=BOTH)
        task38_1 = Entry(frame, width=40)
        task38_1.pack()

        def check47():
            if task38_1.get().lower() == "?awee? tliish yisti":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task38_1.get() == '':
                messagebox.showwarning("Предупреждение", "Переведите третье предложение!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but48 = Button(frame, text='Проверить третье предложение', command=check47)
        but48.pack()

        task39 = Label(frame,
                       text="\nДжон держит варенье из ягод.")
        task39.pack(fill=BOTH)
        task39_1 = Entry(frame, width=40)
        task39_1.pack()

        def check48():
            if task39_1.get().lower() == "jaan didze yistlee?":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task39_1.get() == '':
                messagebox.showwarning("Предупреждение", "Переведите четвертое предложение!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but49 = Button(frame, text='Проверить четвёртое предложение', command=check48)
        but49.pack()

        task40 = Label(frame,
                      text="\nЗадание 5. Синтаксическая типология. \nОпределите строй языков ниже, выбрав подходящее прилагательное в И.п.:\nактивно-стативный, эргативно-абсолютивный, номинативно-аккузативный"
                           "\nПервый пример: "
                           "\nʢu	uzulri"
"\nты	работаешь"	

"\nʢu-ni	ʒuz	buTʆulri"
"\nты	книгу	читаешь")
        task40.pack(fill=BOTH)
        task40_1 = Entry(frame, width=40)
        task40_1.pack()

        def check49():
            if task40_1.get().lower() == "эргативно-абсолютивный":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task40_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but50 = Button(frame, text='Проверить первый пример', command=check49)
        but50.pack()

        task41 = Label(frame,
                       text="\nPutn-s	lidoja.	"
"птица	летит"	

"\nBērn-s	zīmē	putn-u."
"\nребёнок	рисует	птица"

"\nBērn-s	guļ."
"\nребёнок	спит")
        task41.pack(fill=BOTH)
        task41_1 = Entry(frame, width=40)
        task41_1.pack()

        def check50():
            if task41_1.get().lower() == "номинативно-аккузативный":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task41_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but51 = Button(frame, text='Проверить второй пример', command=check50)
        but51.pack()

        task42 = Label(frame,
                       text="\nokolcá	hóhca-li-halpí:s"
"\nколодец	копать-я-могу"
"\n‘Я могу копать колодец’"

"\ntálwa-li-mp"
"\nпою-я-говорит"
"\n‘Он говорит, что я пою’"

"\nca-pa:batáplit"
"\nменя-ударил по спине"
"\n‘Он меня ударил по спине’"

"\nca-o:wíllilahoV̦"
"\nя-утону")
        task42.pack(fill=BOTH)
        task42_1 = Entry(frame, width=40)
        task42_1.pack()

        def check51():
            if task42_1.get().lower() == "активно-стативный":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task42_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but51 = Button(frame, text='Проверить третий пример', command=check51)
        but51.pack()

        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        def return5():
            fifth_window.deiconify()
            sixth_window.withdraw()
        but31=Button(sixth_window, text='Вернуться назад к блоку лингвистических задач',
                       command=return5)
        but31.pack()
        def return6():
            root.deiconify()
            sixth_window.withdraw()
        but32=Button(sixth_window, text='Домой',
                       command=return6)
        but32.pack()
    but17=Button(fifth_window, text='Синтаксис', command=syntax)
    but17.pack()
    def morphology():
        fifth_window.withdraw()
        seventh_window = Toplevel(fifth_window)
        seventh_window.protocol("WM_DELETE_WINDOW", fifth_window.destroy)
        seventh_window.title("Задачи по морфологии")
        seventh_window.geometry('1000x1300')
        canvas = Canvas(seventh_window)
        frame = Frame(canvas)  # , padx=10, pady=10)
        # frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = Scrollbar(seventh_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")

        canvas.pack(fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        # editor = Text(sixth_window)
        # editor.pack(fill=BOTH)
        # editor.insert("1.0", "\nДля решения задач потребуется знание основных понятий синтаксиса, синтаксической типологии, а также умение находить универсалии, связанные с порядком слов")
        task31 = Label(frame,
                       text="\nРаздел 2. Морфология"
        "\nЗадание 1. Тема – «Морфологические типы языков»"
        "\nДаны предложения на языке яки и их переводы на русский язык:"
        "\nPeo bwana. Пео плачет."
"\nMaria kaba’ita jinuk. Мария купила лошадь."
"\nAurelia usim bicha. Аурелия видит детей."
"\nIban Peota bwanajikkak. Иван слышал, как Пео плакал."
"\nMaria Aureliata laabenta ponajikka.Мария слышит, как Аурелия играет на скрипке."
"\nIban Mariata ye’ebichak. Иван видел, как Мария танцевала."
"\nGoyo Mariata kaba’im etbwatebo. Гойо велит Марии украсть лошадей."
"\nPeo usita chu’uta jinutebok. Пео велел ребёнку купить собаку."
"\nAurelia Goyota ye’eroka. Аурелия обещает Гойо танцевать."
"\nСделайте задачи по языку яки. (юто-ацтекская семья языков)"
"\nЗадача 1. Переведите на русский язык: Iban laabenta pona.")
        task31.pack(fill=BOTH)
        task31_1 = Entry(frame, width=40)
        task31_1.pack()

        def check52():
            if task31_1.get().lower() == "иван играет на скрипке":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task31_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but52 = Button(frame, text='Проверить первую задачу', command=check52)
        but52.pack()

        task32 = Label(frame,
                       text="\nЗадача 2. Переведите на русский язык: Chu’u Goyota kaba’ita etbwabichak")
        task32.pack(fill=BOTH)
        task32_1 = Entry(frame, width=40)
        task32_1.pack()
        def check53():
            if task32_1.get().lower() == "собака видела, как гойо украл лошадь" or task32_1.get().lower() == "собака видела как гойо украл лошадь":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task32_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but54 = Button(frame, text='Проверить вторую задачу', command=check53)
        but54.pack()

        task33 = Label(frame,
                       text="\nЗадача 3. Переведите на русский язык: Maria Aureliata ye’etebo.")
        task33.pack(fill=BOTH)
        task33_1 = Entry(frame, width=40)
        task33_1.pack()

        def check54():
            if task33_1.get().lower() == "мария велит аурелии танцевать":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task33_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but55 = Button(frame, text='Проверить третью задачу', command=check54)
        but55.pack()

        task34 = Label(frame,
                       text="\nЗадача 4. Переведите на язык яки: Ребёнок слышит собак.")
        task34.pack(fill=BOTH)
        task34_1 = Entry(frame, width=40)
        task34_1.pack()

        def check55():
            if task34_1.get().lower() == "usi chu'um jikka":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task34_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but56 = Button(frame, text='Проверить четвертую задачу', command=check55)
        but56.pack()

        task35 = Label(frame,
                       text="\nЗадача 5. Переведите на язык яки: Аурелия танцевала.")
        task35.pack(fill=BOTH)
        task35_1 = Entry(frame, width=40)
        task35_1.pack()

        def check56():
            if task35_1.get().lower() == "aurelia ye'ek":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task35_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but57 = Button(frame, text='Проверить пятую задачу', command=check56)
        but57.pack()

        task36 = Label(frame,
                       text="\nЗадача 6. Переведите на язык яки: Гойо обещал Ивану играть на скрипке.")
        task36.pack(fill=BOTH)
        task36_1 = Entry(frame, width=40)
        task36_1.pack()

        def check57():
            if task36_1.get().lower() == "goyo ibanta laabenta ponarokak":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task36_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but58 = Button(frame, text='Проверить шестую задачу', command=check57)
        but58.pack()

        task37 = Label(frame,
                       text="\nЗадача 7 Переведите на язык яки: Лошадь видит, как Пео покупает скрипку.")
        task37.pack(fill=BOTH)
        task37_1 = Entry(frame, width=40)
        task37_1.pack()

        def check58():
            if task37_1.get().lower() == "Kaba'i Peota laabenta jinubicha":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task37_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but59 = Button(frame, text='Проверить седьмую задачу', command=check58)
        but59.pack()

        task38 = Label(frame,
                       text="\nЗадание 2. 'Типы морфем'. \nДаны слова на языке эсперанто и их переводы на русский язык:"
"\nbela - красивый, longiĝi - удлиняться, blanka - белый, malpakis - распаковал, is - был, malvarmigos - охладит, karno - плоть, parolanta - говорящий, konkordigas - примиряет, pentrita - нарисованный, leginta - прочитавший"
"\nПримечание. ĝ читается примерно как русское дж."
                       "\nПереведите на русский с эсперанто: parola.")
        task38.pack(fill=BOTH)
        task38_1 = Entry(frame, width=40)
        task38_1.pack()

        def check59():
            if task38_1.get().lower() == "устный":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task38_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but60 = Button(frame, text='Проверить первую задачау', command=check59)
        but60.pack()

        task39 = Label(frame,
                       text="\nПереведите на русский с эсперанто: konkordo.")
        task39.pack(fill=BOTH)
        task39_1 = Entry(frame, width=40)
        task39_1.pack()

        def check60():
            if task39_1.get().lower() == "мир":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task39_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but61 = Button(frame, text='Проверить вторую задачау', command=check60)
        but61.pack()

        task40 = Label(frame,
                       text="\nПереведите на русский с эсперанто: malbeliĝas.")
        task40.pack(fill=BOTH)
        task40_1 = Entry(frame, width=40)
        task40_1.pack()

        def check61():
            if task40_1.get().lower() == "дурнеет":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task40_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but62 = Button(frame, text='Проверить третью задачау', command=check61)
        but62.pack()

        task41 = Label(frame,
                       text="\nПереведите на русский с эсперанто: onta.")
        task41.pack(fill=BOTH)
        task41_1 = Entry(frame, width=40)
        task41_1.pack()

        def check62():
            if task41_1.get().lower() == "будущий":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task41_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but63 = Button(frame, text='Проверить четвертую задачу', command=check62)
        but63.pack()

        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        def return7():
            fifth_window.deiconify()
            seventh_window.withdraw()
        but64=Button(seventh_window, text='Вернуться назад к блоку лингвистических задач',
                       command=return7)
        but64.pack()
        def return8():
            root.deiconify()
            seventh_window.withdraw()
        but65=Button(seventh_window, text='Домой',
                       command=return8)
        but65.pack()

    but53 = Button(fifth_window, text='Морфология', command=morphology)
    but53.pack()

    def fonetics():
        fifth_window.withdraw()
        eighth_window = Toplevel(fifth_window)
        eighth_window.protocol("WM_DELETE_WINDOW", fifth_window.destroy)
        eighth_window.title("Задачи по фонетике")
        eighth_window.geometry('1000x1300')
        canvas = Canvas(eighth_window)
        frame = Frame(canvas)  # , padx=10, pady=10)
        # frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = Scrollbar(eighth_window, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")

        canvas.pack(fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        task42=Label(frame, text="В этом разделе представлены ознакомительные задачи по фонетике. Больше задач - Сириус.Курсы по фонетике. \nЗадание 1. Гласные"
                     "\nДаны турецкие слова, приблизительная запись их произношения русскими буквами и переводы: "
                     "\naltın	[алтын]	золото"
"\nbilge	[бильге]	начитанный"
"\nbir	[бир]	один"
"\nböbrek	[бёбрекь]	почка"
"\ndoktor	[доктор]	доктор"
"\ndöl	[дёль]	зародыш"
"\ngök	[гёкь]	небо"
"\ngüzel	[гюзель]	красивый"
"\nnereye	[нерейе]	куда"
"\nokul	[окул]	школа"
"\noluşma	[олушма]	формирование"
"\npeki	[пеки]	ладно"
"\nportakal	[портакал]	апельсин"
"\nsekmek	[секьмекь]	прыгать"
"\nsen	[сен]	ты"
"\nsıklık	[сыклык]	теснота"
                     "\nЗапишите в русской транскрипции турецкое слово almak ‘взять’.")
        task42.pack()
        task42_1=Entry(frame,  width=40)
        task42_1.pack()

        def check63():
            if task42_1.get().lower() == "алмак":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task42_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but67 = Button(frame, text='Проверить первую задачу', command=check63)
        but67.pack()

        task43 = Label(frame, text="Запишите в русской транскрипции турецкое слово benlik ‘эгоизм’.")
        task43.pack()
        task43_1 = Entry(frame, width=40)
        task43_1.pack()

        def check64():
            if task43_1.get().lower() == "бенликь":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task43_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but68 = Button(frame, text='Проверить вторую задачу', command=check64)
        but68.pack()

        task44 = Label(frame, text="Запишите в русской транскрипции турецкое слово gülmek ‘смеяться’.")
        task44.pack()
        task44_1 = Entry(frame, width=40)
        task44_1.pack()

        def check65():
            if task44_1.get().lower() == "гюльмекь":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task44_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but69 = Button(frame, text='Проверить третью задачу', command=check65)
        but69.pack()

        task45 = Label(frame, text="Запишите в русской транскрипции турецкое слово topuk ‘каблук’.")
        task45.pack()
        task45_1 = Entry(frame, width=40)
        task45_1.pack()

        def check66():
            if task45_1.get().lower() == "топук":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task45_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but70 = Button(frame, text='Проверить четвертую задачу', command=check66)
        but70.pack()

        task46 = Label(frame, text="Запишите в русской транскрипции турецкое слово sükse ‘успех’.")
        task46.pack()
        task46_1 = Entry(frame, width=40)
        task46_1.pack()

        def check67():
            if task46_1.get().lower() == "сюкьсе":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task46_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but71 = Button(frame, text='Проверить пятую задачу', command=check67)
        but71.pack()

        task47 = Label(frame, text="Задание 2. «Речевой аппарат человека. Согласные»"
                       "\nЧислительное ‘3’ по-японски может произноситься как [san], [sam] или [saŋ]: например, [san-ten] ‘3 очка’, [sam-pun] ‘3 минуты’, [saŋ-gooʃitsu] ‘комната №3’."
                       "\nВ следующих задачах заполните пропуски. Заменяйте ŋ на ng"
                       "\nЗадача 1. [...-nen]	‘3 года’")
        task47.pack()
        task47_1 = Entry(frame, width=40)
        task47_1.pack()

        def check68():
            if task47_1.get().lower() == "san":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task47_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but72 = Button(frame, text='Проверить первую задачу', command=check68)
        but72.pack()

        task48 = Label(frame, text="\nЗадача 2. […-ko]	‘3 предмета’")
        task48.pack()
        task48_1 = Entry(frame, width=40)
        task48_1.pack()

        def check69():
            if task48_1.get().lower() == "sang":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task48_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but73 = Button(frame, text='Проверить вторую задачу', command=check69)
        but73.pack()

        task49 = Label(frame, text="\nЗадача 3. […-ban]	‘число 3’")
        task49.pack()
        task49_1 = Entry(frame, width=40)
        task49_1.pack()

        def check70():
            if task49_1.get().lower() == "sam":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task49_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but74 = Button(frame, text='Проверить третью задачу', command=check70)
        but74.pack()

        task50 = Label(frame, text="\nЗадача 4. […-dan]	‘3 шага’")
        task50.pack()
        task50_1 = Entry(frame, width=40)
        task50_1.pack()

        def check71():
            if task50_1.get().lower() == "san":
                messagebox.showinfo("Состояние ответа", "Верный ответ")
            elif task50_1.get() == '':
                messagebox.showwarning("Предупреждение", "Введите ответ!!")
            else:
                messagebox.showinfo("Состояние ответа", 'Пока неверно. Подумайте ещё!')

        but75 = Button(frame, text='Проверить четвертую задачу', command=check71)
        but75.pack()

        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        def return9():
            fifth_window.deiconify()
            eighth_window.withdraw()

        but76 = Button(eighth_window, text='Вернуться назад к блоку лингвистических задач',
                       command=return9)
        but76.pack()

        def return10():
            root.deiconify()
            eighth_window.withdraw()

        but77 = Button(eighth_window, text='Домой',
                       command=return10)
        but77.pack()
    but66=Button(fifth_window, text='Фонетика', command=fonetics)
    but66.pack()
    def return4():
        root.deiconify()
        fifth_window.withdraw()
    but16=Button(fifth_window, text='Домой', command=return4)
    but16.pack()
button_l = Button(root, text='Лингвистические задачи', command=window5)
button_l.pack()
def recomendation():
    root.withdraw()
    nineth_window = Toplevel(root)
    nineth_window.protocol("WM_DELETE_WINDOW", root.destroy)
    nineth_window.title("Общие рекомендации")
    nineth_window.geometry('1000x1300')
    rec = Text(nineth_window)
    rec.pack(fill=BOTH, expand=1)
    # editor.insert("1.0", "Найдите русские аналоги для следующих понятий:  \nгенитивный, генеративный, нарративный, рефлексивный")
    rec.insert("1.0",
                   "Рекомендации от Даниила М. и Айлар: \nРекомендации по немецкому языку: \n Описание должно представлять собой связный и логичный текст. В тексте"
                   "должны присутствовать оценочные суждения, отвечающие коммуникативному"
                   "намерению заинтересовать читателей. Стиль текста должен соответствовать"
                   "потенциальной целевой аудитории. В тексте не должно быть стилистических,"
                   "грамматических, лексических и пунктуационных ошибок."
                   "Критерии оценивания заданий по иностранным языкам – см. спецификацию."
                   "\nРекомендации от Айлар"
                   "\n▎1. Определите цели и сроки:"
                   "\n• Установите конкретные цели для каждой темы или раздела."
                   "\n• Составьте план подготовки с учетом времени до олимпиады."
                   "\n▎2. Изучите программу олимпиады:"
                   "\n• Ознакомьтесь с темами, которые будут охвачены."
                   "\n• Проанализируйте формат заданий: тесты, задачи, эссе и т.д."
                   "▎3\n. Соберите необходимые материалы:"
                   "\n• Учебники, методические пособия, онлайн-курсы и видеоуроки."
                   "\n• Примеры заданий с прошлых олимпиад."
                   "\n▎4. Создайте расписание занятий"
                   "\n• Разделите время на изучение теории и практику."
                   "\n• Включите регулярные перерывы для отдыха."
                   "\n▎5. Практикуйтесь на заданиях"
                   "\n• Решайте задачи из прошлых олимпиад и тестов."
                   "\n• Участвуйте в тренировочных соревнованиях."
                   "\n▎6. Обсуждайте с единомышленниками"
                   "\n• Найдите группу для подготовки или товарищей по учебе."
                   "\n• Обсуждайте сложные темы и решайте задачи вместе."
                   "\n▎7. Обратная связь и анализ ошибок"
                   "\n• После выполнения заданий анализируйте свои ошибки."
                   "\n• Попросите учителей или более опытных товарищей дать обратную связь."
                   "\n▎8. Работа над слабостями"
                   "\n• Определите свои слабые стороны и уделите им больше времени."
                   "\n• Не бойтесь задавать вопросы и искать помощь."
                   "\n▎9. Регулярно повторяйте пройденное"
                   "\n• Используйте метод активного повторения, чтобы закрепить знания."
                   "\n• Создавайте конспекты или карточки с ключевыми понятиями."
                   "\n▎10. Подготовьте себя психологически"
                   "\n• Учитесь управлять стрессом и волнением."
                   "\n• Практикуйте техники релаксации и позитивного мышления."
                   "\n▎11. Обратите внимание на здоровье"
                   "\n• Соблюдайте режим сна, питания и физической активности."
                   "\n• Не забывайте делать перерывы для отдыха и восстановления."
                   "\n▎12. День перед олимпиадой"
                   "\n• Проведите легкую повторение, не перегружая себя новыми темами."
                   "\n• Подготовьте все необходимое для участия (документы, канцелярия)."
                   "\nРекомендации от команды 'Сириус.курсы'"
                   "\nПеред стартом заключительного этапа Всероссийской олимпиады школьников команда Сириус.Курсов обратилась к Константину Владимировичу Парфёнову – члену ЦПМК ВсОШ по физике, попросив поделиться ошибками школьников, из-за которых можно потерять драгоценные баллы. Эти советы пригодятся не только тем, кто выходит в финальные туры олимпиады, но и всем тем, кого в будущем ждёт написание важных работ."
                   "\nПервая ошибка связана с нехваткой знаний. Некоторые темы, встречающиеся на финале, могут быть не пройдены. Внимательно ознакомьтесь с демоверсией олимпиады текущего года, прорешайте её, выявите свои слабые места. Если отнесётесь несерьезно к предлагаемым составителями материалам, потеряете много баллов. Нужно смотреть демоверсию, спецификатор интересующей олимпиады, прорешивать архив заданий и делать выводы."
                   "\nВторая ошибка – недостаточная психологическая готовность – выражена так: в спокойной обстановке участник решает всё правильно, а на олимпиаде может наломать дров. Необходимо с этим бороться: изучить себя, понять, что мешает трудиться, сформировать собственную систему работу над заданиями. Например, одним удобно начинать с простых задач и постепенно разгоняться. Другим, наоборот, легче на свежую голову сделать трудное, а потом доделывать понятное. Кому-то нужна сильная мотивация, других же она нервирует."
                   "\nЧтобы привыкнуть к стрессовой обстановке на олимпиаде, необходимо поместить себя в условия стресса: решать задачи, пока домашние специально отвлекают, ставить заведенный будильник. Помимо изучения предмета, придется работать над собой."
                   "\nПоследняя ошибка качается оформления работы. Хаотичные записи не только приводят к путанице в мыслях, но и мешают проверяющим увидеть логику вашего решения. Решение должно быть структурированным. Решение может быть неполным, и за него можно будет получить часть баллов. Не бойтесь написать хоть что-то, даже глупость, главное – разборчивым почерком."
                   "\nСледуя этим рекомендациям, вы сможете значительно повысить свои шансы на успех в олимпиаде. Удачи в выполнении заданий!")

    def return11():
        root.deiconify()
        nineth_window.withdraw()

    butdel = Button(nineth_window, text='Домой',
                   command=return11)
    butdel.pack()
button_rec=Button(root, text="Общие советы для подготовки к олимпиаде", command=recomendation)
button_rec.pack()

def common():
    root.withdraw()
    tenth_window = Toplevel(root)
    tenth_window.protocol("WM_DELETE_WINDOW", root.destroy)
    tenth_window.title("Общие рекомендации")
    tenth_window.geometry('1000x1300')
    rec1 = Text(tenth_window)
    rec1.pack(fill=BOTH, expand=1)
    # editor.insert("1.0", "Найдите русские аналоги для следующих понятий:  \nгенитивный, генеративный, нарративный, рефлексивный")
    rec1.insert("1.0",
                   "Приложение должно помочь в подготовке к олимпиаде 'Я — профессионал' по языкознанию. Оно содержит задания формата олимпиады с возможностью автопроверки по следующим блокам: \n1. Русский язык; \n2. Иностранный язык (английский и немецкий). \n3. Лингвистическая задача. "
                   "\nВ блоке иностранного языка составлены 19 заданий, включающих 51 задачу. На очном туре 2 задания, но последнее задание включает 5 задач, а первое - одну задачу. Первый вопрос подразумевает выполнение ряда заданий к тексту на иностранном языке (например, дать толкование, перевести на русский язык, привести примеры синонимов и т.д.). Максимальная оценка составляет 10 баллов. Второе задание связано с написанием "
"аннотации к тексту на русском языке и ее переводом на иностранный язык (оценивается в 15 баллов). Пятый блок оценивается максимально в 25 баллов. Антонов Даниил составил 10 заданий для тренировки первого вопроса блока 'Английский язык'. Мохамед составил 7 заданий второго вопроса, включающих по 5 задач каждый. Поэтому по английскому 17 заданий и 45 задач. Марков Даниил составил 1 вариант блока 'Немецкий язык': 2 задания (6 задач). "
                   "По русскому языку были составлены задания к 4 вопросам олимпиады: 1, 2, 3, 6. Над блоком трудились Антонов Даниил и Шаляхина Арина. 5 заданий по паронимам (6 вопрос), 4 задания по словарю Даля (1 вопрос). Эти задания проверяют навыки лексического анализа слов. "
                "2 вопрос олимпиады посвящён знанию синтаксису и умению находить и объяснять синтаксическую неоднозначность: нами были составлены 3 задания на разные типы неоднозначностей. "
                   "3 вопрос олимпиды проверяет знание лингвистических терминов и умение подбирать к ним синонимы: в этом задании 4 задачи - 4 слова, к которым нужно подобрать аналоги. "
                   "Вопрос 13 настоящей олимпиады проверяет Компетенции в сфере теоретической и прикладной лингвистики, терминологии: нужно исправить ошибки в предложениях. Нами предложены 11 предложений с искаженными терминами для исправлений. \nВ блоке 'Лингвистическая задача' проверяется общий уровень языковой компетенции. Опираясь на Сириус.Курсы мы включили в программу задания по морфологии, синтаксису, фонетике: \n5 заданий, в которых 33 задачи, по синтаксису,  \n2 задания по морфологии (11 задач), \nпо фонетике 2 задания (9 задач). \nвсего 9 лингвистических заданий, включающих 53 задачи в блоке лингвистических задач"
                   "\nИтого: 10 типов заданий, 48 заданий, 147 задач."
                   "\nДля лучшей подготовки к блоку 'Лингвистическая задача' советуем Сириус.Курсы по лингвистике"
                   "\nСписок рекомендованной составителями литературы: \n1. Бурлак С.А., Старостин С.А. Сравнительноисторическое языкознание. М., 2005 (или переиздание)."
"\n2. Лингвистические задачи. М.: Просвещение, 1983."
"\n3. Лотман Ю.М. Анализ поэтического текста. Л., 1972, или переиздания."
"\n4. Маслов Ю.С. Введение в языкознание (любое издание)."
"\n5. Пропп В.Я. Морфология сказки. Любое издание."
"\n6. Русский язык. Школьный энциклопедический словарь. СПб., 2013 (или переиздание)."
"\n7. Сухих И.Н. Теория литературы. Практическая поэтика. СПб.: СПбГУ, 2014."
"\n8. Федоров А.В. Основы общей теории перевода (любое издание)."
"\n9. Холшевников В.Е. Основы стиховедения. Русское стихосложение. СПб.: Филологический факультет СПбГУ; М.: Академия, 2002."
"\n10. Шмид В. Нарратология. М., 2002."
                   "\nАрхив заданий и варианты текущго года (без решений) доступны на официальном сайте 'Я профессионал'")

    def return15():
        root.deiconify()
        tenth_window.withdraw()

    butdel1 = Button(tenth_window, text='Домой',
                   command=return15)
    butdel1.pack()
button_com=Button(root, text="О программе", command=common)
button_com.pack()

root.mainloop()
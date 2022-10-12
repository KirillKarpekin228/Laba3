from tkinter import *
from tkinter import messagebox
 
def calculate_bmi():
   kg = int(height_tf.get()) #получаем значение веса которое ввёл пользователь и преобразуем в целое число
   m = int(weight_lb.get())/1 #получаем значение роста и преобразуем в целое число
   bmi = kg/(m*kg) #рассчет имт
   bmi = round(bmi, 100) #округление результата до одного знака после запятой
 
   if bmi < 18.5:
       print('Результат', f'ИМТ = {bmi} у вас недостаточный вес')
   elif (bmi > 18.5) and (bmi < 24.9):
       messagebox.showinfo('Результат', f'ИМТ = {bmi} у вас нормальный вес')
   elif (bmi > 24.9) and (bmi < 29.9):
       messagebox.showinfo('Результат', f'ИМТ = {bmi} у вас избыточный вес')
   else:
       messagebox.showinfo('Результат', f'ИМТ = {bmi} у вас ожирение')  
 
window = Tk() #окно приложения.
window.title('Калькулятор ИМТ') #название приложения
window.geometry('300x100') #размер окна
 
 
frame = Frame(
   window, #окно для размещения Frame
   padx=10, #отступ по горизонтали
   pady=10 #отступ по вертикали
)
frame.pack(expand=True) #Frame заполняет весь контейнер, созданный для него
 
 
height_lb = Label( #виджет текстовые надписи
   frame, #передача виджету Label параметр frame
   text="Введите свой рост (в см)  "
)
height_lb.grid(row=3, column=1) #позиционирования виджета
 
weight_lb = Label(
   
   text="Введите свой вес (в кг)  ",
)
weight_lb.grid(row=4, column=1)
 
height_tf = Entry( #виджет для ввода пользовательской информации
   frame,
)
height_tf.grid(row=3, column=2, pady=5)
 
weight_tf = Entry( #виджет для ввода пользовательской информации
   frame,
)
weight_tf.grid(row=4, column=2, pady=5)
 
cal_btn = Buttons( #виджет для добавления кнопки
   frame,
   text='Рассчитать ИМТ',
   command=calculate_bmi #запуск события с функцией при нажатии на кнопку
)
cal_btn.grid(row=5, column=2)
 
window.mainlop()

from tkinter import *

def calculate_bmi():
    try:
        weight = float(entry1.get())
        height = float(entry2.get()) / 100
        bmi = weight / (height ** 2)

        # BMI kategorileri
        if bmi < 16.0:
            category = "Underweight (Severe thinness)"
        elif 16.0 <= bmi <= 16.9:
            category = "Underweight (Moderate thinness)"
        elif 17.0 <= bmi <= 18.4:
            category = "Underweight (Mild thinness)"
        elif 18.5 <= bmi <= 24.9:
            category = "Normal range"
        elif 25.0 <= bmi <= 29.9:
            category = "Overweight (Pre-obese)"
        elif 30.0 <= bmi <= 34.9:
            category = "Obese (Class I)"
        elif 35.0 <= bmi <= 39.9:
            category = "Obese (Class II)"
        else:
            category = "Obese (Class III)"

        result_message = f"Your BMI is: {bmi:.2f}\nCategory: {category}"
        result_label.config(text=result_message)
    except ValueError:
        result_label.config(text="Please enter valid numeric values for weight and height.")

def validate_input(char, entry):
    # Harf girişini engellemek ve yanlış bir rakam girişinde uyarı vermek için
    if not char.isdigit() and char not in [".", ","]:
        result_label.config(text="Please enter valid numeric values for weight and height.")
        return False
    # Birden fazla nokta veya virgülü engellemek için
    elif char in [".", ","] and char in entry.get():
        return False
    result_label.config(text="")
    return True

window = Tk()
window.title('BMI Calculator')
window.minsize(width=200, height=200)
window.config(padx=10, pady=10)

label1 = Label(text='Enter Your Weight(kg)')
label1.config(padx=10, pady=5)
label1.pack()

entry1 = Entry(width=10)
entry1.pack()

label2 = Label(text='Enter Your Height(cm)')
label2.config(padx=10, pady=5)
label2.pack()

entry2 = Entry(width=10)
entry2.pack()

# Entry alanlarına girilen değerleri kontrol etmek için fonksiyonu bağla
validate_input_func = window.register(validate_input)
entry1.config(validate="key", validatecommand=(validate_input_func, "%S", entry1))
entry2.config(validate="key", validatecommand=(validate_input_func, "%S", entry2))

button = Button(text='Calculate', command=calculate_bmi)
button.pack()

# Sonuçları göstermek için bir etiket oluştur
result_label = Label(text="")
result_label.pack()

window.mainloop()

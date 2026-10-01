weight = float(input("لطفا وزن بیمار را به کیلوگرم وارد کنید: "))
height = float(input("لطفا قد بیمار را به متر وارد کنید: "))

bmi = weight / (height ** 2)
print(f"شاخص توده بدنی (BMI): {bmi}")

if bmi < 18.5:
    print("وضعیت: کمبود وزن")
elif bmi < 25:
    print("وضعیت: وزن طبیعی")
elif bmi < 30:
    print("وضعیت: اضافه وزن")
else:
    print("وضعیت: چاقی")

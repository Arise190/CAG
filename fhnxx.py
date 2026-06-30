subjects = []

while True:
    data = input("Subject,Grade,Credit : ")

    if data.lower() == "exit":
        break

    try:
        subject, grade, credit = data.split(",")

        grade = float(grade)
        credit = int(credit)

        if grade < 0 or grade > 4:
            print("เกรดไม่ถูกต้อง")
            continue

        subjects.append([subject, grade, credit])

    except ValueError:
        print("รูปแบบไม่ถูกต้อง")

total_grade = 0
total_credit = 0

print("\nรายวิชา")

for sub in subjects:
    print(f"วิชา : {sub[0]} เกรด : {sub[1]} หน่วยกิต : {sub[2]}")
    total_grade += sub[1] * sub[2]
    total_credit += sub[2]

if total_credit > 0:
    print(f"\nGPA : {total_grade / total_credit:.2f}")
else:
    print("ไม่มีข้อมูล")
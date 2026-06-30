subjects = []

while True:
    data = input("Subject,Grade,Credit : ")

    if data.lower() == "exit":
        break

    try:
        subject, grade, credit = data.split(",")

        grade = float(grade)
        credit = int(credit)

        if not (0 <= grade <= 4):
            print("เกรดไม่ถูกต้อง")
            continue

        subjects.append([subject, grade, credit])

    except:
        print("รูปแบบไม่ถูกต้อง")
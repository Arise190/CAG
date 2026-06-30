def calculate_average_grade():
    s = []
    g = []
    w = []

    while True:
        x = input("กรุณาป้อนชื่อวิชา : ")
        s.append(x)

        while True:
            try:
                y = float(input("กรุณาป้อนเกรด : "))
                if y < 0 or y > 4:
                    print("กรุณาป้อนเกรดระหว่าง 0.0 ถึง 4.0")
                    continue

                g.append(y)
                break

            except ValueError:
                print("กรุณาป้อนเกรดเป็นตัวเลขและเป็นทศนิยม")

        while True:
            try:
                z = int(input("กรุณาป้อนจำนวนหน่วยกิต : "))

                if z <= 0:
                    print("กรุณาป้อนจำนวนหน่วยกิตเป็นจำนวนเต็มบวก")
                    continue

                w.append(z)
                break

            except ValueError:
                print("กรุณาป้อนจำนวนหน่วยกิตเป็นตัวเลข")

        
        while True:
            st = input("คุณต้องการไปต่อหรือไม่ : y/n : ").lower()

            if st not in ["y", "n"]:
                print("กรุณาป้อนเฉพาะ y หรือ n")
            else:
                break

        if st == "n":
            break
       

    for i in range(len(s)):
        print(f"รายวิชา : {s[i]} เกรด : {g[i]} หน่วยกิต : {w[i]}")

    avg_grad = sum([g[i] * w[i] for i in range(len(g))]) / sum(w)
    print(f"เกรดเฉลี่ยของคุณคือ : {avg_grad:.2f}")

    
    while True:
        cn = input("คุณต้องการคำนวณใหม่หรือไม่ : y/n : ").lower()

        if cn == "y":
            return calculate_average_grade()

        elif cn == "n":
            print("จบการทำงาน")
            return

        else:
            print("กรุณาป้อนเฉพาะ y หรือ n")
    


calculate_average_grade()
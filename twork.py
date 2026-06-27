def calculate_average_grade():
    s = []
    g = []
    w = []

    while True:
        try:
            x = str(input("กรุณาป้อนชื่อวิชา : "))
            s.append(x)
        except ValueError:
            print("กรุณาป้อนชื่อวิชาเป็นข้อความ")
        while True:
            try:
                y = float(input("กรุณาป้อนเกรด : "))
                g.append(y)
                if y < 0 or y > 4:
                    print("กรุณาป้อนเกรดระหว่าง 0.0 ถึง 4.0")
                    g.pop()
                    continue
                break
            except ValueError:
                print("กรุณาป้อนเกรดเป็นตัวเลขและเป็นทศนิยม")
        while True:
            try:
                z = int(input("กรุณาป้อนจำนวนหน่วยกิต : "))
                if z < 0:
                    print("กรุณาป้อนจำนวนหน่วยกิตเป็นจำนวนเต็มบวก")
                    continue
                w.append(z)
                break
            except ValueError:
                print("กรุณาป้อนจำนวนหน่วยกิตเป็นตัวเลข")
        
        while True:
            st = str(input("คุณต้องการไปต่อหรือไม่ : y/n : ")).lower()
            if st not in ["n","y"]:
                print("กรุณาป้อนเฉพาะ y หรือ n")
            else:
                if st == "n":
                    break
        if st == "n":
            break



    for i in range(len(s)):
        print(f"รายวิชา : {s[i]} เกรด : {g[i]} หน่วยกิต : {w[i]}")
        
    avg_grad = sum([g[i] * w[i] for i in range(len(g))]) / sum(w)
    print(f"เกรดเฉลี่ยของคุณคือ : {avg_grad:.2f}")


    while True:
        cn = str(input("คุณต้องการคำนวณใหม่หรือไม่ : y/n : ")).lower()
        if cn == "y":
            calculate_average_grade()
        elif cn == "n":
            print("จบการทำงาน")
            break
    return s,g,w


calculate_average_grade()

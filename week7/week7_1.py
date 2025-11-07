def main():
    # students 為儲存所有學生資料的清單，每個學生是一個小清單：
    # [學號, 姓名, 國文分數, 英文分數, 數學分數]
    students = []
    # 提示使用者先輸入至少 5 位學生資料
    print("請先輸入至少 5 位學生資料：")
    
    # 先輸入至少5位學生資料（count 計數）
    count = 0
    while count < 5:
        count += 1
        # 讀取學號（字串）
        print(f"學號：", end="")
        student_id = input().strip()
        
        # 讀取姓名（字串）
        print(f"姓名：", end="")
        name = input().strip()
        
        # 讀取國文成績，並轉成整數
        print(f"國文成績：", end="")
        chinese = int(input())
        
        # 讀取英文成績，並轉成整數
        print(f"英文成績：", end="")
        english = int(input())
        
        # 讀取數學成績，並轉成整數
        print(f"數學成績：", end="")
        math = int(input())
        
        # 把讀到的資料封裝成一個列表並加入 students
        student_data = [student_id, name, chinese, english, math]
        students.append(student_data)
        
        print(f"目前已輸入 {count} 位學生")
        print()
    
    print("---")
    print()
    
    # 主選單循環：直到使用者選擇 0 結束程式
    while True:
        print("=== 學生成績系統 ===")
        print("1) 新增學生資料")
        print("2) 顯示各科平均")
        print("3) 顯示每位同學的總分與平均")
        print("0) 結束程式")
        print("請選擇：", end="")
        
        choice = input().strip()
        print()
        
        # 根據使用者選擇呼叫不同的函式
        if choice == '1':
            add_student(students)               # 新增學生
        elif choice == '2':
            show_subject_averages(students)     # 顯示三科平均
        elif choice == '3':
            show_student_totals(students)      # 顯示每位同學總分與平均
        elif choice == '0':
            print("結束程式")
            break                              # 離開迴圈結束程式
        else:
            print("無效的選擇，請輸入 0-3")
        
        print()

def add_student(students):
    """新增學生資料並加入 students 清單（就地修改）"""
    print("學號：", end="")
    student_id = input().strip()
    
    print("姓名：", end="")
    name = input().strip()
    
    print("國文成績：", end="")
    chinese = int(input())
    
    print("英文成績：", end="")
    english = int(input())
    
    print("數學成績：", end="")
    math = int(input())
    
    # 建立學生資料並 append 到 students
    student_data = [student_id, name, chinese, english, math]
    students.append(student_data)
    
    print(f"已新增學生 {name}")

def show_subject_averages(students):
    """計算並顯示三科（國文/英文/數學）的平均成績"""
    if not students:  # 如果 students 為空，提示後返回
        print("目前沒有任何學生資料")
        return
    
    # 初始化三科分數總和
    total_chinese = 0
    total_english = 0
    total_math = 0
    
    # 累加每位學生的三科分數
    for student in students:
        total_chinese += student[2]  # student[2] = 國文
        total_english += student[3]  # student[3] = 英文
        total_math += student[4]     # student[4] = 數學
    
    count = len(students)
    # 計算平均（注意：除法會回傳浮點數）
    avg_chinese = total_chinese / count
    avg_english = total_english / count
    avg_math = total_math / count
    
    # 以小數點一位顯示平均
    print(f"國文平均： {avg_chinese:.1f}")
    print(f"英文平均： {avg_english:.1f}")
    print(f"數學平均： {avg_math:.1f}")

def show_student_totals(students):
    """顯示每位同學的總分與平均"""
    if not students:
        print("目前沒有任何學生資料")
        return
    
    for student in students:
        # 解包 student 的欄位
        student_id, name, chinese, english, math = student
        total = chinese + english + math
        average = total / 3
        
        # 若平均是整數（例如 90.0），則以一位小數顯示；否則顯示二位小數
        # 注意：這裡用 int(average) 比較可能受浮點精度影響，更穩健的寫法可用 average.is_integer()
        if average == int(average):
            print(f"{student_id} {name} 總分：{total} 平均：{average:.1f}")
        else:
            print(f"{student_id} {name} 總分：{total} 平均：{average:.2f}")

# 程式進入點：當此檔案被直接執行時，呼叫 main()
if __name__ == "__main__":
    main()

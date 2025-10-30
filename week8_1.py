def main():
    students = []
    #建立空列表來儲存
    print("請先輸入至少 5 位學生資料：")
    
    # 先輸入至少5位學生資料
    count = 0
    while count < 5:
        count += 1
        print(f"學號：", end="")
        student_id = input().strip()
        
        print(f"姓名：", end="")
        name = input().strip()
        
        print(f"國文成績：", end="")
        chinese = int(input())
        
        print(f"英文成績：", end="")
        english = int(input())
        
        print(f"數學成績：", end="")
        math = int(input())
        
        #加入列表
        student_data = [student_id, name, chinese, english, math]
        students.append(student_data)
        
        print(f"目前已輸入 {count} 位學生")
        print()
    
    print("---")
    print()
    
    # 主選單
    while True:
        print("=== 學生成績系統 ===")
        print("1) 新增學生資料")
        print("2) 顯示各科平均")
        print("3) 顯示每位同學的總分與平均")
        print("0) 結束程式")
        print("請選擇：", end="")
        
        choice = input().strip()
        print()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            show_subject_averages(students)
        elif choice == '3':
            show_student_totals(students)
        elif choice == '0':
            print("結束程式")
            break
        else:
            print("無效的選擇，請輸入 0-3")
        
        print()

def add_student(students):
    """新增學生資料"""
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
    
    student_data = [student_id, name, chinese, english, math]
    students.append(student_data)
    
    print(f"已新增學生 {name}")

def show_subject_averages(students):
    """顯示各科平均成績"""
    if not students:
        print("目前沒有任何學生資料")
        return
    
    total_chinese = 0
    total_english = 0
    total_math = 0
    
    for student in students:
        total_chinese += student[2]  # 國文
        total_english += student[3]  # 英文
        total_math += student[4]     # 數學
    
    count = len(students)
    avg_chinese = total_chinese / count
    avg_english = total_english / count
    avg_math = total_math / count
    
    print(f"國文平均： {avg_chinese:.1f}")
    print(f"英文平均： {avg_english:.1f}")
    print(f"數學平均： {avg_math:.1f}")

def show_student_totals(students):
    """顯示每位同學的總分與平均"""
    if not students:
        print("目前沒有任何學生資料")
        return
    
    for student in students:
        student_id, name, chinese, english, math = student
        total = chinese + english + math
        average = total / 3
        
        if average == int(average):
            print(f"{student_id} {name} 總分：{total} 平均：{average:.1f}")
        else:
            print(f"{student_id} {name} 總分：{total} 平均：{average:.2f}")

# 執行程式
if __name__ == "__main__":
    main()
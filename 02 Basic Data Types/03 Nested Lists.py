if __name__ == '__main__':
    student_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name, score])
    
    def myfunc(x):
        return x[1]
        
    student_grades.sort(key= myfunc)
         
    min_grade = student_grades[0][1]
    
    second_lowest_grade_students = []
    
    record = False
    second_lowest_grade = None
    
    for student_grade in student_grades:
        if student_grade[1] != min_grade and second_lowest_grade == None: 
            record = True
            second_lowest_grade = student_grade[1]
            
        if second_lowest_grade and second_lowest_grade != student_grade[1]:
            break
        
        if record: 
            second_lowest_grade_students.append(student_grade[0])
        
    second_lowest_grade_students.sort()
    
    for student in second_lowest_grade_students:
        print(student)
            
        


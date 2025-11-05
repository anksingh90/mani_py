# 🎯 School Management System (Lists & Tuples)

A clean, minimal, menu-driven Python program to manage student records using a list of tuples.

---

## ✨ Overview
Store student data as tuples:
(roll_no, name, class_name, marks1, marks2, marks3)  
Use a list called `students` to hold all records and simple console I/O for interaction.

---

## ✅ Features
- Add student records
- Display all students (tabular)
- Search student by roll number
- Update student marks (replace the tuple)
- Delete student record
- Calculate totals, averages, and pass/fail status
- Exit with a friendly message

---

## 🧩 Data Structure Example
```python
students = [
    (101, "Alice", "10A", 85, 78, 92),
    (102, "Bob",   "10A", 56, 64, 70)
]
```

---

## 📋 Sample Table (for reference)

| Roll No | Name  | Class | Marks 1 | Marks 2 | Marks 3 |
|--------:|-------|:------|--------:|--------:|--------:|
| 101     | Alice | 10A   | 85      | 78      | 92      |
| 102     | Bob   | 10A   | 56      | 64      | 70      |

---

## 🛠️ Menu (Console)
```
===== SCHOOL MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Show Result Summary
7. Exit
Enter your choice:
```

---

## ℹ️ Result Summary Rules
- Total = marks1 + marks2 + marks3  
- Average = Total / 3  
- Pass if Average ≥ 40 (customize as needed)

---

## 💡 Tips
- Use tuple immutability to enforce record integrity; replace tuples when updating.
- Keep roll numbers unique — use them as keys for search/update/delete.
- Validate numeric input for marks and roll numbers.

---

Thank you — scalable, readable, and easy to extend for file persistence or a GUI.

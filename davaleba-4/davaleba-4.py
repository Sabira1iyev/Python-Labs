import sqlite3
import matplotlib.pyplot as plt
import random
import os



def gpa_pie_chart(gpa_list):
    intervals = [0] * 8
    labels = [
        "0.0-0.5",
        "0.5-1.0",
        "1.0-1.5",
        "1.5-2.0",
        "2.0-2.5",
        "2.5-3.0",
        "3.0-3.5",
        "3.5-4.0",
    ]
    colors = ["red", "green", "orange", "gray", "pink", "chocolate", "purple", "cyan"]

    for gpa in gpa_list:
        if gpa == 4:
            intervals[7] += 1
        else:
            index = int(gpa // 0.5)
            intervals[index] += 1

    plt.figure()
    plt.pie(intervals, labels=labels, colors=colors, autopct="%1.1f%%")
    plt.title("GPA Pie Chart")
    plt.show()


def subject_grade_plot(subjects, subject_names):
    grade_labels = ["missed", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"]
    grade_perebi = ["pink", "blue", "orange", "green", "red", "purple", "chocolate"]

    plt.figure(figsize=(12, 8))

    for i, subject in enumerate(subjects):
        counts = [0] * 7
        for grade in subject:
            if grade == -1:
                counts[0] += 1
            elif 41 <= grade <= 50:
                counts[1] += 1
            elif 51 <= grade <= 60:
                counts[2] += 1
            elif 61 <= grade <= 70:
                counts[3] += 1
            elif 71 <= grade <= 80:
                counts[4] += 1
            elif 81 <= grade <= 90:
                counts[5] += 1
            elif 91 <= grade <= 100:
                counts[6] += 1
        plt.subplot(2, 2, i + 1)
        plt.bar(grade_labels, counts, color=grade_perebi)
        plt.title(f"{subject_names[i]}")

    plt.tight_layout()
    plt.show()


conn = sqlite3.connect("students_ge.db")
cursor = conn.cursor()

cursor.execute("SELECT GPA FROM Student")
gpa_list = [row[0] for row in cursor.fetchall()]

all_subjects = [
    "subj_01",
    "subj_02",
    "subj_03",
    "subj_04",
    "subj_05",
    "subj_06",
    "subj_07",
    "subj_08",
    "subj_09",
    "subj_10",
]
selected_subjects = random.sample(all_subjects, 4)

subject_grades = []
for subj in selected_subjects:
    cursor.execute(f"SELECT {subj} FROM Student")
    grades = [row[0] for row in cursor.fetchall()]
    subject_grades.append(grades)
conn.close()

gpa_pie_chart(gpa_list)
subject_grade_plot(subject_grades, selected_subjects)

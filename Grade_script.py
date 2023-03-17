import csv

# Initialize a dictionary to store the grades for each student
student_grades = {}

# Loop over the 5 CSV files and add the grades to the dictionary
for quiz_number in range(6,9):
        with open(f"Quiz-{quiz_number}_scores.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                first_name = row[0]
                last_name = row[1]
                email = row[3]
                grade = float(row[5]) if row[5] else 0
                name = f"{last_name}, {first_name}"
#                print(grade)
                if name not in student_grades:
                    student_grades[name] = {"email": email, "quiz_grades": [0,0, 0], "num_quizzes_taken": 0}
                student_grades[name]["quiz_grades"][quiz_number-6] = grade
                if grade != 0:
                    student_grades[name]["num_quizzes_taken"] += 1

# Compute the total and average grade for each student
for name, data in student_grades.items():
    data["total_score"] = sum(data["quiz_grades"])
    data["average_score"] = data["total_score"] / 3

# Write the results to a new CSV file with the desired format
with open("quiz_results3.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Student", "SIS Login ID","Quiz 6", "Quiz 7", "Quiz 8", "Average Score"])
    writer.writerow(["    Points Possible", "", "", "", "", ""])

    for name, data in sorted(student_grades.items(), key=lambda x: (x[0].split(", ")[0], x[0].split(", ")[1])):
        last_name, first_name = name.split(", ")
        email = data["email"]
        quiz_scores = data["quiz_grades"]
        total_score = data["total_score"]
        average_score = data["average_score"]
        writer.writerow([last_name + ", " + first_name, email] + quiz_scores + [average_score])


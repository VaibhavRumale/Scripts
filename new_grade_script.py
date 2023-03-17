import csv
import os

# Set the path to the directory containing the CSV files
dir_path = "New Folder With Items 2"

# Set the output file name
output_file = "Result_grade_2.csv"

# Create an empty dictionary to store the quiz scores
quiz_scores = {}

# Loop through each CSV file in the directory
for filename in os.listdir(dir_path):
    if filename.endswith(".csv"):
        with open(os.path.join(dir_path, filename)) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Loop through each row in the CSV file
            for row in csv_reader:
                # Get the student's name in the format (Last Name, First Name)
                name = "{}, {}".format(row["Last Name"], row["First Name"])
                # Get the quiz number from the file name
                quiz_number = filename.split("_")[1].split(".")[0]
                # Add the quiz score to the student's total score
                if name not in quiz_scores:
                    quiz_scores[name] = {"total_score": 0, "quiz_scores": {}}
                try:
                    total_score = float(row["Total Score"])
                except ValueError:
                    # Skip this row if Total Score is not a number
                    continue
                quiz_scores[name]["total_score"] += total_score
                quiz_scores[name]["quiz_scores"][quiz_number] = total_score

# Create the output CSV file
with open(output_file, mode="w", newline="") as csv_file:
    fieldnames = ["Student", "SIS Login ID", "Quiz 1"]
    quiz_numbers = sorted(set(score_dict["quiz_scores"].keys() for score_dict in quiz_scores.values()))
    fieldnames.extend(["Quiz {}".format(qn) for qn in quiz_numbers])
    fieldnames.append("Average Score")
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through each student in the dictionary and write their data to the output CSV file
    for name, scores in quiz_scores.items():
        average_score = scores["total_score"] / len(scores["quiz_scores"])
        row_data = {"Student": name, "SIS Login ID": "", "Quiz 1": scores["quiz_scores"].get("1", 0)}
        for qn in quiz_numbers:
            row_data["Quiz {}".format(qn)] = scores["quiz_scores"].get(qn, 0)
        row_data["Average Score"] = average_score
        writer.writerow(row_data)

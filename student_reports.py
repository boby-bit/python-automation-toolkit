def generate_report(name, marks):
    total = sum(marks)
    avg = total / len(marks)

    report = f"""
Student: {name}
Total: {total}
Average: {avg:.2f}
Maximum: {max(marks)}
Minimum: {min(marks)}
"""

    with open("student_report.txt", "a") as f:
        f.write(report + "\n")

    print(report)

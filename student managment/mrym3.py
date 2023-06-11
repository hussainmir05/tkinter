import tkinter as tk
import matplotlib.pyplot as plt
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Connect to the SQL database
conn = sqlite3.connect('rms.db')
cursor = conn.cursor()

# Get the list of courses
cursor.execute('SELECT DISTINCT course FROM result')
courses = cursor.fetchall()

# Count students below 50 in each course
student_counts = {}
for course in courses:
    course_name = course[0]
    cursor.execute('SELECT COUNT(*) FROM result WHERE CAST(per AS INTEGER) <= 100 AND course=?',
                   (course_name,))
    result = cursor.fetchone()
    count = result[0]
    student_counts[course_name] = count

# Close the database connection
conn.close()

# Create a bar graph for number of students below 50 in each course using Tkinter and matplotlib
root = tk.Tk()
root.title("Number of Students Below 50 in Each Course")

courses = list(student_counts.keys())
student_numbers = list(student_counts.values())

fig = plt.figure(figsize=(8, 6))
plt.bar(courses, student_numbers)

plt.xlabel('Course')
plt.ylabel('Number of Students')
plt.title('Number of Students Below 50 in Each Course')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

# Display the graph
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Start the Tkinter event loop
tk.mainloop()

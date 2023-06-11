import tkinter as tk
import matplotlib.pyplot as plt
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Connect to the SQL database
conn = sqlite3.connect('rms.db')
cursor = conn.cursor()

# Grade Ranges
grade_ranges = {
    'Below 50': (0, 50),
    '50 - 70': (49, 70),
    '70 - 80': (69, 80),
    'Above 80': (79, 100)
}

# Count students in each grade range
grade_counts = {}
for grade, (lower, upper) in grade_ranges.items():
    cursor.execute('SELECT COUNT(*) FROM result WHERE CAST(per AS INTEGER) >= ? AND CAST(per AS INTEGER) < ?', (lower, upper))
    result = cursor.fetchone()
    count = result[0]
    grade_counts[grade] = count

# Close the database connection
conn.close()

# Create a bar graph using Tkinter and matplotlib
root = tk.Tk()
root.title("Grade Distribution")

grades = list(grade_counts.keys())
counts = list(grade_counts.values())

fig = plt.figure(figsize=(6, 4))
plt.bar(grades, counts)

plt.xlabel('Grade Range')
plt.ylabel('Count')
plt.title('Grade Distribution')

plt.tight_layout()

# Display the graph
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Start the Tkinter event loop
tk.mainloop()

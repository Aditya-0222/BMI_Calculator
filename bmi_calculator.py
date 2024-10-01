import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime
from ttkthemes import ThemedTk  # For additional themes

# Define the absolute path for the database file
db_path = 'bmi_data.db'

# BMI Calculation Logic
def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ValueError:
        return None

# Categorize BMI into health categories
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Function to save data to SQLite
def save_to_db(user, weight, height, bmi):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bmi_records (
                    user TEXT,
                    weight REAL,
                    height REAL,
                    bmi REAL,
                    timestamp TEXT
                )''')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO bmi_records (user, weight, height, bmi, timestamp) VALUES (?, ?, ?, ?, ?)",
              (user, weight, height, bmi, timestamp))
    conn.commit()
    conn.close()

# View Historical Data for a User
def view_user_trend(user):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT weight, height, bmi, timestamp FROM bmi_records WHERE user=?", (user,))
    records = c.fetchall()
    conn.close()

    if not records:
        messagebox.showinfo("No Data", f"No historical data found for user: {user}")
        return

    # Data Visualization: Matplotlib Plot
    timestamps, bmis = zip(*[(row[3], row[2]) for row in records])

    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, bmis, marker='o', linestyle='-', color='#007bff')
    plt.title(f'BMI Trend Analysis for {user}')
    plt.xlabel('Date')
    plt.ylabel('BMI')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# View All Users and Their Historical Data
def view_all_users():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT DISTINCT user FROM bmi_records")
    users = c.fetchall()
    conn.close()

    if not users:
        messagebox.showinfo("No Data", "No users found in the database.")
        return

    # Create a new window to list all users
    user_window = tk.Toplevel()
    user_window.title("User List")

    def on_user_click(user):
        view_user_trend(user)

    # List all users with clickable names
    for user in users:
        user_button = ttk.Button(user_window, text=user[0])
        user_button.bind("<Button-1>", lambda e, u=user[0]: on_user_click(u))
        user_button.pack(pady=5, padx=10, fill='x')

# Full-Screen GUI using ThemedTk
def create_gui():
    root = ThemedTk(theme="arc")  # You can choose different themes like "breeze", "equilux", etc.
    root.title("BMI Calculator")

    # Full-Screen Mode
    root.attributes('-fullscreen', True)

    # Style Configuration
    style = ttk.Style()
    style.configure('TLabel', font=('Arial', 14), background='#f0f4f8', padding=10)
    style.configure('TEntry', font=('Arial', 14), padding=5)
    style.configure('TButton', font=('Arial', 14), padding=10)
    style.map('TButton',
              background=[('active', '#007bff'), ('pressed', '#0056b3')],
              foreground=[('pressed', '#ffffff')])

    # Create Frames for Layout
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill='both', expand=True)

    # Labels and Entry Fields
    ttk.Label(main_frame, text="Name:").grid(row=0, column=0, sticky="w")
    ttk.Label(main_frame, text="Weight (kg):").grid(row=1, column=0, sticky="w")
    ttk.Label(main_frame, text="Height (cm):").grid(row=2, column=0, sticky="w")

    name_var = tk.StringVar()
    weight_var = tk.StringVar()
    height_var = tk.StringVar()

    name_entry = ttk.Entry(main_frame, textvariable=name_var)
    weight_entry = ttk.Entry(main_frame, textvariable=weight_var)
    height_entry = ttk.Entry(main_frame, textvariable=height_var)

    name_entry.grid(row=0, column=1, padx=10, pady=5)
    weight_entry.grid(row=1, column=1, padx=10, pady=5)
    height_entry.grid(row=2, column=1, padx=10, pady=5)

    # Button Actions
    def on_calculate():
        name = name_var.get()
        weight = weight_var.get()
        height = height_var.get()

        bmi = calculate_bmi(weight, height)
        if bmi is None:
            messagebox.showerror("Input Error", "Please enter valid weight and height!")
            return

        category = bmi_category(bmi)
        messagebox.showinfo("BMI Result", f"Your BMI is {bmi} ({category})")

        # Save to Database
        save_to_db(name, weight, height, bmi)

    calculate_button = ttk.Button(main_frame, text="Calculate BMI", command=on_calculate)
    calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    view_users_button = ttk.Button(main_frame, text="View All Users", command=view_all_users)
    view_users_button.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()

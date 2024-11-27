import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import filedialog
import json
import os

# File system simulation (stored in a JSON structure)
file_system = {
    "root": {
        "file1.txt": "This is the content of file1.",
        "folder1": {
            "file2.txt": "Content of file2",
            "folder2": {
                "file3.txt": "Content of file3"
            }
        }
    }
}

# Dummy check_face function (replace with actual function in your use case)
def check_face():
    return "John Doe"  # Example, you can set to "" to simulate unauthorized

# Function to handle login and face recognition
def on_login():
    # Call the check_face function (which returns the name of the employee or an empty string)
    employee_name = check_face()

    if employee_name:
        # If a valid name is returned, show the welcome frame
        create_welcome_frame(employee_name)
    else:
        # If face is not recognized, show an error dialog
        messagebox.showerror("Unauthorized", "Face not recognized. Unauthorized access is prohibited.")

# Function to create the welcome frame after successful login
def create_welcome_frame(employee_name):
    global current_path
    current_path = "root"  # Starting at the root directory in the file system

    header.config(text=f"FaRec\nWelcome back, {employee_name}!")
    button_frame.pack_forget()  # Hide the login/add user buttons
    file_manager_frame.pack()  # Show the file manager frame

    # Update the path display
    update_path_display()

    # Create the file and directory buttons
    create_file_buttons()

# Function to update the path display in the header
def update_path_display():
    path_display.config(text=f"Path: /{current_path}")

# Function to create file and directory buttons
def create_file_buttons():
    # Clear the existing buttons
    for widget in file_frame.winfo_children():
        widget.destroy()

    # Get the files and directories in the current path
    path_data = get_path_data(current_path)
    row, col = 0, 0

    for item, content in path_data.items():
        if isinstance(content, dict):  # It's a directory
            button = tk.Button(file_frame, text=item, command=lambda i=item: navigate_to(i))
            button.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
        else:  # It's a file
            button = tk.Button(file_frame, text=item, command=lambda i=item: open_file(i))
            button.grid(row=row, column=col, sticky="ew", padx=5, pady=5)

        # Position buttons in a grid
        col += 1
        if col > 3:  # After 4 columns, move to the next row
            col = 0
            row += 1

# Get data for a specific directory
def get_path_data(path):
    if path == "root":
        return file_system["root"]
    # Navigate recursively for subdirectories
    dirs = path.split('/')
    data = file_system
    for dir in dirs:
        data = data[dir]
    return data

# Function to navigate into a directory
def navigate_to(directory):
    global current_path
    current_path = f"{current_path}/{directory}"  # Update current path
    update_path_display()  # Update path label
    create_file_buttons()  # Refresh the file and folder buttons

# Function to open a file and display its content
def open_file(filename):
    file_content = get_file_content(filename)
    if file_content:
        # Display file content in a new window or a pop-up
        display_file_content(filename, file_content)

# Get file content from the file system
def get_file_content(filename):
    path_data = get_path_data(current_path)
    return path_data.get(filename, None)

# Display file content
def display_file_content(filename, content):
    file_content_window = tk.Toplevel(root)
    file_content_window.title(f"Viewing: {filename}")
    text_widget = tk.Text(file_content_window, wrap="word", height=20, width=50)
    text_widget.insert(tk.END, content)
    text_widget.pack(padx=10, pady=10)
    text_widget.config(state=tk.DISABLED)  # Make it read-only

# Function to add a new file or directory
def add_file_or_directory():
    file_dir_name = simpledialog.askstring("New File/Directory", "Enter the name of the file or directory:")
    if file_dir_name:
        choice = messagebox.askquestion("Choose Type", "Is this a directory?", icon="question")
        if choice == 'yes':  # Create directory
            create_directory(file_dir_name)
        else:  # Create file
            create_file(file_dir_name)

# Create a new directory in the current path
def create_directory(directory_name):
    path_data = get_path_data(current_path)
    if directory_name in path_data:
        messagebox.showwarning("Error", "Directory already exists!")
    else:
        path_data[directory_name] = {}  # Add empty directory
        create_file_buttons()  # Refresh file manager

# Create a new file in the current path
def create_file(file_name):
    path_data = get_path_data(current_path)
    if file_name in path_data:
        messagebox.showwarning("Error", "File already exists!")
    else:
        path_data[file_name] = ""  # Add empty file
        create_file_buttons()  # Refresh file manager

# Create the main window
root = tk.Tk()
root.title("FaRec")
root.geometry("540x960")  # 9:16 aspect ratio
root.config(bg='#f0f0f0')

# Header
header = tk.Label(root, text="FaRec", font=("Helvetica", 24), bg='#4CAF50', fg='white', height=2)
header.pack(fill='x')

# Path display label
path_display = tk.Label(root, font=("Helvetica", 14), bg='#f0f0f0')
path_display.pack(fill='x')

# Main frame containing buttons
button_frame = tk.Frame(root)
button_frame.pack()

# File manager frame
file_manager_frame = tk.Frame(root)
file_manager_frame.pack_forget()  # Initially hidden

# Frame to hold file and directory buttons
file_frame = tk.Frame(file_manager_frame, bg='#f0f0f0')
file_frame.pack(fill='both', expand=True)

# Add a 'Log In' button to the main screen
login_button = tk.Button(button_frame, text="Log In", font=("Helvetica", 18), width=20, height=2, command=on_login)
login_button.pack(pady=20)

# Add a 'Add User' button to the main screen
add_user_button = tk.Button(button_frame, text="Add User", font=("Helvetica", 18), width=20, height=2)
add_user_button.pack(pady=20)

# Add a 'Add File/Directory' button for the file manager screen
add_button = tk.Button(file_manager_frame, text="Add File/Directory", font=("Helvetica", 18), command=add_file_or_directory)
add_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

import tkinter as tk
def expand_options():
    # Remove the existing widgets from the main frame
    for widget in main_frame.winfo_children():
        widget.grid_remove()

    # Create and display additional widgets
    username_label = tk.Label(main_frame, text="Username:")
    username_entry = tk.Entry(main_frame)
    password_label = tk.Label(main_frame, text="Password:")
    password_entry = tk.Entry(main_frame, show="*")  # Password entry
    email_label = tk.Label(main_frame, text="Email:")
    email_entry = tk.Entry(main_frame)
    register_button = tk.Button(main_frame, text="Register User", command=show_confirmation)

    username_label.grid(row=0, column=0, sticky="w")
    username_entry.grid(row=0, column=1)
    password_label.grid(row=1, column=0, sticky="w")
    password_entry.grid(row=1, column=1)
    email_label.grid(row=2, column=0, sticky="w")
    email_entry.grid(row=2, column=1)
    register_button.grid(row=3, column=0, columnspan=2)

def show_confirmation():
    # Create a small window with a confirmation message
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Confirmation")
    confirmation_label = tk.Label(confirmation_window, text="User inserted in the system.")
    confirmation_label.pack(padx=20, pady=20)

    # After a delay, destroy the confirmation window and reset the main menu
    root.after(2000, lambda: (confirmation_window.destroy(), reset_main_menu()))

def reset_main_menu():
    # Clear any widgets in the main frame and show the main menu again
    for widget in main_frame.winfo_children():
        widget.grid_remove()

    main_menu_label.grid(row=0, column=0)
    user_button.grid(row=1, column=0)
    exit_button.grid(row=2, column=0)

# Create the main application window
root = tk.Tk()
root.title("Expandable Options")

# Create the main frame to hold the widgets
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=1)

# Create widgets for the main menu
main_menu_label = tk.Label(main_frame, text="Select an option:")
user_button = tk.Button(main_frame, text="User", command=expand_options)
exit_button = tk.Button(main_frame, text="Exit", command=root.destroy)

main_menu_label.grid(row=0, column=0)
user_button.grid(row=1, column=0)
exit_button.grid(row=2, column=0)

root.mainloop()

import subprocess
import os
import tkinter as tk
from tkinter import messagebox

def open_firefox_with_profile(url, profile_path):
    firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Update this path if Firefox is installed elsewhere
    try:
        # Launch Firefox with the URL and specified profile
        subprocess.run([firefox_path, '-P', profile_path, '-no-remote', url], check=True)
        print(f"Firefox opened successfully with profile: {profile_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open Firefox. Error: {e}")
        messagebox.showerror("Error", f"Failed to open Firefox. Error: {e}")
    except FileNotFoundError:
        print("Firefox is not installed or not found at the specified path.")
        messagebox.showerror("Error", "Firefox is not installed or not found at the specified path.")

def open_url():
    url = url_entry.get()
    profile = profile_var.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return
    if profile == "Select Profile":
        messagebox.showwarning("Warning", "Please select a profile.")
        return
    open_firefox_with_profile(url, profile)

# Create the main window
root = tk.Tk()
root.title("Firefox Profile Switcher")

# Create and place the URL entry field
tk.Label(root, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the profile dropdown menu
tk.Label(root, text="Select Profile:").grid(row=1, column=0, padx=10, pady=10)
profile_var = tk.StringVar(root)
profile_var.set("Select Profile")  # Default value
profiles = ['profile1', 'profile2']  # Replace with actual profile names
profile_menu = tk.OptionMenu(root, profile_var, *profiles)
profile_menu.grid(row=1, column=1, padx=10, pady=10)

# Create and place the open button
open_button = tk.Button(root, text="Open URL", command=open_url)
open_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()

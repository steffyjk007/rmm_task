# import tkinter as tk

import requests
import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Device Data")

# Create a Text widget to display the data
text_widget = tk.Text(root)
text_widget.pack()

# Function to fetch and display data
def fetch_and_display_data():
    response = requests.get('http://localhost:8000/api/get_device_data/')  # Replace with your Django app's URL
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            text_widget.insert(tk.END, f"Device Name: {entry['device_name']}\nStatus: {entry['status']}\nLast Update Time: {entry['last_update_time']}\n\n")
    else:
        text_widget.insert(tk.END, "Failed to fetch data")

# Button to trigger data fetch
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_and_display_data)
fetch_button.pack()

# Start the Tkinter main loop
root.mainloop()

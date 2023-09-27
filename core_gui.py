
import tkinter as tk
from tkinter import ttk
import requests

# Define the URL of your Django API endpoint
API_URL = 'http://localhost:8000/devices/'


class DeviceViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Device Viewer")

        # Create a treeview widget to display data
        self.tree = ttk.Treeview(root, columns=('id','Device Name', 'Status', 'Last Update Time'))
        self.tree.heading('#1', text="Id")
        self.tree.heading('#2', text='Device Name')
        self.tree.heading('#3', text='Status')
        self.tree.heading('#4', text='Last Update Time')
        self.tree.pack()

        # Fetch and display device data from the API
        self.fetch_and_display_data()

    def fetch_and_display_data(self):
        try:
            response = requests.get(API_URL)
            response.raise_for_status()  # Check for HTTP errors
            device_data = response.json()

            # Clear existing data in the treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Populate the treeview with device data
            for device in device_data:
                self.tree.insert('', 'end',
                                 values=(device['id'],device['device_name'], device['status'], device['last_update_time']))

        except requests.exceptions.RequestException as e:
            # Handle connection or request errors
            print(f"Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DeviceViewerApp(root)
    root.mainloop()

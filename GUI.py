import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.visual=False
        self.graph=False
        self.close=False
        self.title("Pysico")
        self._object_data = []
        self._setting_data = []

        # Configure grid weights
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Create and place frames
        self.object_frame = Object_Frame(self)
        self.object_frame.grid(row=0, column=0,columnspan=2, sticky="nsew",padx=5,pady=5)

        self.setting_frame = Settings_Frame(self)
        self.setting_frame.grid(row=0, column=2, sticky="nsew",padx=5,pady=5)

        # Visual Start button
        self.visual_btn = ttk.Button(self, text="Visual", command=self.btn_visual)
        self.visual_btn.grid(row=1, column=0, columnspan=1, sticky="nsew",padx=5,pady=5)
        
        # Visual Graph button
        self.graph_btn = ttk.Button(self, text="Graph", command=self.btn_graph)
        self.graph_btn.grid(row=1, column=1, columnspan=1, sticky="nsew",padx=5,pady=5)
        
        # Exit button
        self.exit_btn = ttk.Button(self, text="Exit", command=self.btn_exit)
        self.exit_btn.grid(row=1, column=2, columnspan=1, sticky="nsew",padx=5,pady=5)

        # Info Part
        ttk.Label(
            text="To use the engine please set the settings and save the wanted values for the settings if not choosen it will automaticly be set for the equvilients of our world MADE BY xMOHADIx"
        ).grid(row=2, column=0, columnspan=2, sticky="nswe")

    def btn_visual(self):
        self.visual = True
        self._object_data = self.object_frame.objects
        self._setting_data = self.setting_frame.settings
        self.destroy()
    
    def btn_graph(self):
        self.graph = True
        self._object_data = self.object_frame.objects
        self._setting_data = self.setting_frame.settings
        self.destroy()
    def btn_exit(self):
        self.close = True
        self._object_data = self.object_frame.objects
        self._setting_data = self.setting_frame.settings
        self.destroy()


    @property
    def objects(self):
        return self._object_data

    @property
    def settings(self):
        return self._setting_data


class Object_Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self._objects = []

        # Configure grid columns
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        self.columnconfigure(7, weight=1)

        # Configure grid rows
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        # Listbox
        self.list_box = tk.Listbox(self)
        self.list_box.grid(row=0, column=0, rowspan=7, sticky="nsew", padx=0, pady=0)

        # Delete button
        self.del_btn = ttk.Button(self, text="Del", command=self.delete_button)
        self.del_btn.grid(row=0, column=1, sticky="nw", padx=0, pady=0)

        # Object Name
        ttk.Label(self, text="Object Name:").grid(
            row=0, column=2, sticky="ne", padx=5, pady=5
        )
        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(
            row=0, column=3, columnspan=4, sticky="nwe", padx=5, pady=5
        )

        # Mass Row
        ttk.Label(self, text="Mass:").grid(row=1, column=2, sticky="ne", padx=5, pady=5)
        self.mass_entry = ttk.Entry(self)
        self.mass_entry.grid(
            row=1, column=3, columnspan=4, sticky="nwe", padx=5, pady=5
        )
        ttk.Label(self, text="kg").grid(row=1, column=7, sticky="nw", padx=5, pady=5)

        # Velocity Row
        ttk.Label(self, text="Velocity:").grid(
            row=2, column=2, sticky="ne", padx=5, pady=5
        )
        self.velocity_entry_i = ttk.Entry(self)
        self.velocity_entry_i.grid(
            row=2, column=3, columnspan=1, sticky="nwe", padx=5, pady=5
        )
        tk.Label(self, text="i m/s").grid(row=2, column=4, sticky="nw", padx=5, pady=5)
        self.velocity_entry_j = ttk.Entry(self)
        self.velocity_entry_j.grid(
            row=2, column=5, columnspan=1, sticky="nwe", padx=5, pady=5
        )
        tk.Label(self, text="j m/s").grid(row=2, column=6, sticky="nw", padx=5, pady=5)

        # Accelaration Row
        ttk.Label(self, text="Accelaration:").grid(
            row=3, column=2, sticky="ne", padx=5, pady=5
        )
        self.accelaration_entry_i = ttk.Entry(self)
        self.accelaration_entry_i.grid(
            row=3, column=3, columnspan=1, sticky="nwe", padx=5, pady=5
        )
        tk.Label(self, text="i m/s^2").grid(
            row=3, column=4, sticky="nw", padx=5, pady=5
        )
        self.accelaration_entry_j = ttk.Entry(self)
        self.accelaration_entry_j.grid(
            row=3, column=5, columnspan=1, sticky="nwe", padx=5, pady=5
        )
        tk.Label(self, text="j m/s^2").grid(
            row=3, column=6, sticky="nw", padx=5, pady=5
        )

        # Corddinate Row
        ttk.Label(self, text="Coordinate:").grid(
            row=4, column=2, sticky="ne", padx=5, pady=5
        )
        self.x_entry = ttk.Entry(self)
        self.x_entry.grid(row=4, column=3, columnspan=1, sticky="nwe", padx=5, pady=5)
        tk.Label(self, text="x").grid(row=4, column=4, sticky="nw", padx=5, pady=5)
        self.y_entry = ttk.Entry(self)
        self.y_entry.grid(row=4, column=5, columnspan=1, sticky="nwe", padx=5, pady=5)
        tk.Label(self, text="y").grid(row=4, column=6, sticky="nw", padx=5, pady=5)

        # Add Button
        self.btn = ttk.Button(self, text="Add", command=self.add_button)
        self.btn.grid(row=5, column=3, columnspan=4, sticky="nwe", padx=5, pady=5)

    def add_button(self):
        # Define regex patterns
        scalar_regex = r"^-?\d+(?:\.\d+)?$"  # For mass
        vector_component_regex = r"^-?\d+(?:\.\d+)?$"  # For vector components
        
        # Get all data
        data = {
            "Name": self.name_entry.get(),
            "Mass": self.mass_entry.get(),
            "Velocity i": self.velocity_entry_i.get(),
            "Velocity j": self.velocity_entry_j.get(),
            "Acceleration i": self.accelaration_entry_i.get(),
            "Acceleration j": self.accelaration_entry_j.get(),
            "x": self.x_entry.get(),
            "y": self.y_entry.get()
        }
        
        # Check name
        if not data["Name"]:
            messagebox.showwarning("Warning", "Please enter a name!")
            return
        
        # Check mass (scalar)
        if not re.fullmatch(scalar_regex, data["Mass"]):
            messagebox.showwarning("Warning", "Mass must be a rational number!")
            return
        
        # Check vector components
        vector_fields = ["Velocity i", "Velocity j", 
                        "Acceleration i", "Acceleration j",
                        "x", "y"]
        
        for field in vector_fields:
            if not re.fullmatch(vector_component_regex, data[field]):
                messagebox.showwarning("Warning", f"{field} must be a rational number!")
                return
        
        # Add to list
        self.list_box.insert(tk.END, data["Name"])
        self.name_entry.delete(0, tk.END)
        self.mass_entry.delete(0,tk.END)
        self.velocity_entry_i.delete(0,tk.END)
        self.velocity_entry_j.delete(0,tk.END)
        self.accelaration_entry_i.delete(0,tk.END)
        self.accelaration_entry_j.delete(0,tk.END)
        self.x_entry.delete(0,tk.END)
        self.y_entry.delete(0,tk.END)
        self.objects.append(data)

    def delete_button(self):
        try:
            selected_index = self.list_box.curselection()
            if not selected_index:
                messagebox.showwarning("Warning", "Please select an item for deleting")
                return
            self.objects.remove(self.objects[int(selected_index[0])])
            self.list_box.delete(selected_index)
        except:
            messagebox.showerror("Error", "An Error occured")

    @property
    def objects(self):
        return self._objects


class Settings_Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self._settings = [
            {"Name": "Air", "Toggle": False, "Data": "1.225"},
            {"Name": "Planet Gravity", "Toggle": False, "Data": "9.8"},
            {"Name": "Gravitational Force", "Toggle": False, "Data": "0.000000000066743"},
        ]

        # The way for creating buttons
        """
        self.var = tk.BooleanVar()
        self.check = tk.Checkbutton(self, text="Toggle", variable=self.var, command=self.show_state)
        self.check.grid(row=0, column=0)
        """
        # Air ON OFF button
        ttk.Label(self, text="Air:").grid(row=0, column=0, sticky="nwe", padx=5, pady=5)
        self.air_var = tk.BooleanVar()
        self.air_check = tk.Checkbutton(
            self, text="", variable=self.air_var, command=self.air_func
        )
        self.air_check.grid(row=0, column=1, sticky="nw", padx=5, pady=5)
        ttk.Label(self, text="Density:").grid(
            row=0, column=2, sticky="nw", padx=5, pady=5
        )
        self.air_entry = ttk.Entry(self)
        self.air_entry.grid(row=0, column=3, sticky="nw", padx=5, pady=5)
        ttk.Label(self, text="kg/m^3").grid(
            row=0, column=4, sticky="nwe", padx=5, pady=5
        )

        # Planet Gravity ON OFF Button
        ttk.Label(self, text="Planet Gravity:").grid(
            row=1, column=0, sticky="nwe", padx=5, pady=5
        )
        self.planet_var = tk.BooleanVar()
        self.planet_check = tk.Checkbutton(
            self, text="", variable=self.planet_var, command=self.planet_func
        )
        self.planet_check.grid(row=1, column=1, sticky="nw", padx=5, pady=5)
        ttk.Label(self, text="Accelaration:").grid(
            row=1, column=2, sticky="nw", padx=5, pady=5
        )
        self.planet_entry = ttk.Entry(self)
        self.planet_entry.grid(row=1, column=3, sticky="nw", padx=5, pady=5)
        ttk.Label(self, text="m/s^2").grid(
            row=1, column=4, sticky="nwe", padx=5, pady=5
        )

        # Gravational Force
        ttk.Label(self, text="Gravitational Force:").grid(
            row=2, column=0, sticky="nwe", padx=5, pady=5
        )
        self.gravity_var = tk.BooleanVar()
        self.gravity_check = tk.Checkbutton(
            self, text="", variable=self.gravity_var, command=self.planet_func
        )
        self.gravity_check.grid(row=2, column=1, sticky="nw", padx=5, pady=5)
        ttk.Label(self, text="Constant:").grid(
            row=2, column=2, sticky="nw", padx=5, pady=5
        )
        self.gravity_entry = ttk.Entry(self)
        self.gravity_entry.grid(row=2, column=3, sticky="nw", padx=5, pady=5)

        # Save Button
        self.save_btn = ttk.Button(self, text="Save", command=self.save_button)
        self.save_btn.grid(row=3, column=0, columnspan=4, sticky="nwe", padx=5, pady=5)

    def air_func(self):
        if self._settings[0]["Toggle"] == False:
            self._settings[0]["Toggle"] = True
        else:
            self._settings[0]["Toggle"] = False

    def planet_func(self):
        if self._settings[1]["Toggle"] == False:
            self._settings[1]["Toggle"] = True
        else:
            self._settings[1]["Toggle"] = False

    def gravity_func(self):
        if self._settings[2]["Toggle"] == False:
            self._settings[2]["Toggle"] = True
        else:
            self._settings[2]["Toggle"] = False

    def save_button(self):
        self._settings[0]["Data"] = self.air_entry.get()
        self._settings[1]["Data"] = self.planet_entry.get()
        self._settings[2]["Data"] = self.gravity_entry.get()

    @property
    def settings(self):
        return self._settings

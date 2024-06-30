import tkinter as tk
from tkinter import messagebox

class Vehicle:
    def __init__(self, vehicle_type):
        # Initialize the Vehicle with a type (e.g., car, truck, plane, boat, or broomstick)
        self.vehicle_type = vehicle_type

    def __str__(self):
        # Return a string representation of the Vehicle
        return f"Vehicle Type: {self.vehicle_type}"

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # Initialize the Automobile with specific attributes, inheriting from Vehicle
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        # Return a string representation of the Automobile
        return (f"{super().__str__()}\n"
                f"Year: {self.year}\n"
                f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Doors: {self.doors}\n"
                f"Roof: {self.roof}")

class VehicleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Information")

        # Create labels and entries for vehicle attributes
        self.create_widgets()

    def create_widgets(self):
        # Vehicle Type Dropdown
        tk.Label(self.root, text="Vehicle Type:").grid(row=0, column=0)
        self.vehicle_type_var = tk.StringVar()
        self.vehicle_type_var.set("Car")
        vehicle_types = ["Car", "Truck", "Plane", "Boat", "Broomstick"]
        self.vehicle_type_menu = tk.OptionMenu(self.root, self.vehicle_type_var, *vehicle_types, command=self.on_vehicle_type_change)
        self.vehicle_type_menu.grid(row=0, column=1)

        # Year
        tk.Label(self.root, text="Year:").grid(row=1, column=0)
        self.year_entry = tk.Entry(self.root)
        self.year_entry.grid(row=1, column=1)

        # Make
        tk.Label(self.root, text="Make:").grid(row=2, column=0)
        self.make_entry = tk.Entry(self.root)
        self.make_entry.grid(row=2, column=1)

        # Model
        tk.Label(self.root, text="Model:").grid(row=3, column=0)
        self.model_entry = tk.Entry(self.root)
        self.model_entry.grid(row=3, column=1)

        # Doors
        tk.Label(self.root, text="Doors (2 or 4):").grid(row=4, column=0)
        self.doors_entry = tk.Entry(self.root)
        self.doors_entry.grid(row=4, column=1)

        # Roof
        tk.Label(self.root, text="Roof (solid or sun roof):").grid(row=5, column=0)
        self.roof_entry = tk.Entry(self.root)
        self.roof_entry.grid(row=5, column=1)

        # Submit Button
        tk.Button(self.root, text="Submit", command=self.create_automobile).grid(row=6, columnspan=2)

        # Initial state
        self.on_vehicle_type_change("Car")

    def on_vehicle_type_change(self, vehicle_type):
        # Disable door selection for boats and broomsticks
        if vehicle_type in ["Boat", "Broomstick"]:
            self.doors_entry.config(state="disabled")
            self.doors_entry.delete(0, tk.END)
        else:
            self.doors_entry.config(state="normal")

        # Disable roof selection for broomsticks
        if vehicle_type == "Broomstick":
            self.roof_entry.config(state="disabled")
            self.roof_entry.delete(0, tk.END)
        else:
            self.roof_entry.config(state="normal")

    def create_automobile(self):
        # Retrieve input values
        vehicle_type = self.vehicle_type_var.get()
        year = self.year_entry.get()
        make = self.make_entry.get()
        model = self.model_entry.get()
        doors = self.doors_entry.get()
        roof = self.roof_entry.get()

        # Validate inputs
        if not (vehicle_type and year and make and model):
            messagebox.showerror("Error", "All fields are required!")
            return

        if vehicle_type not in ["Boat", "Broomstick"] and not doors:
            messagebox.showerror("Error", "Doors are required for cars, trucks, and planes!")
            return

        if vehicle_type != "Broomstick" and not roof:
            messagebox.showerror("Error", "Roof is required for cars, trucks, and planes!")
            return

        try:
            year = int(year)
            if doors:
                doors = int(doors)
                if doors not in [2, 4]:
                    raise ValueError
            if roof and roof not in ["solid", "sun roof"]:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid input for year, doors, or roof!")
            return

        # Create Automobile instance
        automobile = Automobile(vehicle_type, year, make, model, doors if doors else "N/A", roof if roof else "N/A")

        # Display Automobile details
        messagebox.showinfo("Automobile Information", str(automobile))

        # Clear the form
        self.clear_form()

    def clear_form(self):
        # Reset all entry fields to default state
        self.vehicle_type_var.set("Car")
        self.year_entry.delete(0, tk.END)
        self.make_entry.delete(0, tk.END)
        self.model_entry.delete(0, tk.END)
        self.doors_entry.config(state="normal")
        self.doors_entry.delete(0, tk.END)
        self.roof_entry.config(state="normal")
        self.roof_entry.delete(0, tk.END)

        # Reset the initial state for Car
        self.on_vehicle_type_change("Car")

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

class TemperatureConverter:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x250")

        # Label and entry for input temperature
        self.temperature_label = ttk.Label(root, text="Enter Temperature:")
        self.temperature_label.pack(pady=10)
        self.temperature_entry = ttk.Entry(root)
        self.temperature_entry.pack(pady=10)

        # Label and combobox for selecting input unit
        self.input_unit_label = ttk.Label(root, text="Input Unit:")
        self.input_unit_label.pack(pady=5)
        self.input_unit_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit"], state="readonly")
        self.input_unit_combobox.pack(pady=5)
        self.input_unit_combobox.current(0)  # Set default selection to Celsius

        # Label and combobox for selecting output unit
        self.output_unit_label = ttk.Label(root, text="Output Unit:")
        self.output_unit_label.pack(pady=5)
        self.output_unit_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit"], state="readonly")
        self.output_unit_combobox.pack(pady=5)
        self.output_unit_combobox.current(1)  # Set default selection to Fahrenheit

        # Button to perform conversion
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_temperature)
        self.convert_button.pack(pady=20)

        # Labels to display the conversion result
        self.result_label = ttk.Label(root, text="Result:")
        self.result_label.pack(pady=10)
        self.result_value = ttk.Label(root, text="", font=("Helvetica", 14))
        self.result_value.pack(pady=10)

        # Bind combobox selection events to update the other combobox
        self.input_unit_combobox.bind("<<ComboboxSelected>>", self.update_output_unit)
        self.output_unit_combobox.bind("<<ComboboxSelected>>", self.update_input_unit)

    # Update output unit based on selected input unit
    def update_output_unit(self, event):
        input_unit = self.input_unit_combobox.get()
        if input_unit == "Celsius":
            self.output_unit_combobox.set("Fahrenheit")
        elif input_unit == "Fahrenheit":
            self.output_unit_combobox.set("Celsius")

    # Update input unit based on selected output unit
    def update_input_unit(self, event):
        output_unit = self.output_unit_combobox.get()
        if output_unit == "Celsius":
            self.input_unit_combobox.set("Fahrenheit")
        elif output_unit == "Fahrenheit":
            self.input_unit_combobox.set("Celsius")

    # Convert the temperature based on selected units
    def convert_temperature(self):
        try:
            # Get input temperature and selected units
            temperature = float(self.temperature_entry.get())
            input_unit = self.input_unit_combobox.get()
            output_unit = self.output_unit_combobox.get()

            # Perform the conversion based on selected units
            if input_unit == "Celsius" and output_unit == "Fahrenheit":
                result = celsius_to_fahrenheit(temperature)
                self.result_value.config(text=f"{result:.2f} °F")
            elif input_unit == "Fahrenheit" and output_unit == "Celsius":
                result = fahrenheit_to_celsius(temperature)
                self.result_value.config(text=f"{result:.2f} °C")
            elif input_unit == output_unit:
                # If input and output units are the same, just display the input temperature
                self.result_value.config(text=f"{temperature:.2f} °{input_unit[0]}")
            else:
                messagebox.showerror("Error", "Invalid conversion selection.")
        except ValueError:
            # Handle invalid temperature input
            messagebox.showerror("Error", "Invalid temperature entered. Please enter a numeric value.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()

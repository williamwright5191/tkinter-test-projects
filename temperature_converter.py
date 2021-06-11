import tkinter as tk

class KelvinConverter():

    def __init__(self):
        window = tk.Tk()
        window.title("Temperature Converter")

        frm_entry = tk.Frame(master=window)
        self.ent_temperature = tk.Entry(master=frm_entry, width=10)
        lbl_temperature = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}") 

        self.ent_temperature.grid(row=0, column=0, sticky="e")
        lbl_temperature.grid(row=0, column=1, sticky="w")

        btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=self.convert_kelvin)
        self.lbl_result = tk.Label(master=window, text="\N{KELVIN SIGN}")

        frm_entry.grid(row=0, column=0, padx=10)
        btn_convert.grid(row=0, column=1, pady=10)
        self.lbl_result.grid(row=0, column=2, padx=10)

        window.mainloop()

    def convert_kelvin(self):
        temp_fahrenheit = self.ent_temperature.get()

        temp_kelvin = ((int(temp_fahrenheit) - 32) * 5/9 + 273.15)
        self.lbl_result["text"] = f"{round(temp_kelvin, 2)} \N{KELVIN SIGN}"

def main():
    converter = KelvinConverter()
    

if __name__ == "__main__":
    main()
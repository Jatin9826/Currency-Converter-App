import tkinter as tk
from tkinter import ttk, messagebox
from api import get_currencies, call_api, format_latest_url
from currency import extract_api_result


class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter Pro")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        # Set theme colors
        self.bg_color = "#57bcf7"
        self.primary_color = "#f01d1d"
        self.secondary_color = "#2e7511"
        self.accent_color = "#00cec9"
        
        self.root.configure(bg=self.bg_color)
        
        # Load currencies
        self.currencies = get_currencies()
        
        # Create widgets
        self.create_widgets()
        
        # Center the window
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        # Main container frame
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_frame = tk.Frame(main_frame, bg=self.bg_color)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(
            header_frame, 
            text="Currency Converter Pro", 
            font=("Helvetica", 20, "bold"), 
            fg=self.primary_color,
            bg=self.bg_color
        ).pack(side=tk.LEFT)
        
        # Separator
        ttk.Separator(main_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)
        
        # Conversion form
        form_frame = tk.Frame(main_frame, bg=self.bg_color)
        form_frame.pack(fill=tk.X, pady=10)
        
        # From Currency
        tk.Label(
            form_frame, 
            text="From Currency", 
            font=("Helvetica", 10), 
            fg=self.primary_color,
            bg=self.bg_color
        ).grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.from_currency = ttk.Combobox(
            form_frame, 
            values=self.currencies, 
            state="readonly",
            font=("Helvetica", 10),
            height=15
        )
        self.from_currency.current(0)
        self.from_currency.grid(row=1, column=0, sticky=tk.EW, pady=(0, 15))
        
        # To Currency
        tk.Label(
            form_frame, 
            text="To Currency", 
            font=("Helvetica", 10), 
            fg=self.primary_color,
            bg=self.bg_color
        ).grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        
        self.to_currency = ttk.Combobox(
            form_frame, 
            values=self.currencies, 
            state="readonly",
            font=("Helvetica", 10),
            height=15
        )
        self.to_currency.current(1)
        self.to_currency.grid(row=3, column=0, sticky=tk.EW, pady=(0, 15))
        
        # Amount
        tk.Label(
            form_frame, 
            text="Amount", 
            font=("Helvetica", 10), 
            fg=self.primary_color,
            bg=self.bg_color
        ).grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        
        self.amount_entry = ttk.Entry(
            form_frame, 
            font=("Helvetica", 12),
            justify=tk.RIGHT
        )
        self.amount_entry.grid(row=5, column=0, sticky=tk.EW, pady=(0, 20))
        
        # Convert Button
        convert_btn = tk.Button(
            form_frame,
            text="CONVERT",
            command=self.convert_currency,
            bg=self.secondary_color,
            fg="white",
            font=("Helvetica", 12, "bold"),
            bd=0,
            padx=20,
            pady=10,
            activebackground=self.accent_color,
            activeforeground="white"
        )
        convert_btn.grid(row=6, column=0, sticky=tk.EW, pady=(10, 20))
        
        # Result Frame
        result_frame = tk.Frame(
            main_frame,
            bg="white",
            highlightbackground="#dfe6e9",
            highlightthickness=1,
            padx=10,
            pady=10
        )
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.result_label = tk.Label(
            result_frame, 
            text="Enter amount and currencies to convert", 
            font=("Helvetica", 11), 
            fg=self.primary_color,
            bg="white",
            wraplength=400,
            justify="center"
        )
        self.result_label.pack(expand=True)
        
        # Footer
        footer_frame = tk.Frame(main_frame, bg=self.bg_color)
        footer_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(
            footer_frame, 
            text="Currency Converter Pro v1.0", 
            font=("Helvetica", 8), 
            fg="#636e72",
            bg=self.bg_color
        ).pack(side=tk.RIGHT)

    def convert_currency(self):
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        amount = self.amount_entry.get()

        # Input Validation
        if not amount.strip().replace('.', '', 1).isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
            return

        url = format_latest_url(from_curr, to_curr) + f"&amount={amount}"
        response = call_api(url)

        if response:
            data = response.json()
            currency_obj = extract_api_result(data)
            currency_obj.reverse_rate()
            msg = (
                f"💰 Conversion Result\n\n"
                f"Date: {currency_obj.date}\n"
                f"Amount: {currency_obj.amount} {currency_obj.from_currency}\n"
                f"Result: {currency_obj.amount * currency_obj.rate:.4f} {currency_obj.to_currency}\n\n"
                f"Exchange Rate: 1 {currency_obj.from_currency} = {currency_obj.rate:.6f} {currency_obj.to_currency}\n"
                f"Inverse Rate: 1 {currency_obj.to_currency} = {currency_obj.inverse_rate:.6f} {currency_obj.from_currency}"
            )
            self.result_label.config(text=msg)
        else:
            messagebox.showerror("API Error", "Failed to fetch data from the API.")


if __name__ == "__main__":
    root = tk.Tk()
    
    # Set window icon (replace with your own icon if available)
    try:
        root.iconbitmap('currency_icon.ico')
    except:
        pass
    
    app = CurrencyConverterApp(root)
    root.mainloop()
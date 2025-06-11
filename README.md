Currency Converter App ✨

A Python desktop application to convert currencies using real-time exchange rates provided by the Frankfurter API. 
The app is built using Tkinter for the graphical interface and follows a clean modular architecture with API interaction, currency logic, CLI, GUI, and testing components.
🔧 Features

Real-time exchange rate retrieval using the Frankfurter API

Simple, modern GUI built using Tkinter

Dropdown selection for 30+ currencies

Input validation for currency amounts

Shows both direct and inverse exchange rates

CLI version for quick command-line conversions

Unit tests for core functionalities.

CurrencyConverterApp/
|
|-- api.py              # Handles API URL formatting and requests
|-- currency.py         # Currency class and logic for validation and result formatting
|-- main.py             # Command-line interface for currency conversion
|-- gui_app.py          # Tkinter-based GUI application
|-- test_currency.py    # Unit tests for validation and conversion logic
|-- requirements.txt    # List of required packages (mainly requests)
|-- README.md           # Project documentation


User Input (GUI or CLI)

→ Currency codes validated via Frankfurter /currencies endpoint

→ API request to /latest?from=XXX&to=YYY&amount=ZZ

→ JSON response parsed and processed

→ Output shown on terminal or GUI

![image](https://github.com/user-attachments/assets/71629449-c2df-4102-95d8-8e6fdf98b495)

👨‍💼 Author

Jatin KumarB.Tech CSE (AI & ML)

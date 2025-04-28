import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "4caeac3dec7d893123147d6b1b5efb64"

def get_weather():
    city = city_entry.get()
    if not city or city.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()

        result_label.config(
            text=f"📍 {city.title()}\n\n"
                 f"🌡 Temperature: {temperature}°C\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"🌤 Description: {description}",
            fg="#FFFFFF"
        )
    else:
        result_label.config(text="")
        messagebox.showerror("Error", f"City '{city}' not found.\nPlease check the spelling.")

# UI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#2c3e50")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Weather App", font=("Helvetica", 22, "bold"), bg="#2c3e50", fg="#1abc9c")
title_label.pack(pady=20)

# Entry Frame
entry_frame = tk.Frame(root, bg="#2c3e50")
entry_frame.pack()

city_entry = tk.Entry(entry_frame, width=25, font=("Helvetica", 14), bg="#ecf0f1", fg="#2c3e50", bd=0, justify='center')
city_entry.pack(ipady=8)
city_entry.insert(0, "Enter city name")

# Search Button
search_button = tk.Button(root, text="Get Weather", command=get_weather,
                          font=("Helvetica", 12, "bold"), bg="#1abc9c", fg="white",
                          activebackground="#16a085", activeforeground="white", bd=0, padx=20, pady=10)
search_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#2c3e50", justify="left")
result_label.pack(pady=10)

root.mainloop()

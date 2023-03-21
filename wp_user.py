import os
import requests
import tkinter as tk

def get_wp_username():
    targetdomain = domain_entry.get()
    urlpfad = "/wp-json/wp/v2/users"
    gesamtes = targetdomain + urlpfad
    response = requests.get(gesamtes)
    if response.status_code == 200:
        usernames = [user["name"] for user in response.json()]
        result_label.config(text="WordPress Username: " + ", ".join(usernames))
    else:
        result_label.config(text="Fehler: " + str(response.status_code))

root = tk.Tk()
root.title("WP User Check")

domain_label = tk.Label(root, text="Domain:")
domain_entry = tk.Entry(root)
get_button = tk.Button(root, text="Abfragen", command=get_wp_username)
result_label = tk.Label(root, text="")

domain_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
domain_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
get_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.EW)
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

root.mainloop()

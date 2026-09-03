
import requests
import tkinter as tk


def shorten_link(full_link):        #(full_link,link_name)
    API_KEY = "fdd899c6ba135a9e6b4e46a6bdbb6b3a"

    BASE_URL = "https://cutt.ly/api/api.php"

    payload = {
        'key': API_KEY,
        'short': full_link,
        #'name': link_name
       
    }

    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        # Show output in Tkinter
        output_entry.delete(0, tk.END)
        output_entry.insert(0, short_link)

    except:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, str(data))


def run_shortener():
    link = link_entry.get()
    #name = name_entry.get()

    shorten_link(link)        #(link,name)


# ---------------- TKINTER BOX----------------

root = tk.Tk()
root.title("Rifat's URL Shortener")
root.geometry("500x350")


# Heading
heading = tk.Label(
    root,
    text="URL Shortener",
    font=("Cooper Black", 20, "bold")
)
heading.pack(pady=20)


# Link input
link_entry = tk.Entry(
    root,
    width=50,
    font=("Courier New", 13)
)
link_entry.pack(pady=20)

link_entry.insert(0, "Enter your link...")


# Name input
#name_entry = tk.Entry(
    #root,
    #width=50,
    #font=("Courier New", 13))

#name_entry.pack(pady=20)

#name_entry.insert(0, "Give your link a name...")


# Button
button = tk.Button(
    root,
    text="Shorten Link",
    font=("Arial", 12),
    command=run_shortener
)
button.pack(pady=15)

#output statement
heading2 = tk.Label(
    root,
    text="Short Link will be generated here :- ",
    font=("Fixedsys", 15)
)
heading2.pack(pady=20)

# Output
output_entry = tk.Entry(
    root,
    width=50,
    font=("Arial", 13)
)
output_entry.pack(pady=20)


root.mainloop()
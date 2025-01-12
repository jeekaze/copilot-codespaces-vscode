import tkinter as tk

# Function to change the window content to the second page
def show_second_page():
    # Remove the current widgets from the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Add "Bus 1" button
    bus1_button = tk.Button(root, text="Bus 1", font=("Brush Script MT", 16), command=show_route1, bg="#008000", fg="white")
    bus1_button.pack(pady=10)

    # Add "Bus 2" button
    bus2_button = tk.Button(root, text="Bus 2", font=("Brush Script MT", 16), command=show_route2, bg="#0000FF", fg="white")
    bus2_button.pack(pady=10)
    
    # Add "Bus 3" button
    bus3_button = tk.Button(root, text="Bus 3", font=("Brush Script MT", 16), command=show_route3, bg="#FFD700", fg="white")
    bus3_button.pack(pady=10)

    # Add "Bus 4" button
    bus4_button = tk.Button(root, text="Bus 4", font=("Brush Script MT", 16), command=show_route4, bg="#FF4500", fg="white")
    bus4_button.pack(pady=10)

    # Add "Back" button
    back_button = tk.Button(root, text="Back", font=("Brush Script MT", 14), command=show_first_page, bg="#808080", fg="white")
    back_button.pack(side="bottom", pady=20)

# Function to show route from Assam to Agra (Bus 1)
def show_route1():
    # Remove the current widgets from the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Add route text
    route_label = tk.Label(root, text="Route:", font=("Brush Script MT", 24), bg="#ffcc00", fg="black")
    route_label.pack(pady=10)

    # Add a canvas to draw the route line
    canvas = tk.Canvas(root, width=400, height=100, bg="#ffcc00", highlightthickness=0)
    canvas.pack()

    # Draw the line representing the route
    canvas.create_line(50, 50, 350, 50, fill="black", width=4)

    # Add labels for Assam, West Bengal, and Agra
    canvas.create_text(50, 70, text="Assam", fill="black", font=("Brush Script MT", 16))
    canvas.create_text(200, 70, text="West Bengal", fill="black", font=("Brush Script MT", 16))
    canvas.create_text(350, 70, text="Agra", fill="black", font=("Brush Script MT", 16))

    # Add a green dot above West Bengal
    canvas.create_oval(195, 45, 205, 55, fill="green", outline="green")

    # Add black dots centered on Assam and Agra
    canvas.create_oval(45, 45, 55, 55, fill="black", outline="black")  # Centered on Assam
    canvas.create_oval(345, 45, 355, 55, fill="black", outline="black")  # Centered on Agra

    # Add total seats label
    seats_label = tk.Label(root, text="Total Seats: 69", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    seats_label.pack(pady=10)

    # Add available seats label
    available_seats_label = tk.Label(root, text="Available Seats: 50", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    available_seats_label.pack(pady=5)

    # Add occupied seats label
    occupied_seats_label = tk.Label(root, text="Occupied Seats: 19", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    occupied_seats_label.pack(pady=5)

    # Add "Back" button
    back_button = tk.Button(root, text="Back", font=("Brush Script MT", 14), command=show_second_page, bg="#808080", fg="white")
    back_button.pack(side="bottom", pady=20)

# Function to show route from Kerala to Kashmir (Bus 2)
def show_route2():
    # Remove the current widgets from the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Add route text
    route_label = tk.Label(root, text="Route:", font=("Brush Script MT", 24), bg="#ffcc00", fg="black")
    route_label.pack(pady=10)

    # Add a canvas to draw the route line
    canvas = tk.Canvas(root, width=400, height=100, bg="#ffcc00", highlightthickness=0)
    canvas.pack()

    # Draw the line representing the route
    canvas.create_line(50, 50, 350, 50, fill="black", width=4)

    # Add labels for Kerala, Maharashtra, and Kashmir
    canvas.create_text(50, 70, text="Kerala", fill="black", font=("Brush Script MT", 16))
    canvas.create_text(200, 70, text="Maharashtra", fill="black", font=("Brush Script MT", 16))
    canvas.create_text(350, 70, text="Kashmir", fill="black", font=("Brush Script MT", 16))

    # Add a green dot above Maharashtra
    canvas.create_oval(195, 45, 205, 55, fill="green", outline="green")

    # Add black dots centered on Kerala and Kashmir
    canvas.create_oval(45, 45, 55, 55, fill="black", outline="black")  # Centered on Kerala
    canvas.create_oval(345, 45, 355, 55, fill="black", outline="black")  # Centered on Kashmir

    # Add total seats label
    seats_label = tk.Label(root, text="Total Seats: 68", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    seats_label.pack(pady=10)

    # Add available seats label
    available_seats_label = tk.Label(root, text="Available Seats: 45", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    available_seats_label.pack(pady=5)

    # Add occupied seats label
    occupied_seats_label = tk.Label(root, text="Occupied Seats: 23", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    occupied_seats_label.pack(pady=5)

    # Add "Back" button
    back_button = tk.Button(root, text="Back", font=("Brush Script MT", 14), command=show_second_page, bg="#808080", fg="white")
    back_button.pack(side="bottom", pady=20)

# Function to show route for Bus 3
def show_route3():
    # Remove the current widgets from the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Add route text
    route_label = tk.Label(root, text="Route:", font=("Brush Script MT", 24), bg="#ffcc00", fg="black")
    route_label.pack(pady=10)

    # Add a canvas to draw the route line
    canvas = tk.Canvas(root, width=400, height=100, bg="#ffcc00", highlightthickness=0)
    canvas.pack()

    # Draw the line representing the route
    canvas.create_line(50, 50, 350, 50, fill="black", width=4)

    # Add labels for Karnataka, Goa, and Andhra Pradesh
    canvas.create_text(50, 70, text="Karnataka", fill="black", font=("Brush Script MT", 16))
    canvas.create_text(200, 70, text="Goa", fill="black", font=("Brush Script MT", 16))
    canvas.create_text(350, 70, text="Andhra Pradesh", fill="black", font=("Brush Script MT", 16))

    # Add a green dot above Goa
    canvas.create_oval(195, 45, 205, 55, fill="green", outline="green")

    # Add black dots centered on Karnataka and Andhra Pradesh
    canvas.create_oval(45, 45, 55, 55, fill="black", outline="black")  # Centered on Karnataka
    canvas.create_oval(345, 45, 355, 55, fill="black", outline="black")  # Centered on Andhra Pradesh

    # Add total seats label
    seats_label = tk.Label(root, text="Total Seats: 70", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    seats_label.pack(pady=10)

    # Add available seats label
    available_seats_label = tk.Label(root, text="Available Seats: 55", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    available_seats_label.pack(pady=5)

    # Add occupied seats label
    occupied_seats_label = tk.Label(root, text="Occupied Seats: 15", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    occupied_seats_label.pack(pady=5)

    # Add "Back" button
    back_button = tk.Button(root, text="Back", font=("Brush Script MT", 14), command=show_second_page, bg="#808080", fg="white")
    back_button.pack(side="bottom", pady=20)

# Function to show route for Bus 4
def show_route4():
    # Remove the current widgets from the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Add route text
    route_label = tk.Label(root, text="Route:", font=("Brush Script MT", 24), bg="#ffcc00", fg="black")
    route_label.pack(pady=10)

    # Add a canvas to draw the route line
    canvas = tk.Canvas(root, width=400, height=100, bg="#ffcc00", highlightthickness=0)
    canvas.pack()

    # Draw the line representing the route
    canvas.create_line(50, 50, 350, 50, fill="black", width=4)

    # Add labels for Maharashtra, Rajasthan, and Delhi
    canvas.create_text(50, 70, text="Maharashtra", fill="black", font=("Brush Script MT", 16))
    canvas.create_text(200, 70, text="Rajasthan", fill="black", font=("Brush Script MT", 16))
    canvas.create_text(350, 70, text="Delhi", fill="black", font=("Brush Script MT", 16))

    # Add a green dot above Rajasthan
    canvas.create_oval(195, 45, 205, 55, fill="green", outline="green")

    # Add black dots centered on Maharashtra and Delhi
    canvas.create_oval(45, 45, 55, 55, fill="black", outline="black")  # Centered on Maharashtra
    canvas.create_oval(345, 45, 355, 55, fill="black", outline="black")  # Centered on Delhi

    # Add total seats label
    seats_label = tk.Label(root, text="Total Seats: 80", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    seats_label.pack(pady=10)

    # Add available seats label
    available_seats_label = tk.Label(root, text="Available Seats: 60", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    available_seats_label.pack(pady=5)

    # Add occupied seats label
    occupied_seats_label = tk.Label(root, text="Occupied Seats: 20", font=("Brush Script MT", 16), bg="#ffcc00", fg="black")
    occupied_seats_label.pack(pady=5)

    # Add "Back" button
    back_button = tk.Button(root, text="Back", font=("Brush Script MT", 14), command=show_second_page, bg="#808080", fg="white")
    back_button.pack(side="bottom", pady=20)

# Function to show the first page
def show_first_page():
    # Remove the current widgets from the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Add "BUSINO" in large, Brush Script MT font
    busino_label = tk.Label(root, text="BUSINO", font=("Brush Script MT", 40, "bold"), fg="black", bg="#ffcc00", padx=20, pady=20)
    busino_label.pack(pady=50)

    # Button to show second page
    next_button = tk.Button(root, text="Click For Buses Details", font=("Brush Script MT", 16), command=show_second_page, bg="#ff0000", fg="white")
    next_button.pack()

# Create the main window for the first page
root = tk.Tk()
root.title("Busino - Transport App")

# Set window size and vibrant background color
root.geometry("400x400")
root.configure(bg="#ffcc00")  # Vibrant yellow background

# Start the main loop to run the app
show_first_page()
root.mainloop()

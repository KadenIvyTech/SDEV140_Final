"""
Kaden Stephens
10/14/23
this program allows a user to either create or view a help desk ticket.
when creating a ticket, the user can select the category of their issue and a text box for them to describe their problem.
when viewing tickets, you can select from a list of ticket ID, and it will display the ticket ID, category of the issue, user description of the issue, and the time and date of creation.
"""

__Author__ = "Kaden Stephens"

# import needed libraries
import tkinter as tk
from datetime import datetime
import json

"""
this class holds the user input data as well as the data created by the program
"""
class Ticket:
    def __init__(self, ticket_id, issue_category, user_issue, date_time):
        self.ticket_id = ticket_id
        self.issue_category = issue_category
        self.user_issue = user_issue
        self.date_time = date_time

# Initialize the current_ticket_id to 0
current_ticket_id = 0

# creates a dictionary for the submitted_tickets
submitted_tickets = {}

# created a function that saves the tickets to a JSON file
def save_tickets_to_file():
    with open("tickets.json", "w") as file:
        json.dump(submitted_tickets, file, default=lambda x: x.__dict__)

# created a function that loads tickets from the JSON file
def load_tickets_from_file():
    try:
        with open("tickets.json", "r") as file:
            data = json.load(file)
            global current_ticket_id
            # get the maximum ticket_id and load it and update current_ticket_id
            current_ticket_id = max(int(ticket_id) for ticket_id in data.keys())
            for ticket_id, ticket_data in data.items():
                submitted_tickets[int(ticket_id)] = Ticket(**ticket_data)
    except FileNotFoundError:
        pass
    
# create a function that submit that data recorded from there user as well as the data genrated by the program
# validates the user both selevted an options and enter the issue in the text widget
def submit_data(entry, option_variable, window):
    selected_option = option_variable.get()
    entered_text = entry.get("1.0", tk.END).strip()

    if not selected_option or entered_text == "":
        # Show an error message if the user hasn't selected an option or entered text
        error_message = tk.Toplevel(window)
        error_message.title("Error")
        error_label = tk.Label(error_message, text="Please select an option and describe your issue.")
        error_label.pack()
    else:
        global current_ticket_id
        # Increment ticket_id
        current_ticket_id += 1  

        # Get the current date and time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Create a Ticket object
        ticket = Ticket(str(current_ticket_id), selected_option, entered_text, current_time)

        # Store the ticket in the dictionary with ticket_id as the key
        submitted_tickets[current_ticket_id] = ticket

        # Save the data to the JSON file
        save_tickets_to_file()

        window.withdraw()
        main_window.deiconify()


# Load tickets from the JSON file
load_tickets_from_file()

"""
create the a function creates the main_window
the window has a header using an image
the window has a button that calls the open_create_ticket_window function
the window has a button that calls the open_view_tickets_window function
the window has a button that calls the exit_program function
"""
def main_window():
    global main_window
    main_window = tk.Tk()
    main_window.title("KS Help Desk Ticket System")
    main_window.geometry("800x400")
    main_window.configure(bg="#6748DB")

    # creates a header label with the adjusted image
    header_image = tk.PhotoImage(file="Header.gif")
    header_label = tk.Label(main_window, image=header_image, text="KS Help Desk Ticket System", bd=0)
    header_label.pack()

    # the frame for the main window
    frame = tk.Frame(main_window, bg="#6748DB")
    frame.pack(expand=True)

    # creates a button that calls the open_created_ticket_window function
    create_ticket_button = tk.Button(frame, text="Create a Ticket", command=open_created_ticket_window, width=15, height=2)
    create_ticket_button.pack(side="left", padx=10, pady=20)

    # creates a button that calls the open_view_tickets_window function
    view_tickets_button = tk.Button(frame, text="View Tickets", command=open_view_tickets_window, width=15, height=2)
    view_tickets_button.pack(side="left", padx=(40, 10), pady=20)

    # creates a button that calls the exit_program function
    exit_button = tk.Button(main_window, text="EXIT", command=exit_program, width=10)
    exit_button.pack(side="right", pady=10, padx=10)

    # when the window is closed, the program ends
    main_window.protocol("WM_DELETE_WINDOW", exit_program)

    main_window.mainloop()

# create a function that opens the create_ticket_window and closes the main_window
def open_created_ticket_window():
    main_window.withdraw()
    make_create_ticket_window()

# create a function that opens the view_tickets_window and closes the main_window
def open_view_tickets_window():
    main_window.withdraw()
    make_view_tickets_window()

# create a function that closes the other window and re-opens the main_window
def back_to_main(window):
    window.withdraw()
    main_window.deiconify()

# create a function that, if the user closes one of the non-main_windows, the program will close the window and re-show the main_window
def on_closing(window):
    window.withdraw()
    main_window.deiconify()
    window.destroy()
    main_window.protocol("WM_DELETE_WINDOW", exit_program)

# create a function to close the program
def exit_program():
    main_window.destroy()

"""
create a function that creates a new window called make_create_ticket_window.
the window has a back button in the top left corner
the window has a logo in the top right corner
the window has a title that tells the user to select a category
the window has a drop-down option
the window has a title telling the user to enter their issue
the window has a text entry for the user to enter their issue
the window has a submit button that saves their ticket
"""
def make_create_ticket_window():
    create_ticket_window = tk.Toplevel(main_window)
    create_ticket_window.title("Create Ticket")
    create_ticket_window.geometry("800x400")
    create_ticket_window.configure(bg="#6748DB")

    # adds the logo
    Logo = tk.PhotoImage(file="Logo.gif")
    logo_label = tk.Label(create_ticket_window, image=Logo, text="Logo", bd=0)
    logo_label.image = Logo
    logo_label.place(relx=1.0, rely=0.0, anchor="ne")

    # creates the back button
    back_button1 = tk.Button(create_ticket_window, text="Back", command=lambda: on_closing(create_ticket_window))
    back_button1.pack(anchor="nw", padx=10, pady=10)

    # creates the category select label
    title_label = tk.Label(create_ticket_window, text="Select the Category of Your Issue", bg="#6748DB")  # Set the background color here
    title_label.pack(padx=10, pady=10)

    # creates the drop-down options
    option_variable = tk.StringVar(create_ticket_window)
    # Set it to an empty string to display a blank option initially
    option_variable.set("")
    option_menu = tk.OptionMenu(create_ticket_window, option_variable, "Internet", "Email", "Blue Screen", "No video", "Other")
    option_menu.pack(padx=10, pady=10)

    # creates the issue description label
    issue_description_label = tk.Label(create_ticket_window, text="Describe the Issue You Are Having:", bg="#6748DB")  # Set the background color here
    issue_description_label.pack(padx=10, pady=(0, 10))

    # creates the issue description text entry box
    issue_description_entry = tk.Text(create_ticket_window, width=60, height=10)
    issue_description_entry.pack(fill="both", padx=10, pady=10)

    # creates a submit button that saves the data
    submit_button = tk.Button(create_ticket_window, text="Submit")
    submit_button.pack()
    submit_button.config(command=lambda: submit_data(issue_description_entry, option_variable, create_ticket_window))

    # if the window is closed, call the on_closing function
    create_ticket_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(create_ticket_window))

"""
create a function that creates a new window called make_view_tickets_window
the window has a back button in the top left corner
the window has a logo in the top right corner
the window has a title that tells the user to select a ticket
the window has a drop-down option of the created ticket ID
the window has an entry that displays the details of the selected ticket
there is a placeholder that will display if the user has not selected a ticket yet
"""
def make_view_tickets_window():
    window2 = tk.Toplevel(main_window)
    window2.title("View Tickets")
    window2.geometry("800x400")
    window2.configure(bg="#6748DB")

    # adds the logo
    logo = tk.PhotoImage(file="Logo.gif")  # Replace "your_image2.gif" with the path to your image
    logo_label = tk.Label(window2, image=logo, text="Logo", bd=0)
    logo_label.image = logo  # To prevent garbage collection
    logo_label.place(relx=1.0, rely=0.0, anchor="ne")

    # creates the back button
    back_button2 = tk.Button(window2, text="Back", command=lambda: on_closing(window2))
    back_button2.pack(anchor="nw", padx=10, pady=10)

    # creates the select label telling the user to select a ticket ID
    select_label = tk.Label(window2, text="Select a Ticket ID:", bg="#6748DB")
    select_label.pack(padx=10, pady=10)

    # declare the selected_ticket_id as a StringVar
    selected_ticket_id = tk.StringVar()
    # creates a drop-down menu to display available ticket IDs
    if submitted_tickets:
        ticket_id_dropdown = tk.OptionMenu(window2, selected_ticket_id, *submitted_tickets.keys())
        ticket_id_dropdown.pack(pady=10)
    else:
        # creates an empty dropdown with a disabled option if there are no tickets
        selected_ticket_id.set("No Tickets Found")
        ticket_id_dropdown = tk.OptionMenu(window2, selected_ticket_id, "No Tickets Found")
        ticket_id_dropdown.configure(state="disabled")
        ticket_id_dropdown.pack(pady=10)

    # creates a button to select and display the chosen ticket
    select_button = tk.Button(window2, text="Select", command=lambda: display_ticket(selected_ticket_id.get()))
    select_button.pack()

    # creates a widget to display ticket information
    ticket_info = tk.Text(window2, width=60, height=10)
    ticket_info.pack(fill="both", padx=10, pady=10)
    ticket_info.insert("1.0", "You haven't selected a ticket, please select a ticket or create one")
    ticket_info.tag_configure("placeholder", foreground="red")
    ticket_info.tag_add("placeholder", "1.0", "1.end")
    ticket_info.pack(fill="both", padx=10, pady=10)
    # Make the widget read-only
    ticket_info.config(state="disabled")

    """
    create a function to display the ticket in the widget.
    validate that the ticket that's selected is in the JSON file
    validate that a ticket is selected
    """
    def display_ticket(selected_ticket_id):
        try:
            # convert the selected_ticket_id to an integer
            ticket_id = int(selected_ticket_id)
            if ticket_id in submitted_tickets:
                ticket = submitted_tickets[ticket_id]
                # enable editing temporarily
                ticket_info.config(state="normal")
                # Clear the text in the widget
                ticket_info.delete("1.0", tk.END)
                ticket_info.insert(tk.END, f"Ticket ID: {ticket.ticket_id}\n")
                ticket_info.insert(tk.END, f"Issue Category: {ticket.issue_category}\n")
                ticket_info.insert(tk.END, f"User Issue:\n{ticket.user_issue}\n")
                ticket_info.insert(tk.END, f"Date and Time: {ticket.date_time}\n")
                # Make it read-only again
                ticket_info.config(state="disabled")
            else:
                # enable editing temporarily
                ticket_info.config(state="normal")
                # clear the text in the widget
                ticket_info.delete("1.0", tk.END)
                ticket_info.insert(tk.END, "Ticket not found.")
                # make it read-only again
                ticket_info.config(state="disabled")
        except ValueError:
            # enable editing temporarily
            ticket_info.config(state="normal")
            ticket_info.delete("1.0", tk.END)
            ticket_info.insert(tk.END, "Invalid Ticket ID.")
            # make it read-only again
            ticket_info.config(state="disabled")
            
    # if the window is closed, call the on_closing function
    window2.protocol("WM_DELETE_WINDOW", lambda: on_closing(window2))

# start only the main_window function on run
if __name__ == "__main__":
    main_window()

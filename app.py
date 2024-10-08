import tkinter as tk
from tkinter import messagebox

# Create the main window
def create_window():
    # MENU BAR-----------------------------------------------------------------------------------
    root = tk.Tk()
    root.title("Application with Menu Bar")
    
    # Set window icon
    root.iconbitmap("./logo.ico")  # Replace with your icon file path
    
    # window size and positions
    # Set window size (4:3 ratio)
    window_width = 800
    window_height = 600

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # print("screen_width:", screen_width, "screen_height:", screen_height)

    # Calculate center position
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    # print("x_coordinate:", x_coordinate, "y_coordinate:", y_coordinate)

    # Set window size and position
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    
    # Set the window to maximize
    root.state("zoomed")  # This will maximize the window
    
    # Define menu functions
    def add_item():
        messagebox.showinfo("Add", "The add functionality is not yet implemented")

    def show_help():
        messagebox.showinfo("Help", "This is the help content!")

    # Create the menu bar
    menu_bar = tk.Menu(root)

    # Create "File" menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Add", command=add_item)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=confirm_quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Create "Help" menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="Help", command=show_help)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    # Attach the menu bar to the window
    root.config(menu=menu_bar)

    # CONTENT PART--------------------------------------------------------------------------
    
    # Create a PanedWindow to hold the left and right panels
    paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
    paned_window.pack(fill="both", expand=True)

    # Create the left frame
    left_frame = tk.Frame(paned_window, bg="white", width=400)
    paned_window.add(left_frame)  # Add left frame to the paned window
    # print("width:", width)

    # Create the right frame
    right_frame = tk.Frame(paned_window, bg="white")
    paned_window.add(right_frame)  # Add right frame to the paned window

    # # Add content to the left frame
    # left_label = tk.Label(left_frame, text="Left Panel", bg="lightgray")
    # left_label.pack(padx=10, pady=10)

# Add "Database" title to the left frame
    # title_label = tk.Label(left_frame, text="Database", bg="white", font=("Arial", 12, "bold"))
    title_label = tk.Label(left_frame, text="Database", bg="white", font=("Arial", 12), anchor="w")  # 'anchor="w"' aligns to the left
    title_label.pack(pady=10)

    # Add lists to the left frame
    lists = [
        "Inboxes (5)",
        "Tags (10)",
        "Trash (2)",
        "Demo (127)",
        "Astronomy (104)",
        "Bookmarks (46)",
        "Feeds (1120)",
        "Nature (4)",
        "Office (1)",
        "Research (52)",
        "Sheets (4)",
        "WWF (12)",
        "All Images",
        "All PDF Documents",
        "Duplicates",
        "Release (454)",
        "Astronomy (254)"
    ]

    for item in lists:
        list_label = tk.Label(left_frame, text=item, bg="lightblue")
        list_label.pack(anchor="w", padx=20)  # Align to the left with padding


    # Add content to the right frame
    right_label = tk.Label(right_frame, text="Right Panel", bg="white")
    right_label.pack(padx=10, pady=10)
    
    return root

# Define quit function with confirmation
def confirm_quit():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.quit()
        
# Main entry point of the application
if __name__ == "__main__":
    root = create_window()
    
    # # Bind F11 to toggle maximized state
    # root.bind("<F11>", lambda event: root.state("normal") if root.state() == "zoomed" else root.state("zoomed"))
    # # Bind ESC to exit the application with confirmation
    # root.bind("<Escape>", lambda event: confirm_quit())
    
    # # Bind the closing event of the window to show the confirmation dialog
    # root.protocol("WM_DELETE_WINDOW", confirm_quit)
    
    root.mainloop()  # Start the main event loop

from tkinter import filedialog, messagebox, Tk



def select_folder_via_gui():
    root = Tk()
    root.withdraw()

    choose_folder = filedialog.askdirectory(
        initialdir='/Users/evgeniy/Pictures/2023',
        title="Select your Source directory")
    if len(choose_folder) > 0:
        return choose_folder
    else:
        messagebox.showwarning("Warning", "You haven't chosen a folder. Program terminated.")
        root.destroy()


if __name__ == '__main__':
    # display_info("NO KEYWORDS FOR WORK")
    select_folder_via_gui()

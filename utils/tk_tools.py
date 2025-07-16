from tkinter import filedialog, messagebox, Tk


def select_folder_via_gui(initial_dir):
    root = Tk()
    root.withdraw()

    choose_folder = filedialog.askdirectory(
        initialdir=initial_dir,
        title="Select your Source directory")
    if len(choose_folder) > 0:
        return choose_folder
    else:
        messagebox.showwarning("Warning", "You haven't chosen a folder. Program terminated.")
        root.destroy()




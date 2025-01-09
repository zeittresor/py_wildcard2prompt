import tkinter as tk
from tkinter import filedialog
import os

def transform_file(filepath, save_dir=None):
    folder, filename = os.path.split(filepath)
    name, ext = os.path.splitext(filename)
    new_filename = f"dp_{name}{ext}"

    if save_dir is not None:
        output_path = os.path.join(save_dir, new_filename)
    else:
        output_path = os.path.join(folder, new_filename)

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    transformed_lines = [line.replace(" ", "_") for line in lines]
    joined_string = "{%s}" % "|".join(transformed_lines)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(joined_string)

    return output_path

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return

    save_question = tk.messagebox.askyesno("Choose Save Location", "Do you want to choose a different save location?")
    if save_question:
        save_dir = filedialog.askdirectory(title="Select a target folder")
        if not save_dir:
            return
    else:
        save_dir = None

    output_path = transform_file(file_path, save_dir)
    tk.messagebox.showinfo("Done", f"File has been created:\n{output_path}")

def main():
    root = tk.Tk()
    root.title("File Transformer")
    root.geometry("300x150")

    open_btn = tk.Button(root, text="Select Text File", command=select_file)
    open_btn.pack(pady=20)

    import tkinter.messagebox
    root.mainloop()

if __name__ == "__main__":
    main()

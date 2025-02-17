import os

from tkinter import filedialog, ttk
import pandas as pd
import tkinter as tk


class CSVViewerApp(object):
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Viewer")
        self.root.geometry("800x500")

        # Button to open CSV file
        self.open_button = tk.Button(root, text="Open CSV", command=self.load_csv, padx=10, pady=5)
        self.open_button.pack(pady=10)

        # Treeview for displaying table
        self.tree_frame = tk.Frame(root)
        self.tree_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(self.tree_frame, show="headings")
        self.tree.pack(side="left", fill="both", expand=True)

        # Scrollbars
        self.v_scroll = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.h_scroll = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        self.v_scroll.pack(side="right", fill="y")
        self.h_scroll.pack(side="bottom", fill="x")

        # TODO(x): Remove before release.
        self.load_csv('/home/data/work/test.csv')

    def load_csv(self, file_path=None):
        file_path = file_path or filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path is None or not os.path.exists(file_path):
            return

        # Read CSV
        df = pd.read_csv(file_path)

        # Clear old data
        self.tree.delete(*self.tree.get_children())

        # Set column headers
        self.tree["columns"] = list(df.columns)
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)

        # Insert data
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewerApp(root)
    root.mainloop()

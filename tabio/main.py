import os

from absl import app, logging
from tkinter import filedialog, ttk
import pandas as pd
import tkinter as tk


class TabioApp(object):
    def __init__(self):
        self.df = None

        self.root = tk.Tk()
        self.root.title("Tabio")
        self.root.geometry("1200x900")

        self.toolbox = tk.Frame(self.root)
        self.toolbox.pack(fill="x")
        self.open_button = ttk.Button(self.toolbox, text="Open", command=self.load_file)
        self.open_button.pack(side="left")
        self.transpose_button = ttk.Button(self.toolbox, text="Transpose", command=self.transpose)
        self.transpose_button.pack(side="left")

        # Treeview for displaying table
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(self.tree_frame, show="headings")
        self.tree.tag_configure("evenrow", background="#E8E8E8")
        self.tree.tag_configure("oddrow", background="white")

        self.v_scroll = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.h_scroll = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.v_scroll.grid(row=0, column=1, sticky="ns")
        self.h_scroll.grid(row=1, column=0, sticky="ew")
        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)

        # TODO(x): Remove before release.
        self.load_file('/home/data/work/test.csv' if os.name == 'posix' else 'C:/test.csv')

    def load_file(self, file_path=None):
        file_path = file_path or filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path is None or not os.path.exists(file_path):
            logging.error(F"Invalid file path: {file_path}")
            return
        # TODO(x): Add more file types.
        self.df = pd.read_csv(file_path, sep=None, engine="python")
        self.refresh()

    def transpose(self):
        if self.df is not None:
            self.df = self.df.T
            self.refresh()

    def refresh(self):
        if self.df is None:
            return
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(self.df.columns)
        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100, stretch=False)
        for i, row in self.df.iterrows():
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=list(row), tags=(tag,))

    def run(self):
        self.root.mainloop()


def main(argv):
    TabioApp().run()


if __name__ == "__main__":
    app.run(main)

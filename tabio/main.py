import os

from absl import app, logging
from tkinter import filedialog, ttk
import pandas as pd
import tkinter as tk

from tabio.df_plotter import DFPlotter


CHECK_ON = "☑"
CHECK_OFF = "☐"


class TabioApp(object):
    def __init__(self):
        self.df = None

        self.root = tk.Tk()
        self.root.title("Tabio")
        self.root.geometry("1200x900")

        # Toolbox row 1.
        self.toolbox1 = tk.Frame(self.root)
        self.toolbox1.pack(fill="x")
        ttk.Button(self.toolbox1, text="Open", command=self.load_file).pack(side="left")
        ttk.Button(self.toolbox1, text="Transpose", command=self.transpose).pack(side="left")

        # Toolbox row 2 for plotting.
        self.toolbox2 = tk.Frame(self.root)
        self.toolbox2.pack(fill="x")

        tk.Label(self.toolbox2, text="Plot As").pack(side="left")
        self.plot_button = tk.StringVar(self.root)
        self.plot_button.set("Histogram")
        plot_types = ["Histogram", "Scatter", "Line"]
        tk.OptionMenu(self.toolbox2, self.plot_button, *plot_types, command=self.on_plot).pack(side="left")

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
        self.load_file("/home/data/work/test.csv" if os.name == "posix" else "C:/test.csv")

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
            self.tree.heading(col, text=F"{col} {CHECK_OFF}", command=lambda _col=col: self.toggle_column(_col))
            self.tree.column(col, anchor="center", width=100, stretch=False)

        for i, row in self.df.iterrows():
            if type(i) is not int:
                return
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=list(row), tags=(tag,))

    def toggle_column(self, column):
        text = self.tree.heading(column)["text"]
        mark = CHECK_ON if text.endswith(CHECK_OFF) else CHECK_OFF
        self.tree.heading(column, text=F"{text[:-1]}{mark}")

    def on_plot(self, plot_type):
        # Plot the selected columns based on the plot type with matplotlib.
        selected = [col for col in self.df.columns if self.tree.heading(col)["text"].endswith(CHECK_ON)]
        if not selected:
            logging.error("No columns selected for plotting.")
            return
        logging.info(F"Plotting {selected} as {plot_type}.")
        df_plotter = DFPlotter(self.df[selected])
        if plot_type == "Line":
            df_plotter.line()
        elif plot_type == "Scatter":
            df_plotter.scatter()
        elif plot_type == "Histogram":
            df_plotter.hist()
        else:
            logging.error(F"Unsupported plot type: {plot_type}.")

    def run(self):
        self.root.mainloop()


def main(argv):
    TabioApp().run()


if __name__ == "__main__":
    app.run(main)

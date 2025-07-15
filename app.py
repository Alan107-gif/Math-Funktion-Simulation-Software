import tkinter as tk
from tkinter import messagebox
import math

from expression import detect_variables
from domain import Domain
from evaluation import compute_values, compute_stats
from plot import draw_line_plot


class FunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Function Explorer")
        self.func_var = tk.StringVar()
        tk.Label(root, text="Enter function f(...):").pack(padx=10, pady=5)
        tk.Entry(root, textvariable=self.func_var, width=50).pack(padx=10, pady=5)
        tk.Button(root, text="Define Domains", command=self.open_domain_window).pack(pady=10)
        self.domain_win = None
        self.domain_entries = {}
        self.variables = []
        self.expr = ""

    def open_domain_window(self):
        expr = self.func_var.get()
        if not expr:
            messagebox.showerror("Input Error", "Please enter a function expression.")
            return
        try:
            vars_found = detect_variables(expr)
        except Exception as exc:
            messagebox.showerror("Parse Error", str(exc))
            return
        if not vars_found:
            messagebox.showerror("Parse Error", "No variables detected in expression.")
            return
        self.variables = vars_found
        self.expr = expr
        if self.domain_win:
            self.domain_win.destroy()
        self.domain_win = tk.Toplevel(self.root)
        self.domain_win.title("Variable Domains")
        self.domain_entries = {}
        for row, var in enumerate(self.variables):
            tk.Label(self.domain_win, text=var).grid(row=row, column=0, padx=5, pady=5)
            e_start = tk.Entry(self.domain_win, width=7)
            e_start.insert(0, "0")
            e_start.grid(row=row, column=1, padx=5)
            e_end = tk.Entry(self.domain_win, width=7)
            e_end.insert(0, "10")
            e_end.grid(row=row, column=2, padx=5)
            e_step = tk.Entry(self.domain_win, width=7)
            e_step.insert(0, "1")
            e_step.grid(row=row, column=3, padx=5)
            self.domain_entries[var] = (e_start, e_end, e_step)
        tk.Button(self.domain_win, text="Compute", command=self.compute).grid(columnspan=4, pady=10)

    def compute(self):
        domains = {}
        try:
            for var, entries in self.domain_entries.items():
                start = float(entries[0].get())
                end = float(entries[1].get())
                step = float(entries[2].get())
                domains[var] = Domain(start, end, step)
        except Exception as exc:
            messagebox.showerror("Domain Error", str(exc))
            return
        try:
            combos, results = compute_values(self.expr, self.variables, domains)
            stats = compute_stats(results)
        except Exception as exc:
            messagebox.showerror("Evaluation Error", str(exc))
            return
        self.show_results(combos, results, stats, domains)

    def show_results(self, combos, results, stats, domains):
        win = tk.Toplevel(self.root)
        win.title("Results")
        row = 0
        for key, val in stats.items():
            tk.Label(win, text=f"{key}: {val}").grid(row=row, column=0, sticky="w", padx=5)
            row += 1
        table = tk.Text(win, width=60, height=10)
        table.grid(row=0, column=1, rowspan=row)
        table.insert(tk.END, "Values:\n")
        for combo, res in zip(combos, results):
            table.insert(tk.END, f"{combo} -> {res}\n")
        table.config(state=tk.DISABLED)
        plot_row = row
        for var in self.variables:
            canvas = tk.Canvas(win, width=400, height=300, bg="white")
            canvas.grid(row=plot_row, column=0, columnspan=2, pady=10)
            xs = domains[var].values()
            midpoint = {v: domains[v].values()[len(domains[v].values()) // 2] for v in self.variables}
            ys = []
            env = {name: None for name in self.variables}
            env.update(math.__dict__)
            for x in xs:
                env.update(midpoint)
                env[var] = x
                ys.append(eval(self.expr, {"__builtins__": {}}, env))
            draw_line_plot(canvas, xs, ys, f"{var} effect")
            plot_row += 1


def main():
    root = tk.Tk()
    FunctionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk  # GUI ფანჯრების შესაქმნელად
from tkinter import messagebox # გაფრთხილების ან საინფორმაციო ფანჯრების გამოსაჩენად
import os

from data_loader import EVDataLoader
from data_processor import EVDataProcessor
from database_manager import DatabaseManager
from visualizer import EVVisualizer

class EVGuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Electric vehicle data analysis")
        self.df = None
        self.processor = None
        self.csv_path = os.path.join("..", "data", "Electric_Vehicle_Population_Data (1).csv")
        self.db_path = os.path.join("..", "database", "ev_data.db")
        self._build_ui()


    def _build_ui(self):
        tk.Button(self.root, text="Load csv", width=30, command=self.load_csv).pack(pady=5)
        tk.Button(self.root, text="Process Data", width=30, command=self.process_data).pack(pady=5)
        tk.Button(self.root, text="Save to Database", width=30, command=self.save_to_db).pack(pady=5)
        tk.Button(self.root, text="Show Carts", width=30, command=self.show_charts).pack(pady=5)


    def load_csv(self):
        try:
            loader = EVDataLoader(self.csv_path)
            self.df = loader.load_data()
            messagebox.showinfo("warmatebulia",f"monatsemebi tsarmatebit chaitvirta, chanatserebis raodenoba:{len(self.df)}")
        except Exception as e:
            messagebox.showerror("error",str(e))

    def process_data(self):
        if self.df is None:
            messagebox.showwarning("jer chatvirtet CSV faili!!")
            return
        self.processor = EVDataProcessor(self.df)
        messagebox.showinfo("warmatebulia","Monatsemebi tsarmatebit damushavda")

    def save_to_db(self):
        if self.processor is None:
            messagebox.showwarning("jer daamushavet monatsemebi!")
            return
        os.makedirs(os.path.dirname(self.db_path), exist_ok = True)
        db = DatabaseManager(self.db_path)

        by_year = self.processor.vehicles_by_year()
        by_make = self.processor.vehicles_by_make().head(10)
        by_type = self.processor.vehicle_type_distribution()

        db.save_dataframe(by_year.reset_index(name="count"), "vehicles_by_year")
        db.save_dataframe(by_make.reset_index(name="count"), "vehicles_by_make")
        db.save_dataframe(by_type.reset_index(name="count"), "vehicles_by_distribution")
        messagebox.showinfo("warmatebulia", "monatsemebi shenakhulia monatsemta bazashi")

    def show_charts(self):
        if self.processor is  None:
            messagebox.showwarning("jer daamushavet monatsemebi!")
            return

        visualizer = EVVisualizer()

        visualizer.plot_line(
            self.processor.vehicles_by_year(),
            "Number of electric vehicles by year",
                "Model year",
            "Vehicle count"
        )

        visualizer.plot_bar(
            self.processor.vehicles_by_make().head(10),
            "Top 10 electric vehicle manufacturers",
            "manufacturer",
            "vehicle count"
        )

        visualizer.plot_pie(
            self.processor.vehicle_type_distribution(),
            "Electric vehicle type distribution",
        )

if __name__ == "__main__":
    main__root = tk.Tk()
    app = EVGuiApp(main__root)
    main__root.mainloop()

































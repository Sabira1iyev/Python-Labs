# main.py aertianebs da martavs klasesa da modulebs ert adgilas
from  data_loader import EVDataLoader
from data_processor import EVDataProcessor
from database_manager import DatabaseManager
from threaded_writer import ThreadedWriter
from visualizer import EVVisualizer
import os # sashualebas gvadlevs vmartot pailebi, saqaghaldebi da operatsiuli sistemis skhva punktsiebi


def main():


    csv_path = os.path.join("..", "data", "Electric_Vehicle_Population_Data (1).csv") #ინახავს ფაილის გზას, რაც ამარტივებს
                                                                            # CSV-თან წვდომას პროგრამის სხვა ნაწილებიდან

    db_path = os.path.join("..", "database", "ev_data.db") #განსაზღვრავს SQLite მონაცემთა ბაზის შესანახ ადგილსა და ფაილის სახელს

    os.makedirs(os.path.dirname(db_path), exist_ok=True) #ქმნის მონაცემთა ბაზის საქაღალდეს, თუ ის არ არსებობს, ხოლო თუ არსებობს არაფერს ცვლის

    loader = EVDataLoader(csv_path)  # CSV ფაილის გზას გადასცემს EVDataLoader კლასს
    df = loader.load_data()

    if df is None:   # თუ DataFrame-ი არარის
        print("monatsemebis chatvirtva ver mokherkhda, programa mushaobas asrulebs")
        return
    print("monatsemebi tsarmatebit chaitvirta") # თუ არის
    print(f"chanatserebis saerto raodenoba: {len(df)}")

    processor = EVDataProcessor(df)   # წაკითხულ ცხრილს-DataFrame გადასცემს EVDataProcessor კლასს

    vehicles_by_year = processor.vehicles_by_year()
    vehicles_by_make = processor.vehicles_by_make().head(10) #head(10)-ის საშუალებით ვიღებთ პირველ 10 ჩანაწერს.
    vehicle_type_dist = processor.vehicle_type_distribution()

    db_manager = DatabaseManager(db_path) # აქ მონაცემთა ბაზის გზა გადაეცემა DatabaseManager კლასს

    def write_to_db():    # ფუნქცია მოიცავს SQLite-ში მონაცემების შენახვის ნაბიჯებს
        db_manager.save_dataframe(
            vehicles_by_year.reset_index(name="count"),  # reset_index() – სერიის ინდექსს გარდაქმნის სვეტად,
            "vehicles_by_year"                                   # ანუ Model Year ხდება ჩვეულებრივი სვეტი
        )                                                # name='count' – ძველი სერიის მნიშვნელობები ანუ რიცხვები
        db_manager.save_dataframe(                                       # ხდება სვეტი სახელწოდებით count
            vehicles_by_make.reset_index(name="count"),
            "vehicles_by_make"
        )
        db_manager.save_dataframe(
            vehicle_type_dist.reset_index(name="count"),
            "vehicles_by_distribution"
        )
        print("monatsemebi sheinakha SQLite monatsemta bazashi")

    writer = ThreadedWriter(write_to_db)
    writer.start()
    writer.join()

    visualizer = EVVisualizer() # ვქმნით ობიექტს EVVisualizer კლასიდან

    # წლების მიხედვით ავტომობილების რაოდენობას აჩვენებს ხაზოვანი გრაფიკით
    visualizer.plot_line(
        vehicles_by_year,
        "elektromobilebis raodenoba tslebis mikhedvit",
        "modelis tseli",
        "avtomobilebis raodenoba"
    )

    # მარკების მიხედვით ავტომობილების რაოდენობას აჩვენებს სვეტოვანი გრაფიკით
    visualizer.plot_bar(
        vehicles_by_make,
        "qvelaze popularuli ati elektromobilis brendi",
        "brendi",
        "avtomobilebis raodenoba"
    )

    # ავტომობილის ტიპებს (BEV/PHEV) აჩვენებს წრიული გრაფიკით
    visualizer.plot_pie(
        vehicle_type_dist,
        "Elektromobilebis tipebis ganatsileba(BEH/PHEV)"
    )

if __name__ == "__main__":
    main()

































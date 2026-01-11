# EVDataLoader: კითხულობს მოცემულ CSV ფაილს და აბრუნებს მას Pandas DataFrame-ის სახით
# ფაილის ვერპოვნის ან წაკითხვისას შეცდომის შემთხვევაში, გამოაქვს გაფრთხილება და აბრუნებს None-ს


import pandas as pd   # ტვირთავს Pandas ბიბლიოთეკას და საშუალებას გვაძლევს გამოვიყენოთ ის „pd“ შემოკლებით.
                    #   ბიბლიოთეკა, რომელიც საშუალებას გვაძლევს წავიკითხოთ და დავამუშაოთ CSV, Excel და JSON ფაილები ცხრილების ანუ DataFrame სახით

class EVDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path # CSV ფაილის გზას ინახავს კლასის შიგნით
    def load_data(self):
        try:   # აქ ვათავსებთ CSV ფაილის წაკითხვის პროცესს
            df = pd.read_csv(self.file_path)  # Pandas-ის მეშვეობით კითხულობს CSV ფაილს, წარმატებული წაკითხვის შემთხვევაში მონაცემებს ანიჭებს df ცვლადს DataFrame-ის სახით
            return df
        except FileNotFoundError:  # ფაილის არ-არსებობის შემთხვევაში
            print("csv file not found")
            return None
        except Exception as e: # სხვა პრობლემების შემთხვევაში
            print("error loading csv", e)
            return None

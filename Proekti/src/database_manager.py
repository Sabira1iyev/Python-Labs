# DatabaseManager კლასი უზრუნველყოფს დამუშავებული მონაცემების შენახვას
# SQLite3 მონაცემთა ბაზაში და ერთ ადგილზე აერთიანებს ბაზასთან დაკავშირებულ ყველა ოპერაციას.

# sqlite3 => SQLite მონაცემთა ბაზასთან დაკავშირება, Pandas DataFrame-ების შენახვა ცხრილების სახით

import sqlite3

class DatabaseManager:
    def __init__(self,db_path):
        self.db_path = db_path
    def connect(self): # იყენებს db_path ფაილს, რომელიც გადავეცით DatabaseManager-ს და ქმნის კავშირის ობიექტს
        return sqlite3.connect(self.db_path)  # sqlite3.connect => დაუკავშირდით მონაცემთა ბაზას
    def save_dataframe(self,df,table_name): # იღებს Pandas DataFrame-ს და ინახავს მას SQLite მონაცემთა ბაზაში ცხრილის სახით
        conn = self.connect() #ხსნის კავშირს SQLite მონაცემთა ბაზასთან
        df.to_sql(table_name,conn,if_exists="replace",index=False)
        conn.close()
                                # df.to_sql => პირდაპირ წერს Pandas DataFrame-ს ცხრილის სახით SQLite მონაცემთა ბაზაში
                                # table_name =>შესაქმნელი ცხრილის სახელი
                                # conn => რომელ მონაცემთა ბაზაში ჩაიწერება
                                # if_exists = "replace" =>  თუ ცხრილი არსებობს, წაშალე და თავიდან ჩაწერე
                                # index=False => არ ჩაწერო DataFrame-ის ინდექსი ცხრილში
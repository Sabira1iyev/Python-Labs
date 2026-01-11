from base_analyzer import BaseAnalyzer

class EVDataProcessor(BaseAnalyzer): # ახდენს BaseAnalyzer კლასის იმპორტირებას
    def vehicles_by_year(self): # აჯგუფებს ავტომობილების რაოდენობას მოდელის წლის მიხედვით და აბრუნებს შედეგს
        return self.df.groupby("Model Year").size()
    # groupby("Model Year") => აიღე თითოეული განსხვავებული მნიშვნელობა 'Model Year' სვეტიდან, როგორც ცალკეული ჯგუფი
    # size() => ითვლის სტრიქონების რაოდენობას თითოეულ ჯგუფში (წელში), ანუ რამდენი ავტომობილია იმ კონკრეტულ წელს

    def vehicles_by_make(self):
        return self.df.groupby("Make").size().sort_values(ascending=False)
    # ითვლის თითოეული ბრენდის ავტომობილების რაოდენობას
    # sort_values(ascending=False) => დაალაგე ეს რიცხვები კლებადობის მიხედვით
    # ascending=False => ნიშნავს კლებადობის მიხედვით

    def vehicle_type_distribution(self):
        return self.df.groupby("Electric Vehicle Type").size()
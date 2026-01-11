import matplotlib.pyplot as plt

class EVVisualizer:
    def plot_bar(self,data,title,xlabel,ylabel):
        data.plot(kind="bar") # მონაცემებს გამოსახავს სვეტოვანი გრაფიკის - Bar Chart სახით
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_line(self,data,title, xlabel, ylabel):
        data.plot(kind="line") # ხაზოვანი გრაფიკის - Line Chart სახით
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def plot_pie(self, data,title):
        data.plot(kind="pie", autopct="%1.1f%%") # წრიული გრაფიკის - Pie Chart)
        plt.title(title)                   # autopct="%1.1f%%"-ის მეშვეობით თითოეული
        plt.ylabel("")                     # სეგმენტის პროცენტულ წილს აჩვენებს გრაფიკზე
        plt.show()
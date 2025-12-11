import csv
import matplotlib.pyplot as plt

class logic:
    def __init__(self):
        self.x = []
        self.y = []

    def load_csv(self, filename):
        self.data = []
        self.filename = filename
        with open(self.filename, "r") as f:
            reader = csv.reader(f)

            header = next(reader)
            for row in reader:
                converted = []
                for cell in row:
                    try:
                        converted.append(float(cell))
                    except ValueError:
                        converted.append(cell)
                self.data.append(converted)
        return self.data
    
    def grab_cols(self, data):
        num_cols = len(data[0])

        print("\nAvailable columns:")
        for i in range(num_cols):
            print(f"{i} = Column {i}")

        x_col = int(input("[+] Enter X column number: "))
        y_col = int(input("[+] Enter Y column number: "))

        self.x = [row[x_col] for row in data]
        self.y = [row[y_col] for row in data]
        return self.x, self.y

    def show_graphs(self, data, x, y, choice):
        
        if choice == "1":
            plt.plot(x, y)
            plt.title("Line Graph")
            plt.show()
            file = "line_graph.png"
            plt.savefig(file)

        if choice == "2":
            plt.scatter(x, y)
            plt.title("Scatter Graph")
            plt.show()
            file = "bar_graph.png"
            plt.savefig(file)

        if choice == "3":
            plt.bar(x, y)
            plt.title("Bar Graph")
            plt.show()
            file = "bar_graph.png"
            plt.savefig(file)


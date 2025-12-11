import csv
import matplotlib.pyplot as plt
import os

class logic:
    def __init__(self):
        self.graph_dir = os.path.abspath("./stathat-graphs")
        if not os.path.exists(self.graph_dir):
            os.mkdir(self.graph_dir)
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

        x_col = int(input("[?] Enter X column number: "))
        y_col = int(input("[?] Enter Y column number: "))

        self.x = [row[x_col] for row in data]
        self.y = [row[y_col] for row in data]
        return self.x, self.y

    def show_graphs(self, x, y, choice):
        graph_type = {
            1: ("plot", "Line Graph", "line_graph.png"),
            2: ("scatter", "Scatter Graph", "scatter_graph.png"),
            3: ("bar", "Bar Graph", "bar_graph.png")
        }
        
        if choice not in graph_type:
            print("[-] QUITTING... Invalid graph choice.")
            quit(1)
        
        plot_type, title, file = graph_type[choice]

        plt.figure()
        getattr(plt, plot_type)(x, y)
        plt.title(title)
        plt.savefig(f"{self.graph_dir}/{file}")
        plt.show()
    
    def clean_up(self):
        os.system('clear' if os.name == 'posix' or 'unix' else 'cls')
        print("[!] Cleaning up resources...")
        plt.close("all")
        print("[!] Cleaned up matplotlib resources.")
        print("[!] Exiting logic module.")
        print("[!] Goodbye!")
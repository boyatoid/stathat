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

    def load_csv(self, filename: str) -> list:
        '''Loads CSV file and returns a readable list'''
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
    
    def grab_cols(self, data: list) -> tuple:
        '''Grabs two columns from the data based on user input'''
        num_cols = len(data[0])

        print("\nAvailable columns:")
        for i in range(num_cols):
            print(f"{i} = Column {i}")

        x_col = int(input("[?] Enter X column number: "))
        y_col = int(input("[?] Enter Y column number: "))

        self.x = [row[x_col] for row in data]
        self.y = [row[y_col] for row in data]
        print(f"[+] Grabbed columns (X) {self.x[:1]} ({type(self.x[1]).__name__}) and (Y) {self.y[:1]} ({type(self.y[1]).__name__}).")
        while True:
            confirm = input("[?] Is this the correct selection? (y/n/q): ").lower()
            if confirm == 'y':
                print("[+] Columns confirmed.")
                return self.x, self.y
            elif confirm == 'n':
                print("[-] Re-selecting columns.")
                return self.grab_cols(data)
            elif confirm == 'q':
                quit("[-] QUITTING... User requested exit.")
            else:
                print("[-] Invalid input. Please enter 'y' or 'n'.")
                quit("[-] QUITTING... Invalid confirmation input.")

    def show_graphs(self, x, y, choice: int) -> None:
        '''Displays and saves graphs'''
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
    
    def clean_up(self) -> None:
        '''Cleans up script resources'''
        os.system('clear' if os.name == 'posix' or 'unix' else 'cls')
        print("[!] Cleaning up resources...")
        plt.close("all")
        print("[!] Cleaned up matplotlib resources.")
        while True:
            confirm = input("[?] Clear download folder? (y/n): ").lower()
            if confirm == 'y':
                os.system(f'rm -rf ./stathat-downloads/*')
                print("[+] Download folder cleared.")
                print("[!] Exiting logic module.")
                quit("[!] Goodbye!")
            elif confirm == 'n':
                print("[+] Continuing without deleting downloads.")
                print("[!] Exiting logic module.")
                quit("[!] Goodbye!")
            else:
                print("[-] Invalid input. Please enter 'y' or 'n'.")
                quit("[-] QUITTING... Invalid confirmation input.")

import csv
import matplotlib.pyplot as plt
import wget
import os


def get_data():
    print("1: URL")
    print("2: File name")
    choice = input("Do you have a URL or file name?\n")
    if int(choice) == 1:
        plot = input("Enter URL for CSV file\n")
        current_dir = os.getcwd()
        file_name = 'downloaded_data.csv'
        file_path = os.path.join(current_dir, file_name)
        wget.download(plot, file_path)
        print(f"\nFile downloaded and saved to {file_path}")
    elif int(choice) == 2:
        file_name = input("Enter CSV file name:\n")
    return file_name



def load_csv(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.reader(f)

        header = next(reader)
        for row in reader:
            converted = []
            for cell in row:
                try:
                    converted.append(float(cell))
                except ValueError:
                    converted.append(cell)
            data.append(converted)
    return data


def show_graphs(data):
    num_cols = len(data[0])

    print("\nAvailable columns:")
    for i in range(num_cols):
        print(f"{i} = Column {i}")

    x_col = int(input("\nEnter X column number: "))
    y_col = int(input("Enter Y column number: "))

    x = [row[x_col] for row in data]
    y = [row[y_col] for row in data]

    print("\nChoose graph option:")
    print("1 = Line graph")
    print("2 = Scatter graph")
    print("3 = Bar graph")
    print("4 = Show all 3 graphs")

    choice = input("Enter choice: ")

    if choice == "1":
        plt.plot(x, y)
        plt.title("Line Graph")
        plt.show()
        file_path = "line.png"
    
        # Save
        plt.savefig(file_path)

    elif choice == "2":
        plt.scatter(x, y)
        plt.title("Scatter Graph")
        plt.show()
        file_path = "scatter.png"
    
        # Save
        plt.savefig(file_path)

    elif choice == "3":
        plt.bar(x, y)
        plt.title("Bar Graph")
        plt.show()
        file_path = "bar_graph.png"
    
        # Save
        plt.savefig(file_path)

    elif choice == "4":
        fig, axs = plt.subplots(3, 1, figsize=(6, 10))

        axs[0].plot(x, y)
        axs[0].set_title("Line Graph")

        axs[1].scatter(x, y)
        axs[1].set_title("Scatter Graph")

        axs[2].bar(x, y)
        axs[2].set_title("Bar Graph")

        plt.tight_layout()
        plt.show()

    else:
        print("Invalid choice.")

#Main Program
filename = get_data()
data = load_csv(filename)

print("\nFirst 5 rows:")
for row in data[:5]:
    print(row)

show_graphs(data)

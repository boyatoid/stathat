import csv
import matplotlib.pyplot as plt
import os
import re
from core import pull





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

    elif choice == "2":
        plt.scatter(x, y)
        plt.title("Scatter Graph")
        plt.show()
        file_path = "bar_graph.png"
    
        # Save the plot as a PNG file
        plt.savefig(file_path)

    elif choice == "3":
        plt.bar(x, y)
        plt.title("Bar Graph")
        plt.show()
        file_path = "bar_graph.png"
    
        # Save the plot as a PNG file
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
dp = pull.DataPuller()
url = input("What is the URL?\n")
try:
    dp.goto_url(url)
    page_source = dp.grab_source()
    print('attempting to find element via data format tag...')
    if dp.find_elm_by_XPATH("//a[@data-format='csv']"):
        element = dp.find_elm_by_XPATH("//a[@data-format='csv']")
        print(f'found element: {element}')
        download_button = element
    else:
        print('could not find element via data format tag, trying partial link text "CSV"...')
        element = dp.find_elm_by_PARTEXT("CSV")
        print(f'found element: {element}')
        download_button = element

    file_path = dp.download_file(download_button, wait_time=60)

    print("Download complete:", file_path)

finally:
    print("finishing up...")
    dp.close()

data = load_csv(file_path)

print("\nFirst 5 rows:")
for row in data[:5]:
    print(row)

show_graphs(data)

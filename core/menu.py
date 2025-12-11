from core import logic
logic = logic.logic()


class CoreMenu:
    def __init__(self, data):
        self.data = data
        self.choice = None
    
    def input_process(self):
        try:
            self.choice = int(input("[+] Enter Number Choice: "))
        except ValueError:
            print("[-] Invalid input. Please enter a number.")
            self.choice = None
        finally:
            if self.choice not in [1, 2, 3] or self.choice is None:
                print("[-] QUITTING... Please select a valid option. (1, 2, or 3)")
            return self.choice

    def graph_choice(self):
        choice = self.choice
        logic.grab_cols(self.data)
        logic.show_graphs(self.data, logic.x, logic.y, choice)

    def display_menu(self):
        print("=== Stathat Menu ===")
        print("1. Line graph")
        print("2. Scatter graph")
        print("3. Bar graph")
        self.input_process()
        self.graph_choice()
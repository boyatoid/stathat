from core import logic
logic = logic.logic()

class CoreMenu:
    def __init__(self, data: list):
        self.data = data
        self.choice = None
    
    def input_process(self) -> int:
        '''processes user input for graph choice'''
        try:
            self.choice = int(input("[?] Enter Number Choice: "))
        except ValueError:
            print("[-] Invalid input. Please enter a number.")
            self.choice = None
        finally:
            if self.choice not in [1, 2, 3] or self.choice is None:
                print("[-] QUITTING... Please select a valid option. (1, 2, or 3)")
                exit(1)
            return self.choice

    def graph_choice(self) -> None:
        '''Processes the graph choice, grabs the columns, and runs graph display logic'''
        choice = self.choice
        logic.grab_cols(self.data)
        logic.show_graphs(logic.x, logic.y, choice)

    def display_menu(self) -> None:
        '''Displays the menu'''
        print("================================")
        print("=|  Please Pick A Graph Type  |=")
        print("================================")
        print("1. Line graph")
        print("2. Scatter graph")
        print("3. Bar graph")
        self.input_process()
        self.graph_choice()
        logic.clean_up()
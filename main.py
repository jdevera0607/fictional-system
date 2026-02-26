def main():
    running = True
    while running:
            show_menu()
            choice = input()
            running = handle_choice(choice)

def show_menu():
      print("Welcome to the CLI ticket-system")
      print("Select an option")
      print("""
      === Ticket System ===
      1. Create Ticket
      2. View Tickets
      3. Update Tickets
      4. Delete Ticket
      5. Exit
        """)

def menu_dictionary():
      menu = {
            "1" : create_ticket,
            "2" : view_tickets,
            "3" : update_tickets,
            "4" : delete_ticket,
            "5" : exit_program
      }
      return menu
def handle_choice():
      pass
      
if __name__ == "__main__":
      main()
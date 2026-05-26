from models.admin import Admin
from models.hotel_system import HotelSystem

class Main:
    def __init__(self):
        self.hotel_system = HotelSystem()
        self.run_loop()

    def run_loop(self):
        while True:
            print('1. Search Rooms')
            print('2. Create Reservation')
            print('3. Check Out')
            print('4. View Reservation')
            print('5. Access Admin Actions')
            print('6. List all rooms')
            print('7. Exit')

            choice = input('Enter your choice: ')
            match choice:
                case '1':
                    break

                case '5':
                    # admin_id = int(print('Enter admin id: '))
                    # id(admin_id)
                    self.admin_options()

                case '6':
                    self.list_rooms()
                
                case '7':
                    print('Thank you. Have a great day.')
                    break

                case _:
                    print('Please select available options (1-6).')

    def admin_options(self):
        print('--Admin Actions--')
        print('1. Add Room')
        print('2. Remove Room')
        print('3. Exit')
        print('-----------')

        admin_choice = input('Enter admin option: ')
        if(admin_choice == '1'):
            admin = Admin()
            admin.add_rooms()
        
        elif(admin_choice == '2'):
            pass

        else:
            print('Redirecting to main options\n')

    def list_rooms(self):
        self.hotel_system.list_all_rooms()


if __name__ == '__main__':
    Main()

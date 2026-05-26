from models.user import User

class Guest(User):
    def __init__(self, user_id, name, email, bookings):
        super().__init__(user_id, name, email)
        self.bookings = bookings
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def save(self, email):
        try:

            # try saving data...
            self.model.email = email
            self.model.save()

            # show a success message if data was saved
            self.view.show_success(f'The email {email} was saved!')

        except ValueError as error:
            # show an error message...
            self.view.show_error(error)
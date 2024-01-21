import pandas

df = pandas.read_csv('hotels.csv', dtype={'id': str})
df_cards = pandas.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pandas.read_csv('card_security.csv', dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        '''Book a hotel by changing its availability to no'''
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        '''Check if the hotel is available'''
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = name
        self.hotel = hotel_object

    def generate(self):
        content = f'''
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        '''
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {'number': self.number, 'expiration': expiration,
                     'holder': holder, 'cvc': cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[
            df_cards_security['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        else:
            return False


class SpaReservationTicket:
    def __init__(self, customer_name, hotel_object, spa_option):
        self.customer_name = name
        self.hotel = hotel_object
        self.spa_option = spa_option

    def user_choice(self):
        while True:
            if self.spa_option == 'yes':
                return True
            elif self.spa_option == 'no':
                return False

    def generate(self):
        message = f'''
        Thank you for your SPA reservation!
        Here are your SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        '''
        return message


print(df)
hotel_id = input('Enter the id of the hotel: ')
hotel = SpaHotel(hotel_id)
if hotel.available():
    credit_card = SecureCreditCard(number='1234567890123456')
    if credit_card.validate(expiration='12/26',
                            holder='JOHN SMITH', cvc='123'):
        if credit_card.authenticate(given_password='mypass'):
            hotel.book()
            name = input('Enter your name: ')
            reservation_ticket = ReservationTicket(customer_name=name,
                                                   hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print('Credit card authentication failed.')
    else:
        print('There was a problem with your payment')
    SPA_OPTION = input('Do you want to book a spa package? ')
    user_name = name
    spa_reservation_ticket = SpaReservationTicket(
        customer_name=user_name, hotel_object=hotel, spa_option=SPA_OPTION)
    if spa_reservation_ticket.user_choice():
        hotel.book_spa_package()
        print(spa_reservation_ticket.generate())
else:
    print('Hotel is not free.')

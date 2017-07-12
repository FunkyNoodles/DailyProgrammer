class Address:
    def __init__(self, address_string):
        self.address_string = address_string
        self.name = ''
        self.business = ''
        self.street = ''
        self.city_state = ''
        self.postcode = ''
        self.country = ''
        self.phone = ''

    @staticmethod
    def has_numbers(line):
        return any(c.isdigit() for c in line)

    def parse(self):
        lines = self.address_string.split('\n')
        lines = filter(lambda a: a != '', lines)

        street_index = 0
        if self.has_numbers(lines[1]):
            # No name field
            self.business = lines[0]
            street_index = 1
        else:
            self.name = lines[0]
            self.business = lines[1]
            street_index = 2

        self.street = lines[street_index]
        postcode_index = 0
        if self.has_numbers(lines[street_index + 1]):
            # No city or state field
            postcode_index = street_index + 1
        else:
            self.city_state = lines[street_index + 1]
            postcode_index = street_index + 2

        self.postcode = lines[postcode_index]
        self.country = lines[postcode_index + 1]
        if postcode_index + 1 < len(lines) - 1:
            # There is phone number
            self.phone = lines[postcode_index + 2]

    def print_address(self):
        if len(self.name):
            print 'name=' + self.name
        print 'business=' + self.business
        print 'street=' + self.street
        if len(self.city_state) > 0:
            print 'city=' + self.city_state.split(', ')[0]
            print 'state=' + self.city_state.split(', ')[1]
        print 'postal_code=' + self.postcode
        print 'country=' + self.country
        if len(self.phone) > 0:
            print 'phone=' + self.phone


temp_address = """
Alex Bergman
Wilhelmgalerie
Platz der Einheit 14
14467 Potsdam
Germany
+49 331 200900
"""

address = Address(temp_address)
address.parse()
address.print_address()

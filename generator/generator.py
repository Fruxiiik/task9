from data.data import Person
from faker import Faker

faker_en = Faker('En')


def generated_person():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        postal_code=faker_en.postcode()
    )

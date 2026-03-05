from faker import Faker
from random import randrange


def data_samples():
    vasya = Faker("ru_RU")
    return [[vasya.name(), vasya.address(), vasya.city(), randrange(1, 10)] for _ in range(20)]

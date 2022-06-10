import pickle


class Company(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


company = Company('foo', 'bar')


def save_object(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


save_object(company, 'company.pkl')

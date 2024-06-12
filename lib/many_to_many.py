
class Author:
    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        self.books_list = []

    def contracts(self):
        return self.contracts_list
    
    def books(self):
        return self.books_list
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)

class Book:
    def __init__(self, title):
        self.title = title
        self.contracts_list = []
        self.author_list = []

    def contracts(self):
        return self.contracts_list
    
    def authors(self):
        return self.author_list

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid Author type")
        elif not isinstance(book, Book):
            raise Exception("Invalid Book type")
        elif (type(date) in (int, float)):
            raise Exception("Invalid Date type")
        elif not (type(royalties) in (int, float)):
            raise Exception("Invalid Royalties type")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        author.contracts_list.append(self)
        author.books_list.append(book)
        book.contracts_list.append(self)
        book.author_list.append(author)

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        contracts = []
        for contract in cls.all:
            if contract.date == date:
                contracts.append(contract)
        return contracts
        # return [contract for contract in cls.all if contract.date == date]
    
    
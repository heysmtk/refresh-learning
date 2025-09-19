# Možnost schovat některé věci uvnitře objektu, aby k nim neměl přímý přístup každý.

# data nelze omylem přepsat z venčí
# můžu mít nad tím kontrolu (setter/getter)

# public = normální atribut, přístupný všude
# _protected = jen "doporučení", že to není pro venek
# __private = Python ho přejmenuje, aby se k němu nedalo jednoduše dostat

class Dog:
    def __init__(self, name):
        self.__name = name  # private
        
    def get_name(self):
        return self.__name
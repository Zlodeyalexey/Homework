class Category:
    categories = ['cars', 'trains', 'ships']

    def _add_(self, x):
       self.x = x
       x = 'helicopter'
       return x + Category.categories

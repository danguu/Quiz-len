class Recomendador:
    def __init__(self):
        self.compras = {}

    def add_purchase(self, user, product):
        if user not in self.compras:
            self.compras[user] = []
        self.compras[user].append(product)

    def get_recommendations(self, user):
        if user not in self.compras:
            return []
        recommendations = set()
        user_products = set(self.compras[user])
        for other_user, products in self.compras.items():
            if other_user != user:
                common_products = set(products).intersection(user_products)
                if common_products:
                    recommendations.update(set(products) - user_products)
        return list(recommendations)

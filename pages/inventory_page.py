class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.items = page.locator('[data-test="inventory-item"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.prices = page.locator('[data-test="inventory-item-price"]')

    def item_count(self):
        return self.items.count()

    def add_item_by_name(self, name):
        item = self.items.filter(has_text=name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_item_by_name(self, name):
        item = self.items.filter(has_text=name)
        item.get_by_role("button", name="Remove").click()

    def cart_count(self):
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def sort_by(self, option):
        self.sort_dropdown.select_option(label=option)

    def price_list(self):
        return [float(p.inner_text().replace("$", "")) for p in self.prices.all()]

    def open_cart(self):
        self.cart_link.click()
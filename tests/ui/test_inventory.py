from pages.inventory_page import InventoryPage

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


def test_all_products_are_listed(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    assert inventory.title.inner_text() == "Products"
    assert inventory.item_count() == 6


def test_cart_is_empty_before_adding(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    assert inventory.cart_count() == 0


def test_add_two_items_updates_cart_badge(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_by_name(BACKPACK)
    inventory.add_item_by_name(BIKE_LIGHT)
    assert inventory.cart_count() == 2


def test_removing_an_item_decreases_the_badge(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_by_name(BACKPACK)
    inventory.add_item_by_name(BIKE_LIGHT)
    inventory.remove_item_by_name(BACKPACK)
    assert inventory.cart_count() == 1


def test_sorting_by_price_low_to_high(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("Price (low to high)")
    prices = inventory.price_list()
    assert prices == sorted(prices)
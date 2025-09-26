"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    counts_dict = dict()
    for elm in items:
        counts_dict[elm] = counts_dict.get(elm, 0) + 1
    return counts_dict
        


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    inventory_from_items = create_inventory(items)
    for elm, count in inventory_from_items.items():
        inventory[elm] = inventory.get(elm, 0)+count
    
    
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    
    for item in items:
        if item in inventory and inventory[item]>=1:
            inventory[item]-=1

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

     
    for key in inventory.keys():
        if item == key:
            inventory.pop(item)
            break
            
    return inventory



def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    res = [(key, val) for key, val in inventory.items() if  inventory.get(key)>0]
    return res


# inventory.py


def display_inventory(inventory):
    total_items = 0
    for item in inventory:
        print(f'{inventory[item]}  {item}')
        total_items += inventory[item]
    print(f'Total number of items: {total_items}\n')


#  display_inventory(stuff)


def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)   #  this adds a (defaulted to zero value) key to the inventory dict if it's not already there
        inventory[item] += 1            #  and this increases that value by one, each time that item appears in the loot list
    return inventory


inv = {'gold coin': 42, 'rope': 1}
display_inventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)

import json

class InventoryHelper:

    def getInventory(self):
        inventory = json.load(open('inventory.json'))
        return json.dumps(inventory)
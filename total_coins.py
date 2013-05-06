import command
import json
import mongo

class TotalCoins(command.Command):
    """ 
    {"cmd":"total_coins"}
    """
    required = ["total_coins"]

    def handle(self):
        self.success({"amount":mongo.db.coins.count()})        
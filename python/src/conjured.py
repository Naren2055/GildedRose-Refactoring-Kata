from python.components.gilded_rose import GildedRose, Item




class ConjuredItem(GildedRose):
    def __init__(self, item: Item):
        super().__init__(item)

    def update_quality(self):
        if self.quality > 0:
            self.quality -= 2
        if self.sell_in <= 0 and self.quality > 0:
            self.quality -= 2
        self.sell_in -= 1
        return self.quality, self.sell_in
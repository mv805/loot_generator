import random
from collections import Counter
from typing import Dict, Set, Tuple


class LootGenerator:

    _loot_table: Dict[str, Tuple[str, str]] = {
        "Rusty Sword": ("common", "weapon"),
        "Healing Potion": ("common", "consumable"),
        "Iron Dagger": ("common", "weapon"),
        "Leather Boots": ("common", "armor"),
        "Bread Loaf": ("common", "consumable"),
        "Wooden Shield": ("common", "armor"),
        "Silver Shield": ("rare", "armor"),
        "Mana Potion": ("rare", "consumable"),
        "Steel Sword": ("rare", "weapon"),
        "Chain Mail": ("rare", "armor"),
        "Dragon Blade": ("epic", "weapon"),
        "Phoenix Feather": ("epic", "material"),
        "Crystal Staff": ("epic", "weapon"),
        "Godslayer Axe": ("legendary", "weapon"),
        "Crown of Kings": ("legendary", "accessory"),
    }

    _rarity_weights: Dict[str, int] = {"common": 70, "rare": 20, "epic": 9, "legendary": 1}

    def __init__(self) -> None:
        pass

    def drop_item(self) -> str:
        """Weighted loot drops against the loot table"""
        items = list(self._loot_table.keys())
        weights = [self._rarity_weights[self._loot_table[item][0]] for item in items]
        dropped_item = random.choices(items, weights=weights, k=1)[0]
        dropped_item_rarity, dropped_item_type = self._loot_table[dropped_item]

        return f"{dropped_item} [{dropped_item_rarity}] ({dropped_item_type})"

    def drop_chest(self) -> Set[str]:
        chest = set()
        number_of_items = random.randint(3, 5)
        while len(chest) < number_of_items:
            chest.add(self.drop_item())

        return chest

    def print_chest(self, chest: Set[str]) -> None:
        print("Loot Chest Opened!")
        for item in chest:
            print(f"- {item}")

    def DEBUG_drop_counter(self) -> Dict[str, float]:
        """run simulated runs to see how often items drop"""
        counts = Counter()

        for i in range(100_000):  # 100k is accurate enough and fast
            counts[self.drop_item()] += 1

        total = sum(counts.values())
        percentages = {k: round((v / total) * 100, 2) for k, v in counts.items()}
        return percentages

    def DEBUG_expected_percentages(self) -> Dict[str, float]:
        """Calculate what percentages we SHOULD see. For debug"""
        total_weight = sum(self._rarity_weights.values())  # 100
        expected = {}
        for item, (rarity, item_type) in self._loot_table.items():
            weight = self._rarity_weights[rarity]
            expected[item] = round((weight / total_weight) * 100, 2)
        return expected


if __name__ == "__main__":
    loot_gen = LootGenerator()

    loot_gen.print_chest(loot_gen.drop_chest())

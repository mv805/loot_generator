import random
from collections import Counter
from typing import Dict


class LootGenerator:

    _loot_table: Dict[str, str] = {
        "Rusty Sword": "common",
        "Healing Potion": "common",
        "Silver Shield": "rare",
        "Dragon Blade": "epic",
        "Godslayer Axe": "legendary",
    }

    _rarity_weights: Dict[str, int] = {"common": 70, "rare": 20, "epic": 9, "legendary": 1}

    def __init__(self) -> None:
        pass

    def drop(self) -> str:
        """Weighted loot drops against the loot table"""
        items = list(self._loot_table.keys())
        weights = [self._rarity_weights[self._loot_table[item]] for item in items]
        dropped_item = random.choices(items, weights=weights, k=1)[0]
        dropped_item_rarity = self._loot_table[dropped_item]

        return f"{dropped_item} [{dropped_item_rarity}]"

    def DEBUG_drop_counter(self) -> Dict[str, float]:
        """run simulated runs to see how often items drop"""
        counts = Counter()

        for i in range(100_000):  # 100k is accurate enough and fast
            counts[self.drop()] += 1

        total = sum(counts.values())
        percentages = {k: round((v / total) * 100, 2) for k, v in counts.items()}
        return percentages

    def DEBUG_expected_percentages(self) -> Dict[str, float]:
        """Calculate what percentages we SHOULD see. For debug"""
        total_weight = sum(self._rarity_weights.values())  # 100
        expected = {}
        for item, rarity in self._loot_table.items():
            weight = self._rarity_weights[rarity]
            expected[item] = round((weight / total_weight) * 100, 2)
        return expected


if __name__ == "__main__":
    loot_gen = LootGenerator()

    print(loot_gen.drop())

import unittest

from ocr.nutrition_map import NutritionLabelMap


class TestNutritionMap(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.label_map = NutritionLabelMap()

    def test_nutrition_map_1(self):
        # test exact matching
        target = "energy"
        key = "energy"
        self.assertIn(target, self.label_map)
        self.assertEqual(key, self.label_map[target])

    def test_nutrition_map_2(self):
        # test inexact matching
        target = "Energy"
        key = "energy"
        self.assertIn(target, self.label_map)
        self.assertEqual(key, self.label_map[target])

    def test_nutrition_map_3(self):
        # test inexact matching with bad characters
        target = "/ENERGY- 2564kj"
        key = "energy"
        self.assertIn(target, self.label_map)
        self.assertEqual(key, self.label_map[target])

    def test_nutrition_map_4(self):
        # test alias matching
        target = "qluten"
        key = "gluten"
        self.assertIn(target, self.label_map)
        self.assertEqual(key, self.label_map[target])

    def test_nutrition_map_5(self):
        # test alias matching
        target = "FAT (TOTAL) -"
        key = "fat-total"
        self.assertIn(target, self.label_map)
        self.assertEqual(key, self.label_map[target])

    def test_nutrition_map_6(self):
        # test alias matching
        target = "Total Fat 12.7g"
        key = "fat-total"
        self.assertIn(target, self.label_map)
        self.assertEqual(key, self.label_map[target])

    def test_default_unit_1(self):
        # test exact matching of default unit
        target = "energy"
        unit = "kJ"
        self.assertEqual(self.label_map.default_unit(target), unit)

    def test_default_unit_2(self):
        # test alias matching of default unit
        target = "ENERGY -"
        unit = "kJ"
        self.assertEqual(self.label_map.default_unit(target), unit)


if __name__ == '__main__':
    unittest.main()

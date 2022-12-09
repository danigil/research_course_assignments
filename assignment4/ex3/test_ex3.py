import unittest

from ex3 import AlgoOutputs
from ex3 import when_pigs_fly


class TestAlgorithmOutput(unittest.TestCase):

    def test_case1(self):
        input = "PIGS are BACONS\nBACONS are GODS\nGODS can FLY"

        expected_output = AlgoOutputs.All_pigs_can_fly

        self.assertEqual(when_pigs_fly(input), expected_output)

    def test_case2(self):
        input = """
                PIGS have FEET
                PIGS are ANIMALS
                ANIMALS with FEET that can RUN can FLY
                ANIMALS can RUN
                """

        expected_output = AlgoOutputs.All_pigs_can_fly

        self.assertEqual(when_pigs_fly(input), expected_output)

    def test_case3(self):
        input = """
                BACONS with WINGS can FLY
                HAMS are PIGS
                HAMLETS are PIGLETS
                BACONS are GODS
                PIGLETS are PIGS
                HAMS are BACONS
                GODS have WINGS
                """

        expected_output = AlgoOutputs.Some_pigs_can_fly

        self.assertEqual(when_pigs_fly(input), expected_output)

    def test_case4(self):
        input = """
                PIGS have FEET
                FEET are LIMBS
                CATS are POPTARTS
                CATS have LIMBS
                PIGS are MAMMALS
                CATS are MAMMALS
                POPTARTS with LIMBS can FLY
                CATS are PIGS
                """

        expected_output = AlgoOutputs.Some_pigs_can_fly

        self.assertEqual(when_pigs_fly(input), expected_output)

    def test_case5(self):
        input = """
                PIGS have MOUSTACHES
                ANIMALS with MOUSTACHES can FLY
                SQUIRRELS have MOUSTACHES
                SQUIRRELS can SCREECH
                SQUIRRELS are PIGS
                REINDEER are SQUIRRELS
                REINDEER are MAMMALS
                MAMMALS that can SCREECH are ANIMALS
                PIGS are ANIMALS
                """

        expected_output = AlgoOutputs.All_pigs_can_fly

        self.assertEqual(when_pigs_fly(input), expected_output)

    def test_case6(self):
        input = """
                BANANAS with HANDS are BUNNIES with LIMBS
                BANANAS have HANDS
                BUNNIES with LIMBS can FLY
                PIGS are BUNNIES
                """

        expected_output = AlgoOutputs.No_pigs_can_fly

        self.assertEqual(when_pigs_fly(input), expected_output)

    def test_case7(self):
        input = """
                COWS are BURGERS
                COWS can EAT
                COWS that can MOO can FLY
                PIGS are COWS
                PIGLETS are PIGS
                PIGLETS are MUSHROOMS
                MUSHROOMS have SPORES
                SPORES are ROCKETSHIPS
                PIGLETS with ROCKETSHIPS can MOO
                """

        expected_output = AlgoOutputs.Some_pigs_can_fly

        self.assertEqual(when_pigs_fly(input), expected_output)

    def test_case8(self):
        input = """
                BONES are ITEMS
                METALS are ITEMS
                ITEMS have COST
                ITEMS have DEMAND
                BLACKSMITHS can CRAFT
                BLACKSMITHS have MATERIALS
                PIGS have ARMOR
                BLACKSMITHS with HAMMERS can SYNTHESIZE
                BEETLES have HUSKS
                BEETLES are INSECTS
                INSECTS with HUSKS can FLY
                """

        expected_output = AlgoOutputs.No_pigs_can_fly

        self.assertEqual(when_pigs_fly(input), expected_output)

    def test_case9(self):
        input = """
                GEESE are CHICKENS
                CHICKENS with BEAKS are LLAMAS with MOUTHS
                MOUTHS are HOLES
                GEESE have BEAKS
                LLAMAS with TOENAILS are PIGS
                PIGS are TREES that can WALK
                CHICKENS with EYES and TOENAILS are TREES that can FLY
                BEAKS are TOENAILS
                CHICKENS have EYES
                """

        expected_output = AlgoOutputs.Some_pigs_can_fly

        self.assertEqual(when_pigs_fly(input), expected_output)


if __name__ == '__main__':
    unittest.main()

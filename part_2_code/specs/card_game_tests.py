import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.d1 = Card("H", 1)
        self.d2 = Card("H",2)
        self.d3 = Card("H",3)
        self.d4 = Card("H",4)
        self.d5 = Card("H",5)
        self.d6 = Card("H",6)
        self.d7 = Card("H",7)
        self.d8 = Card("H",8)
        self.d9 = Card("H",9)
        self.d10 = Card("H",10)

        self.non_ace_cards = (self.d2,self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9)

    def test_for_ace_with_ace(self):
        result = CardGame.check_for_ace(self.d1)
        self.assertEqual(True, result)

    def test_for_ace_without_ace(self):
        for card in self.non_ace_cards:
            result = CardGame.check_for_ace(card)
            self.assertEqual(False, result)

    def test_highest_card_never_1(self):
        for card in self.non_ace_cards:
            result = CardGame.highest_card(self.d1, card)
            self.assertEqual(card, result)

    def test_highest_card_always_10(self):
        for card in self.non_ace_cards:
            result = CardGame.highest_card(self.d10, card)
            self.assertEqual(self.d10, result)

    def test_card_total(self):
        result = CardGame.cards_total(self.non_ace_cards)
        self.assertEqual("You have a total of 44", result)

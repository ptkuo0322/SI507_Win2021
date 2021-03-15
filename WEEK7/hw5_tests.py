#########################################
##### Name: Po-Tsun Kuo             #####
##### Uniqname:ptkuo                #####
#########################################


import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''

        q1 = hw5_cards.Card(0, 12)
        x = self.assertEqual(q1.rank_name, "Queen")
        return q1.rank_name, "Queen"
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q2 = hw5_cards.Card(1, 10)
        x = self.assertEqual(q2.suit_name, "Clubs")
        return q2.suit_name, "Clubs"   
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q3 = hw5_cards.Card(3, 13)
        self.assertEqual(q3.__str__(), "King of Spades")
        return q3.__str__(), "King of Spades"

    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q4= hw5_cards.Deck()
        self.assertEqual(len(q4.cards), 52)
        return len(q4.cards), 52

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q5 = hw5_cards.Deck()
        q6 = hw5_cards.Card(3,13)
        q51 = q5.deal_card()
        self.assertEqual(q51.__str__(), q6.__str__())
        self.assertEqual(q51.suit, 3)
        self.assertEqual(q51.suit_name, "Spades")
        self.assertEqual(q51.rank, 13)
        self.assertEqual(q51.rank_name, "King")
        
        return q51, (3,13)
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q6 = hw5_cards.Deck()
        q61 = q6.deal_card() # deal_card() will remote the card from q6, and return the removed card
        self.assertEqual(len(q6.cards), 51) #q6 is the list after the pop function
        return len(q6.cards), 51
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q7 = hw5_cards.Deck()
        q71 = hw5_cards.Deck() # create this to match the autograder expected output
        q7.deal_card() # deal_card() will remote the card from q7, and return the removed card (3,13)
        q71.deal_card() # q71 is used to test after deal function, the length of q71 should be 51 not 52
        q7.replace_card(hw5_cards.Card(3,13)) # use hw5_cards.Card(3,13) to add back the one being pop out which is King of Spades (3,13)
        self.assertEqual(len(q7.cards), 52) #q7 is the list after pop function and replace function >> length should be 52
        self.assertNotEqual(len(q7.cards), 53) #q7 is the list after pop function and replace function >> length should be 52
        return len(q71.cards)+1, len(q7.cards), 52 # q71 is used to test the length after deal, q7 is the length after deal and replace

    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q8 = hw5_cards.Deck()
        q8.replace_card(hw5_cards.Card(3,13)) # use hw5_cards.Card(3,13) to add the existing one  which is King of Spades (3,13)
        self.assertEqual(len(q8.cards), 52) # if the a card that is already in the deck, the deck size is not affected >> length should be 52
        self.assertNotEqual(len(q8.cards), 53) # Other test for length of the number of the card in the deck
        return len(q8.cards), 52



if __name__=="__main__":
    unittest.main()
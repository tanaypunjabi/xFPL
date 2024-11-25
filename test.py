# ### TESTS ###

import unittest
from main import recommend_transfers
class TestRecommendTransfers(unittest.TestCase):
    def test_recommend_transfers1 (self):
        user_team_list = [201, 350, 495, 311, 255, 99, 491, 19, 58, 351, 148, 109, 17, 309, 116]
        budget = 3 #0.3 million
        diff_exp_points = recommend_transfers(user_team_list, budget)
        self.assertEqual(sum(diff_exp_points)>0, True)

    def test_recommend_transfers2 (self):
        user_team_list = [47, 326, 255, 18, 395, 328, 99, 346, 4, 252, 351, 488, 44, 320, 54]
        budget = 2 
        diff_exp_points = recommend_transfers(user_team_list, budget)
        self.assertEqual(sum(diff_exp_points)>0, True)
    
    def test_recommend_transfers3 (self):
        user_team_list = [15, 3, 350, 498, 368, 182, 23, 327, 19, 351, 447, 185, 129, 163, 219]
        budget = 2
        diff_exp_points = recommend_transfers(user_team_list, budget)
        self.assertEqual(sum(diff_exp_points)>0, True)


if __name__ == '__main__':
    unittest.main()
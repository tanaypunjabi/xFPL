import requests
import pandas as pd

PROCESSED_PLAYERS_TABLE = pd.read_csv('data/processed/2024-25/processed_players.csv')
PLAYER_ID_TO_NAME_DICT = PROCESSED_PLAYERS_TABLE[['id', 'full_name']].set_index('id').T.to_dict()

### GET USER TEAM INFO ###
def get_user_team(team_id):
    """
    Fetches the user's team information from the Fantasy Premier League API.

    Args:
        team_id (int): The unique identifier for the user's team.

    Returns:
        tuple: A tuple containing two elements:
            - list: A list of player IDs in the user's team.
            - int: The current budget available for transfers.
    """
    fpl_api_endpoint = f'https://fantasy.premierleague.com/api/entry/{team_id}/event/8/picks/'
    response = requests.get(fpl_api_endpoint)
    data = response.json()
    team_id_list = [pick['element'] for pick in data['picks']]
    budget = data['entry_history']['bank']
    return team_id_list, budget

### GET USER TEAM PLAYER TABLE ###
def get_user_team_table(user_team_list):
    """
    Constructs a DataFrame containing detailed information about the user's team players.

    Args:
        user_team_list (list): A list of player IDs representing the user's team.

    Returns:
        DataFrame: A DataFrame that merges the user's player IDs with additional player data.
    """
    user_team_df = pd.DataFrame(user_team_list, columns=['id'])
    user_players_table = pd.merge(user_team_df, PROCESSED_PLAYERS_TABLE, on='id')
    return user_players_table

### TRANSFER RECOMMENDATION ###
def recommend_transfers(user_team_list, budget):
    """
    Recommends player transfers based on the user's current team and budget.

    Args:
        user_team_list (list): A list of player IDs in the user's current team.
        budget (int): The user's current budget for transfers.

    Prints:
        str: A message indicating the available budget and recommended transfers.
    """
    user_players_table = get_user_team_table(user_team_list)
    print(user_team_list)
    print(budget)
    user_team_data = user_players_table[['id', 'element_type', 'now_cost']].set_index('id').T.to_dict()

    # recommendations = PROCESSED_PLAYERS_TABLE.sort_values(by='value', ascending=False)[:10]
    model_predictions = pd.read_csv('notebooks/misc/2425gw10_model_preds.csv')
    # model_predictions = model_predictions[['player_id', 'model_pred']]

    # Merge predictions with processed players table
    # recommendations = pd.merge(PROCESSED_PLAYERS_TABLE, model_predictions, on='player_id')
    recommendations = model_predictions.copy()
    recommendations = recommendations.sort_values(by='model_pred', ascending=False)

    recommended_transfers = []

    for _, recommended_player in recommendations.iterrows():
        if recommended_player['player_id'] not in user_team_list:
            for user_player, user_player_data in user_team_data.items():
                if (recommended_player['position'] == user_player_data['element_type'] and 
                    (user_player_data['now_cost'] + budget) >= recommended_player['value']):
                    
                    expected_points_diff = recommended_player['model_pred'] - model_predictions.loc[model_predictions['player_id'] == user_player, 'model_pred'].values[0]
                    
                    recommended_transfers.append(
                        {
                            'out': PLAYER_ID_TO_NAME_DICT[user_player]['full_name'],
                            'in': recommended_player['full_name'],
                            'position': recommended_player['position'],
                            'expected_points_diff': expected_points_diff
                        }
                    )
                    break

    # Sort transfers by descending order of expected points difference
    recommended_transfers = sorted(recommended_transfers, key=lambda x: x['expected_points_diff'], reverse=True)[:5]

    diff_exp_points = []
    print(f'You have ${budget/10}m in the bank currently.')
    print('Your recommended transfers are: ')
    for rec in recommended_transfers:
        print(f'Transfer {rec["out"]} out for {rec["in"]} (Position: {rec["position"]})')
        diff_exp_points.append(rec['expected_points_diff'])
    
    return diff_exp_points
   
    # recommended_transfers = []

    # for _, recommended_player in recommendations.iterrows():
    #     if recommended_player['id'] not in user_team_list:
    #         for user_player, user_player_data in user_team_data.items():
    #             if (recommended_player['element_type'] == user_player_data['element_type'] and 
    #                 (user_player_data['now_cost'] + budget) >= recommended_player['now_cost']):
    #                 recommended_transfers.append(
    #                     {
    #                         'out': PLAYER_ID_TO_NAME_DICT[user_player]['full_name'],
    #                         'in': recommended_player['full_name'],
    #                         'position': recommended_player['element_type'],
    #                     }
    #                 )
    #                 break
    
    # print(f'You have ${budget/10}m in the bank currently.')
    # print('Your recommended transfers are: ')
    # for rec in recommended_transfers:
        # print(f'Transfer {rec["out"]} out for {rec["in"]} (Position: {rec["position"]})')

### CAPTAINCY RECOMMENDATION ###
def recommend_captain(user_team_list):
    """
    Recommends captain choices for the user's team based on total points.

    Args:
        user_team_list (list): A list of player IDs representing the user's team.

    Prints:
        str: A list of recommended captain picks.
    """
    user_players_table = get_user_team_table(user_team_list)
    captain_recs = user_players_table.sort_values(by='total_points', ascending=False)['full_name'].tolist()[:3]
    print('Your recommended captain picks are: ')
    for rec in captain_recs:
        print(rec)

### MAIN FUNCTION ###
def main():
    """
    Interactive Recommender for Fantasy Premier League (FPL).

    This function serves as the entry point for the xFPL assistant, allowing users to interactively
    retrieve and analyze their Fantasy Premier League team information. The user is prompted to
    input their team ID, after which the assistant fetches team details, provides transfer 
    recommendations based on the current budget, and suggests captain choices.

    Workflow:
    1. Prompts for the user's FPL team ID.
    2. Fetches the user's team data from the Fantasy Premier League API.
    3. Recommends player transfers based on the user's team and available budget.
    4. Suggests captain choices based on the user's team.
    """
    print('Welcome to xFPL: your personal FPL assistant!')
    team_id = input('Please enter your FPL team ID: ')
    print('\n')
    print('Fetching your FPL team info...')
    try:
        team_list, budget = get_user_team(team_id)
    except:
        print('Invalid team ID.')
        return
    print('\n')
    recommend_transfers(team_list, budget)
    print('\n')
    recommend_captain(team_list)
    print('\n')
    print('Thanks for using xFPL!')

# if __name__ == "__main__":
#     main()


# ### TESTS ###

import unittest
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
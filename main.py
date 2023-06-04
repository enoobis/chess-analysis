import pandas as pd
import numpy as np

# chess dataset
data = pd.read_csv("C:\\Users\\enoobis\\Desktop\\data\\games_data.csv")


######################

white_wins = data[data["winner"] == "white"].shape[0]
black_wins = data[data["winner"] == "black"].shape[0]
total_games = data.shape[0]

white_winning_chance = white_wins / total_games
black_winning_chance = black_wins / total_games

print("White winning chance: {}%".format(white_winning_chance * 100))
print("Black winning chance: {}%".format(black_winning_chance * 100))

########################

average_duration = data["turns"].mean()
print("Average game duration: {:.2f} turns".format(average_duration))

unique_players = data["white_id"].nunique() + data["black_id"].nunique()
print("Number of unique players: {}".format(unique_players))


########################

most_common_openings = data["opening_name"].value_counts().head(5)
print("Most common opening moves:")
print(most_common_openings)


########################

draws = data[data["winner"] == "draw"].shape[0]
draw_percentage = draws / total_games * 100
print("Percentage of games that ended in a draw: {:.2f}%".format(draw_percentage))



########################

rating_diff = data["white_rating"] - data["black_rating"]
average_rating_diff = rating_diff.mean()
print("Average rating difference between players: {:.2f}".format(average_rating_diff))


########################

termination_reasons = data["victory_status"].value_counts()
print("Most common game termination reasons:")
print(termination_reasons)

########################

higher_rating_wins = data[(data["winner"] == "white") & (data["white_rating"] > data["black_rating"])].shape[0]
higher_rating_wins += data[(data["winner"] == "black") & (data["black_rating"] > data["white_rating"])].shape[0]
higher_rating_win_percentage = higher_rating_wins / total_games * 100
print("Percentage of games won by the player with higher rating: {:.2f}%".format(higher_rating_win_percentage))



#######################

average_white_rating = data[data["winner"] == "white"]["white_rating"].mean()
print("Average rating for white players: {:.2f}".format(average_white_rating))

average_black_rating = data[data["winner"] == "black"]["black_rating"].mean()
print("Average rating for black players: {:.2f}".format(average_black_rating))
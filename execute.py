from player import game_stats
import re

def analyze_game_stats(file_path):
    player1=None
    players=[]
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()
        for line in contents.splitlines():
            words = line.replace('-', ' ').split()
            if len(words) > 0 and words[0] == "GAME":
                if player1 is not None:
                    players.append(player1)
                player1 = game_stats(words[1], words[2], words[3], words[4], words[5])
            if len(words) > 1 and words[1] == "Luka":
                if len(words) > 3:
                    third_word = words[3]
                    if third_word == "makes":
                        if words[4].isdigit():
                            dist=int(words[4])
                            if dist<=5:
                                player1.shot_stats["short_attempt"] += 1
                                player1.shot_stats["short_make"] += 1
                            elif 5<dist<=23:
                                player1.shot_stats["medium_attempt"] += 1
                                player1.shot_stats["medium_make"] += 1
                            else:
                                player1.shot_stats["long_attempt"] += 1
                                player1.shot_stats["long_make"] += 1
                        elif words[4] == 'driving' or words[4]=='running':
                            player1.shot_stats["short_attempt"] += 1
                            player1.shot_stats["short_make"] += 1   
                        elif words[4]=='free':
                            player1.shot_stats["free_throw_attempt"] += 1
                            
                    elif third_word == "misses":
                        if words[4].isdigit():
                            dist=int(words[4])
                            if dist<=5:
                                player1.shot_stats["short_attempt"] += 1
                            elif 5<dist<=23:
                                player1.shot_stats["medium_attempt"] += 1
                            else:
                                player1.shot_stats["long_attempt"] += 1
                        elif words[4] == 'driving' or words[4]=='running':
                            player1.shot_stats["short_attempt"] += 1
        
        # append last collected player1 (if any) before returning
        if player1 is not None:
            players.append(player1)

        return players

result = analyze_game_stats("c:\\Users\\zhoul\\OneDrive\\Documents\\NBA_project\\LAvJazz_q1.txt")
for player in result:
    print(player.opponent_height, player.opponent_weight, player.opponent_age, player.opponent_def_rating, player.minutes_played)
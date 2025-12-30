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
                player1 = game_stats(age=words[1], height=words[2], weight=words[3], guard_def_rating=words[4], cen_def_rating=words[5], guards=words[6])
            if len(words) > 1 and words[1] == "Luka":
                if len(words) > 3:
                    third_word = words[3]
                    if third_word == "makes":
                        if words[4].isdigit():
                            dist=int(words[4])
                            if dist<=5:
                                player1.shot_stats["short_attempt"] += 1
                                player1.shot_stats["short_make"] += 1
                            elif 5<dist<=22:
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
                            elif 5<dist<=21.5:
                                player1.shot_stats["medium_attempt"] += 1
                            else:
                                player1.shot_stats["long_attempt"] += 1
                        elif words[4] == 'driving' or words[4]=='running':
                            player1.shot_stats["short_attempt"] += 1
            elif len(words) > 1 and words[3] == "Luka's":
                if(len(words) > 6 and words[6].isdigit()):
                    dist=int(words[6])
                    if dist>=22:
                        player1.shot_stats["long_attempt"] += 1
        
        # append last collected player1 (if any) before returning
        if player1 is not None:
            players.append(player1)

        return players

result = analyze_game_stats("c:\\Users\\zhoul\\OneDrive\\Documents\\NBA_project\\data.txt")
for player in result:
    print(player.opponent_age, player.opponent_height, player.opponent_weight, player.opponent_gdef_rating, player.opponent_cdef_rating, player.guards, player.shot_stats["long_attempt"])
    print('\n')
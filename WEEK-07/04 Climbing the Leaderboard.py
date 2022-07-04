def climbingLeaderboard(ranked, player):
    # removing duplicates from the ranked list
    ordered_map = {}
    for rank in ranked:
        if rank not in ordered_map: ordered_map[rank] = True
        
    # duplicates have been removed, get back the list
    ranked = list(ordered_map.keys())
    stack = []
        
    # resultant ranks of all the players according to their scores in list player
    result = []
    
    # this will help us not append the scores back into the ranked list from the stack
    player.sort()
    
    # assuming current score's rank to be the last, and we will update it as we compare it with scores in stack
    counter = len(ranked) + 1
    
    for score in player:

        while len(ranked) != 0:
            popped = ranked.pop()

            if popped > score:
                # append the resultant rank
                result.append(counter)
                
                # for next comparison, as the next elment is guaranteed to be either equal or greater than current score
                ranked.append(popped)
                
                # rank for this score has been determined break out of the loop
                break
            
            counter -= 1
                        
        # when the while loop will determine that the current element's rank is 1
        # the ranked list will get empty and the rank will not be appended
        # hence, this check is necessary    
        if counter == 1: result.append(1)
        
    return result

# Kunal Wadhwa

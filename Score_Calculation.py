from Score_Input import Score_Input

class Score_Calculation:
    def __init__(self, score):
        self.score = score


    def calc_score(self):
        if(self.score == (Score_Input.strike) or self.score ==(Score_Input.spare)):
            return Score_Input.all_pins
        elif(self.score == Score_Input.zero):
            return Score_Input.zero_pins
        else:
            return int(self.score)

    
    def calc_score_final_frame(self):
        score_total = 0

        for final_frame_roll in self.score:
            if(final_frame_roll == Score_Input.strike) :
                score_total += Score_Input.all_pins
            elif(final_frame_roll ==(Score_Input.spare)):
                score_total += Score_Input.all_pins - int(self.score[0])
            elif(final_frame_roll == Score_Input.zero):
                score_total +=Score_Input.zero_pins
            else:
                score_total += int(final_frame_roll)
        
        return score_total
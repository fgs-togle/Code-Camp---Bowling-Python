from Score_Input import Score_Input
from Score_Calculation import Score_Calculation

class Score_Types:
    def __init__(self, bowling_frames):
        self.bowling_frames = bowling_frames


    def score_a_strike(self, frame):
        totals = 10
        totals += self.score_of_next_rolls_after_a_strike(frame)
        return totals


    def score_of_next_rolls_after_a_strike(self, frame):
        get_frame_scores_one_frame_after_current = list(self.bowling_frames[frame + 1])
        get_frame_scores_two_frames_after_current = self.find_two_frames_after_current(frame)
        combined_frame_scores = get_frame_scores_one_frame_after_current + get_frame_scores_two_frames_after_current

        first_score_after_strike = Score_Calculation(combined_frame_scores[0]).calc_score()
        second_score_after_strike = Score_Calculation(combined_frame_scores[1]).calc_score()
        return first_score_after_strike + second_score_after_strike

    
    def find_two_frames_after_current(self, frame):
        if(frame < 8):
            return list(self.bowling_frames[frame + 2])
        else:
            return list(self.bowling_frames[len(self.bowling_frames)-1])

        
    def score_a_spare(self, frame):
        totals = 10
        get_frame_scores_one_frame_after_current = list(self.bowling_frames[frame + 1])
        totals += Score_Calculation(get_frame_scores_one_frame_after_current[0]).calc_score()
        return totals


    def score_open_frame(self, frame):
        return Score_Calculation(self.bowling_frames[frame][0]).calc_score() + Score_Calculation(self.bowling_frames[frame][1]).calc_score()


    def score_final_frame(self, frame):
        final_frame_scores = list(self.bowling_frames[frame + 1])
        return Score_Calculation(final_frame_scores).calc_score_final_frame()

       
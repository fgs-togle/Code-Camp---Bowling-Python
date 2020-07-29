from Score_Input import Score_Input
from Score_Types import Score_Types

class Score:
    def __init__(self, bowling_frames):
        self.bowling_frames = bowling_frames
    
    def score(self):
        total_score = 0
        frames_length = len(self.bowling_frames)
        score_types = Score_Types(self.bowling_frames)

        for frame in range(frames_length-1):
            if(self.bowling_frames[frame].find(Score_Input.strike) >= 0): 
                total_score += score_types.score_a_strike(frame)
            elif(self.bowling_frames[frame].find(Score_Input.spare) >= 0):
                total_score += score_types.score_a_spare(frame)
            else:
                total_score += score_types.score_open_frame(frame)
        
        total_score += score_types.score_final_frame(frame)
        return total_score
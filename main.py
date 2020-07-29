from Score_Input import Score_Input
from Frames import Frames
from Score import Score

def main():
    bowling_scores = Score_Input().get_user_input()
    bowling_frames = Frames(bowling_scores).create_frames_from_bowling_marks()
    bowling_final_score = Score(bowling_frames).score()

    print(f"Total Bowling Score: {bowling_final_score}")

if __name__ == "__main__":
    main()
    
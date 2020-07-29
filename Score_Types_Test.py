from Score_Types import Score_Types
from Frames import Frames

class Test_Score_Types:
    def build_frames(self, scores):
       return Frames(scores).create_frames_from_bowling_marks()


    def test_ScoreAStrike_GivenStrikeInThirdFrame_ReturnCorrectScore(self):
        bowling_frames = self.build_frames("545/X449/54XX72XXX")
        result = Score_Types(bowling_frames).score_a_strike(2)
        assert result == 18


    def test_ScoreOfNextRollsAfterAStrike_GivenStrikeInThirdFrameAndAnOpenFrameFollowing_ReturnCorrectScore(self):
        bowling_frames = self.build_frames("545/X449/54XX72XXX")
        result = Score_Types(bowling_frames).score_of_next_rolls_after_a_strike(2)
        assert result == 8


    def test_ScoreASpare_GivenSpareInFifthFrameWithNextRollAFive_ReturnCorrectScore(self):
        bowling_frames = self.build_frames("545/X449/54XX72XXX")
        result = Score_Types(bowling_frames).score_a_spare(4)
        assert result == 15


    def test_ScoreOpenFrame_GivenOpenFrameInNinthFrame_ReturnCorrectScore(self):
        bowling_frames = self.build_frames("545/X449/54XX72XXX")
        result = Score_Types(bowling_frames).score_open_frame(8)
        assert result == 9


    def test_ScoreFinalFrame_GivenThreeStrikesInFinalFrame_ReturnCorrectScore(self):
        bowling_frames = self.build_frames("545/X449/54XX72XXX")
        result = Score_Types(bowling_frames).score_final_frame(8)
        assert result == 30


    def test_ScoreFinalFrame_GivenASparePlusBonusRollOfFourInFinalFrame_ReturnCorrectScore(self):
        bowling_frames = self.build_frames("545/X449/54XX725/4")
        result = Score_Types(bowling_frames).score_final_frame(8)
        assert result == 14
        

    def test_ScoreFinalFrame_GivenOpenFrameInFinalFrame_ReturnCorrectScore(self):
        bowling_frames = self.build_frames("545/X449/54XX7232")
        result = Score_Types(bowling_frames).score_final_frame(8)
        assert result == 5

    
    def test_ScoreFinalFrame_GivenSparePlusBonusRollOfZeroInFinalFrame_ReturnCorrectScore(self):
        bowling_frames = self.build_frames("545/X449/54XX728/-")
        result = Score_Types(bowling_frames).score_final_frame(8)
        assert result == 10
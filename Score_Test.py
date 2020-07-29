from Score import Score
from Frames import Frames

class Test_Score:
    def build_frames(self, scores):
       return Frames(scores).create_frames_from_bowling_marks()


    def test_Score_GivenPerfectGame_ReturnsPerfectTotalScore(self):
        bowling_frames = self.build_frames("XXXXXXXXXXXX")
        totals = Score(bowling_frames).score()
        assert totals == 300


    def test_Score_GivenAllSparesPlusBonusRoll_ReturnsCorrectTotalScore(self):
        bowling_frames = self.build_frames("5/5/5/5/5/5/5/5/5/5/5")
        totals = Score(bowling_frames).score()
        assert totals == 150


    def test_Score_GivenOpenFrames_ReturnsCorrectTotalScore(self):
        bowling_frames = self.build_frames("43434343434343434343")
        totals = Score(bowling_frames).score()
        assert totals == 70


    def test_Score_GivenRandomScore_ReturnsCorrectTotalScore(self):
        bowling_frames = self.build_frames("545/X449/54XX72XXX")
        totals = Score(bowling_frames).score()
        assert totals == 164


    def test_Score_GivenZeroScore_ReturnsCorrectTotalScore(self):
        bowling_frames = self.build_frames("--------------------")
        totals = Score(bowling_frames).score()
        assert totals == 0




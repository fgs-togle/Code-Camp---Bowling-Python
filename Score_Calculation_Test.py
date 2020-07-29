from Score_Calculation import Score_Calculation

class Test_Score_Calculation:
    def test_CalcScore_GivenAStrikeResultForAnyFrame_ReturnsCorrectScore(self):
        result = Score_Calculation("X").calc_score()
        assert result == 10


    def test_CalcScore_GivenASpareResultForAnyFrame_ReturnsCorrectScore(self):
        result = Score_Calculation("/").calc_score()
        assert result == 10


    def test_CalcScore_GivenAZeroResultForAnyFrame_ReturnsCorrectScore(self):
        result = Score_Calculation("-").calc_score()
        assert result == 0


    def test_CalcScore_GivenAnOpenFrameResultForAnyFrame_ReturnsCorrectScore(self):
        result = Score_Calculation("5").calc_score()
        assert result == 5


    def test_CalcScoreFinalFrame_GivenAllStrikesForFinalFrame_ReturnsCorrectScore(self):
        result = Score_Calculation(["X", "X", "X"]).calc_score_final_frame()
        assert result == 30

    
    def test_CalcScoreFinalFrame_GivenASpareAndStrikeBonusFrameForFinalFrame_ReturnsCorrectScore(self):
        result = Score_Calculation(["7", "/", "X"]).calc_score_final_frame()
        assert result == 20


    def test_CalcScoreFinalFrame_GivenASpareAndOpenBonusFrameForFinalFrame_ReturnsCorrectScore(self):
        result = Score_Calculation(["7", "/", "5"]).calc_score_final_frame()
        assert result == 15

    
    def test_CalcScoreFinalFrame_GivenAnOpenFrameForFinalFrame_ReturnsCorrectScore(self):
        result = Score_Calculation(["7", "2"]).calc_score_final_frame()
        assert result == 9


    def test_CalcScoreFinalFrame_GivenAZeroFrameForFinalFrame_ReturnsCorrectScore(self):
        result = Score_Calculation(["-", "-"]).calc_score_final_frame()
        assert result == 0

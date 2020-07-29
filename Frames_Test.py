from Frames import Frames

class Test_Frames:
    def test_CreateFramesFromBowlingMarks_GivenAPerfectGame_ReturnsListOfTenItems(self):
        bowling_frames = Frames("XXXXXXXXXXXX").create_frames_from_bowling_marks()
        assert len(bowling_frames) == 10

    
    def test_CreateFramesFromBowlingMarks_GivenAllSpares_ReturnsListOfTenItems(self):
        bowling_frames = Frames("5/5/5/5/5/5/5/5/5/5/5").create_frames_from_bowling_marks()
        assert len(bowling_frames) == 10


    def test_CreateFramesFromBowlingMarks_GivenOpenFrames_ReturnsListOfTenItems(self):
        bowling_frames = Frames("54545454545454545454").create_frames_from_bowling_marks()
        assert len(bowling_frames) == 10

    
    def test_CreateFramesFromBowlingMarks_GivenRandomScores_ReturnsListOfTenItems(self):
        bowling_frames = Frames("545/X449/54XX72XXX").create_frames_from_bowling_marks()
        assert len(bowling_frames) == 10
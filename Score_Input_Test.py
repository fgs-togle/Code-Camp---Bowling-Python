from Score_Input import Score_Input

class Test_Score_Input:
    def test_CleanUpInputString_GivenAStringWithSpaces_ReturnStringWithoutSpaces(self):
        score = Score_Input().clean_up_input_string("  X X X X X X X X X X X X ")
        assert score == "XXXXXXXXXXXX"


    def test_CleanUpInputString_GivenAStringWithLowerCaseLetters_ReturnStringWithUpperCaseLetters(self):
        score = Score_Input().clean_up_input_string("xxxxxxxxxxxx")
        assert score == "XXXXXXXXXXXX"


    def test_CleanUpInputString_GivenAStringWithLowerCaseLettersAndSpaces_ReturnStringWithUpperCaseLettersAndNoSpaces(self):
        score = Score_Input().clean_up_input_string("  x x xx 5/ 65 x x x 5/7 ")
        assert score == "XXXX5/65XXX5/7"

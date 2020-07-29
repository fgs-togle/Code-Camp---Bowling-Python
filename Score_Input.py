class Score_Input:
    strike = "X"
    spare  = "/"
    zero = "-"
    all_pins = 10
    zero_pins = 0


    def get_user_input(self):
        user_input = input("Enter your bowling scores by frame: ")
        return self.clean_up_input_string(user_input)


    def clean_up_input_string(self, user_input):
        return user_input.upper().replace(" ", "")

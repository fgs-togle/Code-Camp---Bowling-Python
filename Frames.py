from Score_Input import Score_Input

class Frames:
    def __init__(self, marks):
        self.marks = marks
    
    def create_frames_from_bowling_marks(self):
        bowling_frames = []
        frame_count = 1
        frame_rolls = ''

        for mark in self.marks:
            frame_rolls += mark

            if self.ready_to_create_frame(mark, frame_rolls, frame_count):
                bowling_frames.append(frame_rolls)
                frame_count+=1
                frame_rolls = ''

        bowling_frames.append(frame_rolls) 
        return bowling_frames

    def ready_to_create_frame(self, mark, frame_rolls, frame_count):
        create_frame = True if ((mark == Score_Input.strike or len(frame_rolls)==2) and frame_count < 10) else False
        return create_frame



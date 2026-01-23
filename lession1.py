class Students:
    name = "Trọng"
    score = {
        'math': 0,
        'english': 0,
        'history': 0
    }
    
    def score_average(self):
        avg_score = (self.score['math'] + self.score['english'] + self.score['history']) / 3
        return avg_score
    
    def show_rank(self):
        avg_score = self.score_average()
        if avg_score >= 9:
            rank = 'A'
        elif avg_score >= 8:
            rank = 'B'
        elif avg_score >= 7:
            rank = 'C'
        elif avg_score >= 6:
            rank = 'D'
        else:
            rank = 'F'
        return rank
    
    def show_info_student(self):
        print(f"Name: {self.name}")
        print(f"Avg Score: {self.score_average()}")
        print(f"Rank: {self.show_rank()}")
        print("\n--------------------------------\n")
        
    
std1 = Students()
std1.name = "Bao Long"
std1.score['math'] = 9
std1.score['english'] = 8
std1.score['history'] = 7

std1.show_info_student()

std2 = Students()
std2.name = "Trong"
std2.score['math'] = 2
std2.score['english'] = 3
std2.score['history'] = 4

std2.show_info_student()



class inf_list:
    def __init__(self):
        listing = [0,1]
        listing[1:1] = [listing]
        self.listing = listing

    def unlazy_eval(self,size):
        to_eval = "self.listing[1]"
        answer = []
        for i in xrange(size):
            to_eval += "[1]"
            answer.append(eval(to_eval))
        return answer

    

class Card():
    def __init__(self, qid):
        self.qid = qid
        self.answers = {}

    def set(self, question, answer):
        self.answers[question] = answer
        
    def get(self, question):
        return self.answers.get(question, None)

    def has(self, question, answer):
        a = self.get(question)
        if isinstance(a, list):
            return answer in a
        else:
            return answer == a
    
    def __repr__(self):
        s = "id:%d\n" % self.qid
        for key in self.answers.keys():
            s += " question: %d" % key
            s += " answer: %d\n" % self.answers[key]
        return s
    

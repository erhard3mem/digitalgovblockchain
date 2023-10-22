import hashlib

class Vote:
    """
        This class symbolizes a vote in a poll. It is represented by it's result value and can be viewed as hash and as plain string.
    """
    def v(self,pos):
        self.voting = pos;

    def string(self):
        return str(self.voting);

    def hash(self):
        result = hashlib.md5(self.string().encode())
        return result.hexdigest()


class Government:
    """
        This class symbolizes the government with its polling capacity and to add new poll decisions as well as define an poll text.
        When polling a vote is taken and hash in the blockchain.
    """
    decision = []
    
    def define(self,text_input):
        self.text = text_input;
    
    def addDecision(self, decision_input):
        self.decision.insert(len(self.decision),decision_input);

    def startPoll(self,poll_counter):
        bchain = Blockchain()
        decs = ''
        print(self.text);
        for r in range(len(self.decision)):
            decs = decs + ' ' + self.decision[r] + ' '
        for p in range(poll_counter):
            v = Vote();
            res = input(decs +": ")
            for r in range(len(self.decision)):                
                if(res == self.decision[r]):                
                    v.v(r);                
            print(bchain.hash(v));
        bchain.print_statistics();
        



class Blockchain:    
    """
        This class is the container for all voting results chained and hashed. It also contains the initial hashcode from which the chain is calculating.
    """
    votings = []
    initial_hash = hashlib.md5('.'.encode()).hexdigest()
    chain = initial_hash


    def hash(self, vote):        
        self.votings.insert(len(self.votings),vote);                
        self.chain = self.chain + '.' + str(vote.hash())
        result = hashlib.md5(self.chain.encode())
        return result.hexdigest()

    def print_statistics(self):
        #stats = [len(self.votings)]
        for v in self.votings:
            print(v.voting, end=" ")
            
        #print(stats)



stop_war = Government()
stop_war.define('Should the war be stopped?');
stop_war.addDecision('Yes');
stop_war.addDecision('No');
stop_war.startPoll(5);




from flask import Flask,render_template,request 
import hashlib

class Vote:
    """
        This class symbolizes a vote in a poll. It is represented by it's result value and can be viewed as hash and as plain string.
    """
    voting = 0;
    def v(self,pos):
        self.voting = pos;

    def string(self):
        return str(self.voting);

    def hash(self):
        result = hashlib.md5(self.string().encode())
        return result.hexdigest()
    
    def __str__(self):
        return str(self.voting);


class Government:
    """
        This class symbolizes the government with its polling capacity and to add new poll decisions as well as define an poll text.
        When polling a vote is taken and hash in the blockchain.
    """
    decision = []

    def getText(self):
        return self.text;
    
    def define(self,text_input):
        self.decision = []
        self.text = text_input;
    
    def addDecision(self, decision_input):
        self.decision.insert(len(self.decision),decision_input);

    def vote(self,input,chain):                
        v = Vote();            
        for r in range(len(self.decision)):                
            if(input == self.decision[r]):
                v.v(r) 
        chain.chain = chain.hash(v)


class Blockchain:    
    """
        This class is the container for all voting results chained and hashed. It also contains the initial hashcode from which the chain is calculating.
    """
    votings = []
    initial_hash = hashlib.md5('.'.encode()).hexdigest()
    chain = initial_hash

    def clear(self):
        self.votings = []
        self.initial_hash = hashlib.md5('.'.encode()).hexdigest()
        self.chain = self.initial_hash

    def hash(self, vote):        
        self.votings.insert(len(self.votings),vote);                
        self.chain = self.chain + '.' + str(vote.hash())
        result = hashlib.md5(self.chain.encode())
        return result.hexdigest()

    def print_statistics(self):
        print(chain);
        for v in self.votings:
            print(v.voting, end=" ")
    
    def getStatistics(self):
        return [chain,self.votings];

    def __str__(self):
        return str(self.chain)
            

app = Flask(__name__)

tmp_gov = Government()
chain = Blockchain()
decisions = ['Yes','No']

@app.route("/")
def start():    
    return render_template('start.html')
 
@app.route("/gov/stats")
def stats():
    statis = chain.getStatistics()
    text_input = tmp_gov.getText()
    count_1 = 0;
    count_0 = 0;
    decs = '<ol>'
    for i in statis[1]:
        decs += '<li>'+str(i)+'</li>'
        if(str(i)=='0'):
            count_0+=1;
        if(str(i)=='1'):
            count_1+=1;
    decs += '</ol>'
    decs += '<div class="block1"><h1>Yes: '+str(count_0)+', No: '+str(count_1)+'</h1></div>'
    return render_template(
     'stats.html',hc=str(statis[0]),decs=decs,txt=text_input)
 
@app.route("/gov/", methods = ['POST', 'GET'])
def startgov():
    if request.method == 'POST':
        chain.clear();
        form_data = request.form   
        name = str(form_data.getlist('name')[0]);
        hash = 'start';
        tmp_gov.define(name);
        tmp_gov.addDecision(decisions[0])    
        tmp_gov.addDecision(decisions[1])    
        return render_template(
            'form.html',name=name,vote=decisions,hash=hash)
 
@app.route("/gov/<string:name>/<string:hash>/")
def gov(name,hash):
    tmp_gov.define(name);
    tmp_gov.addDecision(decisions[0])    
    tmp_gov.addDecision(decisions[1])    
    return render_template(
     'form.html',name=name,vote=decisions,hash=hash)
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/gov/[poll]' to submit form"
    if request.method == 'POST':
        form_data = request.form   
        vote = str(form_data.getlist('vote')[0]);
        tmp_gov.vote(vote,chain);
        chain.print_statistics();
        return render_template(
            'form.html',name="hash",vote=decisions,hash=chain.chain,url="http://"+request.host+"/gov/"+tmp_gov.getText()+"/"+chain.chain);
         
 
app.run(host='localhost', port=5000)
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import random
import json

app = Flask(__name__)
CORS(app)
api = Api(app)

class Card:
    def __init__(self, invalue) :
        self.suit = invalue[0]
        self.rank = invalue[1]
        self.value = cardranking.get(self.rank)
        self.unicode = carddeck.get(invalue)
        self.name = rankname.get(self.rank)+" of "+suitname.get(self.suit)

    def __str__(self) :
        return str(self.unicode)
    
    def __repr__(self) :
        return repr({
            "Suit":self.suit,
            "Rank":self.rank,
            "Value":self.value,
            "Unicode":self.unicode,
            "Name":self.name
        })

rankname = {"1":"Ace","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","A":"Ten","B":"Jack","D":"Queen","E":"King",}
suitname = {"A":"Spades","B":"Hearts","C":"Diamonds","D":"Clubs"}
cardranking = {"1":14,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"D":12,"E":13}
carddeck = {"A1":"🂡","A2":"🂢","A3":"🂣","A4":"🂤","A5":"🂥","A6":"🂦","A7":"🂧","A8":"🂨","A9":"🂩","AA":"🂪","AB":"🂫","AD":"🂭","AE":"🂮","B1":"🂱","B2":"🂲","B3":"🂳","B4":"🂴","B5":"🂵","B6":"🂶","B7":"🂷","B8":"🂸","B9":"🂹","BA":"🂺","BB":"🂻","BD":"🂽","BE":"🂾","C1":"🃁","C2":"🃂","C3":"🃃","C4":"🃄","C5":"🃅","C6":"🃆","C7":"🃇","C8":"🃈","C9":"🃉","CA":"🃊","CB":"🃋","CD":"🃍","CE":"🃎","D1":"🃑","D2":"🃒","D3":"🃓","D4":"🃔","D5":"🃕","D6":"🃖","D7":"🃗","D8":"🃘","D9":"🃙","DA":"🃚","DB":"🃛","DD":"🃝","DE":"🃞"}
kartlar = [Card('A1'),Card('A2'),Card('A3'),Card('A4'),Card('A5'),Card('A6'),Card('A7'),Card('A8'),Card('A9'),Card('AA'),Card('AB'),Card('AD'),Card('AE'),Card('B1'),Card('B2'),Card('B3'),Card('B4'),Card('B5'),Card('B6'),Card('B7'),Card('B8'),Card('B9'),Card('BA'),Card('BB'),Card('BD'),Card('BE'),Card('C1'),Card('C2'),Card('C3'),Card('C4'),Card('C5'),Card('C6'),Card('C7'),Card('C8'),Card('C9'),Card('CA'),Card('CB'),Card('CD'),Card('CE'),Card('D1'),Card('D2'),Card('D3'),Card('D4'),Card('D5'),Card('D6'),Card('D7'),Card('D8'),Card('D9'),Card('DA'),Card('DB'),Card('DD'),Card('DE')]

class PokerAPI(Resource) :
    def get(self) :
        cards = kartlar.copy()
        random.shuffle(cards)
        board = []
        hand = []
        for i in range(5) :
            board.append(cards.pop())
        for i in range(2) :
            hand.append(cards.pop())
        return json.dumps([obj.__dict__ for obj in board])

api.add_resource(PokerAPI, '/poker/')

if __name__ == '__main__':
    app.run(debug=True)
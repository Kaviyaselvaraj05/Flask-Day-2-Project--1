from flask import Flask
app=Flask('__name__')
@app.route('/')
def Cricket():
    return "<h1>MS Dhoni</h1>"
@app.route('/About')
def Cricket1():
    return "<h1>Dhoni has captained the most international matches and is the most successful Indian captain. He has led India to victory in the 2007 ICC World Twenty20, the 2011 Cricket World Cup, and the 2013 ICC Champions Trophy, being the only captain to win three different limited overs ICC tournaments.</h1>"   
@app.route('/History')
def Cricket2():
    return "<h1>The atmosphere was epic, and a sense of a breathtaking climax was upon us with 10 runs required on the last 2 balls. The largest cricket stadium in the world, the Narendra Modi stadium had turned yellow, as all fans had come to see one man lift the IPL trophy for the fifth time. Mahendra Singh Dhoni sat calmly on his seat in the dugout watching as Mohit marked on his run up to bowl to Ravindra Jadeja. Tension was palpable as the match was more in the hands of Gujarat Titans than CSK. But then came the moment of the tournament, Jadeja smashed the last two balls, one for six and the other for a boundary. The crowd went into a frenzy, unable to contain their joy. It was the legendary MSD who etched his name in history, steering the Chennai Super Kings to their record-breaking 5th IPL title. Dhoni, the hero, remained calm under immense pressure, leading his team to a glorious victory that will be etched cricketing folklore forever.</h1>"
@app.route('/Early Life')
def Cricket3():
    return "<h1>MS Dhoni celebrates his birthday on 7th July and was born in the year 1981 in a small town in Ranchi, Jharkhand. We have all surely watched the movie, MS Dhoni-The Untold Story, and already know how a young boy, who was a goalkeeper in his school football team found his love in cricket. His skills were unmatched and his drive and work ethic all led him to where he is today. Quickly climbing up the ladders of the domestic cricket circuit, his performances were such that his selection for higher levels of the sport were inevitable. He was only a few steps away from making his debut for the National team. </h1>"
@app.route('/Sportsmanship')
def Cricket4():
    return "<h1>Under his leadership, India He won the 2007 T20 World Cup, 2011 ODI World Cup and 2013 Champions Trophy. His composure and strategic thinking on the field is commendable. Dhoni's dedication, sportsmanship and humility make him my favorite sportsman. He is a true inspiration for young cricketers and sports lovers.</h1>" 
if __name__=='__main__':
    app.run(debug=True)
from boggle import Boggle

boggle_game = Boggle()

@app.route("/")
def homepage():
    """Show board"""
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    return render_template("index.html", board=board, highscore=highscore
    numplays=numplays)

    @app.route("/check-word")
    def check_word():

        score=request.json["score"]
        highscore = session.get("highscore", 0)
        numplays = session.get("numplays", 0)

        session['numplays'] = numplays + 1
        session['highscore'] = max(score, highscore)

        return jsonify(brokenRecord = score > highscore)

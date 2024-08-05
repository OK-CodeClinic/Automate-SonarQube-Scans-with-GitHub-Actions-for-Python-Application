## file: app.py
## Auth: Kehinde Omokungbe

from flask import Flask, render_template, redirect, url_for
from config import Config
from models import get_all_candidates, get_candidate, vote_for_candidate
from forms import VoteForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    candidates = get_all_candidates()
    return render_template('index.html', candidates=candidates)

@app.route('/vote/<int:candidate_id>', methods=['GET', 'POST'])
def vote(candidate_id):
    candidate = get_candidate(candidate_id)
    form = VoteForm()
    if form.validate_on_submit():
        vote_for_candidate(candidate_id)
        return redirect(url_for('results'))
    return render_template('vote.html', candidate=candidate, form=form)

@app.route('/results')
def results():
    candidates = get_all_candidates()
    return render_template('results.html', candidates=candidates)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

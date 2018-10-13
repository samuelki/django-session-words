from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(req):
    if 'word_list' not in req.session:
        req.session['word_list'] = []
    return render(req, 'session_words/index.html')

def add_word(req):
    if req.method != 'POST':
        return redirect('/')
    
    if 'size' not in req.POST:
        size = 'small'
    else:
        size = 'big'

    word = {
        'word': req.POST['word'],
        'color': req.POST['color'],
        'size': size
    }

    req.session['word_list'].append(word)
    req.session.modified = True

    return redirect('/')

def clear(req):
    if 'word_list' in req.session:
        del req.session['word_list']

    return redirect('/')
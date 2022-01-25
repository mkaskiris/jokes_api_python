from werkzeug.exceptions import BadRequest

jokes = [
    {'id':1, 'joke': 'Why did the chicken cross the road?', 'punchline':'To get to the other side!'},
    {'id':2, 'joke': 'Whats the difference between a duck and a bicycle?', 'punchline':'A duck can swim!'},
    {'id':3, 'joke': 'Why were the Star Wars films released 4, 5, 6, 1, 2, 3?', 'punchline':'Because in charge of the release schedule, Yoda was.'},
    {'id':4, 'joke': 'Who is a dusty indv?', 'punchline':'Talha'},
    {'id':5, 'joke': 'A dusty bear walks into a bar and says "Give me a ameretto and ... apple juice. "Why the big pause" the bartender asks','punchline':'The dusty bear shrugged: "Im not sure, I was born with them"'}
    
]

def index(req):
    return [j for j in jokes], 200

def show(req, id):
    joke = find_by_id(id)
    return joke, 200

def create(req):
    new_joke = req.get_json()
    new_joke['id'] = sorted([j['id'] for j in jokes])[-1] + 1
    jokes.append(new_joke)
    return new_joke, 201


def find_by_id(id):
    try:
        return next(joke for joke in jokes if joke['id'] == id)
    except:
        raise BadRequest(f"Joke not found with id {id}. I have failed you")
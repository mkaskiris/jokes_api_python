import json

class TestAPICase():
    def test_home(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Hello from Team J.U.M.P!'

    def test_get_jokes(self, api):
        res = api.get('/api/jokes')
        assert res.status == '200 OK'
        assert len(res.json) == 2
    
    def test_get_joke(self, api):
        res = api.get('/api/jokes/6')
        assert res.status == '200 OK'
        assert res.json['joke'] == 'Test Joke 1'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']
    
    def test_joke_not_found(self,api):
        res = api.get('/api/jokes/10')
        assert res.status == '400 BAD REQUEST'
        assert 'Oops!' in res.json['message']
    
    def test_create_joke(self, api):
        mock_data = json.dumps({'joke': 'Testing post','punchline':'Cool'})

        mock_headers = {'Content-Type': 'application/json'}
        
        res = api.post('/api/jokes',data=mock_data, headers=mock_headers)
        
        assert res.json['id'] == 8
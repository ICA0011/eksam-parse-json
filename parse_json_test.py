import parse_json as pj

def test_assignment():
    assert pg.parse_json('http://upload.itcollege.ee/~aleksei/eksam.json') == "ICA0011"

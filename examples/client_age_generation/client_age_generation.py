def get_client_age_generation_py(client):
    age = client.get('age')
    if age is None or age < 0:
        return {'set': False}

    if age <= 18:
        generation = 'Gen.Z'
    elif age < 34:
        generation = 'Gen.Y'
    else:
        generation = 'Gen.X'

    return {'gen': generation, 'set': True}

def test_valid_client_age_under_18():
    client = {'age': 8}
    expected_res = {'gen': 'Gen.Z', 'set': True}
    assert get_client_age_generation_py(client) == expected_res

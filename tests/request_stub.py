from tests.json_stub import JsonStub


def get(url: str):
    return JsonStub(url)


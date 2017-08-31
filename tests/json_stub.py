from .resources.quotes import quotes


class JsonStub(object):

    def __init__(self, url):
        self.url = url

    def json(self):
        param = self.url.rsplit('/', 1)[1]

        if param.isdigit():
            return {"quote": quotes[int(param)]}
        elif param == "random":
            return {"quote": quotes[2]}

        return {"quotes": quotes}

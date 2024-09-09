import pyjokes

def generate_joke(lenguage):
    joke = pyjokes.get_joke(lenguage)
    return joke
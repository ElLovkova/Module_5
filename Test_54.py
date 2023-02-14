import json

class Model:
    title = '1'
    text = '2'
    author = '3'
    def __str__(self):
        return self.title, self.text, self.author
    def save(self):
        result = {}
        model = Model()
        l = list(filter(lambda x: not x.startswith('_') and isinstance(getattr(Model, x), str), Model.__dict__))
        #l.reverse()
        #print(l)
        result = {a:getattr(model, a) for a in l}
        #print(result)
        with open('model.json', 'w') as f:
            json.dump(result, f)

a = Model()
a.save()








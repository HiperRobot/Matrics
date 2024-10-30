from microhorario_dl import Microhorario
import json

micro = Microhorario.download()
# <Microhorario object at ...>

print(json.dumps(micro.as_json(), indent=2))

# micro.disciplinas
# [<Disciplina [ACN1000]>, <Disciplina[ACN1002]>, ...]
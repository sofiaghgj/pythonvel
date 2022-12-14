import json


def load_candidates() -> list[dict[str, int | str]]:
    with open('candidates.json', 'r', encoding='utf-8') as f:
        return json.load(f)

#
# def get_all():
#     inf = load_candidates()
#     a = '<pre>'
#     for i in inf:
#         a += f"""
#         {i['name']}\n
#         {i['position']}\n
#         {i['skills']}\n
#         """
#     a += '/<pre>'
#     return a

def get_all():
    candidates = load_candidates()
    for i in candidates:
        print(i["name"])
    return candidates
print(get_all())


def get_by_pk(pk):
    candidat = load_candidates()
    for i in candidat:
        if i['pk'] == pk:
            return i


def get_by_skill(skill_name):
    candidat = load_candidates()
    text = []
    for i in candidat:
        if skill_name.lower() in i['skills'].lower():
            text.append(i)
    return text


def main(list_can):
    sym = ''
    for i in range(len(list_can)):
        sym += f'''
        Имя кандидата - {list_can[i]['name']}
        Позиция кандидата {list_can[i]['position']}
        Навыки' {list_can[i]['skills']}
        '''
    return f'<pre>{sym}</pre>'










    

from models.users import User


def perform_search(query):

    search_ids = set()

    response = []
    first_names = User.query.filter(User.first_name.ilike("%{}%".format(query))).all()
    last_names = User.query.filter(User.last_name.ilike("%{}%".format(query))).all()

    print(first_names)
    print(last_names)
    for fn in first_names:
        if fn.id not in search_ids:
            search_ids.add(fn.id)
            response.append(fn.as_dict())

    for ln in last_names:
        if ln.id not in search_ids:
            search_ids.add(ln.id)
            response.append(ln.as_dict())

    return response

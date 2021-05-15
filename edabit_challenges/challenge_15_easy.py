# ONE WAY YOU CAN DO IT BELOW
'''relations = {
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother",
    "R2D2": "droid"
}

def relation_to_luke(name):
    for relation in relations:
        if name == relation:
            return relations[relation]

print("Luke, I am your " + relation_to_luke("Darth Vader"))'''


father = "Luke, I am your father."
sister = "Luke, I am your sister."
brother = "Luke, I am your brother in law."
droid = "Luke, I am your droid."

def relation_to_luke(name):
    if name == "Darth Vader":
        return father
    elif name == "Leia":
        return sister
    elif name == "Han":
        return brother
    else:
        return droid

print(relation_to_luke("Darth Vader"))
from transformers import pipeline

ner_pipeline = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)


def extract_entities(text):

    entities = ner_pipeline(text)

    people = []
    organizations = []
    locations = []

    for entity in entities:

        label = entity["entity_group"]
        word = entity["word"]

        if label == "PER":
            if word not in people:
                people.append(word)

        elif label == "ORG":
            if word not in organizations:
                organizations.append(word)

        elif label == "LOC":
            if word not in locations:
                locations.append(word)

    return {
        "people": people,
        "organizations": organizations,
        "locations": locations
    }
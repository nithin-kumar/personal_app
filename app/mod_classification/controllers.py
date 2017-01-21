"""Authentication Module Controllers."""
from flask import Blueprint, request, jsonify, abort
from multinomial_naive_bayes_classifier import MultinomialNaiveBayesClassifier
from nltk.corpus import stopwords
# Import password / encryption helper tools
# Import password / encryption helper tools

# Import the database object from the main app module
# Import module models (i.e. User)
# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_classification = Blueprint('auth', __name__, url_prefix='/lego')


# Signup method
@mod_classification.route('/api/v1.0/extract_symptom/', methods=['POST'])
def extract_symptom():
    """Signup method."""
    raw_text = request.json.get('text')
    stop = set(stopwords.words('english'))
    processed_text = ' '.join([i for i in raw_text.lower().split() if i not in stop])
    if (raw_text is None):
        abort(400)  # missing arguments

    # entity_classifier = MultinomialNaiveBayesClassifier({'patient': 'symptoms.txt'})
    symptom_classifier = MultinomialNaiveBayesClassifier({'symptom': 'symptoms.txt', 'nonsymptom': 'nonsymptoms.txt'})
    symptom_classifier.train()
    classfified_output = symptom_classifier.classify(processed_text.lower())
    if classfified_output == 'SYMPTOM':
        response = {'status': 1, 'symptom': processed_text}
    else:
        response = {'status': 0}
    return jsonify(response), 200

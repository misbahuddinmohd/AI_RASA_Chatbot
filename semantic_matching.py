'''
from rasa.shared.nlu.training_data.loading import load_data
from rasa.nlu.model import Interpreter
from rasa.core.agent import Agent

def semantic_matching(user_query):
    interpreter = Interpreter.load("C:\\Users\\misba\\Desktop\\chatbot using rasa\\myrasabot\\models\\20230518-230247-faint-procedure.tar.gz")  # Load your trained Rasa model
    # Create a Message object with the user query
    message = interpreter.create_message(user_query)
    
    # Use the interpreter to parse the user query
    interpreter.process(message)
    
    # Get the intent predicted by the interpreter
    predicted_intent = message.get("intent").get("name")
    
    # Load the NLU training data from the nlu.yml file
    training_data = load_data("C:\\Users\\misba\\Desktop\\chatbot using rasa\\myrasabot\\data\\nlu.yml")
    intent_examples = training_data.intents
    
    # Find the best matching example intent from the available intent examples
    best_match = None
    max_similarity = 0.0
    
    for example_intent in intent_examples:
        similarity = interpreter.nlu_model.training_data.intents[example_intent].similarity(message)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = example_intent
    
    return predicted_intent, best_match

# Example usage
user_query = "i have a question"

predicted_intent, best_match = semantic_matching(user_query)

print("Predicted Intent:", predicted_intent)
print("Best Match Example Intent:", best_match)

# Load your Rasa Core model
agent = Agent.load("path/to/your/core/model_directory")

# Retrieve the response for the best matching intent
responses = agent.handle_text(f"/{best_match}")
if responses:
    response = responses[0]
    print("Response:", response["text"])

'''
from rasa.nlu.model import Interpreter

# Load the trained model
model_path = "C:\\Users\\misba\\Desktop\\chatbot using rasa\\myrasabot\\models\\20230518-230247-faint-procedure.tar.gz"
interpreter = Interpreter.load(model_path)

# Parse user inputs
text = "Hello, how are you?"
result = interpreter.parse(text)

# Access the extracted intent and entities
intent = result["intent"]["name"]
entities = result["entities"]

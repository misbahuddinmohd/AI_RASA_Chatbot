# RASA_Chatbot
 
**BERT-Based AI Helpdesk Chatbot in RASA**

**ABSTRACT**

AI helpdesk system (chatbot) is designed to answer the user’s questions or queries with the available knowledge. The chatbot will be designed to provide quick and accurate responses to common questions and issues faced by users, such as technical support, customer support, HR support, and more. The system will be developed using natural language understanding (NLU) framework called RASA integrated with BERT architecture, which can understand and respond to user queries in a conversational manner using natural language processing (NLP) and advance machine learning techniques. The chatbot can be integrated into an existing platform or website and will be able to access a knowledge base containing information relevant to the user's queries.

**RASA OVERVIEW**

Rasa is an open-source framework for building conversational AI chatbots, assistants, and contextual assistants. It provides a complete development environment to build, train, and deploy chatbots that can understand natural language and carry out complex tasks.

**The Rasa framework consists of two main components:** 

1. **Rasa NLU (Natural Language Understanding):** The Rasa NLU component uses machine learning models to recognize intents and extract entities from user inputs. These models can be trained on annotated training data to improve their accuracy. Rasa NLU also allows developers to define custom actions, which can be used to perform tasks based on the user's input.
1. **Rasa Core:** It is responsible for managing the conversation flow and deciding how the chatbot should respond to user inputs. It uses a machine learning-based approach to learn from previous conversations and predict the most appropriate action to take based on the user's intent and the current context.

Rasa also provides tools for testing and evaluating chatbots, as well as deploying them on various platforms such as Facebook Messenger, Slack, and Telegram. 

BERT (Bidirectional Encoder Representations from Transformers) is a powerful language model that uses a bidirectional approach to capture the contextual relationships between words in a sentence. It operates on a transformer architecture. It achieves impressive accuracy by pre-training on vast amounts of unlabelled text data and fine-tuning on specific tasks. BERT utilizes a bidirectional approach, considering both the left and right context of each word. BERT's accuracy is attributed to its ability to generate contextualized word representations, enabling it to understand language semantics and nuances. Its accuracy makes it ideal for tasks like sentiment analysis, named entity recognition, and language translation. 

**Different files in Rasa:**

**nlu.yml**: This file contains the NLU (natural language understanding) data for your chatbot. It includes the training examples for each intent, as well as any entity labels and synonyms.

**stories.yml**: This file contains the stories for your chatbot, which are the examples of conversations between the user and the chatbot. Each story is a sequence of actions that the chatbot takes in response to user input.

**rules.yml**: It allows for specifying custom logic to handle specific user inputs and trigger appropriate responses or actions. Rules are defined using a combination of intents, entities, and conditions. It is mainly used for defining forms and fallback intent.

**domain.yml**: This file contains the intents, entities, actions, slots, and responses. It defines what your chatbot can do and how it should respond to user input.

**config.yml**: This file contains the configuration for the chatbot, which include language, pipeline – Tokenization method, Featurization method, Language Model to be used, Intent and Entity Classifier. policies for processing user input and the hyperparameters for training the model.

**endpoints.yml**: This file contains the endpoints for your chatbot, including the URL of the NLU server and the URL of the action server.

**actions.py**: This file contains the code for the custom actions that your chatbot can take in response to user input. It defines the logic for processing user input and generating responses.

**Standard Operating Procedure for Rasa Chatbot**

**Step 1: Installing Rasa (for Linux)**

1. **Install Python**

Rasa currently works only with python 3.8, 3.9, 3.10 versions. 

$ sudo apt update

$ apt-get install build-essential

$ sudo apt-get install libssl-dev openssl

$ wget <https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz>

$ tar xzvf Python-3.8.0.tgz

$ cd Python-3.8.0

$ ./configure

$ make

$ sudo make install

\# check if python is installed

$ python3 --version

1. **Install pip**

$ sudo apt install python3-pip

\# check if pip is installed

$ pip3 –version

1. **Create a virtual environment using virtual environment**

\# create and enter folder

$ mkdir rasaproject 

$ cd rasaproject

\# next we install python virtual environment 

$ sudo apt install python3-venv

\# we can now create a virtualenv 

$ python3 -m venv ./venv

\# activate virtualenv

$ source ./venv/bin/activate


1. **Install Rasa** 

$ pip install rasa

\# check if rasa is installed

$ rasa --version

**Step 2: Project Initialization**

`  `$ python -m rasa init

This will create a basic project structure with necessary files and directories.

**Step 3: Define Training Data**

1. Define the Intents with their corresponding training examples under the **nlu** section in data/**nlu.yml**

E.g.:  

1. Define different conversational flows using user intents and responses. Map each user intent with an action using the nomenclature ‘utter\_<intent-name>’, which will be invoked when that particular intent is triggered. This is done under **stories** section in data/**stories.yml**

E.g.:




1. Now to define forms or fallback intent (if any), define them in **rules** section of data/**rules.yml**

E.g.:

1. Now in the **intents** section of **domain.yml** mention all the intents present in nlu.yml / stories.yml. Then define all the action in **responses** section of **domain.yml** 

E.g.:

1. Now configure the **pipeline** and **policies** in **config.yml**

We have used a pre-trained BERT language model for training the model and the intent classification is done using DIET Classifier which is a algorithm built by Rasa using Transformer architecture same as BERT.

**Step 4: Train the NLU Model**

`   `# As we are using BERT architecture, so we need to install rasa transformers

` `$ pip install rasa[transformers]

`  `# Now to train the model use

` `$ python -m rasa train

This will train the Rasa model using your defined training data.

**Step 5: Run the Chatbot:**

1. To interact with chatbot in command prompt use (this needs internet) 

$ python -m rasa shell

1. To parse the user query and see its intent classification with confidence score use

$ python -m rasa run nlu

1. **To interact with chatbot using Rest channel or through rasa api over a frontend use**

$ python -m rasa run -m models –-enable-api –-cors “\*”

**Note:** To interact with chatbot using Rest channel or through rasa api uncomment the **rest** section in **credentials.yml** and uncomment the **action\_endpoint** section in **endpoints.yml**

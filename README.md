# Wine Business Chatbot

## Project Overview

This project implements a chatbot designed to provide quick and accurate responses based on a corpus of information about a business that sells wines. The chatbot offers users immediate answers without requiring them to browse lengthy documents. If the chatbot cannot answer a query based on the available corpus, it directs users to contact the business directly.

## Features

- Provides quick, context-based answers from a predefined corpus.
- Informs users to contact the business directly if it's unable to answer.
- Maintains a history of interactions to facilitate context-based responses.

## Requirements

The following packages are required to run the chatbot:

- `langchain`
- `langchain-community`
- `langchain-cohere`
- `langchain-groq`
- `python-dotenv`
- `flask`

You can install these packages using the `requirements.txt` file.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Dawn-Of-Justice/groq_chatbot.git
   cd groq_chatbot
   ```

2. **Set Up a Virtual Environment (Recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a .env file in the root directory and add your API keys, an example_.env file is provided for reference:

    ```env
    COHERE_API_KEY=your_cohere_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. **Activate Your Virtual Environment** (if you are using one):

   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Chatbot Script:**

   ```bash
   python run.py
   ```

This will launch the chatbot, which will prompt you to enter your queries.

### Running the Chatbot

To start the chatbot, follow these steps:

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact salosoja@gmal.com.

# Wine Business Chatbot

## Project Overview

This project implements a chatbot designed to provide quick and accurate responses based on a corpus of information about a business that sells wines. The chatbot is deployed on the business's website to offer users immediate answers without requiring them to browse lengthy documents. If the chatbot cannot answer a query based on the available corpus, it directs users to contact the business directly.

## Features

- Provides quick, context-based answers from a predefined corpus.
- Informs users to contact the business directly if their query is not covered.
- Maintains a history of interactions to facilitate context-based responses.

## Requirements

The following packages are required to run the chatbot:

- `langchain`
- `langchain-community`
- `langchain-cohere`
- `langchain-groq`
- `python-dotenv`

You can install these packages using the `requirements.txt` file.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/wine-business-chatbot.git
   cd wine-business-chatbot
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

    Create a .env file in the root directory and add your API keys:

    ```env
    COHERE_API_KEY=your_cohere_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or inquiries, please contact your-email@example.com.
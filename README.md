# AI Story Ending Rewriter
A simple Python application that uses a Large Language Model (LLM) to create alternative endings for movies and stories.

The user provides the story background, original ending, a specific plot change, and a desired ending type. The program then asks an LLM to generate a new ending based on the user’s instructions and returns the result as structured JSON.

Features

* Generate alternative endings for movies and stories
* Support multiple ending types:
    * Happy Ending
    * Bad Ending
    * Open Ending
    * Bittersweet Ending
* Keep the original characters and fictional world
* Start the rewrite from a user-defined plot change
* Avoid directly copying original dialogue
* Return structured JSON data
* Use Python functions to separate input, LLM processing, and output
* Use environment variables to protect the API key

How It Works

The application follows this workflow:

User Input
    ↓
Python
    ↓
Prompt Construction
    ↓
Qwen LLM API
    ↓
JSON Response
    ↓
Python JSON Parsing
    ↓
Formatted Output

The user provides:

1. Movie or story name
2. Story background
3. Original ending
4. Plot change point
5. Desired ending type

The LLM then generates:

* The selected ending type
* A new ending
* A list of key changes

Project Structure
```text
AI-Story-Ending-Rewriter/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
main.py

Contains the main application logic, including:

* User input
* LLM API request
* JSON parsing
* Result formatting

.env

Stores the API key locally.

Example:

DASHSCOPE_API_KEY=your_api_key_here

Do not upload .env to GitHub.

.gitignore

The .env file should be ignored by Git:

.env

Requirements

* Python 3.10+
* An Alibaba Cloud Model Studio / DashScope API key
* Internet connection

Install the required Python packages:

pip install openai python-dotenv

Configuration

Create a .env file in the project directory:

DASHSCOPE_API_KEY=your_api_key_here

The application uses the OpenAI-compatible API interface provided by Alibaba Cloud Model Studio.

The API client is configured with:

client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

The current project uses the Qwen Flash model.

Usage

Run:

python main.py

The program will ask for several inputs:

Please enter the movie/story name:
Please enter the story background:
Please enter the original ending:
Please enter the plot change point:
Please enter the desired ending type:

For example:

Movie/Story:
The Last Train
Story Background:
Two old friends meet again after many years...
Original Ending:
They leave without resolving their misunderstanding.
Plot Change:
One of them decides to stay and explain what happened.
Ending Type:
Happy Ending

The program then generates an alternative ending.

JSON Output

The LLM is instructed to return a JSON object with the following structure:

{
    "ending_type": "Happy Ending",
    "new_ending": "...",
    "key_changes": [
        "...",
        "..."
    ]
}

Python then parses the JSON response using:

result = json.loads(text)

The structured data can then be processed by Python instead of treating the LLM response as plain text.

Design Principles

The prompt includes several constraints to make the generated ending more consistent:

* Preserve the main character relationships
* Preserve the original fictional world
* Do not directly copy original dialogue
* Do not completely rewrite the previous story
* Make the new ending logically follow the plot change
* Keep character behavior consistent with their established personalities
* Limit the length of the generated ending
* Return only valid JSON

What I Learned

This project was built as a beginner LLM application project.

Through this project, I practiced:

* Calling an LLM API from Python
* Using an OpenAI-compatible API
* Managing API keys with environment variables
* Writing structured prompts
* Using JSON as structured LLM output
* Parsing JSON responses with Python
* Designing functions for different parts of an application
* Connecting user input, an LLM, and Python processing into one workflow

Future Improvements

Possible future improvements include:

* Add exception handling for API and JSON errors
* Validate user input
* Provide a menu instead of requiring users to type the ending type
* Support longer stories through text files
* Save generated endings to local files
* Add conversation history
* Build a simple web interface
* Add more structured story information
* Compare multiple alternative endings
* Connect the application to a web API using FastAPI

Disclaimer

This project is intended for learning and creative experimentation.

Users should provide story information they have the right to use. The application does not intentionally reproduce original dialogue or large portions of copyrighted works.
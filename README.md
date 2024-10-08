# Intelligent Agent

## Description
This intelligent agent is designed to facilitate the management and development of software projects. By integrating various tools and components, it provides a smoother and more efficient development experience. The agent leverages the OpenAI API, specifically ChatGPT-4, to process and respond to queries, aiding automation and decision-making during the software development lifecycle.
## How It Works

This intelligent agent is designed to provide a streamlined user experience by combining various technologies to manage and interact with a knowledge base dynamically.

### Key Features:

1. **Web Interface**: A Flask web application (`app.py`) provides a simple interface for users to interact with the agent. Users can start a new chat session and send messages to the assistant through HTTP endpoints. The agent responds using OpenAI’s API to process each message.

2. **Dynamic Knowledge Base**: The agent creates and manages a knowledge base from Markdown files stored in the `knowledge` directory. This information is loaded into a vector store, which enables the assistant to reference and answer queries with relevant context. Each time the knowledge base is updated, it can be recreated to reflect the latest information.

3. **Assistant Lifecycle**: The lifecycle of the assistant is managed using the script `chat.py`, which provides commands to create or recreate the assistant. When recreated, the assistant:
   - **Uploads Knowledge**: All `.md` files in the `knowledge` directory are uploaded to a vector store, which acts as a backend knowledge source for the assistant.
   - **Generates Instructions**: The assistant is configured with specific behaviors stored in the `behaviors/default.txt` file, ensuring it responds to queries according to predefined guidelines.
   - **Tool Integration**: The assistant has access to tools like a code interpreter and file search, enabling it to perform advanced tasks beyond simple text-based responses.

4. **Message Handling**: Users can interact with the assistant through the web interface. The `send_message` route in the Flask app sends user messages to the assistant and retrieves responses by creating a new message in an active thread. The agent processes the message in real-time, ensuring timely responses.

### Workflow:

1. **Launching the Web Interface**:
   - The Flask app (`app.py`) serves a web page where users can start a new chat and send messages.
   - The server listens for POST requests, handles user input, and communicates with the assistant via the OpenAI API.
  
2. **Managing the Assistant**:
   - The `chat.py` script manages the assistant’s lifecycle. You can create or recreate the assistant using the commands `create` or `recreate`, respectively.
   - The assistant is tightly integrated with the knowledge base and tools that allow it to respond with context-specific and accurate information.

3. **Knowledge Base and Behavior Management**:
   - **Knowledge Base**: Stored in the `knowledge` directory, any update to the Markdown files requires recreating the assistant to ensure it has the latest project information.
   - **Behaviors**: The assistant's response style is defined in the `behaviors/default.txt` file. This allows customization of how the assistant processes and responds to queries.


## Installation and Configuration with Poetry

To manage dependencies and the virtual environment, we use Poetry. Follow the steps below to set up and run the project.

### 1. Installing Poetry
If you don’t have Poetry installed, you can do so by running the following command:

```bash
pip install poetry
```

### 2. Installing Dependencies
Once Poetry is installed, you can install all the required dependencies by running:

```bash
poetry install
```

This will create an isolated virtual environment and download all dependencies listed in the `pyproject.toml` file.

### 3. Activating the Virtual Environment
To activate the virtual environment, run:

```bash
poetry shell
```

This allows you to interact with the configured environment for the project.

## Environment Variable Configuration

The agent requires authentication with the OpenAI API using an API key. You can configure this key in two ways: via an `.env` file or by passing the environment variable directly.

### Using an `.env` File

1. Create a file named `.env` in the root of your project.
2. Inside the file, add the following line:

```plaintext
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

3. Ensure that your application is configured to load environment variables from this file at startup.

### Setting the Environment Variable Directly

Alternatively, you can set the `OPENAI_API_KEY` environment variable directly in your execution environment.

- **On Windows (CMD)**:

```plaintext
set OPENAI_API_KEY=your_api_key_here
```

- **On Linux or macOS (Terminal)**:

```plaintext
export OPENAI_API_KEY=your_api_key_here
```

Remember to replace `your_api_key_here` with your actual OpenAI API key.

> **Important**
> For security reasons, never commit your `.env` file to public repositories or share your OpenAI API key publicly. Use secret managers or configure environment variables securely when collaborating.

## Running the Web Interface
The intelligent agent comes with a web interface for easy interaction. To launch the web server, follow these steps:

1. Ensure Python and necessary dependencies are installed.
2. Run the web server using:

```bash
python app.py
```

3. Access the web interface via your browser at `http://localhost:8888` or the configured port.

## Creating the Knowledge Base
To create and update the knowledge base, use the following commands:

- ```bash
  python chat.py create
  ```: Creates the assistant and its knowledge base from the Markdown files available in the `knowledge` directory.
  
- ```bash
  python chat.py recreate
  ```: Deletes the existing assistant and recreates it, updating the knowledge base with the latest information.

These commands ensure the assistant stays up-to-date with your project’s information.

## Customizing the Assistant

To customize the assistant, you can modify its knowledge base (`knowledge`) and adjust its behaviors (`behaviors`). This section explains how to apply these customizations.

### Updating the Knowledge Base

The assistant uses Markdown files stored in the `knowledge` folder to build its knowledge base. To update this information:

1. **Edit or Add Markdown Files**: Navigate to the `knowledge` folder in your project and edit the existing Markdown files or add new ones with the information you want the assistant to know.

2. **Regenerate the Knowledge Base**: After updating the Markdown files, use the command `python chat.py recreate` to regenerate the assistant with the updated knowledge base. This process deletes the existing assistant and creates a new one with the refreshed content.

### Modifying Behaviors

Behaviors define how the assistant interprets and responds to queries based on the provided knowledge. To adjust these behaviors:

1. **Edit the Behaviors File**: Locate and edit the `default.txt` file in the `behaviors` folder, adjusting the instructions to define how you want the assistant to respond.

2. **Apply the Changes**: Just like with the knowledge base, use the command `python chat.py recreate` to apply the changes to the assistant’s behaviors.

### Important Notes

- After modifying the knowledge base or behaviors, it’s crucial to test the assistant to ensure it behaves as expected. Consider creating a set of questions and answers to validate the new configurations.
  
- Any changes to the knowledge base or behaviors require the assistant to be regenerated for the changes to take effect.

With these customizations, you can tailor the assistant to better fit your project’s needs, enhancing the developer and user experience.

## Docker

If you prefer to run the intelligent agent in a Docker container, you can do so with the following command:

```bash
docker run -e OPENAI_API_KEY=your_api_key_here -p 8000:8000 intelligent-agent
```

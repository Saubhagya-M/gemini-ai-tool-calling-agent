# 🤖 Gemini AI Tool Calling Agent

A Python-based AI agent that uses **Google Gemini** with **tool calling** to perform tasks through custom Python functions.

The project demonstrates how an LLM can understand a user's natural-language request, select an appropriate tool, execute the tool, and return the result to the user.

## 🚀 Overview

This project integrates the **Google GenAI SDK** with custom Python tools.

Currently, the agent has two tools:

* 🧮 **Calculator** — performs basic mathematical operations
* 🎓 **Student Grade Evaluator** — calculates a student's grade based on marks

The Gemini model is configured with these tools, allowing it to decide when a tool should be used based on the user's input.

## ✨ Features

* Google Gemini API integration
* LLM tool calling / function calling
* Natural-language user interaction
* Custom Python tools
* Basic mathematical calculations
* Student grade evaluation
* Environment-variable based API key configuration
* Command-line interface
* Basic exception handling

## 🧠 How the Agent Works

The application follows this workflow:

```text
User Input
     │
     ▼
Google Gemini
     │
     ▼
Understands User Request
     │
     ▼
Selects Appropriate Tool
     │
     ├───────────────┐
     ▼               ▼
Calculator      Grade Evaluator
     │               │
     └───────┬───────┘
             ▼
        Tool Result
             │
             ▼
      Gemini Response
             │
             ▼
            User
```

The tools are registered with Gemini through the `GenerateContentConfig`.

## 🛠️ Tech Stack

* **Python**
* **Google Gemini / Google GenAI SDK**
* **python-dotenv**
* **Google Gemini Tool Calling**
* **Command Line Interface (CLI)**

## 📂 Project Structure

```text
gemini-ai-tool-calling-agent/
│
├── agent.py          # Main AI agent and CLI interface
├── calc.py           # Calculator tool
├── grade.py          # Student grade evaluation tool
├── config.py         # Configuration
├── test_gemini.py    # Gemini API testing
├── requirements.txt  # Python dependencies
├── LICENSE           # MIT License
├── .env              # Environment variables
└── README.md         # Project documentation
```

## 🔧 Available Tools

### 1. Calculator

The calculator tool is defined in `calc.py`.

It supports:

| Operation  | Description    |
| ---------- | -------------- |
| `add`      | Addition       |
| `subtract` | Subtraction    |
| `multiply` | Multiplication |
| `divide`   | Division       |

It also handles division by zero.

Example:

```python
calculator(10, 5, "add")
```

Output:

```text
15
```

### 2. Student Grade Evaluator

The `student_grade()` function evaluates marks using the following grading logic:

|       Marks | Grade |
| ----------: | :---: |
| 90 or above |   A+  |
|       80–89 |   A   |
|       70–79 |   B   |
|       60–69 |   D   |
|    Below 60 |   F   |

Example:

```python
student_grade(92)
```

Output:

```text
A+
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Saubhagya-M/gemini-ai-tool-calling-agent.git
```

Move into the project directory:

```bash
cd gemini-ai-tool-calling-agent
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Key Configuration

The application reads the Gemini API key from the environment variable:

```text
GOOGLE_API_KEY
```

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

The application loads this value using `python-dotenv`.

> ⚠️ **Security:** Never commit your real API key to GitHub. Make sure `.env` is included in `.gitignore`.

## ▶️ Run the Agent

Start the application with:

```bash
python agent.py
```

The program starts an interactive CLI:

```text
#############################
 GEMINI AI CALCULATOR AGENT
type exit to stop

You:
```

Enter a request and Gemini will process it using the available tools when appropriate.

### Example

```text
You: Calculate 25 multiplied by 8

AGENT: 200
```

Another example:

```text
You: A student scored 92 marks. What grade should they receive?

AGENT: A+
```

To stop the application:

```text
You: exit
```

## 🧪 Example Requests

You can try requests such as:

```text
Calculate 50 + 25
```

```text
What is 100 divided by 4?
```

```text
Multiply 15 by 12
```

```text
A student scored 95 marks. What is the grade?
```

```text
A student scored 74 marks. Evaluate the grade.
```

## 📌 Key Concepts Demonstrated

This project focuses on understanding the fundamentals of **AI agents and LLM tool calling**.

### Large Language Models

Google Gemini is used as the reasoning layer that interprets the user's natural-language request.

### Tool Calling

Custom Python functions are passed to Gemini as tools:

```python
mytools = [calculator, student_grade]
```

Gemini can then use the appropriate function for the requested task.

### Environment Variables

The API key is loaded securely through:

```python
os.getenv("GOOGLE_API_KEY")
```

### Modular Design

The calculator and grading functionality are separated into individual Python modules, making the project easier to understand and extend.

## 🔮 Future Improvements

Possible future enhancements include:

* [ ] Add more mathematical tools
* [ ] Add web search capabilities
* [ ] Add date and time tools
* [ ] Add currency conversion
* [ ] Add weather information
* [ ] Add conversation memory
* [ ] Add a Streamlit interface
* [ ] Add automated unit tests
* [ ] Improve tool error handling
* [ ] Add logging
* [ ] Deploy the agent as a web application
* [ ] Add more real-world AI agent tools

## 🎯 Learning Purpose

This project was built to explore the fundamentals of:

* Generative AI
* AI Agents
* Large Language Models
* Gemini API
* Tool Calling
* Function Calling
* Python
* API Integration
* Modular Programming
* Environment Variables

## 👨‍💻 Author

**Saubhagya Munsi**

Computer Science & Engineering
Interested in **Artificial Intelligence, Machine Learning, Data Analytics, and Software Development**.

### GitHub

https://github.com/Saubhagya-M

## 📄 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, consider giving the repository a star.

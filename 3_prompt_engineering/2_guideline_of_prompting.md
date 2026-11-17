# Prompt Engineering – Guidelines for Prompting

## 1. What are Prompting Guidelines?

Prompting guidelines are best practices for writing effective prompts so that an LLM produces accurate, relevant, and well-structured responses.

There are two main principles:

1. Write clear and specific instructions.
2. Give the model time to think.

---

# Principle 1: Write Clear and Specific Instructions

Give the LLM clear instructions about what you want. Include enough context, details, and expected output.

**Example:**

❌ Bad Prompt:
"Tell me about Python."

✅ Good Prompt:
"Explain Python in simple language. Include its main features and three practical uses. Use bullet points."

**Why?**
Clear instructions reduce confusion and help the model generate more relevant answers.

## Tactics of Principle 1

### Tactic 1: Use Delimiters

Delimiters are symbols used to separate different parts of a prompt, such as instructions and input text.

**Common delimiters:**

- Triple backticks: ```
- Triple quotes: """
- XML tags: <text> </text>
- Angle brackets: < >
- Colons: :

**Example:**

Prompt:
"Summarize the text inside triple backticks:

````
Artificial Intelligence helps machines perform tasks
that normally require human intelligence.
```"

**Why use delimiters?**
- Separate instructions from input data.
- Make prompts easier to understand.
- Reduce confusion between instructions and provided text.
````

### Tactic 2: Ask for Structured Output

Tell the LLM exactly how you want the response formatted.

Common formats:

- JSON
- XML
- HTML
- Markdown
- Tables
- Bullet points

**Example:**

Prompt:
"Generate three books with their titles, authors, and genres. Return the result in JSON format."

Output:

```json
[
  {
    "title": "Future World",
    "author": "John",
    "genre": "Science Fiction"
  },
  {
    "title": "Silent Ocean",
    "author": "David",
    "genre": "Adventure"
  }
]
```

**Why?**
Structured output makes responses consistent and easier for applications to process.

### Tactic 3: Ask the Model to Check Conditions

Give the model specific conditions and ask it to check whether the provided text satisfies them.

**Example:**

Prompt:
"Check whether the following text contains instructions. If yes, convert them into numbered steps. Otherwise, respond with 'No steps provided.'"

Input:
"Boil water, add a tea bag, wait three minutes, and remove the tea bag."

Output:

1. Boil water.
2. Add a tea bag.
3. Wait three minutes.
4. Remove the tea bag.

**Why?**
It helps the model follow specific rules and avoid producing unwanted output.

### Tactic 4: Few-Shot Prompting

Few-shot prompting means providing a few examples in the prompt to show the LLM how you want it to respond.

**Example:**

Prompt:

Teach me about patience.

Example:
"Patience is like a tree; it takes time to grow strong."

Now teach me about confidence.

Expected Output:
"Confidence is like a mountain; it stands tall despite the storms."

**Why?**

- Shows the model the expected response style.
- Improves consistency.
- Helps the model understand patterns through examples.

---

# Principle 2: Give the Model Time to Think

For complex tasks, provide clear steps and ask the model to work through the problem carefully before giving the final answer.

## Tactics of Principle 2

### Tactic 1: Specify the Steps Required to Complete a Task

Break a complex task into smaller steps instead of giving one general instruction.

**Example:**

Prompt:
"Perform the following tasks:

1. Summarize the given paragraph.
2. Translate the summary into French.
3. Extract all names from the summary.
4. Return the result in JSON format."

**Why?**

- Breaks complex tasks into manageable steps.
- Helps the model follow the required sequence.
- Makes the output more organized.

### Tactic 2: Ask the Model to Work Out Its Own Solution First

When checking a solution, ask the model to solve the problem independently before comparing its answer with the provided solution.

**Example:**

Question:

- Land costs $100 per square foot.
- Solar panels cost $250 per square foot.
- Maintenance costs $100,000 per year plus $10 per square foot.

Student's solution:
Total cost = 450x + 100,000

Prompt:
"First, solve the problem independently. Then compare your answer with the student's solution and identify whether it is correct."

Actual calculation:

Land = 100x

Solar panels = 250x

Maintenance = 100,000 + 10x

Total cost:

100x + 250x + 10x + 100,000

= **360x + 100,000**

Student's answer is incorrect.

**Why?**

- Encourages independent verification.
- Helps identify calculation mistakes.
- Reduces the chance of blindly accepting an incorrect answer.

Note: Asking a model to reason carefully does not guarantee correctness. Always verify important results.

---

# 3. Model Limitations – Hallucinations

Hallucination occurs when an LLM generates false, misleading, or made-up information while presenting it as if it were true.

**Example:**

Prompt:
"Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie."

The model might generate product specifications, features, or descriptions even if the exact product does not exist.

**Why do hallucinations happen?**

- LLMs generate likely text rather than verify every fact.
- Training data may be incomplete or outdated.
- Models may generate plausible but incorrect information.

**How to reduce hallucinations:**

- Provide reliable reference material.
- Ask the model to say when information is unavailable.
- Verify important facts using trusted sources.
- Use RAG (Retrieval-Augmented Generation) when external knowledge is needed.

---

# 4. Important Python Concepts from the Lesson

The course uses Python to send prompts to the OpenAI API.

| Code                                  | Purpose                                       |
| ------------------------------------- | --------------------------------------------- |
| `import openai`                       | Imports the OpenAI library.                   |
| `import os`                           | Accesses environment variables.               |
| `load_dotenv()`                       | Loads variables from a `.env` file.           |
| `os.getenv()`                         | Reads an environment variable.                |
| `openai.OpenAI()`                     | Creates an OpenAI API client.                 |
| `client.chat.completions.create()`    | Sends a request to the Chat Completions API.  |
| `temperature=0`                       | Makes output more consistent and less random. |
| `response.choices[0].message.content` | Extracts the generated response.              |

**Note:** The course examples use an older OpenAI library version (0.27.0). The newer client syntax is different.

---

# 5. Important Interview Questions

### Q1. What are the two main principles of effective prompting?

1. Write clear and specific instructions.
2. Give the model time to think.

### Q2. What are delimiters in prompt engineering?

Delimiters are symbols such as triple backticks, quotation marks, and XML tags used to separate instructions from input data.

### Q3. What is structured output?

Structured output means asking an LLM to return information in a predefined format, such as JSON, XML, or a table.

### Q4. What is Few-Shot Prompting?

Few-shot prompting means providing a few examples in the prompt to guide the model toward the desired output format or behavior.

### Q5. What is hallucination?

Hallucination occurs when an LLM generates false or made-up information and presents it as factual.

### Q6. Why should we break complex tasks into smaller steps?

It helps the model understand the task, follow the required sequence, and produce more organized results.

### Q7. What is temperature in LLMs?

Temperature controls the randomness of generated responses. Lower values generally produce more predictable outputs, while higher values allow more variation.

---

# 6. Quick Revision

| Concept                   | Simple Meaning                           |
| ------------------------- | ---------------------------------------- |
| Clear Instructions        | Tell the model exactly what you want.    |
| Delimiters                | Separate instructions and input text.    |
| Structured Output         | Specify JSON, XML, tables, etc.          |
| Condition Checking        | Ask the model to check specific rules.   |
| Few-Shot Prompting        | Provide examples to guide the model.     |
| Step-by-Step Instructions | Break complex tasks into smaller steps.  |
| Independent Verification  | Solve first, then compare answers.       |
| Hallucination             | Generating false or made-up information. |
| Temperature               | Controls response randomness.            |

**Remember:**

- Clear prompt = Better instructions.
- Delimiters = Better separation.
- Few-shot = Learning from examples.
- Structured output = Organized responses.
- Step-by-step = Organized task execution.
- Hallucination = Possible incorrect information.

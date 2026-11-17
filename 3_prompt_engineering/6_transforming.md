# Prompt Engineering: Transforming

## 1. What is Transforming?

Transforming means changing text from one form to another while keeping its original meaning.

We can use Large Language Models (LLMs) to transform text into different:

- Languages
- Tones
- Formats
- Writing styles
- Corrected versions

### Common transformation tasks

| Task                | Meaning                                   |
| ------------------- | ----------------------------------------- |
| Translation         | Convert text from one language to another |
| Language Detection  | Identify the language of text             |
| Tone Transformation | Change the tone of writing                |
| Format Conversion   | Convert text from one format to another   |
| Proofreading        | Find and correct writing mistakes         |
| Grammar Correction  | Fix grammatical errors                    |
| Spelling Correction | Fix spelling mistakes                     |
| Style Improvement   | Make writing clearer or more professional |

**Important:** Transformation changes how text is written or presented, but should preserve its intended meaning.

---

# 2. Setup

```python
import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")
```

### Python concepts

| Code            | Purpose                         |
| --------------- | ------------------------------- |
| `import openai` | Import OpenAI library           |
| `import os`     | Access environment variables    |
| `load_dotenv()` | Load variables from `.env` file |
| `find_dotenv()` | Find the `.env` file            |
| `os.getenv()`   | Read an environment variable    |

The API key is stored in the `.env` file instead of directly writing it in the Python code.

## 3. get_completion() Function

```python
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message["content"]
```

### What does this function do?

It sends a prompt to the LLM and returns the generated response.

### Important parameters

| Parameter     | Meaning                               |
| ------------- | ------------------------------------- |
| `prompt`      | Instructions given to the LLM         |
| `model`       | Model used to generate the response   |
| `temperature` | Controls randomness                   |
| `messages`    | Contains the conversation messages    |
| `role`        | Identifies who is sending the message |
| `content`     | Contains the actual prompt            |
| `response`    | Stores the API response               |

### Temperature

```python
temperature=0
```

A temperature of `0` makes the output more consistent and less random.

It is useful for tasks such as:

- Translation
- Grammar correction
- Information extraction

**Note:** This is the older API style used in the notebook. Current OpenAI SDK versions use a different API syntax.

---

# 4. Translation

Translation means converting text from one language into another while preserving its meaning.

### Example

````python
prompt = """
Translate the following English text to Spanish:

```Hi, I would like to order a blender```
"""

response = get_completion(prompt)

print(response)
````

Possible output:

Hola, me gustaría pedir una licuadora.

### Important points

- Specify the source language.
- Specify the target language.
- Provide the text to translate.
- Use delimiters to separate the text from instructions.

### Interview question

**Q: What is translation in Prompt Engineering?**

Answer:

Translation is the process of converting text from one language to another using an LLM while preserving the original meaning.

---

# 5. Language Detection

Language detection means identifying which language a piece of text is written in.

### Example

````python
prompt = """
Tell me which language this is:

```Combien coûte le lampadaire?```
"""

response = get_completion(prompt)

print(response)
````

Possible output:

French

### Important point

The LLM can identify the language without translating the text.

### Interview question

**Q: What is language detection?**

Answer:

Language detection identifies the language of a given text, such as English, French, Spanish, or Chinese.

---

# 6. Translation into Multiple Languages

We can ask an LLM to translate the same text into multiple languages.

### Example

````python
prompt = """
Translate the following text into French, Spanish,
and English pirate language:

```I want to order a basketball```
"""

response = get_completion(prompt)

print(response)
````

Possible output:

French:
Je voudrais commander un ballon de basket.

Spanish:
Quiero pedir un balón de baloncesto.

English pirate:
Arrr, I be wantin' to order a basketball!

### Important point

One prompt can request multiple translations.

We can also specify a special style, such as:

- Formal language
- Informal language
- Pirate language
- Business language

---

# 7. Formal and Informal Translation

The same sentence can have different forms depending on the audience and situation.

### Formal language

Used in:

- Business communication
- Professional emails
- Official requests

### Informal language

Used in:

- Friendly conversations
- Casual messages
- Everyday communication

### Example

Original:

Would you like to order a pillow?

Prompt:

```python
prompt = """
Translate the following text into Spanish
in both formal and informal forms:

"Would you like to order a pillow?"
"""

response = get_completion(prompt)

print(response)
```

Possible output:

Formal:
¿Le gustaría pedir una almohada?

Informal:
¿Te gustaría pedir una almohada?

### Important point

The meaning stays the same, but the language changes according to the audience.

---

# 8. Universal Translator

A universal translator can identify the language of a message and translate it into languages understood by different people.

### Example scenario

Imagine an international company where employees speak different languages.

Employees send IT support messages in:

- French
- Spanish
- Italian
- Polish
- Chinese

The support team needs to understand these messages in English and Korean.

### User messages

```python
user_messages = [
    "La performance du système est plus lente que d'habitude.",
    "Mi monitor tiene píxeles que no se iluminan.",
    "Il mio mouse non funziona",
    "Mój klawisz Ctrl jest zepsuty",
    "我的屏幕在闪烁"
]
```

### Step 1: Identify the language

````python
for issue in user_messages:

    prompt = f"""
    Tell me what language this is:

    ```{issue}```
    """

    lang = get_completion(prompt)

    print(f"Original message ({lang}): {issue}")
````

### Step 2: Translate the message

````python
for issue in user_messages:

    prompt = f"""
    Translate the following text into English and Korean:

    ```{issue}```
    """

    response = get_completion(prompt)

    print(response)
````

### What is happening?

1. `user_messages` stores multiple messages.
2. The `for` loop processes each message.
3. The LLM identifies the language.
4. The LLM translates the message.
5. The translated output helps the support team understand the issue.

### Important Python concepts

| Concept          | Purpose                             |
| ---------------- | ----------------------------------- |
| List             | Stores multiple messages            |
| `for` loop       | Processes messages one by one       |
| Variable `issue` | Stores the current message          |
| f-string         | Inserts the message into the prompt |
| Function call    | Sends the prompt to the LLM         |

**Main point:** A universal translator can help people communicate even when they speak different languages.

---

# 9. Tone Transformation

Tone transformation means changing the style or tone of text while keeping its original meaning.

### Common tones

- Professional
- Formal
- Informal
- Friendly
- Polite
- Persuasive
- Academic

### Example

Original:

"Dude, This is Joe, check out this spec on this standing lamp."

Prompt:

```python
prompt = """
Transform the following slang into a professional
business letter:

"Dude, This is Joe, check out this spec on this standing lamp."
"""

response = get_completion(prompt)

print(response)
```

Possible output:

Dear Sir or Madam,

My name is Joe. Please review the specifications
for this standing lamp.

Best regards,
Joe

### Important points

- Specify the original tone.
- Specify the desired tone.
- Keep the original meaning.
- Consider the intended audience.

### Interview question

**Q: What is tone transformation?**

Answer:

Tone transformation changes the style of writing, such as converting informal language into professional language, while preserving the original meaning.

---

# 10. Format Conversion

Format conversion means changing information from one format into another.

An LLM can convert:

- Python dictionary into HTML
- JSON into a table
- Text into Markdown
- Text into bullet points
- Information into structured JSON

### Example

Original Python dictionary:

```python
data_json = {
    "restaurant employees": [
        {
            "name": "Shyam",
            "email": "shyamjaiswal@gmail.com"
        },
        {
            "name": "Bob",
            "email": "bob32@gmail.com"
        },
        {
            "name": "Jai",
            "email": "jai87@gmail.com"
        }
    ]
}
```

### Prompt

```python
prompt = f"""
Convert the following Python dictionary into an HTML table.

Include:
- A title
- Column headers
- Employee names
- Email addresses

Data:
{data_json}
"""

response = get_completion(prompt)

print(response)
```

### Possible HTML output

```html
<h2>Restaurant Employees</h2>

<table>
  <tr>
    <th>Name</th>
    <th>Email</th>
  </tr>

  <tr>
    <td>Shyam</td>
    <td>shyamjaiswal@gmail.com</td>
  </tr>

  <tr>
    <td>Bob</td>
    <td>bob32@gmail.com</td>
  </tr>

  <tr>
    <td>Jai</td>
    <td>jai87@gmail.com</td>
  </tr>
</table>
```

### Displaying HTML in a notebook

```python
from IPython.display import display, HTML

display(HTML(response))
```

### Important points

- Specify the input format.
- Specify the output format.
- Explain how the output should be structured.
- Include required headers or titles.

**Important:** JSON is a data format. HTML is a markup format used to structure web pages.

---

# 11. Proofreading

Proofreading means checking text for errors and correcting them.

It can identify:

- Spelling mistakes
- Grammar mistakes
- Punctuation mistakes
- Incorrect word usage
- Sentence errors

### Example

Original:

"The girl with the black and white puppies have a ball."

Corrected:

"The girl with the black and white puppies has a ball."

### Prompt

```python
prompt = """
Proofread and correct the following text.

Rewrite the corrected version.

If there are no errors, say "No errors found".

Do not add punctuation around the corrected text.

Text:
"The girl with the black and white puppies have a ball."
"""

response = get_completion(prompt)

print(response)
```

Output:

The girl with the black and white puppies has a ball.

### Important point

Proofreading should correct errors without unnecessarily changing the original meaning.

---

# 12. Grammar and Spelling Correction

Grammar correction fixes errors in sentence structure.

Spelling correction fixes incorrectly written words.

### Example 1: Grammar

Incorrect:

"Yolanda have her notebook."

Correct:

"Yolanda has her notebook."

### Example 2: Spelling

Incorrect:

"This phrase is to cherck chatGPT for speling abilitty."

Correct:

"This phrase is to check ChatGPT for spelling ability."

### Example 3: Commonly confused words

Incorrect:

"Its going to be a long day."

Correct:

"It's going to be a long day."

Explanation:

- Its = possession
- It's = it is or it has

### Example 4: Their, there, and they're

Their:
Shows possession.

There:
Refers to a place or introduces a statement.

They're:
Means they are.

Example:

Incorrect:
"Their going to bring they're suitcases."

Correct:
"They're going to bring their suitcases."

### Example 5: Your and you're

Your:
Shows possession.

You're:
Means you are.

Incorrect:
"Your going to need you're notebook."

Correct:
"You're going to need your notebook."

### Example 6: Affect and effect

Affect:
Usually a verb meaning to influence.

Effect:
Usually a noun meaning a result.

Incorrect:
"That medicine effects my ability to sleep."

Correct:
"That medicine affects my ability to sleep."

### Important point

LLMs can correct grammar, spelling, punctuation, and commonly confused words in a single prompt.

---

# 13. Proofreading a Customer Review

An LLM can correct an entire review instead of correcting one sentence.

### Original review

```python
text = """
Got this for my daughter for her birthday cuz she keeps taking
mine from my room. Yes, adults also like pandas too.

She takes it everywhere with her, and it's super soft and cute.

One of the ears is a bit lower than the other, and I don't think
that was designed to be asymmetrical.

It's a bit small for what I paid for it though.

I think there might be other options that are bigger for
the same price.

It arrived a day earlier than expected, so I got to play
with it myself before I gave it to my daughter.
"""
```

### Prompt

````python
prompt = f"""
Proofread and correct this review:

```{text}```
"""

response = get_completion(prompt)

print(response)
````

### What does the LLM do?

It can:

- Correct grammar.
- Correct spelling.
- Improve punctuation.
- Fix sentence structure.
- Preserve the original meaning.

**Important:** Proofreading does not necessarily mean rewriting the entire review in a new style.

---

# 14. Showing Changes with Redlines

Redlines help show the differences between the original text and corrected text.

They can highlight:

- Added words
- Removed words
- Changed words

### Example

```python
from redlines import Redlines

diff = Redlines(text, response)

display(Markdown(diff.output_markdown))
```

### What is happening?

1. `text` contains the original review.
2. `response` contains the corrected review.
3. `Redlines()` compares both versions.
4. `output_markdown` generates a Markdown representation of the differences.
5. `display()` shows the differences in the notebook.

### Important point

Redlines are useful for reviewing changes instead of only seeing the final corrected text.

---

# 15. Improving Writing for a Specific Audience

An LLM can do more than correct mistakes.

It can also improve writing according to:

- Audience
- Writing style
- Purpose
- Quality requirements

### Example

Prompt:

````python
prompt = f"""
Proofread and correct this review.

Make it more compelling.

Ensure it follows APA style
and targets an advanced reader.

Output in Markdown format.

Text:
```{text}```
"""

response = get_completion(prompt)

display(Markdown(response))
````

### What does this prompt request?

| Instruction        | Meaning                                         |
| ------------------ | ----------------------------------------------- |
| Proofread          | Correct errors                                  |
| Make it compelling | Make writing more engaging                      |
| APA style          | Follow the requested academic writing style     |
| Advanced reader    | Use language suitable for knowledgeable readers |
| Markdown           | Return the result in Markdown format            |

### Important point

The output depends on the instructions provided in the prompt.

A prompt can control:

- What to correct
- How to rewrite
- Who the audience is
- What style to use
- Which format to return

---

# 16. Important Prompting Techniques Used in Transforming

## A. Specify the task

Clearly explain what you want.

Example:

"Translate this text into French."

## B. Specify the target

Tell the model the desired language, tone, or format.

Example:

"Translate into formal French."

## C. Use delimiters

Separate the instructions from the text.

Example:

````text
Translate the following text into Spanish:

```Hello, how are you?```
````

## D. Specify output requirements

Example:

"Return only the corrected sentence."

## E. Preserve meaning

Tell the model not to change the original meaning.

Example:

"Correct grammar without changing the meaning."

## F. Specify the audience

Example:

"Rewrite this message for a professional business audience."

---

# 17. Important Python Concepts

| Python concept | Meaning                        |
| -------------- | ------------------------------ |
| Function       | Reusable block of code         |
| Parameter      | Input accepted by a function   |
| Return         | Sends a value back             |
| List           | Stores multiple values         |
| Dictionary     | Stores key-value pairs         |
| `for` loop     | Repeats code for each item     |
| f-string       | Inserts variables into strings |
| `import`       | Loads a library or module      |
| `display()`    | Displays output in a notebook  |
| `HTML()`       | Represents HTML content        |
| `Markdown()`   | Represents Markdown content    |

---

# 18. Interview Questions

### Q1. What is transforming in Prompt Engineering?

Transforming means changing text into another language, tone, style, or format while preserving its intended meaning.

### Q2. What are common text transformation tasks?

Translation, language detection, tone transformation, format conversion, proofreading, grammar correction, and spelling correction.

### Q3. What is the difference between translation and tone transformation?

Translation changes the language.

Tone transformation changes the style or manner of writing.

### Q4. What is proofreading?

Proofreading checks and corrects spelling, grammar, punctuation, and writing errors.

### Q5. What is format conversion?

Format conversion changes information from one format into another, such as converting a dictionary into an HTML table.

### Q6. What is a universal translator?

A universal translator identifies and translates messages from different languages so people can communicate.

### Q7. What are redlines?

Redlines show differences between the original and corrected text, including additions, deletions, and changes.

### Q8. Can an LLM correct grammar and spelling together?

Yes. A single prompt can request grammar correction, spelling correction, and punctuation improvement.

### Q9. How can we control the output of an LLM?

We can specify the task, target language, tone, audience, output format, and length.

### Q10. Why use delimiters in prompts?

Delimiters separate instructions from the input text, making the task clearer.

---

# 19. Quick Revision

- **Transforming:** Change text while preserving its meaning.
- **Translation:** Convert text into another language.
- **Language detection:** Identify the language.
- **Universal translator:** Translate messages for people speaking different languages.
- **Tone transformation:** Change informal writing into formal or professional writing.
- **Format conversion:** Convert information into JSON, HTML, Markdown, or tables.
- **Proofreading:** Find and correct writing errors.
- **Grammar correction:** Fix sentence structure and grammar.
- **Spelling correction:** Fix misspelled words.
- **Redlines:** Show differences between original and corrected text.
- **Audience-based writing:** Adjust language and style for the intended reader.

## Main takeaway

Transforming allows an LLM to change the language, tone, format, or correctness of text according to instructions.

The most important skill is writing a clear prompt that specifies:

1. What transformation is required.
2. What input text should be transformed.
3. What the desired output should look like.
4. What meaning or information must be preserved.

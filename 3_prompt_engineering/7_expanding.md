# Prompt Engineering: Expanding

## 1. What is Expanding?

Expanding means using an LLM to generate detailed content from a short input, idea, or set of instructions.

For example:

Input:
Customer says the blender stopped working after one year.

Expanded output:
A professional customer service email apologizing for the problem, acknowledging the blender issue, and suggesting that the customer contact support.

### Common uses of Expanding

- Generating customer service emails.
- Expanding short ideas into paragraphs.
- Writing detailed product descriptions.
- Creating professional responses.
- Generating reports from key points.
- Writing personalized messages.

**Main point:** Expanding converts limited input into meaningful, detailed content.

---

## 2. Setup

```python
import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")
```

### Completion function

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

1. Receives a prompt.
2. Sends the prompt to the LLM.
3. Gets the generated response.
4. Returns the response as text.

### Temperature

Temperature controls the randomness of the generated response.

- `temperature=0`: More consistent and predictable responses.
- `temperature=0.7`: Allows more variation and creativity.

For customer service emails, a moderate temperature can help generate natural-sounding replies.

**Important:** Higher temperature does not necessarily mean better output.

---

## 3. Generating Personalized Customer Service Emails

### Scenario

Imagine an online store sells blenders.

A customer writes a negative review about a blender.

The customer mentions:

- The price increased significantly.
- The product's overall quality seems lower.
- The motor started making strange noises after one year.
- The warranty had already expired.
- The customer had to purchase another blender.
- The delivery was fast.

Our task is to generate a professional email responding to this customer.

### Step 1: Identify the sentiment

In the previous lesson (Inferring), we learned how to identify sentiment.

```python
sentiment = "negative"
```

This means the customer's overall experience is negative.

**Why do we need sentiment?**

Because the response should depend on the customer's experience.

| Sentiment | Response                                          |
| --------- | ------------------------------------------------- |
| Positive  | Thank the customer and appreciate their feedback  |
| Neutral   | Thank the customer for sharing their feedback     |
| Negative  | Apologize and suggest contacting customer service |

### Step 2: Store the customer review

```python
review = """
The blender was initially available for around $49,
but its price later increased to $70-$89.

The product quality also seems lower than before.

After about a year, the motor started making
a strange noise.

I contacted customer service, but the warranty
had already expired, so I had to buy another blender.

The delivery was fast, and I received it in about two days.
"""
```

The review contains the customer's actual experience.

### Step 3: Create the prompt

````python
prompt = f"""
You are a customer service AI assistant.

Your task is to write an email reply to a customer.

Instructions:
1. Thank the customer for their review.
2. If the sentiment is positive or neutral,
   appreciate their feedback.
3. If the sentiment is negative,
   apologize for their experience.
4. Suggest contacting customer service if appropriate.
5. Include specific details from the review.
6. Use a concise and professional tone.
7. Sign the email as "AI customer agent".

Customer review:
```{review}```

Review sentiment: {sentiment}
"""
````

### Step 4: Generate the email

```python
response = get_completion(prompt)

print(response)
```

### Possible output

Subject: We Appreciate Your Feedback

Dear Customer,

Thank you for taking the time to share your experience with our blender.

We are sorry to hear that the motor started making unusual noises after approximately one year and that your warranty had already expired when you contacted our support team.

We also appreciate your feedback regarding the product's pricing and quality. Your comments are valuable and help us improve our products and services.

If you need further assistance, please feel free to contact our customer service team.

Best regards,
AI customer agent

---

## 4. Using Specific Details from Customer Reviews

A generic response does not make the customer feel heard.

For example:

**Generic response:**

"Thank you for your feedback. We apologize for the inconvenience."

This response does not mention the customer's actual problem.

**Personalized response:**

"We apologize that your blender's motor started making unusual noises after approximately one year and that your warranty had already expired."

This response is better because it refers to the customer's actual experience.

### Important prompting technique

Tell the LLM explicitly:

"Make sure to use specific details from the customer's review."

This encourages the model to generate a personalized response instead of a generic one.

---

## 5. Changing Temperature to Generate Different Responses

In the notebook, the same prompt is used with two different temperature values.

### First example: Temperature = 0

```python
response = get_completion(prompt, temperature=0)

print(response)
```

The response is generally more consistent and predictable.

### Second example: Temperature = 0.7

```python
response = get_completion(prompt, temperature=0.7)

print(response)
```

The response may use different wording and a more varied writing style.

### Difference

| Temperature | Behavior                        |
| ----------- | ------------------------------- |
| 0           | More consistent and predictable |
| 0.7         | More varied and creative        |

**Important:** Even with the same prompt, changing temperature can change the generated response.

---

## 6. How Expanding Works in This Example

The complete process is:

1. Customer writes a product review.
2. Sentiment is identified using the Inferring technique.
3. The review and sentiment are provided to the LLM.
4. The prompt contains instructions about how to respond.
5. The LLM generates a personalized customer service email.
6. The generated email is returned.

### Workflow

Customer Review
|
v
Sentiment Analysis
|
v
Prepare Prompt
(Review + Sentiment + Instructions)
|
v
Send Prompt to LLM
|
v
Generate Personalized Email
|
v
Display Response

---

## 7. Important Prompting Techniques Used

| Technique                | Purpose                                             |
| ------------------------ | --------------------------------------------------- |
| Role assignment          | Tell the LLM to act as a customer service assistant |
| Clear instructions       | Explain what the email should contain               |
| Conditional instructions | Change the response according to sentiment          |
| Context                  | Provide the customer's original review              |
| Specific details         | Make the reply personalized                         |
| Tone control             | Request a concise and professional email            |
| Output requirements      | Specify the email signature                         |
| Temperature              | Control response randomness                         |

### Conditional instructions

These are instructions that tell the LLM to behave differently depending on a condition.

Example:

"If sentiment is positive, thank the customer. If sentiment is negative, apologize."

This allows one prompt to handle different customer situations.

---

## 8. Important Python Concepts

| Concept            | Purpose                           |
| ------------------ | --------------------------------- |
| Variable           | Stores sentiment and review       |
| String             | Stores customer review and prompt |
| f-string           | Inserts variables into the prompt |
| Function           | Reuses the API request logic      |
| Function parameter | Passes temperature and prompt     |
| Function return    | Returns the generated response    |
| `print()`          | Displays the generated email      |

---

## 9. Interview Questions

### Q1. What is expanding in Prompt Engineering?

Expanding means using an LLM to generate longer and more detailed content from short inputs, ideas, or instructions.

### Q2. What is the purpose of expanding?

It helps generate detailed content such as emails, reports, descriptions, and personalized responses.

### Q3. How can we generate personalized customer service emails?

We provide the customer review, its sentiment, and clear instructions to the LLM. The LLM uses this information to generate a relevant email.

### Q4. Why do we provide sentiment to the LLM?

Because the response depends on the customer's experience. Negative feedback requires an apology, while positive feedback requires appreciation.

### Q5. Why should we include specific details from a review?

Specific details make the response personalized and show that the customer's actual concerns have been considered.

### Q6. What is the role of temperature?

Temperature controls randomness in the model's output. Lower values produce more consistent responses, while higher values allow more variation.

### Q7. What are conditional instructions?

Conditional instructions tell the LLM to perform different actions depending on a condition.

Example:

"If the sentiment is negative, apologize. Otherwise, thank the customer."

### Q8. What is the difference between generic and personalized responses?

A generic response gives a common reply without mentioning the customer's specific experience.

A personalized response uses details from the customer's review.

---

## 10. Quick Revision

- **Expanding:** Generate detailed content from short input.
- **Customer review:** Feedback provided by the customer.
- **Sentiment:** Identifies whether feedback is positive, negative, or neutral.
- **Personalized email:** An email based on the customer's actual experience.
- **Conditional instructions:** Different actions based on conditions.
- **Specific details:** Make the generated response relevant to the customer.
- **Temperature:** Controls randomness in generated output.
- **Role assignment:** Defines the role the LLM should perform.

## Main Takeaway

Expanding allows an LLM to generate meaningful and detailed content from limited input.

In this lesson, we combine two Prompt Engineering concepts:

1. **Inferring:** Identify the sentiment of a customer review.
2. **Expanding:** Use that sentiment and the original review to generate a personalized customer service email.

The key is to provide the LLM with the right context, clear instructions, desired tone, and output requirements.

```

**Remember this simple difference:**

- **Inferring:** Understand what the customer is saying and feeling.
- **Expanding:** Use that understanding to generate a detailed response.

```

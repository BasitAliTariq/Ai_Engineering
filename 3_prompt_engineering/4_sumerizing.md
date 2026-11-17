# Prompt Engineering – Summarizing

## 1. What is Summarizing?

Summarizing means using an LLM to convert long text into shorter text while keeping the most important information.

In Prompt Engineering, we can control:

- Summary length (words, sentences, or characters).
- Topic or information to focus on.
- Output format.

**Example:**

Original Review:
"I bought a panda toy for my daughter. She loves it because it is soft and cute. However, I think it is a little expensive. It arrived earlier than expected."

Summary:
"The panda toy is soft, cute, and arrived early, but the customer feels it is overpriced."

---

## 2. Summarizing with a Word Limit

We can tell the LLM how many words to use in a summary.

**Example Prompt:**

"Summarize the following product review in a maximum of 30 words."

**Purpose:**
To get a short and clear summary without unnecessary details.

---

## 3. Summarizing with a Specific Focus

We can ask the LLM to summarize only information related to a particular topic.

### Example 1: Shipping and Delivery

**Prompt:**
"Summarize the product review in a maximum of 30 words. Focus only on shipping and delivery."

**Expected Output:**
"The product arrived one day earlier than expected."

**Use Case:** Sharing customer feedback with the shipping department.

### Example 2: Price and Value

**Prompt:**
"Summarize the product review in a maximum of 30 words. Focus only on price and product value."

**Expected Output:**
"The customer likes the product but feels it is expensive compared to other available options."

**Use Case:** Sharing customer feedback with the pricing department.

---

## 4. Extraction Instead of Summarization

Sometimes summarization includes information that is not related to our required topic.

In this situation, use **Extraction** instead.

**Summarization:** Converts the complete text into a shorter version.

**Extraction:** Takes out only the specific information we need from the text.

**Example:**

Review:
"The toy is cute and soft. It arrived one day earlier than expected, but I think it was expensive."

Task: Extract shipping information.

Output:
"The product arrived one day earlier than expected."

**Remember:**

- Summarization = Short version of the text.
- Extraction = Only required information from the text.

---

## 5. Summarizing Multiple Product Reviews

We can also use an LLM to summarize multiple customer reviews automatically.

**Example:**

Suppose an e-commerce website has four product reviews.

Instead of summarizing each review manually, we can:

1. Store all reviews in a Python list.
2. Use a `for` loop to process each review.
3. Send each review to the LLM.
4. Generate a short summary of each review.

**Python Example:**

````python
reviews = [review_1, review_2, review_3, review_4]

for i in range(len(reviews)):
    prompt = f"""
    Summarize the following product review
    in a maximum of 20 words:

    Review: ```{reviews[i]}```
    """

    response = get_completion(prompt)
    print(response)
````

**Purpose:**

- Process multiple reviews automatically.
- Save time.
- Understand customer feedback quickly.
- Identify common product problems.

---

## 6. Important Python Concepts

| Code               | Purpose                            |
| ------------------ | ---------------------------------- |
| `reviews = []`     | Stores multiple reviews in a list. |
| `range()`          | Generates a sequence of numbers.   |
| `len()`            | Counts the number of items.        |
| `for` loop         | Processes reviews one by one.      |
| `reviews[i]`       | Accesses a particular review.      |
| `get_completion()` | Sends the prompt to the LLM.       |

---

## 7. Interview Questions

**Q1. What is summarization in Prompt Engineering?**

Summarization means converting long text into shorter text while keeping the important information.

**Q2. Can we control the length of a summary?**

Yes. We can specify a word, sentence, or character limit in the prompt.

**Q3. What is focused summarization?**

It means asking the LLM to summarize only information related to a specific topic, such as price, delivery, or product quality.

**Q4. What is the difference between summarization and extraction?**

Summarization creates a shorter version of the original text, whereas extraction retrieves only specific required information.

**Q5. Can LLMs summarize multiple reviews?**

Yes. We can use Python lists and loops to send multiple reviews to an LLM and generate summaries automatically.

---

## 8. Quick Revision

| Concept               | Simple Meaning                        |
| --------------------- | ------------------------------------- |
| Summarization         | Make long text shorter.               |
| Word Limit            | Control summary length.               |
| Focused Summarization | Summarize a specific topic.           |
| Extraction            | Retrieve only required information.   |
| Multiple Reviews      | Summarize many reviews automatically. |

**Remember:**

- Summarization = Shorten the text.
- Focused Summarization = Focus on a particular topic.
- Extraction = Get only the required information.
- Multiple Reviews = Automate summarization using loops.

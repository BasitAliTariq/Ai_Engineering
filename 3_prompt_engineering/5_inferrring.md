# 1. What is Inferring?

Inferring means analyzing text and identifying useful information from it.

Examples:

- Identify whether a review is positive or negative.
- Identify emotions expressed by a customer.
- Extract product and company names.
- Identify the main topics of a news article.

# 2. Sentiment Analysis

Sentiment analysis means identifying whether the writer has a positive or negative opinion.

Example:

Review:
"The lamp is excellent, and I am happy with the service."

Prompt:
"What is the sentiment of this review?"

Output:
positive

Important:
We can control the output by asking for only one word:
"Give your answer as either positive or negative."

# 3. Identifying Emotions

The LLM can identify emotions expressed in text.

Example:

Review:
"The product is excellent. I am very happy with my purchase."

Prompt:
"Identify the emotions expressed in this review. Return no more than five lowercase words separated by commas."

Possible output:
happiness, satisfaction, excitement

# 4. Identifying Anger

We can ask the LLM whether a person is expressing anger.

Example:

Review:
"The product arrived broken, and the company did not help me."

Prompt:
"Is the writer expressing anger? Answer only yes or no."

Possible output:
yes

# 5. Extracting Product and Company Names

We can extract specific information from a review.

Example:

Review:
"I purchased a lamp from Lumina."

Prompt:
"Identify the product and company name. Return the result as JSON with Item and Brand as keys. If information is missing, use unknown."

Output:
{
"Item": "lamp",
"Brand": "Lumina"
}

Important:

- Extraction means retrieving specific information.
- JSON provides structured output.
- "unknown" handles missing information.

# 6. Performing Multiple Tasks at Once

We can ask the LLM to perform multiple inference tasks in one prompt.

Example:

Prompt:
Identify:

- Sentiment (positive or negative)
- Whether the reviewer is angry (true or false)
- Product name
- Company name

Return the result as JSON.

Output:
{
"Sentiment": "positive",
"Anger": false,
"Item": "lamp",
"Brand": "Lumina"
}

Important:
One prompt can perform multiple tasks, reducing the need for separate API calls.

# 7. Inferring Topics

Topic inference means identifying the main subjects discussed in a text or news article.

Example:

Article:
"NASA employees reported 95% job satisfaction. The government also plans to improve employee satisfaction in other departments."

Prompt:
"Identify five topics discussed in this text. Each topic should contain one or two words."

Possible output:
NASA, employee satisfaction, government, workplace, public sector

# 8. Creating News Alerts

We can use topic inference to monitor news articles for specific topics.

Example:

Topics we want to monitor:

- NASA
- Local government
- Engineering
- Employee satisfaction
- Federal government

We ask the LLM whether each topic appears in an article.

Output:
NASA: 1
Local government: 0
Engineering: 0
Employee satisfaction: 1
Federal government: 1

Meaning:

- 1 = Topic is present.
- 0 = Topic is not present.

Python code:

topic_dict = {
"nasa": 1,
"local government": 0,
"engineering": 0
}

if topic_dict["nasa"] == 1:
print("ALERT: New NASA story!")

Output:
ALERT: New NASA story!

# 9. Important Python Concepts Used

| Python concept | Purpose                                  |
| -------------- | ---------------------------------------- |
| f-string       | Insert variables into prompts            |
| List           | Store multiple topics or reviews         |
| `.split()`     | Convert comma-separated text into a list |
| `join()`       | Combine list items into a string         |
| Dictionary     | Store topics with their results          |
| `int()`        | Convert text into an integer             |
| `if` statement | Check whether a topic is present         |
| `for` loop     | Process multiple items                   |

Example:

response = "NASA, Government, Engineering"

topic_list = response.split(",")

print(topic_list)

Output:
["NASA", " Government", " Engineering"]

# 10. Interview Questions

Q1. What is inferring in Prompt Engineering?

Answer:
Inferring means analyzing given text using an LLM to identify information such as sentiment, emotions, names, and topics.

Q2. What is sentiment analysis?

Answer:
Sentiment analysis identifies whether a piece of text expresses a positive or negative opinion.

Q3. What is the difference between sentiment and emotion?

Answer:
Sentiment identifies the overall opinion (positive or negative), while emotion identifies feelings such as happiness, anger, or disappointment.

Q4. What is topic inference?

Answer:
Topic inference identifies the main subjects discussed in a text or article.

Q5. Can an LLM perform multiple tasks in one prompt?

Answer:
Yes. We can ask an LLM to identify sentiment, emotions, anger, and product details in a single prompt.

Q6. Why use JSON in prompts?

Answer:
JSON provides structured output that is easier for applications and Python programs to process.

Q7. How can we create news alerts using an LLM?

Answer:
We can ask the LLM to check whether selected topics appear in an article. If a topic is present, Python can trigger an alert.

# Quick Revision

- Inferring = Analyzing text to identify useful information.
- Sentiment = Positive or negative opinion.
- Emotion = Feelings expressed by the writer.
- Anger detection = Identify whether the writer is angry.
- Extraction = Retrieve specific information, such as product and company names.
- Multiple tasks = Perform several analysis tasks in one prompt.
- Topic inference = Identify subjects discussed in text.
- News alerts = Check articles for selected topics and trigger alerts.

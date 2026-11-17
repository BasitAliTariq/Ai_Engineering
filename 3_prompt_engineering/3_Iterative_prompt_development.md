# Prompt Engineering – Iterative Prompt Development

## 1. What is Iterative Prompt Development?

Iterative Prompt Development means improving a prompt step by step until the LLM produces the desired output.

Instead of writing one prompt and accepting its response, we:

1. Write an initial prompt.
2. Check the generated response.
3. Identify mistakes or missing details.
4. Improve the prompt.
5. Repeat until we get the desired result.

**Simple Example:**

We want an LLM to write a product description for an office chair.

We improve the prompt whenever we find a problem with the response.

---

## 2. Practical Example

### Step 1: Write the Initial Prompt

Ask the LLM to generate a product description using a technical fact sheet.

**Prompt:**
"Write a marketing description for this office chair using the given product specifications."

**Problem:** The generated description is too long.

### Step 2: Fix the Length

Add a word limit to the prompt.

**Improved Prompt:**
"Write a product description using the given specifications. Use a maximum of 50 words."

**Result:** The description becomes shorter.

### Step 3: Focus on Relevant Information

The description contains unnecessary details. We want to target furniture retailers.

**Improved Prompt:**
"Write a technical product description for furniture retailers. Focus on the materials used to construct the chair. Use a maximum of 50 words."

**Result:** The description focuses on materials instead of general information.

### Step 4: Include Additional Information

We also want the product ID in the description.

**Improved Prompt:**
"Write a technical product description for furniture retailers. Focus on construction materials. Include every 7-character Product ID from the specifications. Use a maximum of 50 words."

**Result:** The description now includes the required product ID.

### Step 5: Add a Dimensions Table

We also want product dimensions in a table.

**Improved Prompt:**
"Write a technical product description for furniture retailers. Focus on construction materials and include every 7-character Product ID.

After the description, create a two-column table containing dimension names and measurements in inches.

Give the table the title 'Product Dimensions'."

**Result:** The output now includes a product description and a dimensions table.

### Step 6: Specify the Output Format

Finally, we want the output in HTML so it can be used on a website.

**Final Prompt:**
"Write a technical product description for furniture retailers. Focus on construction materials and include every 7-character Product ID.

After the description, create a two-column dimensions table with measurements in inches only.

Give the table the title 'Product Dimensions'.

Format the complete output in HTML and place the description inside a `<div>` element."

**Result:** We get website-ready HTML containing the product description and dimensions table.

---

## 3. Main Idea

In this example, we improved the prompt by fixing five issues:

| Issue                | Improvement                        |
| -------------------- | ---------------------------------- |
| Description too long | Added a 50-word limit.             |
| Wrong information    | Focused on construction materials. |
| Missing Product ID   | Asked to include Product ID.       |
| Missing dimensions   | Added a dimensions table.          |
| Wrong output format  | Requested HTML format.             |

---

## 4. Important Python Concepts

| Code                      | Purpose                             |
| ------------------------- | ----------------------------------- |
| `fact_sheet_chair`        | Stores product information.         |
| `f"""..."""`              | Creates a formatted string.         |
| `get_completion(prompt)`  | Sends the prompt to the LLM.        |
| `response`                | Stores the model's response.        |
| `response.split()`        | Splits text into words.             |
| `len()`                   | Counts the number of words.         |
| `display(HTML(response))` | Displays HTML output in a notebook. |

---

## 5. Interview Questions

**Q1. What is Iterative Prompt Development?**

It is the process of improving a prompt step by step by analyzing the model's output and fixing problems until the desired result is achieved.

**Q2. Why do we use Iterative Prompt Development?**

To improve response quality, accuracy, relevance, length, and formatting.

**Q3. What are the main steps involved?**

1. Write a prompt.
2. Generate a response.
3. Analyze the response.
4. Identify problems.
5. Improve the prompt.
6. Repeat until the desired output is achieved.

**Q4. What is the main difference between a normal prompt and iterative prompt development?**

A normal prompt is written once, while iterative prompt development involves testing and improving the prompt multiple times.

---

## 6. Quick Revision

**Iterative Prompt Development = Write → Test → Analyze → Improve → Repeat.**

Remember:

- Control response length.
- Focus on the target audience.
- Include all required information.
- Specify the output format.
- Keep improving until you get the desired result.

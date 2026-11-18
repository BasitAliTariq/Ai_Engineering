# How Large Language Models (LLMs) Work

## Complete Beginner-Friendly Step-by-Step Guide

# Table of Contents

1. [Before Understanding LLMs: How Computers Process Information](#1-before-understanding-llms-how-computers-process-information)
2. [What Is Artificial Intelligence (AI)?](#2-what-is-artificial-intelligence-ai)
3. [Machine Learning vs Deep Learning](#3-machine-learning-vs-deep-learning)
4. [What Is a Neural Network?](#4-what-is-a-neural-network)
5. [What Is Natural Language Processing (NLP)?](#5-what-is-natural-language-processing-nlp)
6. [What Is a Language Model?](#6-what-is-a-language-model)
7. [What Is a Large Language Model (LLM)?](#7-what-is-a-large-language-model-llm)
8. [Understanding GPT](#8-understanding-gpt)
9. [How Does GPT Generate Text?](#9-how-does-gpt-generate-text)
10. [What Is a Transformer?](#10-what-is-a-transformer)
11. [How Does an LLM Convert Text into Numbers?](#11-how-does-an-llm-convert-text-into-numbers)
12. [Tokenization](#12-tokenization)
13. [Vocabulary and Token IDs](#13-vocabulary-and-token-ids)
14. [Vector Embeddings](#14-vector-embeddings)
15. [Positional Information](#15-positional-information)
16. [Understanding the Transformer Architecture](#16-understanding-the-transformer-architecture)
17. [Self-Attention Mechanism](#17-self-attention-mechanism)
18. [Query, Key, and Value (Q, K, V)](#18-query-key-and-value-q-k-v)
19. [Multi-Head Attention](#19-multi-head-attention)
20. [Feed-Forward Neural Network](#20-feed-forward-neural-network)
21. [Normalization and Residual Connections](#21-normalization-and-residual-connections)
22. [Encoder and Decoder Architecture](#22-encoder-and-decoder-architecture)
23. [How LLM Training Works](#23-how-llm-training-works)
24. [How LLM Inference Works](#24-how-llm-inference-works)
25. [Logits, Softmax, and Probability Distribution](#25-logits-softmax-and-probability-distribution)
26. [How Does an LLM Select the Next Token?](#26-how-does-an-llm-select-the-next-token)
27. [Temperature and Text Generation](#27-temperature-and-text-generation)
28. [Complete Working Flow of an LLM](#28-complete-working-flow-of-an-llm)
29. [Using an LLM with Python and Hugging Face](#29-using-an-llm-with-python-and-hugging-face)
30. [Important LLM Terminology](#30-important-llm-terminology)
31. [Common Misunderstandings](#31-common-misunderstandings)
32. [Recommended Learning Roadmap](#32-recommended-learning-roadmap)
33. [Final Summary](#33-final-summary)

---

# 1. Before Understanding LLMs: How Computers Process Information

Before understanding artificial intelligence, let's understand one basic thing:

**Computers work with numbers, not human language directly.**

When we use a computer, we interact with it using:

- Text
- Images
- Videos
- Audio
- Commands

But internally, computers represent and process information using numerical data.

## 1.1 What Is Binary?

Computers use a binary system consisting of two values:

- 0
- 1

These values are called bits.

For example:

```text
01001000 01101001
```

This binary data can represent the text:

```text
Hi
```

The important thing to understand is that computers convert information into numerical representations so that their hardware can process it.

## 1.2 Why Is This Important for LLMs?

An LLM cannot directly perform mathematical operations on ordinary sentences.

It needs numerical representations of text.

For example:

```text
Human Text:
I love AI
       |
       v
Text Processing
       |
       v
Numerical Representation
       |
       v
LLM
```

Later, we will understand how tokenization and embeddings perform this conversion.

**Remember:** Converting text into numbers is one of the first important steps in understanding how LLMs work.

---

# 2. What Is Artificial Intelligence (AI)?

## 2.1 Definition

Artificial Intelligence (AI) is a field of computer science that focuses on building systems that can perform tasks that normally require human intelligence.

Examples include:

- Understanding language
- Recognizing images
- Making predictions
- Solving problems
- Generating content
- Making decisions

For example:

When you use a chatbot and ask:

```text
What is JavaScript?
```

The chatbot processes your question and generates an answer.

This is an example of an AI application.

## 2.2 Main Categories of AI

To understand LLMs, first understand the relationship between AI, Machine Learning, and Deep Learning.

```text
Artificial Intelligence (AI)
            |
            v
      Machine Learning
            |
            v
       Deep Learning
            |
            v
       Neural Networks
            |
            v
      Transformer Models
            |
            v
      Large Language Models
```

This diagram shows a simplified relationship. Neural networks are the foundation of deep learning, and Transformers are one type of neural network architecture.

---

# 3. Machine Learning vs Deep Learning

## 3.1 What Is Machine Learning?

Machine Learning (ML) is a subset of AI.

Instead of writing every rule manually, developers provide data to a machine learning algorithm so that it can learn patterns and make predictions.

### Example: Spam Email Detection

Suppose we want to build a system that identifies spam emails.

We provide examples:

| Email                             | Label    |
| --------------------------------- | -------- |
| Congratulations! You won a prize. | Spam     |
| Meeting scheduled for tomorrow.   | Not Spam |
| Claim your free reward now!       | Spam     |
| Please review the project report. | Not Spam |

The machine learning model learns patterns from these examples.

When it receives a new email, it predicts whether that email is spam.

## 3.2 What Is Deep Learning?

Deep Learning is a subset of Machine Learning.

It uses neural networks with multiple layers to learn complex patterns from data.

Deep learning is used in:

- Image recognition
- Speech recognition
- Natural language processing
- Autonomous systems
- Generative AI
- Large Language Models

## 3.3 Machine Learning vs Deep Learning

| Machine Learning                              | Deep Learning                             |
| --------------------------------------------- | ----------------------------------------- |
| Uses different algorithms to learn from data  | Uses neural networks with multiple layers |
| Often requires manual feature engineering     | Can learn useful features automatically   |
| Can work well with smaller datasets           | Often benefits from large datasets        |
| Includes decision trees and linear regression | Includes CNNs, RNNs, and Transformers     |

## 3.4 Where Do LLMs Fit?

Most modern LLMs are based on Deep Learning.

They use neural networks, particularly Transformer architectures, to learn language patterns.

---

# 4. What Is a Neural Network?

## 4.1 Definition

A Neural Network is a machine learning model inspired by the way biological neurons are connected.

It consists of connected units called artificial neurons.

These neurons are organized into layers.

A basic neural network contains:

1. Input Layer
2. Hidden Layers
3. Output Layer

## 4.2 Understanding Neural Network Layers

```text
          INPUT LAYER
               |
               v
          HIDDEN LAYER
               |
               v
          HIDDEN LAYER
               |
               v
          OUTPUT LAYER
```

### Input Layer

Receives the input data.

For example:

```text
Input: Numerical representation of text
```

### Hidden Layers

Process information and learn patterns.

A neural network can contain many hidden layers.

### Output Layer

Produces the final prediction.

For example:

```text
Prediction: Spam
```

## 4.3 What Are Weights and Biases?

Neural networks contain learnable numerical values called parameters.

Two important types are:

- Weights
- Biases

Weights control how strongly information is transformed or connected.

Biases provide additional adjustable values that help the network learn.

During training, these parameters are updated to improve predictions.

## 4.4 Why Are Neural Networks Important for LLMs?

LLMs are neural network models.

They contain many layers and learnable parameters.

These parameters are adjusted during training so that the model becomes better at predicting the next token.

---

# 5. What Is Natural Language Processing (NLP)?

## 5.1 Definition

Natural Language Processing (NLP) is a field of AI that focuses on enabling computers to process and work with human language.

Human languages include:

- English
- Urdu
- Arabic
- Chinese
- French
- Spanish

NLP helps computers perform tasks such as:

- Text classification
- Sentiment analysis
- Language translation
- Text summarization
- Question answering
- Named entity recognition
- Speech-related language processing

## 5.2 Example

Suppose we provide this sentence:

```text
I love this product.
```

An NLP system might identify its sentiment as:

```text
Positive
```

Another example:

```text
Translate "Hello" into Urdu.
```

An NLP system can process the input and produce:

```text
السلام علیکم
```

## 5.3 How Are LLMs Related to NLP?

LLMs are powerful deep learning models used for many NLP tasks.

They can understand and generate language, answer questions, summarize documents, and perform many other language-related tasks.

---

# 6. What Is a Language Model?

Now that we understand AI, Machine Learning, Deep Learning, Neural Networks, and NLP, let's understand the concept of a Language Model.

## 6.1 Definition

A Language Model is a model that learns patterns in language and estimates the probability of a sequence of tokens.

In simple words:

**A language model learns which words or tokens are likely to appear together and predicts what might come next.**

## 6.2 Simple Example

Consider this sentence:

```text
The sun rises in the ______.
```

A language model may predict:

```text
east
```

Why?

Because the model has learned that "The sun rises in the east" is a likely sequence of words.

Another example:

```text
I am learning ______.
```

Possible predictions include:

- Programming
- Python
- English
- Mathematics

The model calculates which continuation is more likely based on its learned patterns and the context.

## 6.3 What Does a Language Model Learn?

A language model learns statistical patterns such as:

- Which tokens commonly appear together
- Grammar patterns
- Sentence structures
- Relationships between words
- Contextual patterns
- Information represented in its training data

## 6.4 Next Token Prediction

Many modern generative language models are trained using next-token prediction.

For example:

```text
Input:
I am learning
```

The model predicts a likely next token:

```text
Python
```

This is the fundamental idea behind GPT-style language models.

---

# 7. What Is a Large Language Model (LLM)?

## 7.1 Definition

LLM stands for **Large Language Model**.

It is a language model based on a large neural network, trained on large amounts of text data using substantial computational resources.

LLMs learn complex patterns in language and can generate human-like text.

## 7.2 Why Is It Called Large?

The word "Large" generally refers to aspects such as:

1. Large neural network architecture
2. Large number of learnable parameters
3. Large training datasets
4. Significant computational resources

A parameter is a numerical value learned by the model during training.

## 7.3 What Can LLMs Do?

LLMs can perform tasks such as:

- Answering questions
- Generating text
- Writing emails
- Summarizing documents
- Translating languages
- Generating code
- Explaining technical concepts
- Having conversations
- Extracting information from text

## 7.4 Examples of LLMs

| Model Family | Organization |
| ------------ | ------------ |
| GPT          | OpenAI       |
| Gemini       | Google       |
| Claude       | Anthropic    |
| Llama        | Meta         |
| Gemma        | Google       |
| Mistral      | Mistral AI   |

## 7.5 LLM vs Traditional Search Engine

A traditional search engine primarily retrieves relevant information from indexed webpages.

An LLM generates text based on patterns learned during training and the context provided in the prompt.

### Search Engine Workflow

```text
User Query
    |
    v
Search Engine
    |
    v
Search Indexed Information
    |
    v
Return Relevant Webpages
```

### LLM Workflow

```text
User Prompt
    |
    v
Language Model
    |
    v
Process Context
    |
    v
Predict Next Tokens
    |
    v
Generate Response
```

**Important:** Modern AI applications can combine LLMs with search engines, databases, and other tools. For example, Retrieval-Augmented Generation (RAG) combines an LLM with external information retrieval.

---

# 8. Understanding GPT

GPT stands for:

**Generative Pre-trained Transformer**

Let's understand each word.

## 8.1 Generative

Generative means the model can create new content.

For example:

- Text
- Code
- Answers
- Summaries
- Conversations

The model generates content based on the input prompt.

## 8.2 Pre-trained

Pre-trained means the model has already gone through an initial training process before being used by users.

During pre-training, the model learns language patterns by processing large amounts of training data.

Some models also go through additional training stages, such as supervised fine-tuning and preference optimization, to improve their behavior.

## 8.3 Transformer

Transformer is the neural network architecture used by GPT models.

It helps the model process sequences and learn relationships between different tokens using attention mechanisms.

The Transformer architecture was introduced in the research paper:

**Attention Is All You Need (2017)**

The original Transformer was designed for sequence-to-sequence tasks such as machine translation.

GPT models generally use a decoder-only Transformer architecture.

---

# 9. How Does GPT Generate Text?

The most important concept behind GPT is:

**Next Token Prediction**

GPT generates text by predicting one token at a time based on the tokens that came before it.

## 9.1 Simple Example

Suppose the user provides:

```text
Hi, I am
```

The model might predict:

```text
Basit
```

Now the sequence becomes:

```text
Hi, I am Basit
```

The model then predicts another token:

```text
Ali
```

Now the sequence becomes:

```text
Hi, I am Basit Ali
```

The model continues predicting tokens.

## 9.2 Step-by-Step Process

1. The user provides an input prompt.
2. The tokenizer converts the prompt into token IDs.
3. The Transformer processes those token IDs.
4. The model calculates scores for possible next tokens.
5. A decoding strategy selects a token.
6. The selected token is added to the existing sequence.
7. The model repeats the process.

## 9.3 What Is Autoregressive Generation?

Autoregressive means that the model uses previously available tokens to predict the next token.

Each newly generated token becomes part of the context for predicting the following token.

This is how GPT-style models generate responses one token at a time.

---

# 10. What Is a Transformer?

Now we understand what a language model is and how GPT predicts the next token.

But how does GPT process the input and calculate its predictions?

The answer is:

**Transformer Architecture**

## 10.1 Definition

A Transformer is a deep learning architecture designed to process sequences of data.

It uses attention mechanisms to learn relationships between different positions in a sequence.

## 10.2 Why Was the Transformer Introduced?

Before Transformers, architectures such as:

- Recurrent Neural Networks (RNNs)
- Long Short-Term Memory Networks (LSTMs)

were commonly used for sequence-processing tasks.

Transformers introduced a powerful attention-based approach that made it possible to process relationships between tokens more effectively and support parallel processing during training.

## 10.3 Understanding Context

Consider:

```text
The animal was tired because it had been running.
```

To understand the word "it", the model needs to consider other words in the sentence.

The Transformer uses attention mechanisms to learn relationships between tokens.

## 10.4 Main Components of a Transformer

A Transformer-based language model generally uses:

1. Token Embeddings
2. Positional Information
3. Self-Attention
4. Multi-Head Attention
5. Feed-Forward Neural Network
6. Normalization
7. Residual Connections

We will understand these components individually in the following sections.

---

# 11. How Does an LLM Convert Text into Numbers?

Before a Transformer can process text, the text must be converted into numerical representations.

Let's understand the complete process.

```text
Human Text
    |
    v
Tokenizer
    |
    v
Tokens
    |
    v
Token IDs
    |
    v
Embedding Layer
    |
    v
Numerical Vectors
    |
    v
Transformer
```

There are three important concepts here:

1. Tokenization
2. Vocabulary and Token IDs
3. Embeddings

---

# 12. Tokenization

## 12.1 What Is Tokenization?

Tokenization is the process of converting text into smaller units called tokens.

A token can represent:

- A complete word
- Part of a word
- A character
- Punctuation
- A special token

## 12.2 Example

Input:

```text
I love programming.
```

A tokenizer might divide it into:

```text
["I", " love", " programming", "."]
```

The exact tokens depend on the tokenizer.

## 12.3 Why Do We Need Tokenization?

Neural networks do not directly process ordinary human text.

They process numerical data.

Therefore, the input text must first be divided into tokens.

Later, these tokens are converted into numerical IDs.

## 12.4 Tokenization Workflow

```text
Original Text
      |
      v
   Tokenizer
      |
      v
     Tokens
```

## 12.5 Important Point

A token is not necessarily a complete word.

For example, a long or uncommon word may be divided into multiple subword tokens.

This is why the number of tokens and the number of words are different.

---

# 13. Vocabulary and Token IDs

## 13.1 What Is Vocabulary?

Vocabulary is the collection of tokens that a tokenizer knows how to represent.

Each token has a unique numerical ID.

For example:

| Token       | Token ID |
| ----------- | -------: |
| I           |       40 |
| love        |     1250 |
| AI          |      987 |
| programming |     2345 |

These IDs are illustrative. Actual IDs depend on the tokenizer.

## 13.2 What Is a Token ID?

A Token ID is a numerical identifier assigned to a token.

For example:

```text
Text:
I love AI
```

Possible token representation:

```text
["I", " love", " AI"]
```

Possible token IDs:

```text
[40, 1250, 987]
```

The model uses these IDs to look up their corresponding embeddings.

## 13.3 Why Is Vocabulary Important?

The vocabulary defines which token entries are available to the model.

For example, a tokenizer with a vocabulary size of 50,000 has 50,000 token entries.

Different models can use different tokenizers and vocabularies.

## 13.4 Complete Process

```text
Input Text
    |
    v
Tokenizer
    |
    v
Tokens
    |
    v
Vocabulary Lookup
    |
    v
Token IDs
```

---

# 14. Vector Embeddings

## 14.1 What Is an Embedding?

An embedding is a numerical vector that represents a token.

After tokenization, token IDs are passed through an embedding layer.

The embedding layer maps each token ID to a vector of numbers.

Example:

```text
Token:
Cat

Embedding:
[0.25, 0.81, -0.34, 0.62, ...]
```

The actual embedding contains many dimensions.

## 14.2 Why Do We Need Embeddings?

Token IDs are identifiers. They do not directly represent the semantic relationships between words.

For example:

```text
Cat = 100
Dog = 200
Car = 300
```

These numbers are just IDs.

The difference between 100 and 200 does not mean that a cat is semantically closer to a dog than to a car.

Embeddings provide learned vector representations that neural networks can process.

## 14.3 How Do Embeddings Work?

During training, the model learns embedding values that help it perform its language modeling task.

Tokens that appear in similar contexts may develop related representations.

For example:

```text
King
Queen
Man
Woman
```

Their learned representations may capture some semantic and grammatical relationships.

However, embeddings are not exact dictionary definitions.

## 14.4 What Are Embedding Dimensions?

An embedding contains multiple numerical values.

For example:

```text
[0.25, 0.81, -0.34, 0.62]
```

This example contains four dimensions.

Real LLMs generally use much larger embedding dimensions.

## 14.5 Embedding Workflow

```text
Token
  |
  v
Token ID
  |
  v
Embedding Layer
  |
  v
Numerical Vector
```

---

# 15. Positional Information

## 15.1 Why Do We Need Positional Information?

Consider these two sentences:

```text
The dog chased the cat.
```

```text
The cat chased the dog.
```

Both sentences contain the same words, but their meanings are different because the order of the words has changed.

A Transformer needs information about token positions.

## 15.2 What Is Positional Encoding?

Positional encoding is a technique used to provide information about the position of tokens in a sequence.

For example:

```text
Token 1: The
Token 2: dog
Token 3: chased
Token 4: the
Token 5: cat
```

The model receives both:

- Token representation
- Positional information

## 15.3 Types of Positional Information

Different Transformer architectures use different techniques.

Examples:

1. Sinusoidal positional encoding
2. Learned positional embeddings
3. Rotary Positional Embeddings (RoPE)

The original Transformer paper used sinusoidal positional encodings.

Many modern models use other techniques, including RoPE.

## 15.4 Important Point

Positional information helps the model understand the order and relative positions of tokens.

---

# 16. Understanding the Transformer Architecture

Now we have learned:

- What a token is
- How token IDs are created
- What embeddings are
- Why positional information is needed

We can now understand what happens inside a Transformer.

## 16.1 Basic Transformer Workflow

```text
             Input Text
                  |
                  v
              Tokenizer
                  |
                  v
               Token IDs
                  |
                  v
            Token Embeddings
                  |
                  v
          Positional Information
                  |
                  v
           Transformer Blocks
                  |
                  v
             Hidden States
                  |
                  v
              Output Layer
                  |
                  v
             Next Token
```

## 16.2 What Is a Transformer Block?

A Transformer block is a group of neural network operations that processes token representations.

A simplified Transformer block contains:

1. Self-Attention
2. Feed-Forward Network
3. Normalization
4. Residual Connections

A GPT-style model contains multiple Transformer blocks.

The output of one block becomes the input to the next block.

## 16.3 Why Multiple Transformer Blocks?

A single block performs a set of transformations.

Stacking multiple blocks allows the model to build increasingly complex representations of the input.

The exact number of blocks depends on the model architecture.

---

# 17. Self-Attention Mechanism

## 17.1 What Is Self-Attention?

Self-attention is a mechanism that allows each token to consider other tokens in the same sequence.

It helps the model learn which tokens are relevant when processing a particular token.

Consider:

```text
The animal was tired because it had been running.
```

To understand the word "it", the model needs information from the surrounding sentence.

Self-attention helps the model learn these relationships.

## 17.2 Why Is Self-Attention Important?

A sentence contains relationships between different words.

For example:

```text
The developer fixed the bug because he found the issue.
```

The model needs to process the relationship between:

- Developer
- He
- Bug
- Issue

Self-attention helps the model learn these contextual relationships.

## 17.3 How Does Self-Attention Work?

Self-attention uses three important concepts:

1. Query (Q)
2. Key (K)
3. Value (V)

Each input representation is transformed into Query, Key, and Value vectors using learned weight matrices.

We will understand these three concepts next.

---

# 18. Query, Key, and Value (Q, K, V)

## 18.1 What Is Query?

Query represents the information a token is looking for.

In simple words:

**What information does this token need from the other tokens?**

## 18.2 What Is Key?

Key represents information that can be matched against a Query.

In simple words:

**What information does this token provide for matching?**

## 18.3 What Is Value?

Value contains the information that can be passed forward when a token receives attention.

In simple words:

**What information should be taken from this token?**

## 18.4 Simple Analogy

Imagine searching for a book in a library.

- Query: What kind of book are you looking for?
- Key: Information describing each book.
- Value: The actual information contained in the selected book.

The system compares the Query with the Keys.

Based on the similarity scores, it determines how much information to take from each Value.

## 18.5 How Are Q, K, and V Created?

The model uses learned weight matrices to transform input representations into Query, Key, and Value vectors.

Simplified:

```text
Input Representation
        |
        +----------------+
        |        |       |
        v        v       v
       Q         K       V
```

## 18.6 Attention Calculation

The scaled dot-product attention formula is:

\[
Attention(Q,K,V) =
softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

Where:

- Q = Query matrix
- K = Key matrix
- V = Value matrix
- Kᵀ = Transpose of the Key matrix
- dₖ = Dimension of the Key vectors
- Softmax = Converts attention scores into normalized weights

## 18.7 Step-by-Step Attention Process

1. The model receives token representations.
2. It creates Query, Key, and Value vectors.
3. Queries are compared with Keys.
4. Attention scores are calculated.
5. Softmax converts scores into attention weights.
6. Attention weights are applied to Values.
7. The resulting representations contain information from relevant tokens.

## 18.8 Causal Masking in GPT

GPT is an autoregressive model.

When predicting a token, it must not access future tokens that have not yet been generated.

Therefore, GPT uses causal masking.

Example:

```text
The cat is sleeping
```

When processing "cat", the model can attend to:

```text
The
cat
```

But it cannot use future tokens such as:

```text
is sleeping
```

This prevents the model from looking ahead during next-token prediction.

---

# 19. Multi-Head Attention

## 19.1 What Is Multi-Head Attention?

Multi-head attention means running multiple attention mechanisms in parallel.

Instead of using only one attention operation, the model uses several attention heads.

Each head has its own learned Query, Key, and Value projections.

## 19.2 Why Do We Need Multiple Heads?

A sentence contains different types of relationships.

For example:

```text
The developer who built the application fixed the bug.
```

The model needs to process relationships between different words and parts of the sentence.

Multiple attention heads allow the model to examine the sequence through multiple learned attention patterns.

## 19.3 Simple Representation

```text
                 Input
                   |
        -----------------------
        |          |          |
        v          v          v
      Head 1     Head 2     Head 3
        |          |          |
        v          v          v
     Output 1   Output 2   Output 3
        |          |          |
        -----------------------
                   |
                   v
               Concatenate
                   |
                   v
             Final Projection
                   |
                   v
                 Output
```

## 19.4 Important Point

Different attention heads can learn different patterns.

However, we should not assume that every head has one fixed, easily interpretable responsibility.

---

# 20. Feed-Forward Neural Network

## 20.1 What Is a Feed-Forward Network?

After the attention operation, the Transformer uses a Feed-Forward Neural Network (FFN).

The FFN processes each token representation through neural network layers.

It helps transform and refine the information produced by attention.

## 20.2 Basic Structure

A simplified feed-forward network contains:

1. Linear transformation
2. Activation function
3. Another linear transformation

```text
Input
  |
  v
Linear Layer
  |
  v
Activation Function
  |
  v
Linear Layer
  |
  v
Output
```

Common activation functions include:

- ReLU
- GELU
- SwiGLU

The exact architecture depends on the model.

## 20.3 Attention vs Feed-Forward Network

| Self-Attention                        | Feed-Forward Network                      |
| ------------------------------------- | ----------------------------------------- |
| Learns relationships between tokens   | Processes token representations           |
| Uses Query, Key, and Value            | Uses neural network layers                |
| Combines information across positions | Transforms each position's representation |
| Helps understand context              | Helps refine learned representations      |

---

# 21. Normalization and Residual Connections

## 21.1 What Is Normalization?

Normalization helps keep neural network activations within useful numerical ranges.

It can improve training stability and make optimization easier.

Transformers commonly use Layer Normalization or related techniques.

## 21.2 Why Is Normalization Important?

During training, values inside neural networks can change significantly.

Normalization helps control the scale of activations and supports stable learning.

## 21.3 What Are Residual Connections?

A residual connection allows the original input to be added to the output of a neural network operation.

A simplified representation is:

```text
Input
  |
  +----------------------+
  |                      |
  v                      |
Neural Network            |
  |                      |
  v                      |
Output                   |
  |                      |
  +----------------------+
           |
           v
      Add Together
           |
           v
        Result
```

Residual connections help information and gradients flow through deep networks.

**Note:** The exact ordering of normalization, attention, feed-forward layers, and residual connections depends on the Transformer architecture.

---

# 22. Encoder and Decoder Architecture

## 22.1 What Is an Encoder?

An encoder processes input tokens and creates contextual representations.

It is commonly used in models designed to understand or represent input text.

```text
Input Text
    |
    v
  Encoder
    |
    v
Contextual Representations
```

Example:

BERT is an encoder-only Transformer model.

## 22.2 What Is a Decoder?

A decoder generates output tokens.

In an autoregressive language model, it predicts the next token using the tokens that came before it.

```text
Previous Tokens
      |
      v
    Decoder
      |
      v
 Next Token Prediction
```

GPT uses a decoder-only Transformer architecture.

## 22.3 Encoder-Decoder Architecture

The original Transformer architecture introduced in "Attention Is All You Need" contains:

- An encoder
- A decoder

This architecture was designed for sequence-to-sequence tasks such as translation.

## 22.4 Different Transformer Model Types

| Model Type      | Architecture | Common Use                            |
| --------------- | ------------ | ------------------------------------- |
| Encoder-only    | Encoder      | Text understanding and classification |
| Decoder-only    | Decoder      | Autoregressive text generation        |
| Encoder-decoder | Both         | Sequence-to-sequence tasks            |

Examples:

- BERT: Encoder-only
- GPT: Decoder-only
- T5: Encoder-decoder

**Important:** Not every Transformer model uses both an encoder and decoder. GPT models are generally decoder-only.

---

# 23. How LLM Training Works

Now we understand the main components of an LLM.

The next question is:

**How does the model learn all these language patterns?**

The answer is:

Training.

## 23.1 What Is Training?

Training is the process in which a model learns patterns from data by adjusting its internal parameters.

During training, the model receives examples and tries to predict the correct next token.

It compares its predictions with the expected tokens and calculates an error.

The model then updates its parameters to reduce that error.

## 23.2 Step 1: Prepare Training Data

A large text dataset is collected and prepared.

Example:

```text
The sky is blue.
```

The dataset may contain books, articles, websites, code, and other text sources, depending on the model and its training process.

## 23.3 Step 2: Tokenization

The text is converted into token IDs.

For illustration:

```text
["The", " sky", " is", " blue", "."]
```

The tokenizer converts these tokens into numerical IDs.

## 23.4 Step 3: Create Input and Target Sequences

For next-token prediction, the model learns to predict the next token from the preceding tokens.

Example:

| Input           | Target |
| --------------- | ------ |
| The             | sky    |
| The sky         | is     |
| The sky is      | blue   |
| The sky is blue | .      |

This illustrates the basic next-token training objective.

In practice, models often process multiple token positions together using shifted input and target sequences.

## 23.5 Step 4: Forward Pass

The token IDs are converted into embeddings and processed through Transformer layers.

The model produces predictions for the next token.

## 23.6 Step 5: Calculate Loss

The model's predictions are compared with the correct target tokens.

A loss function measures how far the predictions are from the expected answers.

For language modeling, cross-entropy loss is commonly used.

A lower loss generally means the model's predictions are closer to the training targets.

## 23.7 Step 6: Backpropagation

Backpropagation calculates gradients that indicate how model parameters contributed to the loss.

These gradients help determine how the parameters should change.

## 23.8 Step 7: Update Parameters

An optimizer uses these gradients to update the model's weights.

The objective is to reduce the loss over repeated training steps.

## 23.9 Step 8: Repeat Training

The model processes many training examples over many training steps.

Over time, it learns statistical patterns that help it predict tokens.

## 23.10 Training Workflow

```text
Training Dataset
       |
       v
   Tokenization
       |
       v
    Token IDs
       |
       v
   Model Input
       |
       v
  Transformer
       |
       v
  Predictions
       |
       v
 Compare with Targets
       |
       v
   Calculate Loss
       |
       v
  Backpropagation
       |
       v
 Update Model Weights
       |
       v
   Repeat Training
```

## 23.11 Important Training Terms

| Term            | Meaning                                         |
| --------------- | ----------------------------------------------- |
| Dataset         | Collection of training examples                 |
| Parameters      | Learnable values inside the model               |
| Weights         | Numerical values adjusted during training       |
| Forward Pass    | Processing input through the model              |
| Loss            | Measurement of prediction error                 |
| Backpropagation | Calculates gradients                            |
| Optimizer       | Updates model parameters                        |
| Epoch           | One complete pass through a training dataset    |
| Batch           | A group of training examples processed together |

## 23.12 Is Pre-training the Only Training Stage?

No.

Many modern LLMs go through multiple stages.

A simplified example:

```text
Large Text Dataset
        |
        v
  Pre-training
        |
        v
 Pre-trained Model
        |
        v
 Supervised Fine-Tuning
        |
        v
 Instruction-Following Model
        |
        v
 Preference Optimization
        |
        v
 More Helpful Assistant
```

The exact training pipeline varies between models.

---

# 24. How LLM Inference Works

## 24.1 What Is Inference?

Inference means using an already-trained model to generate predictions or responses.

During normal inference, the model uses its learned weights to process the input.

Unlike training, inference does not normally update the model's weights.

## 24.2 Step-by-Step Inference Process

Suppose the user enters:

```text
Explain artificial intelligence.
```

The model performs the following steps.

### Step 1: Receive Prompt

The model receives the user's text.

### Step 2: Tokenization

The tokenizer converts the prompt into token IDs.

### Step 3: Embedding

Token IDs are converted into vectors.

### Step 4: Transformer Processing

The vectors pass through the Transformer layers.

### Step 5: Calculate Logits

The final hidden representation is passed through an output projection layer.

The model produces scores for possible next tokens.

These scores are called logits.

### Step 6: Calculate Probabilities

Softmax converts logits into a probability distribution.

### Step 7: Select the Next Token

A decoding strategy selects the next token.

### Step 8: Repeat

The generated token is added to the sequence.

The model predicts another token.

This continues until the model reaches a stopping condition.

## 24.3 Inference Workflow

```text
User Prompt
     |
     v
 Tokenization
     |
     v
  Token IDs
     |
     v
 Embeddings
     |
     v
 Transformer Layers
     |
     v
 Hidden States
     |
     v
 Linear Layer
     |
     v
    Logits
     |
     v
   Softmax
     |
     v
 Probabilities
     |
     v
 Token Selection
     |
     v
 Generated Token
     |
     v
 Repeat Until Finished
```

## 24.4 Training vs Inference

| Training                  | Inference                              |
| ------------------------- | -------------------------------------- |
| Model learns from data    | Model uses learned parameters          |
| Updates model weights     | Normally does not update model weights |
| Calculates loss           | Generates predictions                  |
| Uses backpropagation      | Does not normally use backpropagation  |
| Computationally expensive | Usually less expensive than training   |

---

# 25. Logits, Softmax, and Probability Distribution

These concepts explain how the model moves from its internal calculations to possible next tokens.

## 25.1 What Are Logits?

After Transformer processing, the model has a hidden representation.

A linear output layer maps that representation to a score for every possible token in the vocabulary.

These raw scores are called **logits**.

Example:

Suppose the possible next tokens are:

```text
cat
dog
car
book
```

The model might produce these illustrative logits:

| Token | Logit |
| ----- | ----: |
| cat   |   3.2 |
| dog   |   2.1 |
| car   |   0.8 |
| book  |  -0.5 |

These are raw scores, not probabilities.

## 25.2 What Is Softmax?

Softmax is a mathematical function that converts logits into probabilities.

The formula is:

\[
P(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}
\]

Where:

- \(x_i\) is a logit
- \(e\) is the exponential function
- The denominator is the sum of exponentials of all logits

After applying softmax:

- Every probability is between 0 and 1.
- All probabilities add up to 1.

Illustrative output:

| Token | Probability |
| ----- | ----------: |
| cat   |        0.65 |
| dog   |        0.25 |
| car   |        0.08 |
| book  |        0.02 |

## 25.3 What Is a Probability Distribution?

A probability distribution represents the likelihood of different possible outcomes.

In an LLM, it represents the probabilities assigned to possible next tokens.

For example:

```text
cat  = 65%
dog  = 25%
car  =  8%
book =  2%
```

The model can use this distribution to select a token.

**Important:** The numbers above are only an example. Actual probabilities depend on the model and input.

---

# 26. How Does an LLM Select the Next Token?

After calculating probabilities, the model needs a strategy to select the next token.

This process is called decoding.

Common decoding strategies include:

## 26.1 Greedy Decoding

Greedy decoding selects the token with the highest probability.

Example:

| Token | Probability |
| ----- | ----------: |
| cat   |        0.65 |
| dog   |        0.25 |
| car   |        0.08 |
| book  |        0.02 |

The model selects:

```text
cat
```

This is because it has the highest probability.

## 26.2 Random Sampling

Random sampling selects a token based on the probability distribution.

The highest-probability token is more likely to be selected, but other tokens may also be selected.

## 26.3 Top-k Sampling

Top-k sampling limits token selection to the k tokens with the highest probabilities.

For example, if k = 3, the model considers only the three highest-probability tokens.

## 26.4 Top-p Sampling

Top-p sampling selects from the smallest group of tokens whose cumulative probability reaches a specified threshold.

For example, if p = 0.9, the model considers a group of likely tokens whose combined probability reaches 90%.

## 26.5 Comparison

| Strategy        | Explanation                                                |
| --------------- | ---------------------------------------------------------- |
| Greedy          | Always selects the highest-probability token               |
| Random Sampling | Samples based on the probability distribution              |
| Top-k           | Samples from the k most likely tokens                      |
| Top-p           | Samples from a group selected using cumulative probability |

---

# 27. Temperature and Text Generation

## 27.1 What Is Temperature?

Temperature is a parameter used during token selection.

It changes the shape of the probability distribution produced from logits.

A simplified temperature-adjusted softmax is:

\[
P(x_i) =
\frac{e^{x_i/T}}{\sum_j e^{x_j/T}}
\]

Where:

- \(x_i\) = Logit
- \(T\) = Temperature

## 27.2 Low Temperature

A lower temperature makes the probability distribution sharper.

This means the model is more likely to select tokens with higher scores.

Example:

```text
Temperature = 0.2
```

Typical behavior:

- More predictable outputs
- Less variation
- More consistent token selection

## 27.3 High Temperature

A higher temperature makes the probability distribution flatter.

This gives lower-probability tokens a greater chance of being selected.

Example:

```text
Temperature = 1.5
```

Typical behavior:

- More variation
- Less predictable outputs
- Greater diversity in generated text

## 27.4 Temperature Comparison

| Temperature | Typical Behavior                 |
| ----------- | -------------------------------- |
| Low         | More predictable                 |
| Medium      | Balanced variation               |
| High        | More varied and less predictable |

## 27.5 Important Point

Higher temperature does not automatically mean better creativity or better answers.

It changes token-selection behavior.

Output quality depends on:

- The model
- The prompt
- The task
- The context
- The decoding configuration

---

# 28. Complete Working Flow of an LLM

Now let's connect everything together.

Suppose a user enters:

```text
What is machine learning?
```

The complete process looks like this.

## Step 1: User Input

The user provides a prompt.

```text
What is machine learning?
```

## Step 2: Tokenization

The tokenizer divides the text into tokens.

```text
["What", " is", " machine", " learning", "?"]
```

## Step 3: Convert Tokens into IDs

Each token is converted into a numerical ID.

```text
[ID1, ID2, ID3, ID4, ID5]
```

The actual IDs depend on the tokenizer.

## Step 4: Embedding

The embedding layer converts token IDs into vector representations.

## Step 5: Positional Information

The model receives information about the positions of tokens.

## Step 6: Transformer Processing

The representations pass through multiple Transformer blocks.

These blocks contain attention and feed-forward operations.

## Step 7: Self-Attention

The model learns relationships between tokens.

## Step 8: Feed-Forward Network

The model transforms the contextual representations.

## Step 9: Linear Layer

The final hidden representation is converted into vocabulary-sized logits.

## Step 10: Softmax

The logits are converted into probabilities.

## Step 11: Token Selection

A decoding strategy selects the next token.

## Step 12: Autoregressive Generation

The selected token is added to the sequence.

The model repeats the process to generate more tokens.

## Step 13: Final Response

The generated tokens are decoded into readable text and returned to the user.

## Complete Architecture Diagram

```text
                 USER PROMPT
                      |
                      v
                  TOKENIZER
                      |
                      v
                   TOKENS
                      |
                      v
                  TOKEN IDs
                      |
                      v
               EMBEDDING LAYER
                      |
                      v
             POSITIONAL INFORMATION
                      |
                      v
              TRANSFORMER BLOCKS
                      |
          +-----------+-----------+
          |                       |
          v                       v
    SELF-ATTENTION          FEED-FORWARD
          |                       |
          +-----------+-----------+
                      |
                      v
               HIDDEN STATES
                      |
                      v
                 LINEAR LAYER
                      |
                      v
                   LOGITS
                      |
                      v
                   SOFTMAX
                      |
                      v
               PROBABILITIES
                      |
                      v
                TOKEN SELECTION
                      |
                      v
               GENERATED TOKEN
                      |
                      v
              UPDATE SEQUENCE
                      |
                      v
               REPEAT PROCESS
                      |
                      v
               FINAL RESPONSE
```

---

# 29. Using an LLM with Python and Hugging Face

Now that we understand the theory, let's see how to use a pre-trained LLM with Python.

The example uses:

```text
google/gemma-2-2b
```

Hugging Face provides libraries that make it easier to download and use pre-trained models.

## 29.1 Install Required Libraries

```bash
pip install transformers torch
```

## 29.2 Import Libraries

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
```

### AutoTokenizer

`AutoTokenizer` loads the tokenizer associated with a model.

It converts text into token IDs and can convert token IDs back into text.

### AutoModelForCausalLM

`AutoModelForCausalLM` loads a causal language model.

A causal language model predicts the next token based on previous tokens.

## 29.3 Load the Model and Tokenizer

```python
model_name = "google/gemma-2-2b"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name)
```

Explanation:

- `model_name` identifies the pre-trained model.
- `tokenizer` loads the corresponding tokenizer.
- `model` loads the language model.

Some models require accepting their license or signing in to Hugging Face before downloading.

The model also requires sufficient memory and computing resources.

## 29.4 Prepare Input Text

```python
prompt = "Explain artificial intelligence in simple words."
```

This is the text that we want the model to process.

## 29.5 Tokenize the Input

```python
inputs = tokenizer(prompt, return_tensors="pt")
```

Explanation:

- `tokenizer()` converts text into token IDs.
- `return_tensors="pt"` asks for PyTorch tensors.
- `inputs` contains the model-ready input.

You can inspect the token IDs:

```python
print(inputs["input_ids"])
```

## 29.6 Pass Input to the Model

```python
outputs = model(**inputs)
```

This performs a forward pass through the model.

The output contains information about the model's predictions.

For a causal language model, the logits are available through:

```python
logits = outputs.logits
```

## 29.7 Understand Logits

```python
print(logits.shape)
```

The logits tensor generally has dimensions:

```text
(batch_size, sequence_length, vocabulary_size)
```

Meaning:

- `batch_size`: Number of input sequences
- `sequence_length`: Number of input tokens
- `vocabulary_size`: Number of possible vocabulary tokens

The logits provide scores for possible next tokens at each sequence position.

## 29.8 Generate Text

```python
generated_ids = model.generate(
    **inputs,
    max_new_tokens=100
)
```

Explanation:

- `model.generate()` generates new tokens.
- `**inputs` passes the tokenized prompt.
- `max_new_tokens=100` limits the number of newly generated tokens.

## 29.9 Decode the Generated Tokens

```python
response = tokenizer.decode(
    generated_ids[0],
    skip_special_tokens=True
)

print(response)
```

Explanation:

- `generated_ids[0]` selects the generated sequence.
- `tokenizer.decode()` converts token IDs back into readable text.
- `skip_special_tokens=True` removes special tokens from the displayed text.

## 29.10 Complete Example

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Model name
model_name = "google/gemma-2-2b"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load model
model = AutoModelForCausalLM.from_pretrained(model_name)

# Input prompt
prompt = "Explain artificial intelligence in simple words."

# Convert text into token IDs
inputs = tokenizer(prompt, return_tensors="pt")

# Get model output
outputs = model(**inputs)

# Inspect logits
logits = outputs.logits
print("Logits shape:", logits.shape)

# Generate new tokens
generated_ids = model.generate(
    **inputs,
    max_new_tokens=100
)

# Convert generated token IDs into text
response = tokenizer.decode(
    generated_ids[0],
    skip_special_tokens=True
)

print(response)
```

**Note:** This is a basic demonstration. For a real application, also consider device placement, memory requirements, inference settings, and model-specific requirements.

---

# 30. Important LLM Terminology

| Term                 | Explanation                                                       |
| -------------------- | ----------------------------------------------------------------- |
| AI                   | Artificial Intelligence                                           |
| ML                   | Machine Learning                                                  |
| DL                   | Deep Learning                                                     |
| NLP                  | Natural Language Processing                                       |
| Neural Network       | Model consisting of interconnected computational units            |
| LLM                  | Large Language Model                                              |
| GPT                  | Generative Pre-trained Transformer                                |
| Transformer          | Neural network architecture based on attention                    |
| Token                | A unit of text processed by a model                               |
| Tokenization         | Converting text into tokens                                       |
| Vocabulary           | Collection of tokens known to a tokenizer                         |
| Token ID             | Numerical identifier assigned to a token                          |
| Embedding            | Numerical vector representation of a token                        |
| Positional Encoding  | Information about token positions                                 |
| Self-Attention       | Mechanism that learns relationships between tokens                |
| Query                | Vector representing what information is being searched for        |
| Key                  | Vector used to match against Queries                              |
| Value                | Vector containing information passed through attention            |
| Multi-Head Attention | Multiple attention operations running in parallel                 |
| Feed-Forward Network | Neural network that transforms token representations              |
| Normalization        | Technique that helps stabilize neural network activations         |
| Encoder              | Processes input into contextual representations                   |
| Decoder              | Generates output tokens                                           |
| Logits               | Raw scores for possible output tokens                             |
| Softmax              | Converts logits into probabilities                                |
| Loss                 | Measurement of prediction error                                   |
| Backpropagation      | Calculates gradients for model training                           |
| Optimizer            | Updates model parameters using gradients                          |
| Training             | Process of learning model parameters from data                    |
| Inference            | Using a trained model to make predictions                         |
| Autoregressive       | Predicting the next token using previous tokens                   |
| Causal Masking       | Prevents access to future tokens during autoregressive prediction |
| Temperature          | Controls the sharpness of the token probability distribution      |
| Fine-Tuning          | Additional training of an already pre-trained model               |

---

# 31. Common Misunderstandings

## 31.1 Tokens Are Not Always Complete Words

A token can be:

- A complete word
- A subword
- A character
- Punctuation
- A special token

Therefore, one word does not always equal one token.

## 31.2 Token IDs Are Not Word Meanings

Token IDs are numerical identifiers.

For example:

```text
Cat = 100
Dog = 200
```

This does not mean that the number 100 represents the meaning of cat.

Embeddings provide learned numerical representations.

## 31.3 Embeddings Are Not Dictionary Definitions

Embeddings are learned numerical vectors.

They capture patterns and relationships learned during training. They are not exact human-readable meanings of words.

## 31.4 GPT Is Generally Decoder-Only

The original Transformer architecture contains an encoder and a decoder.

However, GPT models generally use decoder-only Transformer architectures.

## 31.5 Softmax Does Not Select the Token

Softmax converts logits into probabilities.

A separate decoding strategy then selects the next token.

## 31.6 Temperature Does Not Guarantee Better Creativity

Temperature changes the probability distribution used during token selection.

A higher temperature creates more variation, but it does not guarantee better responses.

## 31.7 Attention Heads Do Not Always Have Fixed Roles

Different attention heads can learn different patterns.

However, it is not correct to assume that every head has one fixed, easily understandable purpose.

## 31.8 Training and Inference Are Different

Training adjusts model parameters using data.

Inference uses the trained parameters to generate predictions.

Normal inference does not update the model's weights.

## 31.9 LLMs Do Not Always Retrieve Facts from the Internet

A basic LLM generates responses using learned parameters and the context provided to it.

It does not automatically search the internet.

External search, databases, and tools can be connected to an LLM to provide additional information.

---

# 32. Recommended Learning Roadmap

If you are a complete beginner, follow this learning order.

| Phase    | Topics                      | Learning Goal                                          |
| -------- | --------------------------- | ------------------------------------------------------ |
| Phase 1  | AI, ML, Deep Learning       | Understand the basic AI ecosystem                      |
| Phase 2  | Neural Networks             | Understand how neural networks learn                   |
| Phase 3  | NLP and Language Models     | Understand how computers process language              |
| Phase 4  | LLMs and GPT                | Understand what LLMs are and how they generate text    |
| Phase 5  | Tokenization and Embeddings | Understand how text becomes numerical data             |
| Phase 6  | Transformer Architecture    | Understand how Transformers process tokens             |
| Phase 7  | Attention Mechanism         | Understand Query, Key, Value, and Multi-Head Attention |
| Phase 8  | Model Training              | Understand loss, backpropagation, and optimization     |
| Phase 9  | Model Inference             | Understand how a trained model generates responses     |
| Phase 10 | Decoding                    | Understand logits, softmax, temperature, and sampling  |
| Phase 11 | Practical Implementation    | Load and use a pre-trained model with Python           |

## Suggested Practical Exercises

After understanding each phase, try these exercises:

### Exercise 1: Understand Tokenization

Use a tokenizer to convert a sentence into token IDs.

### Exercise 2: Inspect Embeddings

Load a small pre-trained model and inspect the shape of its embedding layer.

### Exercise 3: Understand Model Output

Pass a prompt to a causal language model and inspect its logits.

### Exercise 4: Generate Text

Use `model.generate()` to generate a response.

### Exercise 5: Experiment with Temperature

Generate text using different temperature values and compare the results.

---

# 33. Final Summary

Let's summarize the complete working process.

1. Artificial Intelligence is the broader field of building systems that perform intelligent tasks.

2. Machine Learning allows systems to learn patterns from data.

3. Deep Learning uses neural networks with multiple layers.

4. LLMs are deep learning models trained on large amounts of language data.

5. GPT stands for Generative Pre-trained Transformer.

6. GPT uses a Transformer architecture, generally with a decoder-only design.

7. LLMs first convert text into tokens.

8. Tokens are converted into numerical IDs.

9. Embedding layers convert token IDs into numerical vectors.

10. Positional information helps the model understand token order.

11. Self-attention helps the model learn relationships between tokens.

12. Multi-head attention performs multiple attention operations in parallel.

13. Feed-forward networks transform token representations.

14. During training, the model learns by predicting target tokens and updating its parameters.

15. During inference, the trained model uses its learned parameters to generate responses.

16. A linear layer produces logits for possible next tokens.

17. Softmax converts logits into probabilities.

18. A decoding strategy selects the next token.

19. GPT generates text autoregressively, one token at a time.

20. Temperature controls the probability distribution used during token selection.

21. Python libraries such as Hugging Face Transformers make it possible to load and use pre-trained language models.

## The Most Important Concept to Remember

An LLM receives text, converts it into tokens and numerical representations, processes those representations through Transformer layers, calculates probabilities for possible next tokens, and generates a response one token at a time.

**That is the basic working principle behind GPT-style Large Language Models.**

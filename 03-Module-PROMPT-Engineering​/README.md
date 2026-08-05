# Module 3 – Prompt Engineering

## 📖 Overview

Prompt Engineering is the skill of writing clear, structured, and effective instructions (prompts) for AI models like ChatGPT, GPT-4, Claude, Gemini, and other Large Language Models (LLMs).

In simple terms:

> **Ask better questions to get better answers.**

Think of AI as a very smart intern. The better your instructions, the better the results.

Prompt Engineering helps you communicate with AI effectively to generate accurate, structured, and useful responses.

---

# 📚 Course Agenda

1. Prompt Engineering – Introduction
2. Fundamentals of Prompts
3. Mastering the Art of Prompting
4. Anatomy of a Prompt
5. Types of Prompting
6. Zero-shot Prompting
7. Few-shot Prompting
8. Chain-of-Thought Prompting
9. Common LLM Parameters

---

# 1. Prompt Engineering – Introduction

## What is Prompt Engineering?

Prompt Engineering is the process of designing prompts that guide AI models to produce better outputs.

A prompt can be:

- A question
- An instruction
- A conversation
- A request
- A task description

The quality of your prompt directly affects the quality of the AI response.

---

### Simple Example

### ❌ Bad Prompt

```
Explain AI.
```

### ✅ Better Prompt

```
Explain Artificial Intelligence in simple language for a 10-year-old using two real-life examples.
```

Same AI.

Completely different results.

---

## Why is Prompt Engineering Important?

AI doesn't think like humans.

It predicts the next most likely words based on patterns it learned during training.

Your prompt tells AI:

- What to focus on
- How detailed the answer should be
- What format to use
- Which audience to target
- What examples to include

> **Better Prompt = Better Output**

---

# 2. Fundamentals of Prompts

A prompt is simply an instruction given to an AI model.

Good prompts are:

- Clear
- Specific
- Context-aware
- Well structured

---

## Example

### Weak Prompt

```
Tell me about Docker.
```

### Better Prompt

```
Explain Docker to a beginner with a real-world analogy and provide three practical examples.
```

---

# 3. Mastering the Art of Prompting

Writing great prompts is a skill.

Like communication, it improves with practice.

Instead of asking vague questions, learn to give AI complete instructions.

---

## Example

Instead of

```
Write code.
```

Try

```
Write a Python program that reads a CSV file and prints all rows where Age > 30.
```

Notice how the second prompt tells AI exactly what is expected.

---

# 4. Anatomy of a Prompt

A good prompt generally contains five building blocks.

---

## 1. Role

Tell AI who it should act as.

Example:

```
Act as a Senior DevOps Engineer.
```

---

## 2. Task

Clearly define the task.

Example

```
Explain Kubernetes.
```

---

## 3. Context

Provide background information.

Example

```
I am a beginner in DevOps.
```

---

## 4. Output Format

Specify how the response should look.

Examples

- Bullet Points
- Table
- Step-by-Step
- JSON
- Markdown
- Code

Example

```
Explain in five bullet points.
```

---

## 5. Constraints

Limit the response.

Examples

- Under 100 words
- Give only 3 examples
- Don't use technical jargon

---

## Prompt Formula

A simple formula to remember:

```
Role
+ Task
+ Context
+ Output Format
+ Constraints
```

---

## Example

```
Act as a DevOps instructor.

Explain Docker to a beginner.

Use a real-world analogy.

Respond in five bullet points.

Keep the explanation under 150 words.
```

---

# 5. Types of Prompting

Prompting can be categorized based on the task.

---

## Informational Prompt

Purpose: Learn something.

Example

```
What is Kubernetes?
```

---

## Instruction-Based Prompt

Purpose: Ask AI to perform a task.

Example

```
Create a Jenkins Pipeline.
```

---

## Transformational Prompt

Purpose: Modify existing content.

Example

```
Rewrite this email in a professional tone.
```

---

## Analytical Prompt

Purpose: Compare or analyze.

Example

```
Compare AWS and Azure in a table.
```

---

# Beginner Tips

- Start with a simple prompt
- Improve it gradually (Iterate)
- Add more context
- Specify the output format
- Include examples whenever possible
- Break large problems into smaller prompts

---

# Before vs After

### Before

```
Write code.
```

### After

```
Write a Python script that reads a CSV file and displays rows where Age > 30.
```

---

# One-Line Summary

> Prompt Engineering is the art of giving AI clear, structured instructions so it produces exactly the output you need.

---

# 6. Zero-Shot Prompting

## Definition

Zero-Shot Prompting means asking AI to perform a task without providing any examples.

The AI relies entirely on its existing knowledge.

---

## Example

```
Translate "Good Morning" into French.
```

Output

```
Bonjour
```

---

## DevOps Example

```
Explain CI/CD Pipeline in simple terms.
```

No examples are provided.

---

## When to Use

- Simple tasks
- General questions
- Common knowledge
- Well-known patterns

---

## Advantages

- Simple
- Fast
- Easy to write

---

## Limitations

Sometimes responses may vary in style or quality because no guidance is provided.

---

# 7. Few-Shot Prompting

## Definition

Few-Shot Prompting means giving AI a few examples before asking it to perform a similar task.

AI learns the expected pattern from those examples.

---

## Example

```
Translate English to French

Hello -> Bonjour

Thank You -> Merci

Good Night -> ?
```

Output

```
Bonne Nuit
```

---

## DevOps Example

```
Convert environment names to uppercase

dev -> DEV

prod -> PROD

test -> ?
```

Output

```
TEST
```

---

## Why It Works

Instead of guessing the pattern,

AI learns from your examples.

It's similar to teaching a student using sample problems before giving an exercise.

---

## Best Use Cases

- Classification
- Formatting
- Data transformation
- Code generation
- Structured responses

---

# 8. Chain-of-Thought (CoT) Prompting

## Definition

Chain-of-Thought Prompting encourages AI to solve problems step by step instead of jumping directly to the answer.

---

## Without Chain-of-Thought

```
What is 23 × 12?
```

AI gives the answer directly.

---

## With Chain-of-Thought

```
What is 23 × 12?

Explain step by step.
```

Output

```
23 × 10 = 230

23 × 2 = 46

230 + 46 = 276
```

---

## Real-Life Example

```
A person buys

2 apples at $3 each

3 bananas at $2 each

Calculate the total cost and explain every step.
```

AI breaks the problem into logical steps before producing the final answer.

---

## Best Use Cases

- Mathematics
- Debugging
- Decision making
- Logical reasoning
- Multi-step problem solving

---

# Simple Analogy

| Technique | Analogy |
|-----------|----------|
| Zero-Shot | Ask directly |
| Few-Shot | Show examples first |
| Chain-of-Thought | Ask AI to show its work |

---

# Combined Prompt Example

Prompt Engineering techniques can be combined together.

Example

```
Act as a Senior DevOps Engineer.

Below are two examples of Kubernetes YAML files.

Example 1:
...

Example 2:
...

Now create a Deployment YAML file following the same format.

Finally, explain every section step by step.
```

This prompt combines:

- Role Prompting
- Few-Shot Prompting
- Chain-of-Thought Prompting

---

# 9. Common LLM Parameters

Large Language Models expose several parameters that control how responses are generated.

Understanding these parameters helps you produce consistent, creative, or deterministic outputs based on your use case.

---

## 1. Temperature

Controls randomness.

| Value | Behavior |
|--------|-----------|
| 0.0 | Very deterministic |
| 0.3 | Mostly factual |
| 0.7 | Balanced |
| 1.0 | Creative |
| 1.5+ | Highly random |

Example

```
Temperature = 0

Best for:

✔ Code
✔ Technical documentation
✔ SQL queries
```

```
Temperature = 1

Best for:

✔ Stories
✔ Brainstorming
✔ Creative writing
```

---

## 2. Max Tokens

Defines the maximum length of the response.

Higher values produce longer answers.

Lower values keep responses short.

---

## 3. Top-P (Nucleus Sampling)

Controls how many likely words AI considers before choosing the next word.

Lower values make responses focused.

Higher values make responses more diverse.

Typical range:

```
0.8–1.0
```

---

## 4. Frequency Penalty

Reduces repeated words or phrases.

Higher values discourage repetition.

Useful for long-form content generation.

---

## 5. Presence Penalty

Encourages AI to introduce new ideas or topics.

Higher values make responses more exploratory.

Useful for brainstorming and ideation.

---

## Recommended Parameter Settings

| Use Case | Temperature |
|----------|-------------|
| Coding | 0.0 – 0.2 |
| Technical Documentation | 0.2 – 0.4 |
| Learning | 0.5 |
| Chatbot | 0.7 |
| Creative Writing | 0.8 – 1.0 |
| Brainstorming | 1.0+ |

---

# Key Takeaways

- Prompt Engineering is the foundation of working effectively with AI.
- Clear prompts produce better responses.
- Include role, context, task, output format, and constraints.
- Zero-Shot works well for simple tasks.
- Few-Shot teaches AI through examples.
- Chain-of-Thought improves reasoning for complex problems.
- LLM parameters control creativity, consistency, and response length.
- Prompt Engineering is an iterative process—refine your prompts to improve results.

---

# Module Summary

In this module, you learned:

- What Prompt Engineering is
- Why prompts matter
- Building blocks of effective prompts
- Types of prompts
- Zero-Shot Prompting
- Few-Shot Prompting
- Chain-of-Thought Prompting
- Common LLM Parameters
- Best practices for writing effective prompts

You are now ready to create high-quality prompts that unlock the full potential of modern AI systems.


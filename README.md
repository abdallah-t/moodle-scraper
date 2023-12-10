# Moodle Scraper

## Description

This is a simple python script that scrapes the assignments from the Moodle (university online learning platform) and creates:

- json file with the assignments' questions and answers
- pdf file with the assignments' questions and answers made with LaTeX

## Example:

![Example](/images/example.jpeg)

**json output:**

```json
[
  {
    "question": "Which of the following is NOT a learning and support tool for application software?",
    "answers": [
      "a. Online tutorial",
      "b. Software update",
      "c. User guide",
      "d. Online forum or community"
    ],
    "correct_answer": "b. Software update"
  },
  {
    "question": "What is a man-in-the-middle attack?",
    "answers": [
      "a. An attack that redirects users to malicious websites.",
      "b. An attack that intercepts communications between two parties and impersonates one of the parties.",
      "c. An attack that overwhelms computer systems or networks with traffic, making them unavailable to users.An attack that attempts to break encryption.",
      "d. An attack that overwhelms computer systems or networks with traffic, making them unavailable to users."
    ],
    "correct_answer": "b. An attack that intercepts communications between two parties and impersonates one of the parties."
  },
  {
    "question": "1-You should only install software from trusted sources.",
    "answers": [
      "True",
      "False"
    ],
    "correct_answer": "True"
  }
]
```

**pdf output:**

![Output](/images/latex_output.png)

## How to use

1. Clone the repository
2. Install the requirements
3. copy the html of the page with the assignments and paste it in the `data.html` file
4. run the script
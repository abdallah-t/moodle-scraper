# Moodle Scraper

## Description

This Python script serves as a Moodle scraper, extracting assignments from the university's online learning platform. It performs the following tasks:

- Generates a JSON file containing questions and answers for each assignment.
- Creates a PDF file with formatted questions and answers using LaTeX.

## Example:

![Example](/images/example.jpeg)

**JSON Output:**

```json
[
  {
    "question": "Which of the following is NOT a learning and support tool for application software?",
    "choices": [
      "a. Online tutorial",
      "b. Software update",
      "c. User guide",
      "d. Online forum or community"
    ],
    "correct_answer": "b. Software update"
  },
  {
    "question": "What is a man-in-the-middle attack?",
    "choices": [
      "a. An attack that redirects users to malicious websites.",
      "b. An attack that intercepts communications between two parties and impersonates one of the parties.",
      "c. An attack that overwhelms computer systems or networks with traffic, making them unavailable to users.An attack that attempts to break encryption.",
      "d. An attack that overwhelms computer systems or networks with traffic, making them unavailable to users."
    ],
    "correct_answer": "b. An attack that intercepts communications between two parties and impersonates one of the parties."
  },
  {
    "question": "1-You should only install software from trusted sources.",
    "choices": [
      "True",
      "False"
    ],
    "correct_answer": "True"
  }
]
```

**PDF Output:**

![Output](/images/latex_output.png)

## Prerequisites

- Python 3
- BeautifulSoup (bs4)
- pdflatex (for PDF generation)

## Usage

1. Ensure the HTML file containing exam content is in the same directory as the script. Update the `HTML_FILE_PATH` constant in the script if necessary.

2. Run the script:
    ```bash
    python exam_generator.py
    ```

3. The script will generate a JSON file (`example.json`) containing the exam data and a LaTeX file (`example.tex`). A PDF file (`example.pdf`) will also be generated from the LaTeX file.

## Customization

### HTML Structure

Ensure that the HTML file follows a specific structure with the following classes:

- Question text: `qtext`
- Answer choices: `answer`
- Correct answer: `correct`
- Odd row styling: `r0`
- Even row styling: `r1`

### LaTeX Formatting

Customize the LaTeX document by modifying the `convert_to_latex` function in the script. Adjust the document title, author, and formatting as needed.

## Output Files

- `example.json`: Contains exam data in JSON format.
- `example.tex`: LaTeX document generated from the exam data.
- `example.pdf`: PDF document generated from the LaTeX file.

## License

This script is licensed under the [MIT License](LICENSE).

Feel free to use, modify, and distribute this script according to the terms of the license. If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/yourusername/exam-generator/issues).

Happy studying!
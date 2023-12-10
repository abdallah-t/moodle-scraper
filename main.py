from bs4 import BeautifulSoup
import pprint
import json

# Constants
HTML_FILE_PATH = './data.html'
QUESTION_CLASS = 'qtext'
ANSWER_CLASS = 'answer'
CORRECT_ANSWER_CLASS = 'correct'
ODD_ROW_CLASS = 'r0'
EVEN_ROW_CLASS = 'r1'
AUTHOR = "Author"
TITLE = "Example"
GENERATED_FILE_NAME = "example"

def clean_text(text):
    """Remove new lines and extra spaces from the text."""
    return " ".join(text.strip().replace("\n", "").split())

def read_html(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extract_questions(soup):
    questions_soup = soup.find_all(class_=QUESTION_CLASS)
    questions = []

    for question in questions_soup:
        text_question = question.find("span")
        questions.append(text_question if text_question else question)
    
    # Remove new lines and extra spaces
    questions = [clean_text(question.text) for question in questions]

    return questions

def extract_choices(soup):
    choices_soup = soup.find_all(class_=ANSWER_CLASS)

    all_questions_choices = []

    for choices in choices_soup:
        choice_elements = choices.find_all(class_=ODD_ROW_CLASS) + choices.find_all(class_=EVEN_ROW_CLASS)
        formatted_choices = [clean_text(choice.text) for choice in choice_elements]
        all_questions_choices.append(formatted_choices)

    all_questions_choices = [[clean_text(answer) for answer in answers] for answers in all_questions_choices]

    # Swap the second and third choices to fix the order
    for answers in all_questions_choices:
        if len(answers) == 4:
            answers[2], answers[1] = answers[1], answers[2]

    return all_questions_choices

def extract_correct_choices(soup):
    choices_soup = soup.find_all(class_=ANSWER_CLASS)
    all_questions_correct_choice = []

    for choices in choices_soup:
        correct_answer = choices.find(class_=CORRECT_ANSWER_CLASS)
        if correct_answer:
            all_questions_correct_choice.append(correct_answer.text)

    return [clean_text(answer) for answer in all_questions_correct_choice]

def create_question_dict_list(questions, all_answers, all_correct_answers):
    question_dict_list = []

    for i in range(len(questions)):
        question_dict = {
            'question': questions[i],
            'answers': all_answers[i],
            'correct_answer': all_correct_answers[i]
        }
        question_dict_list.append(question_dict)

    return question_dict_list

def export_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

def convert_to_latex(questions):
    latex_code = r"\documentclass{exam}" + "\n\n"
    latex_code += rf"\title{{{TITLE}}}" + "\n"
    latex_code += rf"\author{{{AUTHOR}}}" + "\n"
    latex_code += r"\date{\today}" + "\n\n"
    latex_code += r"\begin{document}" + "\n\n"
    latex_code += r"\maketitle" + "\n\n"
    latex_code += r"\begin{questions}" + "\n\n"
    latex_code += r"\printanswers" + "\n\n"

    for idx, question in enumerate(questions, start=1):
        latex_code += fr"\question {question['question']}" + "\n"
        latex_code += r"\begin{checkboxes}" + "\n"

        for answer in question["answers"]:
            is_correct = answer == question["correct_answer"]
            if is_correct:
                latex_code += fr"\CorrectChoice {answer}" + "\n"
            else:
                latex_code += fr"\choice {answer}" + "\n"
            

        latex_code += r"\end{checkboxes}" + "\n\n"

    latex_code += r"\end{questions}" + "\n\n"
    latex_code += r"\end{document}"

    return latex_code


def main():
    html_content = read_html(HTML_FILE_PATH)
    soup = BeautifulSoup(html_content, 'html.parser')

    questions = extract_questions(soup)
    all_answers = extract_choices(soup)
    all_correct_answers = extract_correct_choices(soup)

    question_dict_list = create_question_dict_list(questions, all_answers, all_correct_answers)


    export_to_json(question_dict_list, f"{GENERATED_FILE_NAME}.json")
    print(f'json data exported to {GENERATED_FILE_NAME}.json')
    
    latex_code = convert_to_latex(question_dict_list)
    with open(f"{GENERATED_FILE_NAME}.tex", "w") as file:
        file.write(latex_code)
    print(f'LaTeX file has been made in {GENERATED_FILE_NAME}.tex')




if __name__ == "__main__":
    main()
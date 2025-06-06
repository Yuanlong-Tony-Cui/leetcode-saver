# Parse the question list in HTML to get: title, link, etc.
from bs4 import BeautifulSoup

def extract_question_titles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title_divs = soup.find_all('div', class_='truncate')
    titles = [div.get_text(strip=True) for div in title_divs]
    return titles

# Example usage:
if __name__ == "__main__":
    input_file = "../data/html/leetcode-100-list.html"

    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    question_titles = extract_question_titles(html_content)
    print(question_titles)

# Output a template in Markdown, where each question has: title, link, solution (code snippet).
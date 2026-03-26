# Wikimedia Outreachy 32 Microtasks T418285 and T418286

This repository includes my solutions to two Wikimedia microtasks that I completed for my May 2026 Outreachy internship application.

I used only built-in features for these solutions, avoiding third-party libraries. This helped me focus on improving my JavaScript and Python skills and practicing core implementation techniques.

## Task 1: Rendering data with HTML and JavaScript

**Objective:** Write JavaScript code that reads a `data` array and displays it as an ordered list of statements in this format:

- `A. Article "ARTICLE TITLE" (Page ID PAGEID) was created at MONTH DAY, YEAR.`
- `B. Article "André Baniwa" (Page ID 6682420) was created at September 12, 2021.`

### Project file

- `Task 1 - Intern.html`

### Implementation

1. I created an ordered list element (`<ol>`) and set its `"type"` attribute to `"A"` to display uppercase letter numbering.
2. I used the `forEach()` method to iterate through the `data` array and generate each `<li>` element based on the item's content.
3. Finally, I used `appendChild()` to add the ordered list to the `#results` section.

### Usage

1. Clone the project.

```console
git clone https://github.com/oluwatobiss/wikimedia-outreachy-32.git
```

2. Navigate to the project repository.

```console
cd wikimedia-outreachy-32
```

3. Open the project folder in VS Code.
4. Install and enable the Live Server extension.
5. Right-click the `Task 1 - Intern.html` file in the Explorer panel.
6. Select `Open with Live Server` from the context menu.

## Task 2: Creating file and URL parser with Python

**Objective:** Create a Python script that reads URLs from the `Task 2 - Intern.csv` file and prints each website's status code as a prefix to each URL, using the following format:

- `A. (STATUS CODE) URL`
- `B. (200) https://www.nytimes.com/1999/07/04/sports/women-s-world-cup-sissi-of-brazil-has-right-stuff-with-left-foot.html`

### Project file

- `Task 2 - Intern.csv`
- `print_urls_status.py`

### Implementation

1. I iterated through each line of the CSV file, extracting valid URLs into a list within the `print_urls_status.py` script.
2. I retrieved the HEAD of each website to obtain its response status code.
3. I then printed the status codes and URLs as an ordered list, formatted with Excel-style labels.
4. Finally, I refactored the codebase into modular functions to improve organization, readability, and maintainability.

### Usage

1. Clone the project if you have not already done so.

```console
git clone https://github.com/oluwatobiss/wikimedia-outreachy-32.git
```

2. Navigate to the project repository if you are not already there.

```console
cd wikimedia-outreachy-32
```

3. Open the project folder in VS Code if you have not already done so.
4. Ensure Python version 3.11 or greater is installed on your system. Use `python --version` on Windows or `python3 --version` on macOS or Linux to verify.
5. Run the project's Python script:

```console
python print_urls_status.py
```

6. Look in your terminal for the script output. It will look like this:

```
A. (504) http://www.futeboldabahia.com.br/Feminino.html
B. (404) http://www.ecuafutbol.org/copa_america/team.aspx?ID=BRA
C. (200) http://sportv.globo.com/site/noticia/2011/11/em-casa-sao-jose-vence-colo-colo-e-e-campeao-da-libertadores-feminina.html
```

## Reference

- **Project Brief:** https://phabricator.wikimedia.org/T418284
- **Task 1 Brief:** https://phabricator.wikimedia.org/T418285
- **Task 2 Brief:** https://phabricator.wikimedia.org/T418286

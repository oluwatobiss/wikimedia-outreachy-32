from urllib import request, error

with open("Task 2 - Intern.csv", "r") as file:
    urls = []
    for line in file:
        if line.strip() and line.strip().startswith("http"):
            urls.append(line.strip())

for index, url in enumerate(urls):
    print(f"{index + 1}. {url}")
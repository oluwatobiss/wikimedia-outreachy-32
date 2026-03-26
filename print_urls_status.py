from urllib import request, error

with open("Task 2 - Intern.csv", "r") as file:
    urls = []
    for line in file:
        if line.strip() and line.strip().startswith("http"):
            urls.append(line.strip())

for index, url in enumerate(urls):
    label = index + 1
    try:
        with request.urlopen(url) as response:
            status = response.getcode()
            text = f"{label}. ({status}) {url}"
            print(text)
    except error.HTTPError as e:
        text = f"{label}. ({e.code}) {url}"
        print(text)
    except error.URLError as e:
        text = f"{label}. (504) {url}"
        print(text)
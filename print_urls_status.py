from urllib import request, error

def convert_number_to_letter(index):
    final_letter = ""
    current_index = index

    while current_index >= 0:
        single_letter = chr((current_index % 26) + 65)
        final_letter =  single_letter + final_letter
        new_index = (current_index // 26) - 1
        current_index = new_index

    return final_letter

with open("Task 2 - Intern.csv", "r") as file:
    urls = []
    for line in file:
        if line.strip() and line.strip().startswith("http"):
            urls.append(line.strip())

for index, url in enumerate(urls):
    label = convert_number_to_letter(index)
    try:
        request_object = request.Request(url, method="HEAD")
        with request.urlopen(request_object) as response:
            status = response.getcode()
            text = f"{label}. ({status}) {url}"
            print(text)
    except error.HTTPError as e:
        text = f"{label}. ({e.code}) {url}"
        print(text)
    except error.URLError as e:
        text = f"{label}. (504) {url}"
        print(text)
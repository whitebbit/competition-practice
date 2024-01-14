import requests
import concurrent.futures


def fetch_url(url):
    try:
        response = requests.get(url)
        return url, response.text
    except Exception as e:
        return url, str(e)


def main():
    urls = ["https://www.example.com", "https://www.example.org"]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_url, urls))

    with open("responses.txt", "w") as file:
        for url, response in results:
            file.write(f"URL: {url}\n")
            file.write(f"Response:\n{response}\n\n")


if __name__ == "__main__":
    main()

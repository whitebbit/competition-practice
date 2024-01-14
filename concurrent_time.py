import requests
import concurrent.futures
import time


def fetch_url(url):
    try:
        response = requests.get(url)
        return url, response.text
    except Exception as e:
        return url, str(e)


def sequential_requests(urls):
    results = []
    for url in urls:
        results.append(fetch_url(url))
    return results


def parallel_requests(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_url, urls))
    return results


if __name__ == "__main__":
    urls = ["https://www.example.com"] * 10

    start_time = time.time()
    results_sequential = sequential_requests(urls)
    end_time = time.time()
    print(f"Sequential Execution Time: {end_time - start_time:.2f} seconds")

    start_time = time.time()
    results_parallel = parallel_requests(urls)
    end_time = time.time()
    print(f"Parallel Execution Time: {end_time - start_time:.2f} seconds")

    assert results_sequential == results_parallel, "Results do not match!"

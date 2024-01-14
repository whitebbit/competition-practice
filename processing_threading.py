import threading
import multiprocessing


def compute_sum(start, end, data, result):
    partial_sum = sum(data[start:end])
    result.append(partial_sum)


def multi_threading_example(data):
    result = []
    threads = []
    chunk_size = len(data) // 2

    for i in range(2):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < 1 else len(data)
        thread = threading.Thread(target=compute_sum, args=(start, end, data, result))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    total_sum = sum(result)
    print(f"Multi-threading result: {total_sum}")


def multi_processing_example(data):
    result = multiprocessing.Manager().list()
    processes = []
    chunk_size = len(data) // 2

    for i in range(2):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < 1 else len(data)
        process = multiprocessing.Process(target=compute_sum, args=(start, end, data, result))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    total_sum = sum(result)
    print(f"Multi-processing result: {total_sum}")


if __name__ == "__main__":
    data = list(range(1, 1000001))
    multi_threading_example(data)
    multi_processing_example(data)

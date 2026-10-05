"""Run a threaded producer-consumer demonstration with a bounded buffer."""

from src.buffer import SharedBuffer
from src.consumer import Consumer
from src.producer import Producer

"""Maximum number of items held in the shared buffer"""
capacity = 3

"""Number of producer threads and consumer threads to start"""
num_threads = 5

def main():
    buffer = SharedBuffer(capacity)

    producers = []
    consumers = []
    for i in range(num_threads):
        producers.append(Producer("Producer " + str(i + 1), buffer))
        consumers.append(Consumer("Consumer " + str(i + 1), buffer))

    for producer in producers:
        producer.start()

    for consumer in consumers:
        consumer.start()

    for producer in producers:
        producer.join()

    for consumer in consumers:
        consumer.join()

    print("No more production or consumption.")


if __name__ == "__main__":
    main()

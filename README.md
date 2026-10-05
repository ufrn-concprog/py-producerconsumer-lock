# The Producer-Consumer Problem: A Solution in Python using Locks and Condition Variables

This project implements a solution to the well-known [producer-consumer](https://en.wikipedia.org/wiki/Producer–consumer_problem) problem using a lock object and condition variables for synchronization. Condition variables enable condition-based synchronization: threads can be suspended or notified to resume execution under certain conditions.

## 📝 The Producer-Consumer Problem

The producer-consumer problem uses a bounded buffer shared by producers and consumers. Producers add values to the buffer, and consumers remove them. The implementation must ensure that:

* Only one thread accesses the buffer for an insertion or removal at a time.
* Producers wait while the buffer is full.
* Consumers wait while the buffer is empty.
* Values are removed in the order they were inserted.

This solution implements the insertion and removal operations as statements controlled by a lock object. The thread attempts to acquire the lock before executing those statements. If the lock is granted (i.e., no other thread holds it in mutual exclusion), the thread executes the statements and releases the lock at the end. If the buffer is full, producer threads should be suspended. If it is possible to add a new element to the buffer, then a suspended consumer thread should eventually be notified to resume execution. Conversely, when the buffer is empty, consumer threads should be suspended. If an element can be removed from the buffer, then a suspended producer thread should be notified to resume execution. These conditions for suspending threads or notifying them for execution are controlled via condition variables associated with the mutual exclusion lock.

## 📂 Repository Structure

Source code in this repository is organized as follows:

```text
+─py-producerconsumer
  ├─── doc                  # Directory where documentation will be generated
  ├─── src                  # Directory with header files
       └─── buffer.py       # Implementation of the shared buffer
       └─── consumer.py     # Implementation of the consumer thread
       └─── producer.py     # Implementation of the producer thread
  └─── main.py              # Main program
    
```

## 🚀 Getting Started

### ✅ Prerequisites

Python 3 is required. The program uses only the Python standard library.

### ▶️ Running

From the repository root:

```bash
python3 main.py
```

The program prints messages as values are inserted into and removed from the buffer, followed by a completion message.

## Generate Documentation

The source modules include docstrings that can be rendered with [pdoc](https://pdoc.dev). Install pdoc and generate HTML documentation from the repository root:

```bash
python3 -m pip install pdoc
python3 -m pdoc -o doc src.buffer src.consumer main src.producer
```

To serve the documentation locally instead of writing HTML files:

```bash
python3 -m pdoc src.buffer src.consumer main src.producer
```

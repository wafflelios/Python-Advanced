import queue
import random
import threading
import time


class Task:
    def __init__(self, priority: int, sleep_time: float):
        self.priority = priority
        self.sleep_time = sleep_time

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        time.sleep(self.sleep_time)
        return f'Task(priority={self.priority}).      sleep({self.sleep_time})'


class Producer(threading.Thread):
    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.count = count
        print('Producer: Running')

    def run(self):
        for i in range(self.count):
            priority = random.randint(0, 6)
            sleep_time = random.random()
            task = Task(priority, sleep_time)
            self.queue.put((priority, task))
        consumer = Consumer(self.queue, self.count)
        consumer.start()
        consumer.join()
        print('Producer: Done')


class Consumer(threading.Thread):
    def __init__(self, queue: queue.PriorityQueue, count: int):
        super().__init__()
        self.queue = queue
        self.tasks_done = 0
        self.count = count
        print('Consumer: Running')

    def run(self):
        while True:
            try:
                priority, task = self.queue.get()
            except queue.Empty:
                continue
            print(f'>running {task}')
            self.queue.task_done()
            self.tasks_done += 1
            if self.tasks_done == self.count:
                print('Consumer: Done')
                break


def main():
    _queue = queue.PriorityQueue()
    producer = Producer(_queue, 10)
    producer.start()
    _queue.join()
    producer.join()


if __name__ == '__main__':
    main()

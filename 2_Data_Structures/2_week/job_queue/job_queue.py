# python3
import math

class Thread:
    def __init__(self, i):
        self.id = i
        self.next_free = 0

class JobQueue:
    def read_data(self):
        self.num_workers, self.m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert self.m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i]) 
    
    def parent(self, i):
        return math.floor((i-1)/2)
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2
    
    def sift_down(self, i):
        min_i = i
        l = self.left_child(i)
        if l < self.num_workers and ((self.thread_list[l].next_free < self.thread_list[min_i].next_free)\
            or (self.thread_list[l].next_free == self.thread_list[min_i].next_free and\
            self.thread_list[l].id < self.thread_list[min_i].id)):
           min_i = l
        r = self.right_child(i)
        if r < self.num_workers and ((self.thread_list[r].next_free < self.thread_list[min_i].next_free)\
            or (self.thread_list[r].next_free == self.thread_list[min_i].next_free\
            and self.thread_list[r].id < self.thread_list[min_i].id)):
            min_i = r
        if min_i != i:
            self.thread_list[i], self.thread_list[min_i] = self.thread_list[min_i], self.thread_list[i]
            self.sift_down(min_i)
        else:
            return
    
    def assign_jobs(self):
        self.thread_list = []
        self.assigned_workers = []
        self.start_times = []
        for i in range(self.num_workers):
            self.thread_list.append(Thread(i))
        for job_no in range(self.m):
            next_worker = self.thread_list[0]
            self.assigned_workers.append(next_worker.id)
            self.start_times.append(next_worker.next_free)
            next_worker.next_free += self.jobs[job_no]
            self.sift_down(0)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()


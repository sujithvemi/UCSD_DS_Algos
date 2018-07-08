# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.hash_table = [[] for i in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (((ans * self._multiplier + ord(c)) % self._prime) + self._prime) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        if len(chain) != 0:
            print(' '.join(chain))
        else:
            print('')

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain([text for text in reversed(self.hash_table[query.ind])])
        elif query.type == "add":
            hash_val = self._hash_func(query.s)
            present = 0
            for text in self.hash_table[hash_val]:
                if text == query.s:
                    present = 1
                    break
            if not present:
                self.hash_table[hash_val].append(query.s)
        elif query.type == "del":
            hash_val = self._hash_func(query.s)
            for i in range(len(self.hash_table[hash_val])):
                if self.hash_table[hash_val][i] == query.s:
                    del self.hash_table[hash_val][i]
                    break
        else:
            hash_val = self._hash_func(query.s)
            present = 0
            for text in self.hash_table[hash_val]:
                if text == query.s:
                    self.write_search_result(True)
                    present = 1
                    break
            if not present:
                self.write_search_result(False)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

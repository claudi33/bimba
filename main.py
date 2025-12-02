def letters_in_word(word):
    l = {}
    for i in word:
        if i not in l:
            l[i] = 1
        else:
            l[i] += 1
    return l

# print(letters_in_word('nigagaiibaggaGGLLl'))

def first_letter(words: list):
    l = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in l:
            l[first_letter] = []
        l[first_letter].append(word)
    return l

# print(first_letter(["apple", "banana", "avocado", "cherry", "blueberry"]))


def anagram(word1, word2):
    l = {}
    for letter in word1:
        if letter not in l:
            l[letter] = 1
        else:
            l[letter] += 1
    l2 = {}       
    for letter in word2:
        if letter not in l2:
            l2[letter] = 1
        else:
            l2[letter] += 1

    return l == l2


# print(anagram('listen', 'silent'))

def non_repeating(word):
    l = {}
    for i in word:
        if i not in l:
            l[i] = 1
        else:
            l[i] += 1
    
    for key, value in l.items():
        if value == 1:
            return key
            
    

# print(non_repeating('aazzbbvvc'))

def students_marks(students: list):
    l = {}
    for name, grade in students:
        if name not in l:
            l[name] = []
        l[name].append(grade)
    return l
# print(students_marks([("Anna", 5), ("Mark", 3), ("Anna", 6), ("John", 2)]))


def duplicates(nums):
    l = {}
    for i in nums:
        if i not in l:
            l[i] = 1
        else:
            l[i] += 1

    for value in l.values():
        if value > 1:
            return True
        else:
            return False
        
# print(duplicates([1, 2, 3, 4, 5]))

def frequency(nums):
    l = {}
    for i in nums:
        if i not in l:
            l[i] = 1
        else:
            l[i] += 1
    
    max_frequency = max(l.values())
    
    for key, v in l.items():
        if v == max_frequency:
           return key
    
# print(frequency([1, 1, 2, 2, 3, 3, 3,4,4,4,4, 4]))

def unique(num):
    l = {}
    for i in num:
        if i not in l:
            l[i] = 1
        else:
            l[i] += 1
    
    for key, value in l.items():
        if value == 1:
            return key

# print(unique([4, 5, 1, 2, 1, 2, 4, 7, 8, 8]))


def group_anagrams(words):
    l = {}
    
    for word in words:
        key = tuple(sorted(word))
        if key not in l:
            l[key] = []
        l[key].append(word)
    return list(l.values())
           
    
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        

def top_k_frequent(nums, k):
    l = {}
    for i in nums:
        l[i] = l.get(i, 0) + 1
     
    k = min(k, len(l))
    res = []

    for _ in range(k):
        max_count = 0
        max_fr = None
        for num, count in l.items():
            if count > max_count:
                max_count = count
                max_fr = num
        res.append(max_fr)
        l.pop(max_fr)
    return res

    

# print(top_k_frequent([1,1,1,2,2,3,3,3,3,4], 556))

def first_unique_ch(word):
    l = {}
    for i in word:
        l[i] = l.get(i, 0) + 1
        
    for i in word:
        if l[i] == 1:
            return i
    return None

# print(first_unique_ch('gaabbccddaz'))

from collections import Counter

def first_unique_chs(word):
    counts = Counter(word)

    for i in word:
        if counts[i] == 1:
            return i
    return None

# print(first_unique_chs('aabbcdde'))

def anagrams(s, p):
    l = {}
    for ch in p:
        l[ch] = l.get(ch, 0) + 1
    
    result = []
    for i in range(len(s) - len(p) + 1):
        window = s[i:i+len(p)]

        window_count = {}
        for ch in window:
            window_count[ch] = window_count.get(ch, 0) + 1

        if window_count == l:
            result.append(i)
    return result

# print(anagrams('abcwabcwabq', 'abc'))

from collections import deque
import heapq

heap = []


patients = [
    ("Alice", 5),
    ("Bob", 8),
    ("Charlie", 5),
    ("David", 10)
]
# queue = deque()
# for patient in patients:
#     queue.append(patient)


# for patient in queue:
#     name, severity = patient
#     heapq.heappush(heap, (-severity, name))


# treatment_order = []
# while heap:
#     severity, name = heapq.heappop(heap)
#     treatment_order.append(name)

# print(treatment_order)

planes = [
    ("FlightA", 3),
    ("FlightB", 10),
    ("FlightC", 5),
    ("FlightD", 10),
    ("FlightE", 3)
]

# queuef = deque()
# for plane in planes:
#     queuef.append(plane)

# for index, plane in enumerate(queuef):
#     name, emergency = plane
#     heapq.heappush(heap, (-emergency, index, name))

# take_off_order = []
# while heap:
#     emergency, index, name = heapq.heappop(heap)
#     take_off_order.append(name)

# print(take_off_order)


tasks = [
    ("Task1", 5, 3),
    ("Task2", 8, 2),
    ("Task3", 5, 1),
    ("Task4", 10, 4),
    ("Task5", 8, 2)
]

queue = deque()
for task in tasks:
    queue.append(task)

for index, task in enumerate(queue):
    name, emergency, wait_time = task
    heapq.heappush(heap, (name, index, -emergency, wait_time))

execute_order = []
while heap:
    name, index, emergency, wait_time = heapq.heappop(heap)
    execute_order.append(name)

# print(execute_order) 

def word_frequency(string):
    res = string.split(',!? ')
    l = {}
    for i in res:
        if i not in l:
            # l.get(i, 0) + 1
            l[i] = 1
        else:
            l[i] += 1
    return l

# print(word_frequency('apple, banana!bomba?sigma sigma sigma bomba'))

def is_balanced(s):
    stack = []
    pairs = {'}': '{', ')': '(', ']': '['}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False    
    return len(stack) == 0

# print(is_balanced("(){}[][]")) 

def reverse_str(s):
    stack = []
    res = []

    for char in s:
        stack.append(char)
    while stack:    
        a = stack.pop()
        res.append(a)
    return "".join(res)

# print(reverse_str('hello'))

def parentheses(s):
    stack = []
    pairs = {'}': '{', ')': '(', ']': '['}

    for ch in s:
        if ch in '{([':
            stack.append(ch)
        elif ch in '}])':
            if not stack:
                return False
            if stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0

# print(parentheses("2 * (3[]] + 5){{}}"))



# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         if not self.root:
#             self.root = Node(value)
#             return
    
#         curr = self.root
#         while True:
#             if value < curr.value:
#                 if curr.left is None:
#                     curr.left = Node(value)
#                     return
#                 curr = curr.left
#             else:
#                 if curr.right is None:
#                     curr.right = Node(value)
#                     return
#                 curr = curr.right
    
#     def search(self, value):
#         curr = self.root
#         while curr:
#             if value == curr.value:
#                 return True
#             elif value < curr.value:
#                 curr = curr.left
#             else:
#                 curr = curr.right
#         return False
    
# tree = BST()
# tree.insert(8)
# tree.insert(3)
# tree.insert(10)
# tree.insert(1)
# tree.insert(1)
# tree.insert(6)

# print(tree.search(6))
# print(tree.search(14))



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        
        curr = self.root
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = Node(value)
                    return 
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(value)
                    return 
                curr = curr.right

    def print_order(self):
        stack = []
        curr = self.root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            print(curr.value)
            curr = curr.right


    def print_order(self):
        stack = []
        curr = self.root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            stack.pop(curr)
            print(curr.value)
            curr = curr.right

    def print_min(self):
        if not self.root:
            return 
        
        curr = self.root
        while curr.left:
            curr = curr.left
        print(curr.value)

        # def inorder(node):
        #     if node is None:
        #         return
        #     inorder(node.right)
        #     print(node.value)
        #     inorder(node.left)

        # inorder(self.root)
            

tree = BST()
tree.insert(1)
tree.insert(6)
tree.insert(3)
tree.insert(4)
tree.insert(2)
tree.print_min()
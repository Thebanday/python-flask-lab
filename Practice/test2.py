# def square(x):
#     return x**2

# print(square(5))

# nums = [1, 2, 3, 4, 5, 6]
# def filter_even(nums):
#     new_list=[list for list in nums if list%2==0]
#     return new_list

# print(filter_even(nums))

# # Count frequency of each word in a sentence
# sentence = "hello world hello"
# # Expected: {'hello': 2, 'world': 1}
# words=sentence.lower().split()
# frequency={}
# for word in words:
#     if word in frequency:
#         frequency[word]+=1
#     else:
#         frequency[word]=1

# print(frequency)

# # Read a list of tasks from a JSON file and write a new one
# import json

# # Example format:
# # [{"id": 1, "task": "Buy milk"}, {"id": 2, "task": "Code"}]

# file="file.json"

# with open(file,"r") as f:
#     tasks=json.load(f)


# with open("file1.json","w") as g:
#     content=json.dumps([{"id": 1, "task": "Buy milk"}, {"id": 2, "task": "Code"}])
#     g.write(content)


# # Create a class `User` with:
# # - username
# # - method to greet the user
# class User:
#     def __init__(self,username):
#         self.user=username
#     def greet(self):
#         return f"Hello {self.user}"

# check=User("majid")

# print(check.greet())


# content={"user":"majid","password":"majid123"}
# with open("test.json","w") as file:
#     json.dump(content,file)

# with open("test.json","r") as f:
#     json.load(f)

# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author

#     def display(self):
#         return f"The book {self.title} is written by {self.author}"

# b1=Book("python prgrammming","john hamer")
# print(b1.display())


class Todo:
    def __init__(self,task):
        self.task=task
        self.done=False
    
    def mark_done(self):
        self.done=True
    def display(self):
        return f"{self.task} is {self.done}"

t1=Todo("This is my first task")
print(t1.display())
t1.mark_done()
print(t1.display())

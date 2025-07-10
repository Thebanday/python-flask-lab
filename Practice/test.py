# # users = [
# #     {"id": 1, "name": "Alice", "password": "12345"},
# #     {"id": 2, "name": "Bob", "password": "qwerty"},
# # ]




# # # for i in users:
# # #     if "password" in i :
# # #         del i["password"]
# # # print(users)
# # #list comprehension
# # user=[{k:v for k,v in u.items() if k!="id"} for u in users ]

# # print(user)




# # products = [
# #     {"id": 1001, "name": "Laptop", "price": 50000},
# #     {"id": 1002, "name": "Phone", "price": 30000},
# # ]

# # for p in products:
# #     p["id"]=str(p["id"])
# #     p["price"]=str(p["price"])+ "Rs."
        
# # print(products)


# # books = [
# #     {"title": "1984", "author": "George Orwell"},
# #     {"title": "Sapiens", "author": "Yuval Noah Harari"},
# # ]

# # # for b in books:
# # #     b["available"]="True"

# # # print(books)
# # import json
# # # json_str = '{"name": "Alice", "age": 30, "city": "New York"}'
# # # print(type(json_str))

# # # data = json.loads(json_str)
# # # print(data)
# # # print(type(data))


# # # newdata=json.dumps(data)
# # # print(type(newdata))


# # # with open("new.json","w") as file:
# # #     test=json.dump({"id":1,"name":"majid"},file,indent=4)

# # # print(type(test))
# # # with open("new.json","r") as file:
# # #     data=json.load(file)


# # # print(data)
# # # print(type(data))




# # nested_data = {
# #     "id": 1,
# #     "name": "John Doe",
# #     "contact": {
# #         "email": "john@example.com",
# #         "phone": "123-456-7890"
# #     },
# # #     "skills": [
# # #         {"name": "Python", "level": "advanced"},
# # #         {"namee": "JavaScript", "level": "intermediate"}
# # #     ],
# # #     "projects": [
# # #         {
# # #             "title": "Website Redesign",
# # #             "year": 2022,
# # #             "details": {
# # #                 "budget": 10000,
# # #                 "team_size": 5
# # #             }
# # #         }
# # #     ]
# # # }


# # # # data=nested_data["contact"]["email"]="majid@gmail.com"
# # # # print(nested_data)
# # # nested_data["skills"][0]="javascript"
# # # print(nested_data)



# # # users = {"id": 1, "name": "Alice", "age": 25,
# # #     "id": 2, "name": "Bob", "age": 30,
# # #     "id": 3, "name": "Charlie", "age": 22,
# # #     "id": 4, "name": "David", "age": 29}


# # # user={
# # #         "status":5
# # #     }


# # # filtered_users=[user for user in users if user["age"]<30]
# # # print(filtered_users)
# # # filtered_users=[user['name'] for user in users if user["age"]<30]
# # # print(filtered_users)

# # # udpadated={**users,**user}
# # # print(udpadated)
# # # # users.update(user)


# # import requests

# # url="https://jsonplaceholder.typicode.com/users"


# # resp=requests.get(url)

# # if resp.status_code==200:
# #     data=resp.json()
# #     print("first user name:",data[0]['name'])
 
# #     print(" All emails\n")
# #     for user in data:
# #         print(user['email'])


# tasks = [
#     {"task": "Learn Python", "done": True},
#     {"task": "Build API", "done": False},
#     {"task": "Read book", "done": True}
# ]

# count=0
# for t in tasks:
#     if t["done"]:
#         count +=1
# print(count)


# # count = len([t for t in tasks if t["done"]])
# # print(count)

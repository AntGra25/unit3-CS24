# Quiz045

## 1. Solution
```.py
from Unit3.Tasks.my_lib3 import DatabaseWorker

haiku = """Code flows like a stream
Algorithms guide its way
In silence, it solves"""

db_name = "haiku.db"
db = DatabaseWorker(name=db_name)

query = """CREATE TABLE if NOT EXISTS Words(
        id integer primary key,
        length integer,
        word text not null)"""

db.run_query(query)
for word in haiku.split():
    query = f"""insert into Words (word, length)
    values('{word}', '{len(word)}')"""
    db.insert(query)

average = """select avg(length) from Words"""
results = db.search(average)

if results is not None:
    print(f'Average word length is {results[0]:.2f}')
else:
    print('No words found')

```
## 2. Proof of Work
![image](https://github.com/AntGra25/unit3-CS24/assets/142757981/97409e63-adb8-4c49-be57-74e2c065731f)

## 3. ER Diagram
![Quiz045C](https://github.com/AntGra25/unit3-CS24/assets/142757981/1327c44a-c4c6-42e8-83f3-c9c858656679)  
**Figure taken from '[2023] Quizzes' Google Slides presentation**

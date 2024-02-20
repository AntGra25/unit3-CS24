# Quiz049

## 1. Solution
```.py
from Unit3.Tasks.my_lib3 import DatabaseWorker


x = DatabaseWorker('bitcoin_exchange.db')
create_user = """create table if not exists users(
id integer primary key,
name text not null,
email text not null
)
"""
x.run_query(create_user)

insert_query = """insert into users (id, name, email) values
(560, 'bob1', 'bob1@xy.z'), 
(371, 'bob2', 'bob2@xy.z'),
(488, 'bob3', 'bob3@xy.z'), 
(561, 'bob4', 'bob4@xy.z'), 
(254, 'bob5', 'bob5@xy.z'), 
(920, 'bob6', 'bob6@xy.z'),
(438, 'alice1', 'alice1@xy.z'), 
(744, 'alice2', 'alice2@xy.z'), 
(261, 'alice3', 'alice3@xy.z')"""
x.run_query(insert_query)

query = "select * from ledger where sender_id = 920 or receiver_id = 920"
results = x.search(query, multiple=True)
print(results)

```
## 2. Proof of Work
![Quiz049](https://github.com/AntGra25/unit3-CS24/assets/142757981/3e6a2fb6-f3fc-4d0f-ad72-99a4aa21f69c)

## 3. ER Diagram
![Quiz049C](https://github.com/AntGra25/unit3-CS24/assets/142757981/6276914e-4c7a-4604-afbd-df44b4abaf53)

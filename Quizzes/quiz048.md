# Quiz048

## 1. Solution
```.py
from Unit3.Tasks.my_lib3 import DatabaseWorker
from Unit3.Tasks.my_lib3 import check_text

my_db = DatabaseWorker('bitcoin_exchange.db')
query = 'Select * from ledger'
results = my_db.search(query=query, multiple=True)
my_db.close()

valid_num = 0
total = 0

for row in results:
    id = row[0]
    sender_id = row[1]
    receiver_id = row[2]
    amount = row[3]
    signature = row[4]

    text = f'id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}'
    valid = check_text(hashed_text=signature, text=text)
    if valid:
        valid_num += 1
        total += amount

print(f"""Number of valid transactions: {valid_num}/{len(results)}
Total amount of bitcoins transferred: {total}""")

```
## 2. Proof of Work
![Quiz048](https://github.com/AntGra25/unit3-CS24/assets/142757981/13d48777-df26-47d1-9438-dcceddd41cf6)

## 3. ER Diagram
![Quiz047C](https://github.com/AntGra25/unit3-CS24/assets/142757981/bfbaa4f3-6f9a-4ecf-87d9-974ac8485e2b)

# Quiz047

## 1. Solution
```.py
from Unit3.Tasks.my_lib3 import DatabaseWorker
from Unit3.Tasks.my_lib3 import check_text

my_db = DatabaseWorker('bitcoin_exchange.db')
query = 'Select * from ledger'
results = my_db.search(query=query, multiple=True)
my_db.close()

for row in results:
    id = row[0]
    sender_id = row[1]
    receiver_id = row[2]
    amount = row[3]
    signature = row[4]

    text = f'id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}'
    valid = check_text(hashed_text=signature, text=text)
    if valid:
        print(f'\33[1;32mTx(id={id})Signature matches\033[00m')
    else:
        print(f'\33[1;31mTx(id={id})Error signature\033[00m')

```
## 2. Proof of Work
![Quiz047](https://github.com/AntGra25/unit3-CS24/assets/142757981/c33dec5f-1d9a-41fb-b8a5-8b01da1501ce)


## 3. ER Diagram
![Quiz047C](https://github.com/AntGra25/unit3-CS24/assets/142757981/59b6b335-92b8-430a-928a-124761011228)

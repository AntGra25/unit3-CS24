# Quiz044

## 1. ER Diagram
![Quiz044 1C](https://github.com/AntGra25/unit3-CS24/assets/142757981/6ddbcf40-35f3-4973-aa03-7df8cf5031ac)

## 2. Create the SQL queries to find the responsible for the fraudulent transaction

```.py
select * from (select sum(case when T.transaction_type = 'deposit' then T.amount else 0 end)  as sum_deposit,
                      sum(case when T.transaction_type = 'withdraw' then T.amount else 0 end) as sum_withdraw,
                      sum(case when T.transaction_type = 'deposit' then T.amount else 0 end) -
                      sum(case when T.transaction_type = 'withdraw' then T.amount else 0 end) as true_balance,
                      A.balance, T.account_id
               from transactions T join accounts A on T.account_id = A.account_id
               group by t.account_id) where true_balance != balance;

select * from customers where customer_id = 12
```

![Quiz044 1](https://github.com/AntGra25/unit3-CS24/assets/142757981/f07a2a12-0117-4205-94b9-0fd732c38f5f)
**Fig 1** Result of the first query. Shows the account id's of all customers where the balance shown by the bank does not match the true balance .  

![Quiz044 2](https://github.com/AntGra25/unit3-CS24/assets/142757981/ef5bd4da-4bdd-4bac-a205-a4c357929846)  
**Fig 2** Result of the second query. Shows the name of the customer where the true balance is lower than the balance shown by the bank.  

## 3. What is the name of the customer and the problem that resulted in the bankruptcy of the bank?

![Quiz044 3](https://github.com/AntGra25/unit3-CS24/assets/142757981/f3550230-9ff6-4888-9144-c9330b77ead3)
**Fig 3** Part of the 'transactions' table that shows the first transaction made by customers 12-19  


The customer's name is Matthew Martin. As seen in row 1 of **Fig 1**, he has a higher balance than he should have, with 400 of a certain currency being unregistered. The issue stems from the fact that the bank does not update their customers' balance: **Fig 3** shows that the amount that customers with id's 12, 13, 15, 17, and 19 initially deposited is the same as the balance shown in column 4 of **Fig 1**. However, this impacts the 4 customers that are not Mr. Martin negatively, as their balance should be higher than the one shown by the bank



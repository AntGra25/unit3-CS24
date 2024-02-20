# Quiz043

## 1. Solution
```.py
select count(*) from sqlite_master where type = 'table';

select count(*) from INHABITANT where gender = 'Male' and state = 'Friendly';

select avg(gold), V.name from INHABITANT join VILLAGE V on V.villageid = INHABITANT.villageid group by V.name;

select count(*) from ITEM where item like 'A%';

select count(distinct job) from INHABITANT;

select item from ITEM join INHABITANT I on (select I.personid where I.job = 'Herbalist') = ITEM.owner
```
## 2. Proof of Work
![Quiz043 1](https://github.com/AntGra25/unit3-CS24/assets/142757981/b3fd2437-b159-4dbd-aea5-46c24457dc5a)
![Quiz043 2](https://github.com/AntGra25/unit3-CS24/assets/142757981/c0745a89-b4b2-4d51-b5e6-aebe563bc4ba)  
![Quiz043 3](https://github.com/AntGra25/unit3-CS24/assets/142757981/84dd5b24-3770-4693-a276-35420b9607a3)  
![Quiz043 4](https://github.com/AntGra25/unit3-CS24/assets/142757981/cefc8fcd-a143-4e53-a9ba-36f16ec26b83)
![Quiz043 5](https://github.com/AntGra25/unit3-CS24/assets/142757981/9d47d1de-981f-482c-bc5b-ff9a6ff18dea)
![Quiz043 6](https://github.com/AntGra25/unit3-CS24/assets/142757981/f04fb0da-dbdd-4829-9a8d-e8dc1107e1b9)

## 3. ER Diagram
![Quiz043 1C](https://github.com/AntGra25/unit3-CS24/assets/142757981/8ee09883-a59e-4498-848e-796973d70ce7)


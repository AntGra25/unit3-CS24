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



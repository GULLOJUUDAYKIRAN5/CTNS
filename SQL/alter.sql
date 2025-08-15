create database col;
use college;
create table school(id int primary key,name varchar(20),age int);
desc school;
insert into school values(1,"uday",19),(2,"kiran",20);
select *from school;
select *from school;
insert into school values(2,"kiran",20);
select *from school;
insert into school values(3,"naveen",30),(4,"kumar",40);
select *from school;
alter table school add mail int;
desc school;
alter table school drop mail;
desc school;
alter table school add marks int;
desc school;
update school set marks=100 where id =1;
select marks from school;
update school set marks =100 where id=3;



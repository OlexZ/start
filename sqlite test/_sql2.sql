create table mydb(id integer primary key, bebe text);
insert into mydb values (1,'one');
insert into mydb (id, name) values (2, 'two');
insert into mydb (name) values ('three');
insert into mydb (name) values ('four');
insert into mydb (name) values ('five');

.mode column
.headers on
select * from cats
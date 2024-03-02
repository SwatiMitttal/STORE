create database rk;

create table items(
    item_id int not null,
    price float4,
    des_id int ,
    fabric varchar(50),
    
    primary key(item_id));
    
    insert into items values
    (1,10,000,1,'silk');
    insert into items values
    (2,10,000,2,'georgette');
    
    alter table  items add  color varchar(50);
    select * from items;
    
    
    
    update items set color ='cred' where item_id=2;
    
    update items set color='myellow' where item_id=1;
    insert into items values
    (3,14,350,3,'silk','fpink');
    
    insert into items values
    (4,14,350,3,'silk','mgreen');
    
    select * from items order by price desc;
    
    insert into items values
    (4,9450,3,'silk','mgreen');
    
    select concat('hello' ,'friend') as welcome_note;
    
    select * from items;
    create table colorr
    (cid int not null,
    color varchar(50),
    primary key(cid));
    
    insert into colorr values
    (1,'fpink'),(2,'mgreen'),(3,'myellow'),(4,'cred'),(5,'maroon');
    
    
    
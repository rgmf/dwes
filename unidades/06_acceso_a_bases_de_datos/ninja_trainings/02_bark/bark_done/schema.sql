-- Create tables
create table users (
       id integer auto_increment primary key,
       username varchar(20) not null
) engine=innodb, charset=utf8;

create table comments (
       id integer auto_increment primary key,
       user integer not null,
       comment varchar(100) not null,
       posted varchar(40) not null,
       category varchar(20) default 'default',
       foreign key(user) references users(id) on delete cascade on update cascade
) engine=innodb, charset=utf8;

create table likes (
       id integer auto_increment primary key,
       user integer not null,
       comment integer not null,
       foreign key(user) references users(id) on delete cascade on update cascade,
       foreign key(comment) references comments(id) on delete cascade on update cascade
) engine=innodb, charset=utf8;

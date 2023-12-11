-- Create tables
create table movies (
    id integer auto_increment primary key,
    title varchar(100),
    release_year integer,
    genre varchar(100)
) engine=innodb, charset=utf8;

create table reviewers (
    id INT auto_increment primary key,
    first_name varchar(100),
    last_name varchar(100)
) engine=innodb, charset=utf8;

create table ratings (
    movie_id integer,
    reviewer_id integer,
    rating integer,
    foreign key(movie_id) references movies(id) on delete cascade on update cascade,
    foreign key(reviewer_id) references reviewers(id) on delete cascade on update cascade,
    primary key(movie_id, reviewer_id)
) engine=innodb, charset=utf8;

-- "movies" table inserts
insert into movies (title, release_year, genre) values
('The Shawshank Redemption', 1994, 'Drama'),
('The Godfather', 1972, 'Crime'),
('The Dark Knight', 2008, 'Action'),
('Pulp Fiction', 1994, 'Crime'),
('The Lord of the Rings: The Return of the King', 2003, 'Adventure'),
('Forrest Gump', 1994, 'Drama'),
('The Matrix', 1999, 'Action'),
('Fight Club', 1999, 'Drama'),
('Inception', 2010, 'Action'),
('The Silence of the Lambs', 1991, 'Crime'),
('Schindler''s List', 1993, 'Biography'),
('The Godfather: Part II', 1974, 'Crime'),
('The Shawshank Redemption', 1994, 'Drama'),
('The Dark Knight Rises', 2012, 'Action'),
('Goodfellas', 1990, 'Biography'),
('The Usual Suspects', 1995, 'Crime'),
('The Lord of the Rings: The Fellowship of the Ring', 2001, 'Adventure'),
('The Pianist', 2002, 'Biography'),
('Gladiator', 2000, 'Action'),
('Schindler''s List', 1993, 'Biography');

-- "reviewers" table inserts
insert into reviewers (first_name, last_name) values
('John', 'Doe'),
('Jane', 'Smith'),
('Alice', 'Johnson'),
('Bob', 'Williams'),
('Charlie', 'Brown');

-- "ratings" table inserts
insert into ratings (movie_id, reviewer_id, rating) values
(1, 1, 5),
(1, 2, 4),
(1, 3, 5),
(2, 1, 5),
(2, 2, 4),
(2, 4, 5),
(3, 2, 5),
(3, 3, 4),
(3, 5, 4),
(4, 1, 4),
(4, 4, 5),
(5, 2, 5),
(5, 3, 4),
(5, 5, 5),
(6, 1, 4),
(6, 2, 5),
(6, 4, 4),
(7, 3, 5),
(7, 5, 5),
(8, 1, 5),
(8, 3, 4),
(8, 4, 5),
(9, 2, 4),
(9, 3, 5),
(10, 1, 4),
(10, 5, 5),
(11, 2, 5),
(11, 3, 4),
(12, 4, 5),
(13, 1, 5),
(13, 2, 4),
(13, 3, 5),
(14, 4, 5),
(14, 5, 4),
(15, 1, 4),
(15, 3, 5),
(15, 5, 4);

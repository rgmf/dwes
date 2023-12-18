select m.title, u.first_name, u.last_name, r.rating
from reviewers u, ratings r, movies m
where u.id=r.reviewer_id and m.id=r.movie_id and u.first_name="Alice";

select m.title, avg(r.rating) average
from movies m, ratings r
where m.id=r.movie_id
group by m.id
order by average desc;

select u.first_name, u.last_name, count(*) number_of_valorations
from reviewers u, ratings r
where u.id=r.reviewer_id
group by u.id
order by number_of_valorations desc
limit 1;

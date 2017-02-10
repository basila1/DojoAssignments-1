select clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
from clients
join billing on clients.id = billing.clients_id;
select sites.domain_name, leads.first_name, leads.last_name 
from sites 
join leads on sites.id = leads.sites_id;
select clients.first_name, clients.last_name, sites.domain_name, leads.first_name
from clients
join sites on clients.id = sites.clients_id
join leads on sites.id = leads.sites_id;
select clients.first_name, clients.last_name, sites.domain_name
from clients
left join sites on clients.id = sites.clients_id; 

use twitter;
SELECT *
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;
SELECT first_name, tweet
FROM users
LEFT JOIN faves
ON users.id = faves.user_id
LEFT JOIN tweets
ON faves.tweet_id = tweets.id
WHERE users.id = 2;
SELECT users.first_name as followed, users2.first_name as follower
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
LEFT JOIN users as users2
ON users2.id = follows.follower_id
WHERE users.id = 1;
SELECT *
FROM users
WHERE users.id NOT IN (
SELECT follower_id
FROM follows
WHERE followed_id = 2
) AND users.id != 2;
SELECT users.first_name as user, COUNT(users2.first_name) as follower_count
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
LEFT JOIN users as users2
ON users2.id = follows.follower_id
WHERE users.id = 1
GROUP BY users.id;




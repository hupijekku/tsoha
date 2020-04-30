Types of user  
------  
Visitor (User that has not logged in)  
User (User that has logged in, inherits Visitor)  
Super user (User with extended privileges, inherits User)  
  
User stories  
------
As a visitor, I can view created posts.  
~~~~sql
SELECT * FROM post;
~~~~
As a visitor, I can create an account.
~~~~sql
INSERT INTO account (date_created, date_modified, full_name, username, password, role, admin) VALUES (current_timestamp, current_timestamp, ?, ?, ?, ?, ?);
~~~~
As a visitor, I can view statistics about the site.
~~~~sql
SELECT account.full_name, COUNT(account.id) as c FROM account LEFT JOIN post ON account.id = post.user_id WHERE post.title IS NOT NULL GROUP BY account.id, post.user_id ORDER BY c DESC;

SELECT DISTINCT tag.name, COUNT(*) as c FROM post_tag LEFT JOIN tag ON tag_id = tag.id GROUP BY tag.name ORDER BY c DESC;

SELECT post.id, post.title, COUNT(vote.post_id) as c FROM vote LEFT JOIN post ON vote.post_id = post.id GROUP BY post.id, post.title ORDER BY c DESC;
~~~~
As a user, I can create new posts and vote on posts created by other users.  
~~~~sql
INSERT INTO post (date_created, date_modified, title, content) VALUES (current_timestamp, current_timestamp, ?, ?);  

INSERT INTO vote (date_created, date_modified, post_id, user_id) VALUES (current_timestamp, current_timestamp, ?, ?);
~~~~
As a user, I can edit or delete posts that I have created.
~~~~sql
UPDATE post SET date_modified=current_timestamp, content=? WHERE post.id=?

DELETE post WHERE post.id=?
~~~~
As a user, I can change my name, username or password.
~~~~sql
UPDATE account SET date_modified=current_timestamp, full_name=?, username=?, password=? WHERE account.id=?
~~~~
As a user, I can delete my account with all its posts and votes permanently.  
~~~~sql
DELETE account WHERE account.id=?
~~~~
As a Super user, I can edit and delete any posts, even ones not created by me.  
~~~~sql
UPDATE post SET date_modified=current_timestamp, content=? WHERE post.id=?

DELETE post WHERE post.id=?
~~~~

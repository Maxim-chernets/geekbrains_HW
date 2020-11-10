USE vk;
DESC profiles;

-- Добавляем внешние ключи
ALTER TABLE profiles
  ADD CONSTRAINT profiles_user_id_fk 
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE,
  ADD CONSTRAINT profiles_photo_id_fk
    FOREIGN KEY (photo_id) REFERENCES media(id)
      ON DELETE SET NULL,
  ADD CONSTRAINT profiles_status_id_fk
    FOREIGN KEY (status_id) REFERENCES profile_statuses(id)
      ON DELETE SET NULL;

ALTER TABLE profiles
  ADD CONSTRAINT profiles_city_id_fk
    FOREIGN KEY (city_id) REFERENCES cities(id)
      ON DELETE SET NULL;

UPDATE profiles SET city_id = 99 WHERE city_id = 100;
SELECT * FROM profiles;
SELECT * FROM cities;
ALTER TABLE cities 
  ADD CONSTRAINT cities_country_id_fk
    FOREIGN KEY (country_id) REFERENCES countries(id);     
     
ALTER TABLE messages
  ADD CONSTRAINT messages_from_user_id_fk 
    FOREIGN KEY (from_user_id) REFERENCES users(id),
  ADD CONSTRAINT messages_to_user_id_fk 
    FOREIGN KEY (to_user_id) REFERENCES users(id);
   
ALTER TABLE communities_users
  ADD CONSTRAINT communities_users_users_id_fk
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE;
ALTER TABLE communities_users
  ADD CONSTRAINT communities_users_communities_id_fk
    FOREIGN KEY (community_id) REFERENCES communities(id)
      ON DELETE CASCADE;


ALTER TABLE friendships 
  ADD CONSTRAINT friendships_users_id_fk
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE,
  ADD CONSTRAINT friendships_friend_id_fk
    FOREIGN KEY (friend_id) REFERENCES users(id)
      ON DELETE CASCADE;     

ALTER TABLE friendships 
  ADD CONSTRAINT friendships_statuses_id_fk
    FOREIGN KEY (status_id) REFERENCES friendship_statuses(id);
   
     
ALTER TABLE likes 
  ADD CONSTRAINT likes_users_id_fk
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE,
  ADD CONSTRAINT likes_target_id_fk
    FOREIGN KEY (target_id) REFERENCES users(id)
      ON DELETE CASCADE,
  ADD CONSTRAINT likes_target_type_id_fk
    FOREIGN KEY (target_type_id) REFERENCES target_types(id)
      ON DELETE SET NULL;    
     

ALTER TABLE media 
  ADD CONSTRAINT media_media_types_id_fk
    FOREIGN KEY (media_type_id) REFERENCES media_types(id);

   
ALTER TABLE posts 
  ADD CONSTRAINT posts_user_id_fk
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE,
  ADD CONSTRAINT posts_community_id_fk
    FOREIGN KEY (community_id) REFERENCES communities(id)
      ON DELETE SET NULL,   
  ADD CONSTRAINT posts_media_id_fk
    FOREIGN KEY (media_id) REFERENCES media(id)
      ON DELETE SET NULL;   
     
DESC posts;
DESC communities_users;
   
     
     
ALTER TABLE profiles DROP FOREIGN KEY profiles_user_id_fk;
ALTER TABLE profiles MODIFY COLUMN photo_id INT(10) UNSIGNED;

UPDATE countries SET id = 191 WHERE id=190;
DESC cities;
SELECT * FROM countries;
DESC countries;

UPDATE countries SET id = id - 190;



SELECT * FROM likes;

-- Определить кто больше поставил лайков (всего) - мужчины или женщины?

SELECT * FROM profiles;
SELECT * FROM likes;


(SELECT COUNT(*) AS count FROM likes WHERE user_id IN 
(SELECT user_id FROM profiles WHERE gender = 'm')) 
UNION
(SELECT COUNT(*) AS count FROM likes WHERE user_id IN 
(SELECT user_id FROM profiles WHERE gender = 'f'));
-- Подсчитать общее количество лайков десяти самым молодым пользователям
-- (сколько лайков получили 10 самых молодых пользователей) - не сделал


SELECT SUM(all_likes) FROM 
(SELECT
(SELECT COUNT(*) FROM likes WHERE target_id =
(SELECT id FROM target_types WHERE name = 'users')) AS all_likes
FROM profiles
ORDER BY birthday
LIMIT 10) AS user_likes;



-- Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети
-- не ставят лайки (нет в столбце likes.user_id) и не загружают медиа

SELECT id AS noActiveUsers FROM users WHERE id <> ALL(
SELECT user_id FROM likes) AND id <> ALL (SELECT user_id FROM media) ORDER BY id;



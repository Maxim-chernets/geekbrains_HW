USE vk;

-- 1. Определить кто больше поставил лайков (всего) - мужчины или женщины?


SELECT profiles.gender, COUNT(*) AS total
FROM likes
JOIN profiles
ON likes.user_id = profiles.user_id
GROUP BY gender
ORDER BY total DESC
LIMIT 1;

-- 2. Подсчитать общее количество лайков десяти самым молодым пользователям
-- (сколько лайков получили 10 самых молодых пользователей).

SELECT SUM(total) AS totatl_for_the_youngest
FROM (
SELECT COUNT(likes.id) AS total, profiles.user_id
FROM profiles
LEFT JOIN likes
ON likes.target_id = profiles.user_id AND target_type_id = 2
GROUP BY profiles.user_id 
ORDER BY profiles.birthday DESC
LIMIT 10) AS youngest;

--  Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети

SELECT users.id,
COUNT(messages.id) + COUNT(likes.id) + COUNT(media.id) AS active
FROM users
LEFT JOIN media
  ON media.user_id = users.id
LEFT JOIN messages
  ON messages.from_user_id = users.id
LEFT JOIN likes
  ON likes.user_id = users.id
GROUP BY users.id
ORDER BY active DESC 
LIMIT 10;
  










           
      
-- Проанализировать какие запросы могут выполняться наиболее
-- часто в процессе работы приложения и добавить необходимые индексы.


USE vk;
CREATE INDEX media_filename_idx ON media(filename); -- поиск по названию файла
CREATE INDEX messages_from_user_id_to_user_id_idx ON messages (from_user_id, to_user_id); -- чтобы идеть переписку между юзерами
CREATE INDEX users_first_name_idx ON users(first_name); -- поиск по имени
CREATE INDEX users_last_name_idx ON users(last_name); -- поиск по фамилии
CREATE INDEX users_first_name_last_name_idx ON users(first_name, last_name);
CREATE UNIQUE INDEX users_email_uq ON users(email);
CREATE UNIQUE INDEX users_phone_uq ON users(phone);
CREATE INDEX communities_name_idx ON communities(name);

SHOW INDEX FROM media;


-- Задание на оконные функции
-- Построить запрос, который будет выводить следующие столбцы:
-- имя группы
-- среднее количество пользователей в группах - НЕ ПОЛУЧИЛОСЬ
-- самый молодой пользователь в группе
-- самый старший пользователь в группе
-- общее количество пользователей в группе
-- всего пользователей в системе
-- отношение в процентах (общее количество пользователей в группе / всего пользователей в системе) * 100


SELECT communities.id, communities.name,
MIN(profiles.birthday) OVER(PARTITION BY communities.name) AS min, -- самый молодой пользователь в группе
MAX(profiles.birthday) OVER(PARTITION BY communities.name) AS max, -- самый старший пользователь в группе
COUNT(profiles.user_id) OVER(PARTITION BY communities.name) AS total_by_group, -- общее количество пользователей в группе
COUNT(profiles.user_id) OVER() AS total_in_vk,  -- всего пользователей в системе
COUNT(profiles.user_id) OVER(PARTITION BY communities.name) / COUNT(profiles.user_id) OVER() *100 AS '%'  -- отношение в процентах
FROM communities
LEFT JOIN communities_users
ON communities.id = communities_users.community_id 
LEFT JOIN profiles
ON communities_users.user_id = profiles.user_id;



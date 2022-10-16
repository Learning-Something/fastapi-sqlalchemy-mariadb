CREATE DATABASE IF NOT EXISTS `test_db`;
GRANT ALL ON `test_db`.* TO 'todo_list'@'%';
FLUSH PRIVILEGES;

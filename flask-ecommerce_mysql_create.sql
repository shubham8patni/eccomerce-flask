create database flask_ecommerce;
use flask_ecommerce;

CREATE TABLE `categories` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`category_name` varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `user_buyers` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`full_name` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL UNIQUE,
	`mobile_number` varchar(255) NOT NULL UNIQUE,
	`password` varchar(255) NOT NULL,
	`status` ENUM('active', 'deleted', 'disabled'),
	`address` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `products` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`category_id` INT NOT NULL,
	`product_name` varchar(255) NOT NULL UNIQUE,
	`description` TEXT,
	`amount` INT NOT NULL,
	`image_url` varchar(255),
	`status` ENUM('active', 'outofstock','deleted'),
	PRIMARY KEY (`id`)
);

CREATE TABLE `orders` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`product_id` INT NOT NULL,
	`amount` INT NOT NULL,
	`address` varchar(255) NOT NULL,
	`start_date` DATETIME NOT NULL,
	`complete_date` DATETIME NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `transactions` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`amount` INT NOT NULL,
	`user_id` INT NOT NULL,
	`product_id` INT NOT NULL,
	`status` ENUM('completed', 'pending', 'rejected'),
	PRIMARY KEY (`id`)
);

ALTER TABLE `products` ADD CONSTRAINT `products_fk0` FOREIGN KEY (`category_id`) REFERENCES `categories`(`id`);

ALTER TABLE `orders` ADD CONSTRAINT `orders_fk0` FOREIGN KEY (`user_id`) REFERENCES `user_buyers`(`id`);

ALTER TABLE `orders` ADD CONSTRAINT `orders_fk1` FOREIGN KEY (`product_id`) REFERENCES `products`(`id`);

ALTER TABLE `transactions` ADD CONSTRAINT `transactions_fk0` FOREIGN KEY (`user_id`) REFERENCES `user_buyers`(`id`);

ALTER TABLE `transactions` ADD CONSTRAINT `transactions_fk1` FOREIGN KEY (`product_id`) REFERENCES `products`(`id`);







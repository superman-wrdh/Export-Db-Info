CREATE TABLE `Roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8

CREATE TABLE `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `is_vip` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `Roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8

CREATE TABLE `products` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `price` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_products_deleted_at` (`deleted_at`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8

CREATE TABLE `resources` (
  `id` varchar(32) NOT NULL,
  `file_key` varchar(255) NOT NULL DEFAULT '',
  `type` varchar(54) NOT NULL DEFAULT '',
  `mime_type` varchar(64) NOT NULL DEFAULT '',
  `reference_id` varchar(32) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  `original_file_name` varchar(255) NOT NULL DEFAULT '',
  `description` varchar(255) NOT NULL DEFAULT '',
  `extension` varchar(64) NOT NULL DEFAULT '',
  `storage_type` varchar(54) NOT NULL DEFAULT '',
  `storage_param` varchar(64) NOT NULL DEFAULT '',
  `size` int(11) NOT NULL DEFAULT '0',
  `meta` varchar(32) NOT NULL DEFAULT '',
  `created_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8


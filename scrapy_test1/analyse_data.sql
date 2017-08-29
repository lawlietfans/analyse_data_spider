/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : analyse_data
tb_apps
Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-08-17 16:33:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `tb_apps`
-- ----------------------------
DROP TABLE IF EXISTS `tb_apps`;
CREATE TABLE `tb_apps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `developer` varchar(100) DEFAULT NULL,
  `description` text,
  `package` varchar(100) NOT NULL, -- 爬取过程中标识不同的app, no null
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for `tb_comment`
-- ----------------------------
DROP TABLE IF EXISTS `tb_comment`;
CREATE TABLE `tb_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_id` int(11) NOT NULL,
  `market` varchar(32) NOT NULL, -- -- 简化之，替代storeid
  `author` varchar(32) DEFAULT NULL, -- 改成varchar
  `score` int(11) NOT NULL,
  `description` text NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_id` (`app_id`),
  CONSTRAINT `tb_comment_ibfk_1` FOREIGN KEY (`app_id`) REFERENCES `tb_apps` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_comment
-- ----------------------------

-- ----------------------------
-- Table structure for `tb_records_day`
-- ----------------------------
DROP TABLE IF EXISTS `tb_records_day`;
CREATE TABLE `tb_records_day` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_id` int(11) NOT NULL,
  `market` varchar(32) NOT NULL, -- -- 简化之，替代storeid
  `version` varchar(32) DEFAULT NULL,
  `tick` datetime NOT NULL,
  `downloads_day` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `tb_records_day_ibfk_1` FOREIGN KEY (`app_id`) REFERENCES `tb_apps` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_records_day
-- ----------------------------

-- ----------------------------
-- Table structure for `tb_records_detail`
-- ----------------------------
DROP TABLE IF EXISTS `tb_records_detail`;
CREATE TABLE `tb_records_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_id` int(11) NOT NULL,
  `market` varchar(32) NOT NULL, -- -- 简化之，替代storeid
  `version` varchar(32) DEFAULT NULL, -- --取消key，直接设version name。没必要再细分
  `tick` datetime NOT NULL,
  `downloads_total` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_id` (`app_id`),
  CONSTRAINT `tb_records_detail_ibfk_1` FOREIGN KEY (`app_id`) REFERENCES `tb_apps` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_records_detail
-- ----------------------------

-- ----------------------------
-- Table structure for `tb_score_sum`
-- ----------------------------
DROP TABLE IF EXISTS `tb_score_sum`;
CREATE TABLE `tb_score_sum` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_id` int(11) NOT NULL,
  `market` varchar(32) NOT NULL, -- -- 简化之，替代storeid
  `date` datetime NOT NULL,
  `score` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_id` (`app_id`),
  CONSTRAINT `tb_score_sum_ibfk_1` FOREIGN KEY (`app_id`) REFERENCES `tb_apps` (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_score_sum
-- ----------------------------

-- ----------------------------
-- Table structure for `tb_stores`， 基本用不上了
-- -- ----------------------------
-- DROP TABLE IF EXISTS `tb_stores`;
-- CREATE TABLE `tb_stores` (
--   `id` int(11) NOT NULL AUTO_INCREMENT,
--   `name` varchar(50) NOT NULL,
--   PRIMARY KEY (`id`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;



-- ----------------------------
-- Table structure for `tb_version_history`
-- ----------------------------
DROP TABLE IF EXISTS `tb_version_history`;
CREATE TABLE `tb_version_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `update_time` datetime NOT NULL,
  `update_description` text,
  PRIMARY KEY (`id`),
  KEY `app_id` (`app_id`),
  CONSTRAINT `tb_version_history_ibfk_1` FOREIGN KEY (`app_id`) REFERENCES `tb_apps` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_version_history
-- ----------------------------

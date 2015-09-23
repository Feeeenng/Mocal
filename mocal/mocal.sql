/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50624
Source Host           : localhost:3306
Source Database       : mocal

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2015-09-23 17:52:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `upload`
-- ----------------------------
DROP TABLE IF EXISTS `upload`;
CREATE TABLE `upload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `path` text NOT NULL COMMENT '上传文件的路径',
  `type` varchar(20) NOT NULL COMMENT '上传文件的类型',
  `md5` varchar(40) NOT NULL COMMENT '上传文件内容的md5码',
  `category` varchar(40) NOT NULL COMMENT '上传文件的分类文件夹',
  `status` int(11) DEFAULT '1' COMMENT '状态',
  `created_at` datetime NOT NULL COMMENT '创建时间',
  `updated_at` datetime NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of upload
-- ----------------------------
INSERT INTO `upload` VALUES ('1', 'static/upload\\carousel\\koala.jpg', 'jpg', '003f1b259ed527dd81a78c687350b56f', 'carousel', '1', '2015-09-23 17:01:49', '2015-09-23 17:01:49');
INSERT INTO `upload` VALUES ('2', 'static/upload\\carousel\\lighthouse.jpg', 'jpg', '0f8cc614a7ca0d9892d58c2e02113d08', 'carousel', '1', '2015-09-23 17:02:17', '2015-09-23 17:02:17');
INSERT INTO `upload` VALUES ('3', 'static/upload\\carousel\\tulips.jpg', 'jpg', '8a5c6da9d37ae336f79680ab92a67114', 'carousel', '1', '2015-09-23 17:02:22', '2015-09-23 17:02:22');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(20) NOT NULL DEFAULT '' COMMENT '昵称',
  `age` int(11) DEFAULT '0' COMMENT '年龄',
  `sex` varchar(6) DEFAULT '' COMMENT '性别',
  `email` varchar(40) DEFAULT '' COMMENT '邮箱',
  `mobile` varchar(11) DEFAULT '' COMMENT '手机号',
  `photo` text COMMENT '相片链接',
  `account` varchar(32) NOT NULL COMMENT '登录账号',
  `password` varchar(32) NOT NULL COMMENT '登录密码',
  `status` int(11) DEFAULT '1' COMMENT '状态',
  `created_at` datetime NOT NULL COMMENT '创建时间',
  `updated_at` datetime NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------

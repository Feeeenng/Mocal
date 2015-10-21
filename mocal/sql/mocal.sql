/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50624
Source Host           : localhost:3306
Source Database       : mocal

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2015-10-21 18:25:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `chat_msg`
-- ----------------------------
DROP TABLE IF EXISTS `chat_msg`;
CREATE TABLE `chat_msg` (
`id`  int(11) NOT NULL AUTO_INCREMENT COMMENT '0:非用户' ,
`uid`  int(11) NULL DEFAULT NULL COMMENT '用户名' ,
`content`  text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '内容' ,
`timestamp`  int(11) NOT NULL COMMENT '聊天时间戳' ,
`status`  int(11) NOT NULL DEFAULT 1 COMMENT '状态' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
AUTO_INCREMENT=1

;

-- ----------------------------
-- Table structure for `upload`
-- ----------------------------
DROP TABLE IF EXISTS `upload`;
CREATE TABLE `upload` (
`id`  int(11) NOT NULL AUTO_INCREMENT ,
`path`  text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '上传文件的路径' ,
`type`  varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '上传文件的类型' ,
`md5`  varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '上传文件内容的md5码' ,
`category`  varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '上传文件的分类文件夹' ,
`status`  int(11) NULL DEFAULT 1 COMMENT '状态' ,
`created_at`  datetime NOT NULL COMMENT '创建时间' ,
`updated_at`  datetime NOT NULL COMMENT '修改时间' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
AUTO_INCREMENT=9

;

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
`id`  int(11) NOT NULL AUTO_INCREMENT ,
`nickname`  varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '昵称' ,
`age`  int(11) NULL DEFAULT 0 COMMENT '年龄' ,
`sex`  varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '性别' ,
`email`  varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '邮箱' ,
`mobile`  varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '手机号' ,
`photo`  text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '相片链接' ,
`account`  varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '登录账号' ,
`password`  varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '登录密码' ,
`status`  int(11) NULL DEFAULT 1 COMMENT '状态' ,
`privileges`  varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0' COMMENT '权限' ,
`role`  int(11) NOT NULL DEFAULT 111 COMMENT '角色' ,
`confirmed`  int(11) NULL DEFAULT 0 COMMENT '账户确认' ,
`created_at`  datetime NOT NULL COMMENT '创建时间' ,
`updated_at`  datetime NOT NULL COMMENT '修改时间' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
AUTO_INCREMENT=30

;

-- ----------------------------
-- Auto increment value for `chat_msg`
-- ----------------------------
ALTER TABLE `chat_msg` AUTO_INCREMENT=1;

-- ----------------------------
-- Auto increment value for `upload`
-- ----------------------------
ALTER TABLE `upload` AUTO_INCREMENT=9;

-- ----------------------------
-- Auto increment value for `user`
-- ----------------------------
ALTER TABLE `user` AUTO_INCREMENT=30;

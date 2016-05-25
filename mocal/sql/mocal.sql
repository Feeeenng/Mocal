/*
Navicat MySQL Data Transfer

Source Server         : Mocal
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : mocal

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2016-05-25 14:53:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `message`
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_uid` int(11) NOT NULL,
  `to_uid` int(11) DEFAULT '0',
  `group` int(11) DEFAULT '0',
  `type` int(10) unsigned NOT NULL DEFAULT '1' COMMENT '1:文本2:图片',
  `content` varchar(200) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of message
-- ----------------------------

-- ----------------------------
-- Table structure for `topic`
-- ----------------------------
DROP TABLE IF EXISTS `topic`;
CREATE TABLE `topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` varchar(200) DEFAULT '',
  `type` int(11) NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `creator_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of topic
-- ----------------------------
INSERT INTO `topic` VALUES ('1', 'mocal你觉得怎么样？', '', '0', '2016-03-29 16:48:03', '2016-03-29 16:48:07', null, '420');
INSERT INTO `topic` VALUES ('2', '来来来来吐槽吧！', '呵呵！', '2', '2016-03-30 18:10:05', '2016-03-30 18:10:05', null, '420');
INSERT INTO `topic` VALUES ('3', '欢迎兰友世来我的网站玩！', '我和梁晓的好朋友来玩', '8', '2016-04-01 22:33:48', '2016-04-01 22:33:48', null, '420');
INSERT INTO `topic` VALUES ('4', '我的名字叫韩能放', '对！是的！我就是大肥', '9', '2016-04-11 19:10:36', '2016-04-11 19:10:36', null, '420');
INSERT INTO `topic` VALUES ('5', 'football', '推荐几款足球游戏吧', '1', '2016-04-11 19:11:37', '2016-04-11 19:11:37', null, '420');
INSERT INTO `topic` VALUES ('6', 'python', '我一直在写这个语言', '2', '2016-04-11 19:12:10', '2016-04-11 19:12:10', null, '420');
INSERT INTO `topic` VALUES ('7', 'flask', '这是本网站的后端框架', '3', '2016-04-11 19:12:34', '2016-04-11 19:12:34', null, '420');
INSERT INTO `topic` VALUES ('8', 'semanticUI', '这个就是轻量级比较炫酷的前端框架了', '4', '2016-04-11 19:13:18', '2016-04-11 19:13:18', null, '420');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(20) NOT NULL DEFAULT '' COMMENT '昵称',
  `email` varchar(40) NOT NULL DEFAULT '' COMMENT '邮箱',
  `password` varchar(32) NOT NULL COMMENT '登录密码',
  `gender` varchar(10) DEFAULT '0' COMMENT '0保密；1男；2女',
  `status` int(11) DEFAULT '1' COMMENT '状态',
  `privileges` varchar(100) NOT NULL DEFAULT '0' COMMENT '权限',
  `role` int(11) NOT NULL DEFAULT '111' COMMENT '角色',
  `confirmed` int(11) DEFAULT '0' COMMENT '账户确认',
  `from` int(11) DEFAULT '0',
  `created_at` datetime NOT NULL COMMENT '创建时间',
  `updated_at` datetime NOT NULL COMMENT '修改时间',
  `deleted_at` datetime DEFAULT NULL,
  `sign_out_at` datetime DEFAULT NULL,
  `sign_in_at` datetime DEFAULT NULL,
  `sign_in_ip` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nickaname` (`nickname`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=431 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('420', 'Mocal', '369685930@qq.com', '472bfe06b32104103964b9bc5e1311f8', 'male', '1', '1', '111', '0', '0', '2016-03-29 16:45:48', '2016-05-18 18:05:17', null, '2016-04-27 19:41:36', '2016-05-18 18:05:17', '43.227.252.50');
INSERT INTO `user` VALUES ('421', 'nickl', '460775568@qq.com', 'ab906f2770361d83276ce70936f736e5', 'secret', '1', '0', '111', '1', '0', '2016-03-30 19:52:56', '2016-04-12 10:32:35', null, null, '2016-04-12 10:32:35', '182.101.50.51');
INSERT INTO `user` VALUES ('422', 'lx', 'nengfang.han@17zuoye.com', '472bfe06b32104103964b9bc5e1311f8', 'female', '1', '0', '111', '0', '0', '2016-03-30 23:12:02', '2016-04-01 18:58:31', null, '2016-04-01 18:58:31', '2016-04-01 18:57:47', '43.227.252.50');
INSERT INTO `user` VALUES ('423', 'sdfsdf', 'sdfsdf2@AA.CCC', 'ea498ce409d74d74d69b2a94ad9de45a', 'male', '1', '0', '111', '0', '0', '2016-03-31 16:52:11', '2016-03-31 16:52:11', null, null, null, null);
INSERT INTO `user` VALUES ('424', 'XYLXI', 'bruce_wzhw@163.com', 'a97b5054a48eeddfc0fba3e01e200b99', 'male', '1', '0', '111', '0', '0', '2016-03-31 16:53:20', '2016-03-31 16:54:17', null, null, '2016-03-31 16:54:17', '115.33.42.140');
INSERT INTO `user` VALUES ('425', 'xp', 'sunday_xp@qq.com', '0aa5891c952af11ec7dde2304186a647', 'secret', '1', '0', '111', '0', '0', '2016-03-31 16:56:27', '2016-03-31 16:56:40', null, null, '2016-03-31 16:56:40', '124.205.212.1');
INSERT INTO `user` VALUES ('426', 'XH', '893681848@qq.com', '87c4a64e7bb879fdba8e467de25ed52c', 'secret', '1', '0', '111', '0', '0', '2016-03-31 17:02:12', '2016-03-31 17:02:12', null, null, null, null);
INSERT INTO `user` VALUES ('427', '红树林', '732658707@qq.com', '7451b0e1c98deaa4249eeff6ffa5fbf6', 'male', '1', '0', '111', '1', '0', '2016-04-01 22:23:32', '2016-04-01 22:24:24', null, null, '2016-04-01 22:24:24', '124.205.212.4');
INSERT INTO `user` VALUES ('428', 'Sir0xb', 'Sir0xb@live.com', '98932ed4af4fa33411913f2654762a39', 'secret', '1', '0', '111', '0', '0', '2016-04-11 19:30:54', '2016-04-11 19:37:12', null, '2016-04-11 19:37:12', '2016-04-11 19:31:03', '43.227.252.50');
INSERT INTO `user` VALUES ('429', '123456', 'dd@163.com', '98932ed4af4fa33411913f2654762a39', 'secret', '1', '0', '111', '0', '0', '2016-04-14 19:27:00', '2016-04-14 19:27:00', null, null, null, null);
INSERT INTO `user` VALUES ('430', '萌萌', '283383308@qq.com', '6d6a8e47c424c5eee04d0d573481fc04', 'male', '1', '0', '111', '0', '0', '2016-04-26 19:23:24', '2016-04-26 19:43:00', null, '2016-04-26 19:43:00', '2016-04-26 19:30:31', '43.227.252.50');

-- ----------------------------
-- Table structure for `user_info`
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL COMMENT 'uid',
  `photo` varchar(100) DEFAULT NULL COMMENT '头像',
  `day` int(11) DEFAULT '0',
  `month` int(11) DEFAULT '0',
  `year` int(11) DEFAULT '0',
  `birthday` datetime DEFAULT NULL COMMENT '生日',
  `desc` varchar(120) DEFAULT NULL COMMENT '个性签名',
  `constellation` int(11) DEFAULT '0' COMMENT '星座',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `daleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`) USING BTREE,
  CONSTRAINT `uid` FOREIGN KEY (`uid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO `user_info` VALUES ('9', '420', '/file/MF20160329164608870', '14', '3', '1992', '1992-03-14 00:00:00', '哈哈！我叫mocal呢？', '2', '2016-03-29 16:45:48', '2016-03-29 16:45:48', null);
INSERT INTO `user_info` VALUES ('10', '421', 'http://mocal.cn/file/MF20160303163719570', '0', '0', '0', null, null, '0', '2016-03-30 19:52:56', '2016-03-30 19:52:56', null);
INSERT INTO `user_info` VALUES ('11', '422', 'http://mocal.cn/file/MF20160303163537835', '0', '0', '0', null, null, '0', '2016-03-30 23:12:02', '2016-03-30 23:12:02', null);
INSERT INTO `user_info` VALUES ('12', '423', 'http://mocal.cn/file/MF20160303163649153', '0', '0', '0', null, null, '0', '2016-03-31 16:52:11', '2016-03-31 16:52:11', null);
INSERT INTO `user_info` VALUES ('13', '424', 'http://mocal.cn/file/MF20160303163649153', '0', '0', '0', null, null, '0', '2016-03-31 16:53:20', '2016-03-31 16:53:20', null);
INSERT INTO `user_info` VALUES ('14', '425', 'http://mocal.cn/file/MF20160303163719570', '0', '0', '0', null, null, '0', '2016-03-31 16:56:27', '2016-03-31 16:56:27', null);
INSERT INTO `user_info` VALUES ('15', '426', 'http://mocal.cn/file/MF20160303163719570', '0', '0', '0', null, null, '0', '2016-03-31 17:02:12', '2016-03-31 17:02:12', null);
INSERT INTO `user_info` VALUES ('16', '427', 'http://mocal.cn/file/MF20160303163649153', '0', '0', '0', null, null, '0', '2016-04-01 22:23:32', '2016-04-01 22:23:32', null);
INSERT INTO `user_info` VALUES ('17', '428', 'http://mocal.cn/file/MF20160303163719570', '0', '0', '0', null, null, '0', '2016-04-11 19:30:54', '2016-04-11 19:30:54', null);
INSERT INTO `user_info` VALUES ('18', '429', 'http://mocal.cn/file/MF20160303163719570', '0', '0', '0', null, null, '0', '2016-04-14 19:27:00', '2016-04-14 19:27:00', null);
INSERT INTO `user_info` VALUES ('19', '430', '/file/MF20160315170830447', '0', '0', '1981', '1981-03-04 00:00:00', '', '0', '2016-04-26 19:23:24', '2016-04-26 19:23:24', null);

-- ----------------------------
-- Table structure for `user_topics`
-- ----------------------------
DROP TABLE IF EXISTS `user_topics`;
CREATE TABLE `user_topics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL COMMENT '用户id',
  `tid` int(11) DEFAULT NULL COMMENT '话题id',
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Records of user_topics
-- ----------------------------
INSERT INTO `user_topics` VALUES ('3', '420', '1', '2016-03-29 16:48:31', '2016-04-11 19:26:57', '2016-04-11 19:26:57');
INSERT INTO `user_topics` VALUES ('4', '420', '2', '2016-03-30 18:10:07', '2016-04-11 19:26:55', '2016-04-11 19:26:55');
INSERT INTO `user_topics` VALUES ('5', '421', '2', '2016-03-30 19:55:11', '2016-03-30 19:55:13', null);
INSERT INTO `user_topics` VALUES ('6', '421', '1', '2016-03-30 19:55:26', '2016-03-30 19:55:26', null);
INSERT INTO `user_topics` VALUES ('7', '422', '2', '2016-03-30 23:12:31', '2016-03-30 23:12:31', null);
INSERT INTO `user_topics` VALUES ('8', '424', '2', '2016-03-31 16:54:28', '2016-03-31 16:54:28', null);
INSERT INTO `user_topics` VALUES ('9', '425', '2', '2016-03-31 16:56:53', '2016-03-31 16:56:53', null);
INSERT INTO `user_topics` VALUES ('10', '427', '1', '2016-04-01 22:25:00', '2016-04-01 22:25:00', null);
INSERT INTO `user_topics` VALUES ('11', '420', '3', '2016-04-01 22:33:51', '2016-04-11 19:26:54', '2016-04-11 19:26:54');
INSERT INTO `user_topics` VALUES ('12', '427', '3', '2016-04-01 22:34:19', '2016-04-01 22:34:19', null);
INSERT INTO `user_topics` VALUES ('13', '420', '4', '2016-04-11 19:15:18', '2016-04-11 19:26:54', '2016-04-11 19:26:54');
INSERT INTO `user_topics` VALUES ('14', '420', '7', '2016-04-11 19:22:09', '2016-04-12 16:06:51', null);
INSERT INTO `user_topics` VALUES ('15', '428', '8', '2016-04-11 19:31:36', '2016-04-11 19:34:07', '2016-04-11 19:34:07');
INSERT INTO `user_topics` VALUES ('16', '428', '7', '2016-04-11 19:32:25', '2016-04-11 19:33:59', '2016-04-11 19:33:59');
INSERT INTO `user_topics` VALUES ('17', '428', '3', '2016-04-11 19:34:45', '2016-04-11 19:35:45', '2016-04-11 19:35:45');
INSERT INTO `user_topics` VALUES ('18', '428', '2', '2016-04-11 19:35:45', '2016-04-11 19:37:06', '2016-04-11 19:37:06');
INSERT INTO `user_topics` VALUES ('19', '428', '1', '2016-04-11 19:37:07', '2016-04-11 19:37:10', '2016-04-11 19:37:10');
INSERT INTO `user_topics` VALUES ('20', '421', '7', '2016-04-12 10:32:55', '2016-04-12 10:32:55', null);
INSERT INTO `user_topics` VALUES ('21', '420', '6', '2016-04-12 19:33:28', '2016-04-12 19:33:28', '2016-04-12 19:33:28');
INSERT INTO `user_topics` VALUES ('22', '420', '5', '2016-04-15 12:16:14', '2016-04-15 12:16:14', null);
INSERT INTO `user_topics` VALUES ('23', '430', '8', '2016-04-26 19:25:54', '2016-04-26 19:25:54', null);
INSERT INTO `user_topics` VALUES ('24', '420', '8', '2016-04-26 19:26:25', '2016-04-26 19:26:25', null);
INSERT INTO `user_topics` VALUES ('25', '430', '7', '2016-04-26 19:37:56', '2016-04-26 19:37:56', null);

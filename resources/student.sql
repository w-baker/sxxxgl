SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` int NOT NULL,
  `name` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sex` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '男',
  `age` int NOT NULL,
  `class` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `zy` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (200050129, '游娟影', '男', 14, '2021级6班', '软件工程');
INSERT INTO `student` VALUES (200050130, '韩云', '男', 18, '2019级7班', '数字媒体技术');
INSERT INTO `student` VALUES (200050131, '程雪璧', '男', 10, '2019级9班', '软件工程');
INSERT INTO `student` VALUES (200050132, '阮娣锦', '女', 12, '2020级5班', '软件工程');
INSERT INTO `student` VALUES (200050133, '邹雅爱', '女', 16, '2020级12班', '计算机科学技术');
INSERT INTO `student` VALUES (200050134, '萧霞', '男', 25, '2022级5班', '数字媒体技术');
INSERT INTO `student` VALUES (200050135, '游珊慧', '男', 27, '2020级1班', '信息与计算科学');
INSERT INTO `student` VALUES (200050136, '苏凡', '女', 14, '2020级3班', '计算机科学技术');
INSERT INTO `student` VALUES (200050137, '蒋卿琴', '男', 13, '2021级8班', '大数据技术');
INSERT INTO `student` VALUES (200050138, '宋桂', '男', 11, '2021级15班', '数字媒体技术');
INSERT INTO `student` VALUES (200050139, '薛冰', '女', 16, '2021级15班', '软件工程');
INSERT INTO `student` VALUES (200050140, '汪桂希', '男', 15, '2021级4班', '数字媒体技术');
INSERT INTO `student` VALUES (200050141, '唐晓咏', '男', 17, '2020级13班', '数字媒体技术');
INSERT INTO `student` VALUES (200050142, '连雪', '男', 16, '2020级9班', '软件工程');
INSERT INTO `student` VALUES (200050143, '叶冰叶', '女', 16, '2019级9班', '数字媒体技术');
INSERT INTO `student` VALUES (200050144, '邵琳寒', '男', 19, '2022级12班', '计算机科学技术');
INSERT INTO `student` VALUES (200050145, '吕芸昭', '男', 13, '2022级2班', '信息与计算科学');
INSERT INTO `student` VALUES (200050146, '何亚', '男', 16, '2019级12班', '信息与计算科学');
INSERT INTO `student` VALUES (200050147, '黎茗', '女', 16, '2019级10班', '计算机科学技术');
INSERT INTO `student` VALUES (200050148, '何君珍', '男', 27, '2022级2班', '数字媒体技术');
INSERT INTO `student` VALUES (200050149, '唐桂凡', '男', 13, '2019级2班', '大数据技术');
INSERT INTO `student` VALUES (200050150, '施娜', '女', 26, '2019级12班', '软件工程');
INSERT INTO `student` VALUES (200050151, '邹婵琬', '女', 30, '2020级11班', '计算机科学技术');
INSERT INTO `student` VALUES (200050152, '程瑾', '女', 15, '2019级6班', '软件工程');
INSERT INTO `student` VALUES (200050153, '洪璧丹', '女', 15, '2022级15班', '大数据技术');
INSERT INTO `student` VALUES (200050154, '黄园可', '男', 10, '2022级6班', '数字媒体技术');
INSERT INTO `student` VALUES (200050155, '蒋珍荔', '女', 20, '2020级1班', '信息与计算科学');
INSERT INTO `student` VALUES (200050156, '谢毓妹', '女', 16, '2019级2班', '大数据技术');
INSERT INTO `student` VALUES (200050157, '胡华惠', '女', 27, '2022级10班', '信息与计算科学');
INSERT INTO `student` VALUES (200050158, '邵瑶琴', '男', 17, '2022级3班', '信息与计算科学');
INSERT INTO `student` VALUES (200050159, '许苑欢', '男', 20, '2022级4班', '计算机科学技术');
INSERT INTO `student` VALUES (200050160, '蒋育梅', '女', 23, '2019级14班', '信息与计算科学');
INSERT INTO `student` VALUES (200050161, '邓丽舒', '女', 12, '2022级6班', '大数据技术');
INSERT INTO `student` VALUES (200050162, '胡霞莎', '男', 23, '2021级8班', '软件工程');
INSERT INTO `student` VALUES (200050163, '徐叶', '男', 15, '2021级10班', '数字媒体技术');
INSERT INTO `student` VALUES (200050164, '赖珊英', '女', 28, '2020级5班', '信息与计算科学');
INSERT INTO `student` VALUES (200050165, '高叶', '男', 29, '2022级6班', '大数据技术');
INSERT INTO `student` VALUES (200050166, '庄娴婷', '男', 30, '2021级15班', '软件工程');
INSERT INTO `student` VALUES (200050167, '周翠雅', '女', 13, '2019级12班', '数字媒体技术');
INSERT INTO `student` VALUES (200050168, '童秋', '女', 12, '2021级3班', '数字媒体技术');
INSERT INTO `student` VALUES (200050169, '古伊', '男', 17, '2019级15班', '大数据技术');
INSERT INTO `student` VALUES (200050170, '薛春茗', '女', 14, '2022级15班', '信息与计算科学');
INSERT INTO `student` VALUES (200050171, '田秋', '男', 26, '2021级13班', '计算机科学技术');
INSERT INTO `student` VALUES (200050172, '田真素', '女', 24, '2022级8班', '数字媒体技术');
INSERT INTO `student` VALUES (200050173, '苏蓉', '女', 30, '2021级1班', '软件工程');
INSERT INTO `student` VALUES (200050174, '庄瑞', '男', 21, '2019级11班', '信息与计算科学');
INSERT INTO `student` VALUES (200050175, '田巧叶', '女', 19, '2021级7班', '信息与计算科学');
INSERT INTO `student` VALUES (200050176, '卢希馨', '男', 26, '2022级8班', '数字媒体技术');
INSERT INTO `student` VALUES (200050177, '唐英怡', '女', 19, '2021级7班', '数字媒体技术');
INSERT INTO `student` VALUES (200050178, '戴芳可', '女', 20, '2019级9班', '软件工程');
INSERT INTO `student` VALUES (200050179, '罗婷巧', '女', 27, '2019级12班', '计算机科学技术');
INSERT INTO `student` VALUES (200050180, '梁秋桂', '男', 13, '2019级6班', '数字媒体技术');
INSERT INTO `student` VALUES (200050181, '颜叶', '男', 29, '2019级6班', '数字媒体技术');
INSERT INTO `student` VALUES (200050182, '叶素淑', '女', 28, '2020级10班', '计算机科学技术');
INSERT INTO `student` VALUES (200050183, '胡荣', '男', 20, '2022级5班', '软件工程');
INSERT INTO `student` VALUES (200050184, '邓玲淑', '男', 11, '2019级8班', '软件工程');
INSERT INTO `student` VALUES (200050185, '游宁青', '男', 24, '2020级10班', '计算机科学技术');
INSERT INTO `student` VALUES (200050186, '韩雪', '男', 30, '2020级5班', '大数据技术');
INSERT INTO `student` VALUES (200050187, '连宜', '男', 18, '2019级15班', '大数据技术');
INSERT INTO `student` VALUES (200050188, '廖爽秋', '女', 15, '2022级3班', '数字媒体技术');
INSERT INTO `student` VALUES (200050189, '魏婉', '男', 10, '2020级10班', '大数据技术');
INSERT INTO `student` VALUES (200050190, '马倩', '女', 11, '2021级8班', '计算机科学技术');
INSERT INTO `student` VALUES (200050191, '卢璐环', '女', 29, '2022级8班', '信息与计算科学');
INSERT INTO `student` VALUES (200050192, '魏枝', '男', 14, '2020级6班', '数字媒体技术');
INSERT INTO `student` VALUES (200050193, '郑蓓', '女', 23, '2022级9班', '计算机科学技术');
INSERT INTO `student` VALUES (200050194, '游琬瑶', '男', 22, '2022级8班', '信息与计算科学');
INSERT INTO `student` VALUES (200050195, '叶筠洁', '女', 25, '2021级1班', '软件工程');
INSERT INTO `student` VALUES (200050196, '古澜', '男', 18, '2019级13班', '信息与计算科学');
INSERT INTO `student` VALUES (200050197, '柯柔纨', '男', 20, '2021级14班', '软件工程');
INSERT INTO `student` VALUES (200050198, '詹莉素', '女', 28, '2019级13班', '软件工程');
INSERT INTO `student` VALUES (200050199, '杨馨玲', '女', 11, '2022级9班', '大数据技术');
INSERT INTO `student` VALUES (200050200, '潘凝', '男', 21, '2020级1班', '软件工程');
INSERT INTO `student` VALUES (200050201, '戴娅', '女', 23, '2021级11班', '计算机科学技术');
INSERT INTO `student` VALUES (200050202, '周爽芳', '女', 10, '2020级10班', '数字媒体技术');
INSERT INTO `student` VALUES (200050203, '古璐', '男', 20, '2022级6班', '计算机科学技术');
INSERT INTO `student` VALUES (200050204, '姜岚', '女', 18, '2019级12班', '信息与计算科学');
INSERT INTO `student` VALUES (200050205, '周菊霄', '男', 26, '2019级2班', '大数据技术');
INSERT INTO `student` VALUES (200050206, '郭飘苑', '女', 17, '2021级13班', '信息与计算科学');
INSERT INTO `student` VALUES (200050207, '杨希瑶', '男', 17, '2019级6班', '数字媒体技术');
INSERT INTO `student` VALUES (200050208, '姚秀', '女', 16, '2021级7班', '计算机科学技术');
INSERT INTO `student` VALUES (200050209, '梁育', '男', 27, '2019级4班', '计算机科学技术');
INSERT INTO `student` VALUES (200050210, '杨飘', '女', 25, '2020级10班', '信息与计算科学');
INSERT INTO `student` VALUES (200050211, '简珠', '女', 30, '2022级5班', '数字媒体技术');
INSERT INTO `student` VALUES (200050212, '柳云瑾', '男', 17, '2022级14班', '计算机科学技术');
INSERT INTO `student` VALUES (200050213, '王思', '女', 17, '2019级3班', '软件工程');
INSERT INTO `student` VALUES (200050214, '童瑶', '女', 18, '2022级12班', '信息与计算科学');
INSERT INTO `student` VALUES (200050215, '萧芸嘉', '女', 30, '2022级11班', '数字媒体技术');
INSERT INTO `student` VALUES (200050216, '曹琳艳', '女', 17, '2020级14班', '数字媒体技术');
INSERT INTO `student` VALUES (200050217, '廖馨雁', '男', 26, '2022级12班', '软件工程');
INSERT INTO `student` VALUES (200050218, '蒋勤', '男', 11, '2020级12班', '计算机科学技术');
INSERT INTO `student` VALUES (200050219, '范玲慧', '女', 30, '2021级14班', '软件工程');
INSERT INTO `student` VALUES (200050220, '龚巧', '男', 25, '2021级5班', '大数据技术');
INSERT INTO `student` VALUES (200050221, '范悦', '女', 24, '2022级10班', '大数据技术');
INSERT INTO `student` VALUES (200050222, '曹霞', '女', 17, '2021级14班', '计算机科学技术');
INSERT INTO `student` VALUES (200050223, '黄凤凡', '男', 13, '2022级8班', '数字媒体技术');
INSERT INTO `student` VALUES (200050224, '白舒', '男', 30, '2021级9班', '大数据技术');
INSERT INTO `student` VALUES (200050225, '李雪柔', '男', 27, '2022级1班', '计算机科学技术');
INSERT INTO `student` VALUES (200050226, '姚淑', '男', 23, '2020级3班', '大数据技术');
INSERT INTO `student` VALUES (200050227, '洪霄', '男', 27, '2022级5班', '大数据技术');

SET FOREIGN_KEY_CHECKS = 1;

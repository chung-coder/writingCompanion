-- MySQL dump 10.13  Distrib 8.3.0, for macos14.2 (arm64)
--
-- Host: localhost    Database: backendDB
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Student'),(2,'Teacher');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,32),(2,1,33),(3,1,34),(5,1,36),(7,1,49),(8,1,53),(4,1,64),(6,1,68),(17,2,29),(18,2,30),(9,2,32),(11,2,36),(14,2,52),(15,2,56),(13,2,61),(16,2,62),(10,2,64),(12,2,68);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add admin',7,'add_admin'),(26,'Can change admin',7,'change_admin'),(27,'Can delete admin',7,'delete_admin'),(28,'Can view admin',7,'view_admin'),(29,'Can add class',8,'add_class'),(30,'Can change class',8,'change_class'),(31,'Can delete class',8,'delete_class'),(32,'Can view class',8,'view_class'),(33,'Can add diary',9,'add_diary'),(34,'Can change diary',9,'change_diary'),(35,'Can delete diary',9,'delete_diary'),(36,'Can view diary',9,'view_diary'),(37,'Can add django content type',10,'add_djangocontenttype'),(38,'Can change django content type',10,'change_djangocontenttype'),(39,'Can delete django content type',10,'delete_djangocontenttype'),(40,'Can view django content type',10,'view_djangocontenttype'),(41,'Can add django migrations',11,'add_djangomigrations'),(42,'Can change django migrations',11,'change_djangomigrations'),(43,'Can delete django migrations',11,'delete_djangomigrations'),(44,'Can view django migrations',11,'view_djangomigrations'),(45,'Can add django session',12,'add_djangosession'),(46,'Can change django session',12,'change_djangosession'),(47,'Can delete django session',12,'delete_djangosession'),(48,'Can view django session',12,'view_djangosession'),(49,'Can add gptassistance',13,'add_gptassistance'),(50,'Can change gptassistance',13,'change_gptassistance'),(51,'Can delete gptassistance',13,'delete_gptassistance'),(52,'Can view gptassistance',13,'view_gptassistance'),(53,'Can add gptinteraction',14,'add_gptinteraction'),(54,'Can change gptinteraction',14,'change_gptinteraction'),(55,'Can delete gptinteraction',14,'delete_gptinteraction'),(56,'Can view gptinteraction',14,'view_gptinteraction'),(57,'Can add loginhistory',15,'add_loginhistory'),(58,'Can change loginhistory',15,'change_loginhistory'),(59,'Can delete loginhistory',15,'delete_loginhistory'),(60,'Can view loginhistory',15,'view_loginhistory'),(61,'Can add student',16,'add_student'),(62,'Can change student',16,'change_student'),(63,'Can delete student',16,'delete_student'),(64,'Can view student',16,'view_student'),(65,'Can add teacher',17,'add_teacher'),(66,'Can change teacher',17,'change_teacher'),(67,'Can delete teacher',17,'delete_teacher'),(68,'Can view teacher',17,'view_teacher');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$pkUxwMbvHreTAs9eFvziob$RQB0AFWmMZBHl2+Ov/4dbyK9+h5hR5V9XtiluiwMLS0=','2024-07-30 11:14:01.957422',1,'admin','','','admin@gmail.com',1,1,'2024-07-03 15:54:24.013039'),(2,'pbkdf2_sha256$600000$06WCy7H8ApXkbyyzeiKFOq$WZrSng6BIWh3j5lHV8/gPfLR97EzaYn3g128HcriBj8=',NULL,0,'chung','曉明','黃','peggy123456@gmail.com',0,1,'2024-07-09 16:20:47.327006'),(3,'pbkdf2_sha256$600000$pljILD2KuVcFFv9HxLgFwz$LDaVHvHplb9byV3dgtRAVDxekya2GAFAKVDZDzk0tSE=',NULL,0,'peggy','測試','高','abc2123465@gmail.com',0,1,'2024-07-11 13:40:19.855196');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Class`
--

DROP TABLE IF EXISTS `Class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Class` (
  `id` int NOT NULL AUTO_INCREMENT,
  `class_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Class`
--

LOCK TABLES `Class` WRITE;
/*!40000 ALTER TABLE `Class` DISABLE KEYS */;
INSERT INTO `Class` VALUES (1,'三年一班'),(2,'三年二班'),(3,'三年三班'),(4,'三年四班'),(5,'三年五班'),(6,'三年六班'),(7,'三年七班'),(8,'三年八班'),(9,'三年九班'),(10,'三年十班');
/*!40000 ALTER TABLE `Class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Diary`
--

DROP TABLE IF EXISTS `Diary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Diary` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `date` date NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `is_favorite` tinyint(1) NOT NULL DEFAULT '0',
  `last_modified_date` date NOT NULL,
  `mood` varchar(50) DEFAULT NULL,
  `target` varchar(255) DEFAULT NULL,
  `diary_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `diary_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Diary`
--

LOCK TABLES `Diary` WRITE;
/*!40000 ALTER TABLE `Diary` DISABLE KEYS */;
INSERT INTO `Diary` VALUES (16,1,'2024-06-13','今天的心情','今天天氣晴朗，我去了公園散步，心情非常愉快。感受到陽光的溫暖，從心底感到幸福。這種感覺真是令人愉悅，我希望未來的每一天都能保持這樣的心情。',1,'2024-06-13','普通','自己','Interaction'),(17,2,'2024-06-13','我的一天','今天我和朋友一起去了動物園，看到了許多可愛的動物，度過了一個愉快的下午。我們一邊觀賞動物，一邊聊天，相互之間的交流讓我感到非常開心。這是一個美好的回憶，我希望可以常常和朋友一起度過這樣的時光。',0,'2024-06-13','好','朋友','Interaction'),(18,3,'2024-06-13','思念的日子','今天我好想念家鄉的風景和父母，想起了和家人一起度過的美好時光。我回憶起家鄉的景色，聽到家人的聲音，心中充滿了溫暖和思念。我知道雖然距離遙遠，但我們的心永遠相連，這份思念將永遠存在。',0,'2024-06-13','很好','家人','Interaction'),(19,4,'2024-06-13','感恩的心','今天我感恩生活中的一切，包括家人、朋友和每一個遇到的人。感謝他們給予我的支持和關愛。雖然生活中有許多挑戰和困難，但有他們的陪伴和支持，我感到充滿力量，堅信可以克服一切困難。',1,'2024-06-13','很差','其他','Assistance'),(20,5,'2024-06-13','學習的日子','今天我認真學習了一整天，從中收穫滿滿，為自己的進步感到高興和自豪。學習不僅讓我獲得了知識和技能，更讓我成長和進步。我會堅持努力學習，不斷提升自己，實現更多的夢想和目標。',1,'2024-06-13','差','自己','Assistance'),(21,1,'2024-07-01','夏日的美好時光','今天下午我和朋友一起去了海灘，享受陽光和海風。我們一起游泳、曬太陽，還在沙灘上建了沙堡。這是一個非常愉快的夏日午後，我們都非常享受這樣的時光。',1,'2024-07-01','好','朋友','Interaction'),(22,1,'2024-07-02','家庭聚會','今天全家人一起聚餐，大家準備了豐盛的晚餐。席間我們聊了很多，分享了彼此的生活近況。這樣的家庭聚會讓我感到非常溫暖，也讓我更加珍惜和家人在一起的時光。',0,'2024-07-02','很好','家人','Interaction'),(23,1,'2024-07-03','工作中的挑戰','今天在工作中遇到了一些困難，但我沒有放棄，反而更加努力地去解決問題。最終，我成功地完成了任務，這讓我感到非常有成就感。這次經歷讓我明白了堅持的重要性。',1,'2024-07-03','普通','自己','Assistance'),(24,1,'2024-07-04','新技能的學習','今天我參加了一個烹飪課程，學到了很多新的烹飪技巧。我學會了如何做出一道美味的意大利麵，這讓我感到非常開心。我會繼續學習，提升自己的烹飪水平。',0,'2024-07-04','好','自己','Assistance'),(25,1,'2024-07-05','與朋友的爭吵','今天和朋友發生了一些爭吵，讓我感到非常難過。但我們冷靜下來後，互相道歉，並解決了誤會。我們的友誼變得更加堅固了。這次經歷讓我明白了溝通和理解的重要性。',1,'2024-07-05','很差','朋友','Interaction'),(26,1,'2024-07-06','運動帶來的快樂','今天我和幾個朋友一起去打籃球，雖然非常累，但大家都非常開心。運動不僅能強身健體，還能增進朋友之間的感情。我們決定以後每周都一起運動一次。',0,'2024-07-06','很好','朋友','Interaction'),(27,1,'2024-07-07','學習的新目標','今天我給自己設定了一個新的學習目標，計劃在三個月內學會一門新的編程語言。雖然這個目標有點挑戰，但我相信通過努力，我一定能夠實現。',1,'2024-07-07','普通','自己','Assistance'),(28,1,'2024-07-08','旅行的計劃','今天我和家人一起計劃了一次旅行，我們決定去一個海邊小鎮放鬆一下。大家都非常期待這次旅行，我們計劃了一些有趣的活動，這次旅行一定會非常難忘。',0,'2024-07-08','好','家人','Interaction'),(29,1,'2024-07-09','閱讀的樂趣','今天我讀了一本非常有趣的小說，讓我完全沉浸在故事中。閱讀不僅能讓人放鬆，還能開闊眼界，增加知識。我決定以後每天都要花一些時間來閱讀。',1,'2024-07-09','很好','自己','Assistance'),(30,1,'2024-07-10','音樂會的體驗','今天我和朋友一起去聽了一場音樂會，現場的氛圍非常棒。音樂讓我感到非常放鬆和愉快，這次音樂會的經歷讓我更加熱愛音樂。我希望以後能有更多機會參加這樣的活動。',0,'2024-07-10','好','朋友','Interaction');
/*!40000 ALTER TABLE `Diary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-07-03 15:56:02.293978','1','admin',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(2,'2024-07-03 15:57:59.699575','1','Student',1,'[{\"added\": {}}]',3,1),(3,'2024-07-03 15:58:57.258474','2','Teacher',1,'[{\"added\": {}}]',3,1),(4,'2024-07-03 15:58:59.701921','2','Teacher',2,'[]',3,1),(5,'2024-07-12 13:53:10.162458','31','Student object (31)',1,'[{\"added\": {}}]',16,1),(6,'2024-07-12 13:54:14.200671','1','Student object (1)',2,'[{\"changed\": {\"fields\": [\"User\"]}}]',16,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'backend','admin'),(8,'backend','class'),(9,'backend','diary'),(10,'backend','djangocontenttype'),(11,'backend','djangomigrations'),(12,'backend','djangosession'),(13,'backend','gptassistance'),(14,'backend','gptinteraction'),(15,'backend','loginhistory'),(16,'backend','student'),(17,'backend','teacher'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-07-03 15:51:34.717842'),(2,'auth','0001_initial','2024-07-03 15:51:35.069885'),(3,'admin','0001_initial','2024-07-03 15:51:35.138511'),(4,'admin','0002_logentry_remove_auto_add','2024-07-03 15:51:35.149816'),(5,'admin','0003_logentry_add_action_flag_choices','2024-07-03 15:51:35.161504'),(6,'contenttypes','0002_remove_content_type_name','2024-07-03 15:51:35.274014'),(7,'auth','0002_alter_permission_name_max_length','2024-07-03 15:51:35.364665'),(8,'auth','0003_alter_user_email_max_length','2024-07-03 15:51:35.395856'),(9,'auth','0004_alter_user_username_opts','2024-07-03 15:51:35.409331'),(10,'auth','0005_alter_user_last_login_null','2024-07-03 15:51:35.446467'),(11,'auth','0006_require_contenttypes_0002','2024-07-03 15:51:35.449040'),(12,'auth','0007_alter_validators_add_error_messages','2024-07-03 15:51:35.465738'),(13,'auth','0008_alter_user_username_max_length','2024-07-03 15:51:35.509501'),(14,'auth','0009_alter_user_last_name_max_length','2024-07-03 15:51:35.553711'),(15,'auth','0010_alter_group_name_max_length','2024-07-03 15:51:35.687941'),(16,'auth','0011_update_proxy_permissions','2024-07-03 15:51:35.712463'),(17,'auth','0012_alter_user_first_name_max_length','2024-07-03 15:51:35.770842'),(18,'backend','0001_initial','2024-07-03 15:51:35.783896'),(19,'sessions','0001_initial','2024-07-03 15:51:35.809162'),(20,'backend','0002_delete_loginhistory','2024-07-03 15:52:49.714493'),(21,'backend','0003_delete_admin','2024-07-03 16:00:03.865693');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0tyzjndq6tkfwyv12v5lc08ajmfy369b','.eJxVjEEOwiAQRe_C2hCGQqd16d4zNFOGkaqBpLQr492VpAvd_vfef6mJ9i1Ne43rtLA6K1Cn322m8Ii5Ab5TvhUdSt7WZdZN0Qet-lo4Pi-H-3eQqKZvHUYeokOQIANa8SLsTOfR9Qwy9uKtCSQkjRAxWBDH4AJ03nhEVO8PBYc4cA:1sRu6X:_DwFBL_IbajqLWAueks_uq0HbDckR8QzR5-awaucWJs','2024-07-25 13:45:01.825161'),('afo13s6qmhj30ql2b1vdgj84fne31f68','.eJxVjEEOwiAUBe_C2hCaUuh36d4zkAcfpGogKe2q8e6GpAvdvpl5h3DYt-z2Fle3sLiKQVx-N4_wiqUDfqI8qgy1bOviZVfkSZu8V47v2-n-HWS03OtRW6OTZjaKmImASVnv4ZOyPFiKGlbTpDgljGEm-FlFBDAZmJTE5wv9_jkx:1sYknp:yBhrGbu5I6nDmCXUoQb4EsHvlcRviXP_v30OagQpcwY','2024-08-13 11:14:01.959033'),('bvyutu5yxce73h88rudtpjiw9pm0oi9p','.eJxVjEEOwiAQRe_C2hCGQqd16d4zNFOGkaqBpLQr492VpAvd_vfef6mJ9i1Ne43rtLA6K1Cn322m8Ii5Ab5TvhUdSt7WZdZN0Qet-lo4Pi-H-3eQqKZvHUYeokOQIANa8SLsTOfR9Qwy9uKtCSQkjRAxWBDH4AJ03nhEVO8PBYc4cA:1sSG24:M7Le0xCo2kOiZaWtIt-Y1cndGW0uTshE7IAgW1VMegA','2024-07-26 13:09:52.556522');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GPTAssistance`
--

DROP TABLE IF EXISTS `GPTAssistance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GPTAssistance` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `diary_id` int NOT NULL,
  `interaction_time` datetime NOT NULL,
  `user_input` text NOT NULL,
  `gpt_response` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `diary_id` (`diary_id`),
  CONSTRAINT `gptassistance_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `gptassistance_ibfk_2` FOREIGN KEY (`diary_id`) REFERENCES `Diary` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GPTAssistance`
--

LOCK TABLES `GPTAssistance` WRITE;
/*!40000 ALTER TABLE `GPTAssistance` DISABLE KEYS */;
/*!40000 ALTER TABLE `GPTAssistance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GPTInteraction`
--

DROP TABLE IF EXISTS `GPTInteraction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GPTInteraction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `diary_id` int NOT NULL,
  `interaction_time` datetime NOT NULL,
  `dialogue_record` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `diary_id` (`diary_id`),
  CONSTRAINT `gptinteraction_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `gptinteraction_ibfk_2` FOREIGN KEY (`diary_id`) REFERENCES `Diary` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GPTInteraction`
--

LOCK TABLES `GPTInteraction` WRITE;
/*!40000 ALTER TABLE `GPTInteraction` DISABLE KEYS */;
/*!40000 ALTER TABLE `GPTInteraction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `gender` char(1) NOT NULL,
  `class_id` int DEFAULT NULL,
  `teacher_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `class_id` (`class_id`),
  KEY `teacher_id` (`teacher_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `Class` (`id`),
  CONSTRAINT `student_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `Teacher` (`id`),
  CONSTRAINT `student_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student`
--

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` VALUES (1,'張小明','M',1,1,1),(2,'李小花','F',1,2,NULL),(3,'王大志','M',2,3,NULL),(4,'趙美麗','F',2,4,NULL),(5,'陳國豪','M',3,5,NULL),(6,'林天成','M',3,1,NULL),(7,'高小英','F',4,2,NULL),(8,'周德華','M',4,3,NULL),(9,'許文龍','M',5,4,NULL),(10,'鄭麗珍','F',5,5,NULL),(11,'劉小平','M',6,1,NULL),(12,'楊志明','M',6,2,NULL),(13,'吳芳芳','F',7,3,NULL),(14,'何國強','M',7,4,NULL),(15,'黃秀麗','F',8,5,NULL),(16,'朱勇志','M',8,1,NULL),(17,'馬志偉','M',9,2,NULL),(18,'郭美華','F',9,3,NULL),(19,'范天龍','M',10,4,NULL),(20,'馮麗萍','F',10,5,NULL),(21,'宋明志','M',1,1,NULL),(22,'沈小青','F',1,2,NULL),(23,'葉大力','M',2,3,NULL),(24,'邱美麗','F',2,4,NULL),(25,'杜志豪','M',3,5,NULL),(26,'戴天佑','M',3,1,NULL),(27,'韓小英','F',4,2,NULL),(28,'蘇德明','M',4,3,NULL),(29,'鍾文傑','M',5,4,NULL),(30,'盧麗珍','F',5,5,NULL),(31,'test','F',1,2,2);
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teacher`
--

DROP TABLE IF EXISTS `Teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Teacher` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teacher`
--

LOCK TABLES `Teacher` WRITE;
/*!40000 ALTER TABLE `Teacher` DISABLE KEYS */;
INSERT INTO `Teacher` VALUES (1,'樊天佑'),(2,'秦德明'),(3,'馮小剛'),(4,'林芳芳'),(5,'程浩然'),(6,'高文傑'),(7,'周德華'),(8,'許文龍'),(9,'姜文淵'),(10,'趙志勇');
/*!40000 ALTER TABLE `Teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-04 11:17:38

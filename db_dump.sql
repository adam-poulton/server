-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: us-cdbr-east-05.cleardb.net    Database: heroku_3e5d99b2aad0cd1
-- ------------------------------------------------------
-- Server version	5.6.50-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `favourite`
--

DROP TABLE IF EXISTS `favourite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favourite` (
  `favourite_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`favourite_id`),
  KEY `product_id` (`product_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `favourite_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE,
  CONSTRAINT `favourite_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favourite`
--

LOCK TABLES `favourite` WRITE;
/*!40000 ALTER TABLE `favourite` DISABLE KEYS */;
INSERT INTO `favourite` VALUES (4,14,14),(14,84,14);
/*!40000 ALTER TABLE `favourite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `feedback_description` varchar(300) NOT NULL,
  `feedback_date` datetime NOT NULL,
  `feedback_rating` decimal(2,1) NOT NULL,
  PRIMARY KEY (`feedback_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (4,14,'Hi! This is a test feedback!','2022-05-19 22:59:55',4.0);
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_barcode` varchar(20) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `product_cate` varchar(50) NOT NULL,
  `product_brand` varchar(50) NOT NULL,
  `product_nutrition` varchar(900) DEFAULT NULL,
  `product_price` float DEFAULT NULL,
  `product_display_img` varchar(200) DEFAULT NULL,
  `product_nutrition_img` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `product_barcode` (`product_barcode`)
) ENGINE=InnoDB AUTO_INCREMENT=134 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (4,'9310072026428','Savoy Original','Biscuits','Arnott\'s','{\"energy\": {\"value\": 1970.0, \"unit\": \"kJ\"}, \"protein\": {\"value\": 7.9, \"unit\": \"g\"}, \"fat-total\": {\"value\": 20.0, \"unit\": \"g\"}, \"fat-saturated\": {\"value\": 3.9, \"unit\": \"g\"}, \"carbohydrate\": {\"value\": 62.6, \"unit\": \"g\"}, \"sugars\": {\"value\": 1.3, \"unit\": \"g\"}, \"sodium\": {\"value\": 848, \"unit\": \"mg\"}}',2.5,NULL,NULL),(14,'7610400074193','Lindor Extra Dark 18pc','Chocolate','Lindt','{\"energy\": {\"value\": 2670.0, \"unit\": \"kJ\"}, \"protein\": {\"value\": 4.9, \"unit\": \"g\"}, \"fat-total\": {\"value\": 53.0, \"unit\": \"g\"}, \"fat-saturated\": {\"value\": 39.0, \"unit\": \"g\"}, \"carbohydrate\": {\"value\": 34.0, \"unit\": \"g\"}, \"sugars\": {\"value\": 31.0, \"unit\": \"g\"}, \"sodium\": {\"value\": 16, \"unit\": \"mg\"}}',3,NULL,NULL),(24,'08968618065','Mi Goreng Fried Noodles Cup','Noodles','Indo mie','{\"energy\": {\"value\": 942.0, \"unit\": \"kJ\"}, \"protein\": {\"value\": 3.4, \"unit\": \"g\"}, \"fat-total\": {\"value\": 10.4, \"unit\": \"g\"}, \"fat-saturated\": {\"value\": 4.9, \"unit\": \"g\"}, \"carbohydrate\": {\"value\": 29.3, \"unit\": \"g\"}, \"sugars\": {\"value\": 3.8, \"unit\": \"g\"}, \"sodium\": {\"value\": 450, \"unit\": \"mg\"}}',0.75,NULL,NULL),(34,'93174440001168','Sweet Potato & Roasted Cashews Dip','Dip','Yumi\'s','{\"energy\": {\"value\": 1050, \"unit\": \"kJ\"}, \"protein\": {\"value\": 3.7, \"unit\": \"g\"}, \"fat-total\": {\"value\": 21.0, \"unit\": \"g\"}, \"fat-saturated\": {\"value\": 2.4, \"unit\": \"g\"}, \"carbohydrate\": {\"value\": 11.0, \"unit\": \"g\"}, \"sugars\": {\"value\": 5.1, \"unit\": \"g\"}, \"sodium\": {\"value\": 394, \"unit\": \"mg\"}}',2.99,NULL,NULL),(44,'9310015240638','Sea Salt & Balsamic Vinegar Flavoured Potato Chips','Chips','Red Rock Deli','{\"energy\": {\"value\": 2050, \"unit\": \"kJ\"}, \"protein\": {\"value\": 7.6, \"unit\": \"g\"}, \"fat-total\": {\"value\": 23.8, \"unit\": \"g\"}, \"fat-saturated\": {\"value\": 1.9, \"unit\": \"g\"}, \"fat-trans\": {\"value\": 0.1, \"unit\": \"g\"}, \"fat-poly\": {\"value\": 2.3, \"unit\": \"g\"}, \"fat-mono\": {\"value\": 5.4, \"unit\": \"g\"}, \"carbohydrate\": {\"value\": 11.0, \"unit\": \"g\"}, \"sugars\": {\"value\": 5.1, \"unit\": \"g\"}, \"sodium\": {\"value\": 394, \"unit\": \"mg\"}}',3.5,NULL,NULL),(54,'9312743010521','Spelt & Sprouted Grain Bread','Bread','Alpine Breads','{\"energy\": {\"value\": 988, \"unit\": \"kJ\"}, \"protein\": {\"value\": 11.9, \"unit\": \"g\"}, \"fat-total\": {\"value\": 1.6, \"unit\": \"g\"}, \"fat-saturated\": {\"value\": 0.6, \"unit\": \"g\"}, \"fat-trans\": {\"value\": 0.1, \"unit\": \"g\"}, \"fat-poly\": {\"value\": 2.3, \"unit\": \"g\"}, \"fat-mono\": {\"value\": 5.4, \"unit\": \"g\"}, \"carbohydrate\": {\"value\": 39.7, \"unit\": \"g\"}, \"sugars\": {\"value\": 5.1, \"unit\": \"g\"}, \"sodium\": {\"value\": 394, \"unit\": \"mg\"}}',4.7,NULL,NULL),(64,'9321582004899','Peanut Butter Smooth','Spreads','Bega','{\"energy\": {\"value\": 988, \"unit\": \"kJ\"}, \"protein\": {\"value\": 11.9, \"unit\": \"g\"}, \"fat-total\": {\"value\": 1.6, \"unit\": \"g\"}, \"fat-saturated\": {\"value\": 0.6, \"unit\": \"g\"}, \"fat-trans\": {\"value\": 0.1, \"unit\": \"g\"}, \"fat-poly\": {\"value\": 2.3, \"unit\": \"g\"}, \"fat-mono\": {\"value\": 5.4, \"unit\": \"g\"}, \"carbohydrate\": {\"value\": 39.7, \"unit\": \"g\"}, \"sugars\": {\"value\": 5.1, \"unit\": \"g\"}, \"sodium\": {\"value\": 394, \"unit\": \"mg\"}}',5.2,NULL,NULL),(74,'1543069428','demo_name','demo_cate','demo_brand','{\"energy\": {\"value\": 1.6, \"unit\": \"kJ\"}, \"protein\": {\"value\": 0.06, \"unit\": \"g\"}, \"fat-total\": {\"value\": 0, \"unit\": \"g\"}, \"fat-saturated\": {\"value\": 0, \"unit\": \"g\"}, \"carbohydrate\": {\"value\": 0.06, \"unit\": \"g\"}, \"sugars\": {\"value\": 0, \"unit\": \"g\"}, \"sodium\": {\"value\": 13, \"unit\": \"mg\"}}',14.59,'',''),(84,'4902777026107','meiji chocolate','Chocolate','Meiji','{}',8.99,'https://res.cloudinary.com/hlvl5cgpe/image/upload/v1652966004/n7gik0rims0zdsqwem7z.jpg','https://res.cloudinary.com/hlvl5cgpe/image/upload/v1652966005/ote2xngjershslrmkvvn.jpg'),(124,'123456789012','Max Coke 200mL','Soft Drink','Pepsi','{}',1.99,'https://res.cloudinary.com/hlvl5cgpe/image/upload/v1653013708/cto3zkajyzjtwgxchpmc.jpg','https://res.cloudinary.com/hlvl5cgpe/image/upload/v1653013708/xly1wd0yvsldke9xbpqs.jpg');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `review_rating` decimal(2,1) NOT NULL,
  `review_date` datetime NOT NULL,
  `review_description` varchar(300) NOT NULL,
  PRIMARY KEY (`review_id`),
  KEY `user_id` (`user_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES (24,44,74,5.0,'2022-05-19 16:38:29','Pretty good！'),(34,14,14,5.0,'2022-05-20 12:52:20','wow the famous product'),(44,54,14,4.0,'2022-05-20 12:58:01','Hey! This is a test!'),(54,54,14,2.0,'2022-05-20 12:58:18','Hey! This is another test!'),(64,14,14,2.5,'2022-05-20 14:13:06','A very tasty chocolate!'),(74,14,14,5.0,'2022-05-20 14:13:47','A very tasty chocolate!');
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scan`
--

DROP TABLE IF EXISTS `scan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scan` (
  `scan_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`scan_id`),
  KEY `product_id` (`product_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `scan_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE,
  CONSTRAINT `scan_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scan`
--

LOCK TABLES `scan` WRITE;
/*!40000 ALTER TABLE `scan` DISABLE KEYS */;
INSERT INTO `scan` VALUES (14,84,14,'2022-05-19 23:30:24'),(64,124,14,'2022-05-23 17:01:09'),(74,64,14,'2022-05-23 17:01:16');
/*!40000 ALTER TABLE `scan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_username` varchar(30) NOT NULL,
  `user_firstname` varchar(30) NOT NULL,
  `user_lastname` varchar(30) NOT NULL,
  `user_email` varchar(40) NOT NULL,
  `user_password` varchar(50) DEFAULT NULL,
  `user_contribution_score` int(11) DEFAULT NULL,
  `user_pimg_url` varchar(256) DEFAULT NULL,
  `user_hash` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_username` (`user_username`),
  UNIQUE KEY `user_email` (`user_email`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (14,'Student','Yinghua','Zhou','yinghua.zho@gmail.com',NULL,30,'https://lh3.googleusercontent.com/a-/AOh14Gj37N6HOGaEbt0suhVQo1tRkqoaFpg2YSkB-DWE=s96-c',NULL),(44,'updated_name','demo_fname','demo_lname','demo@gmail.com','demoPassword123',5,'https://res.cloudinary.com/hlvl5cgpe/image/upload/v1652941498/wtnb0isbvhdxnjagpoeh.png',NULL),(54,'Bot1','Caius','Zhou','1395141398@qq.com',NULL,10,'https://res.cloudinary.com/hlvl5cgpe/image/upload/v1653015456/ildowxwp8szsnf1gnvax.jpg',NULL),(64,'kelleyjohnson.85639@gmail.com','Kelley','Johnson','kelleyjohnson.85639@gmail.com',NULL,0,'https://lh3.googleusercontent.com/a/AATXAJxP2mTAUHl9GL3A5HmaD3L3n4hZQm0Mea8mT3Mn=s96-c',NULL),(74,'marlenetran.13548@gmail.com','Marlene','Tran','marlenetran.13548@gmail.com',NULL,0,'https://lh3.googleusercontent.com/a/AATXAJxwNtQREqMV0UWs7dnK5cUvnwgixc2BhUaz2uvc=s96-c',NULL),(84,'happydog','Happy','Dog','happydog@gmail.com','HappyDog123',0,'https://res.cloudinary.com/hlvl5cgpe/image/upload/v1653397542/uovvxq6okrvx0ycyq1cv.jpg',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'heroku_3e5d99b2aad0cd1'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-25 19:09:20

-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: jing_dong
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

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
-- Table structure for table `customer`
--
use jing_dong;
DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `tel` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `cate_id` int(10) unsigned NOT NULL,
  `brand_id` int(10) unsigned NOT NULL,
  `price` decimal(10,3) NOT NULL DEFAULT '0.000',
  `is_show` bit(1) NOT NULL DEFAULT b'1',
  `is_saleoff` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`id`),
  KEY `cate_id` (`cate_id`),
  KEY `brand_id` (`brand_id`),
  CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`cate_id`) REFERENCES `goods_cates` (`id`),
  CONSTRAINT `goods_ibfk_2` FOREIGN KEY (`brand_id`) REFERENCES `goods_brands` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (1,'r510vc 15.6英寸笔记本',1,2,3399.000,_binary '',_binary '\0'),(2,'y400n 14.0英寸笔记本电脑',1,7,4999.000,_binary '',_binary '\0'),(3,'g150th 15.6英寸游戏本',2,9,8499.000,_binary '',_binary '\0'),(4,'x550cc 15.6英寸笔记本',1,2,2799.000,_binary '',_binary '\0'),(5,'x240 超极本',3,7,4880.000,_binary '',_binary '\0'),(6,'u330p 13.3英寸超极本',3,7,4299.000,_binary '',_binary '\0'),(7,'svp13226scb 触控超极本',3,6,7999.000,_binary '',_binary '\0'),(8,'ipad mini 7.9英寸平板电脑',4,8,1998.000,_binary '',_binary '\0'),(9,'ipad air 9.7英寸平板电脑',4,8,3388.000,_binary '',_binary '\0'),(10,'ipad mini 配备 retina 显示屏',4,8,2788.000,_binary '',_binary '\0'),(11,'ideacentre c340 20英寸一体电脑 ',5,7,3499.000,_binary '',_binary '\0'),(12,'vostro 3800-r1206 台式电脑',5,5,2899.000,_binary '',_binary '\0'),(13,'imac me086ch/a 21.5英寸一体电脑',5,8,9188.000,_binary '',_binary '\0'),(14,'at7-7414lp 台式电脑 linux ）',5,3,3699.000,_binary '',_binary '\0'),(15,'z220sff f4f06pa工作站',6,4,4288.000,_binary '',_binary '\0'),(16,'poweredge ii服务器',6,5,5388.000,_binary '',_binary '\0'),(17,'mac pro专业级台式电脑',6,8,28888.000,_binary '',_binary '\0'),(18,'hmz-t3w 头戴显示设备',7,6,6999.000,_binary '',_binary '\0'),(19,'商务双肩背包',7,6,99.000,_binary '',_binary '\0'),(20,'x3250 m4机架式服务器',6,1,6888.000,_binary '',_binary '\0'),(21,'商务双肩背包',7,6,99.000,_binary '',_binary '\0');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_brands`
--

DROP TABLE IF EXISTS `goods_brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_brands` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_brands`
--

LOCK TABLES `goods_brands` WRITE;
/*!40000 ALTER TABLE `goods_brands` DISABLE KEYS */;
INSERT INTO `goods_brands` VALUES (1,'ibm'),(2,'华硕'),(3,'宏碁'),(4,'惠普'),(5,'戴尔'),(6,'索尼'),(7,'联想'),(8,'苹果'),(9,'雷神'),(16,'海尔'),(17,'清华同方'),(18,'神舟');
/*!40000 ALTER TABLE `goods_brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_cates`
--

DROP TABLE IF EXISTS `goods_cates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_cates` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_cates`
--

LOCK TABLES `goods_cates` WRITE;
/*!40000 ALTER TABLE `goods_cates` DISABLE KEYS */;
INSERT INTO `goods_cates` VALUES (1,'笔记本'),(2,'游戏本'),(3,'超级本'),(4,'平板电脑'),(5,'台式机'),(6,'服务器/工作站'),(7,'笔记本配件'),(8,'路由器'),(9,'交换机'),(10,'网卡');
/*!40000 ALTER TABLE `goods_cates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_detail`
--

DROP TABLE IF EXISTS `order_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_detail` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int(10) unsigned NOT NULL,
  `goods_id` int(10) unsigned NOT NULL,
  `quantity` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  KEY `goods_id` (`goods_id`),
  CONSTRAINT `order_detail_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `order_detail_ibfk_2` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_detail`
--

LOCK TABLES `order_detail` WRITE;
/*!40000 ALTER TABLE `order_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_date_time` datetime NOT NULL,
  `customer_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-11 13:16:44

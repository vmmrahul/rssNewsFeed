-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 24, 2021 at 12:18 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rssnewsfeed`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `mobile` varchar(13) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `username`, `password`, `name`, `mobile`, `type`) VALUES
('admin@gmail.com', 'admin', '1234', 'admin', '6280995201', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`name`, `description`) VALUES
('AutoMobiles', 'AutoMobiles'),
('Business', 'Business'),
('Cities', 'Cities'),
('Entertainment', 'Entertainment'),
('International', 'International'),
('National', 'National'),
('Science', 'Science'),
('sports', 'sports');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `photo` text NOT NULL,
  `shortDescription` varchar(1000) NOT NULL,
  `description` longtext NOT NULL,
  `catName` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`id`, `title`, `photo`, `shortDescription`, `description`, `catName`, `created_at`) VALUES
(2, 'Cyclone Tauktae Expected To Hit Gujarat In Evening, Mumbai Airport Shuts', 'news/7m5ct9jo_taukate-mumbai_625x300_17_May_21 (1)_v6aNzTA.webp', 'Cyclone Tauktae: Around 25,000 people have been evacuated from low-lying areas between Porbandar and Mahuva in Gujarat Bhavnagar district in anticipation of landfall', '<p><span class=789#987place_cont789#987 style=789#987-webkit-tap-highlight-color: transparent; font-weight: bolder; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;789#987>New Delhi:&nbsp;</span><span style=789#987color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;789#987>Cyclone Tauktae - an 789987extremely severe cyclonic storm789987 - is 789#987very likely789#987 to make landfall in Gujarat789987s Bhavnagar between 10 pm and 11 pm, with winds up to 165 km per hour. At 11.30 am it was 145 km west of Mumbai and moving at 15 km per hour.</span></p><p><span style=789#987color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;789#987><br></span></p><p><span style=789#987color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-size: 18px;789#987><br></span></p><h2 class=789#987cheat__ttl789#987 style=789#987-webkit-tap-highlight-color: transparent; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-weight: 700; line-height: 1.4; margin: 35px 0px 0px; font-size: 22px; padding: 0px 0px 20px; position: relative;789#987>Here are the top 10 points in this big story:</h2><ol><li style=789#987-webkit-tap-highlight-color: transparent; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-weight: 700; line-height: 1.4; margin: 35px 0px 0px; font-size: 22px; padding: 0px 0px 20px; position: relative;789#987><span style=789#987font-size: 18px; font-weight: 400;789#987>Mumbai is experiencing heavy to very heavy rain and winds up to 100 km per hour, with&nbsp;</span><a href=789#987https://voddownload.ndtv.com/mp4/17052021_n_PurvaOB_67295_542365_320.mp4789#987 target=789#987_self789#987 style=789#987-webkit-tap-highlight-color: transparent; color: var(--clr-lnk); cursor: pointer; transition-duration: 200ms; transition-timing-function: linear; transition-delay: 0ms; font-size: 18px; font-weight: 400; background-color: rgb(255, 255, 255);789#987>visuals from the iconic Gateway of India</a><span style=789#987font-size: 18px; font-weight: 400;789#987>&nbsp;showing waves crashing into the stone culverts and metal traffic barriers being tossed aside. The&nbsp;</span><a href=789#987https://www.ndtv.com/mumbai-news/cyclone-tauktae-mumbai-monorail-bandra-worli-sea-link-shut-as-cyclone-approaches-2443144?pfrom=home-ndtv_topscroll789#987 target=789#987_self789#987 style=789#987-webkit-tap-highlight-color: transparent; color: var(--clr-lnk); cursor: pointer; transition-duration: 200ms; transition-timing-function: linear; transition-delay: 0ms; font-size: 18px; font-weight: 400; background-color: rgb(255, 255, 255);789#987>airport has been shut till 4 pm and the Bandra-Worli sea link is closed</a><span style=789#987font-size: 18px; font-weight: 400;789#987>. Temporary shelters have been set up in each of the 24 wards and three NDRF teams are on alert.</span></li><li style=789#987-webkit-tap-highlight-color: transparent; color: rgb(46, 46, 46); font-family: Roboto, sans-serif; font-weight: 700; line-height: 1.4; margin: 35px 0px 0px; font-size: 22px; padding: 0px 0px 20px; position: relative;789#987><span style=789#987font-size: 18px; font-weight: 400;789#987>Maharashtra Chief Minister Uddhav Thackeray789987s office said the state - with nearly five lakh active Covid cases - would ensure power and oxygen for hospitals and that patients undergoing treatment at Covid and non-Covid facilities in coastal areas had been relocated. Mr Thackeray789987s office said he was closely monitoring the situation.<br></span><br></li></ol><p><br></p>', 'National', '2021-05-17 08:33:06'),
(3, 'Aerosols Can Travel 10 Metres', 'news/iisq5dv_india-coronavirus-afp-650_625x300_29_July_20.webp', 'At least 2.57 crore people in India have been infected with Covid, which has also led to death of 2.87 lakh people since the pandemic began early last year. ', '<p><b class=789#987place_cont789#987>New Delhi: </b></p><p>Smaller aerosol particles can be\r\n carried in the air for 10 metres, the government warned today as it \r\nshared a set of 789#987easy to follow789#987 guidelines on fighting Covid, which \r\nincludes double masks, social distancing and well-ventilated spaces.</p><p>Use\r\n of proper ventilation can prevent the spread of coronavirus, the Union \r\ngovernment789987s principal scientific adviser K VijayRaghavan789987s office said \r\nin the new advisory which also warns against running air conditioners \r\nwhile keeping windows and doors shut.&nbsp;789#987Running ACs traps infected air \r\ninside the room&nbsp;and increases risk of transmission from an infected \r\ncarrier to others,789#987 it said.&nbsp;</p><p>789#987Always Remember: People who show no\r\n symptoms can also spread the virus,789#987 the document, titled 789#987Stop the \r\nTransmission, Crush the Pandemic789#987 said, urging people to rigorously \r\nfollow Covid appropriate behaviour. While droplets fall within two \r\nmeters from an infected person, smaller aerosol particles are carried in\r\n the air up to 10 metres, it said.</p><p><br></p><p><strong>Aerosol and droplet transmission</strong></p><p>Saliva and \r\nnasal discharged in the form of droplets and aerosols by an infected \r\nperson is the primary mode of virus transmissions, the document said, \r\nadding that an infected person without symptoms also <a href=789#987https://www.ndtv.com/india-news/coronavirus-india-latest-news-live-updates-over-2-63-lakh-covid-19-cases-in-india-may-20-2021-2445338789#987 target=789#987_self789#987>transmit the virus</a>.</p><p>789#987Just\r\n as smells can be diluted by ventilation, the dangerous concentration of\r\n the virus can be reduced by ensuring that outdoor air flows in,789#987 it \r\nsaid.</p><p><strong>Surface transmission</strong></p><p><img style=789#987width: 650px;789#987 src=789#987https://c.ndtvimg.com/2020-07/iisq5dv_india-coronavirus-afp-650_625x300_29_July_20.jpg789#987><strong><br></strong></p><p><strong>Wear Masks</strong></p><p>People should wear a double layer \r\nmask or an N95 mask, which offers maximum protection, the new guidelines\r\n said. For double masking, wear a surgical mask, then wear another tight\r\n fitting cloth mask over it, the advisory said, adding that those who do\r\n not have a surgical mask can wear two cotton masks together.</p><p>789#987Ideally,\r\n surgical mask should be used only once, but when pairing, you can use \r\nit up to 5 times by leaving it in a dry place for 7 days after one use \r\n(ideally give it some sun exposure),789#987 it said.</p><p><strong></strong></p>', 'National', '2021-05-20 08:25:14');

-- --------------------------------------------------------

--
-- Table structure for table `videos`
--

CREATE TABLE `videos` (
  `id` int(11) NOT NULL,
  `description` text NOT NULL,
  `YouTubeLink` text NOT NULL,
  `newsid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `videos`
--

INSERT INTO `videos` (`id`, `description`, `YouTubeLink`, `newsid`) VALUES
(5, '??????????????????-??????????????????????????? ?????? India ????????? 789987?????????????????????789987?', 'https://www.youtube.com/embed/8NyvX5lEE_M', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`),
  ADD KEY `catName` (`catName`);

--
-- Indexes for table `videos`
--
ALTER TABLE `videos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `newsid` (`newsid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `videos`
--
ALTER TABLE `videos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `news`
--
ALTER TABLE `news`
  ADD CONSTRAINT `news_ibfk_1` FOREIGN KEY (`catName`) REFERENCES `category` (`name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

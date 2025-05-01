-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 22, 2025 at 02:00 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `admissions`
--

CREATE TABLE `admissions` (
  `patient_id` int(11) NOT NULL,
  `admission_date` date NOT NULL,
  `discharge_date` date DEFAULT NULL,
  `diagnosis` varchar(50) DEFAULT NULL,
  `attending_doctor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admissions`
--

INSERT INTO `admissions` (`patient_id`, `admission_date`, `discharge_date`, `diagnosis`, `attending_doctor_id`) VALUES
(1, '2003-11-21', NULL, 'Asthma', 3),
(2, '2019-01-21', NULL, 'Covid-19', 3),
(9, '2019-03-08', NULL, 'Diabetes', 4),
(11, '2020-03-25', NULL, 'Diabetes', 2),
(15, '2018-06-02', '2018-07-18', 'Asthma', 8),
(16, '2022-01-11', '2022-03-30', 'Covid-19', 7),
(22, '2003-02-19', NULL, 'Flu', 3),
(23, '2011-06-26', NULL, 'Hypertension', 3),
(23, '2022-08-14', '2011-11-28', 'Flu', 7),
(25, '2018-02-15', NULL, 'Flu', 10),
(26, '2022-01-21', '2020-07-20', 'Hypertension', 4),
(31, '2021-10-12', NULL, 'Hypertension', 5),
(34, '2015-06-20', '2015-07-30', 'Hypertension', 6),
(38, '2017-09-24', '2014-12-23', 'Cancer', 5),
(40, '2019-02-10', NULL, 'Flu', 9),
(42, '2021-09-15', '2022-11-05', 'Cancer', 5),
(57, '2021-12-01', NULL, 'Hypertension', 3),
(63, '2010-12-20', NULL, 'Hypertension', 9),
(98, '2007-12-20', '2024-08-19', 'Covid-19', 3);

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--

CREATE TABLE `doctors` (
  `doctor_id` int(11) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `specialty` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` (`doctor_id`, `first_name`, `last_name`, `specialty`) VALUES
(1, 'Dr. James', 'Smith', 'Cardiologist'),
(2, 'Dr. Emily', 'Jones', 'Orthopedist'),
(3, 'Dr. Michael', 'Taylor', 'Surgeon'),
(4, 'Dr. Sarah', 'Brown', 'Pediatrician'),
(5, 'Dr. David', 'Williams', 'Neurologist'),
(6, 'Dr. Daniel', 'Johnson', 'Psychiatrist'),
(7, 'Dr. Rachel', 'White', 'Generalist'),
(8, 'Dr. William', 'Miller', 'Endocrinologist'),
(9, 'Dr. Olivia', 'Davis', 'Oncologist'),
(10, 'Dr. Sophia', 'Clark', 'Pathologist'),
(11, 'Dr. John', 'Martinez', 'Urologist'),
(12, 'Dr. Laura', 'Roberts', 'Gastroenterologist'),
(13, 'Dr. Chris', 'Lewis', 'Dermatologist'),
(14, 'Dr. Jessica', 'Walker', 'Anesthesiologist'),
(15, 'Dr. Brian', 'Young', 'Ophthalmologist'),
(16, 'Dr. Karen', 'King', 'Radiologist'),
(17, 'Dr. Peter', 'Scott', 'Rheumatologist'),
(18, 'Dr. Emma', 'Harris', 'Nephrologist'),
(19, 'Dr. George', 'Martinez', 'Family Medicine'),
(20, 'Dr. Anna', 'Moore', 'Plastic Surgeon');

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `patient_id` int(11) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `gender` char(1) NOT NULL,
  `birth_date` date NOT NULL,
  `city` varchar(30) DEFAULT NULL,
  `province_id` char(2) DEFAULT NULL,
  `allergies` varchar(80) DEFAULT NULL,
  `height` int(11) NOT NULL,
  `weight` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`patient_id`, `first_name`, `last_name`, `gender`, `birth_date`, `city`, `province_id`, `allergies`, `height`, `weight`) VALUES
(1, 'Sophia', 'Williams', 'F', '1990-05-15', 'Jakarta', '31', 'Peanut', 165, 60),
(2, 'Liam', 'Brown', 'M', '1985-12-25', 'Bandung', '32', 'None', 175, 80),
(3, 'Olivia', 'Johnson', 'F', '1998-07-30', 'Surabaya', '35', 'Penicillin', 160, 55),
(4, 'Aiden', 'Martinez', 'M', '1982-03-13', 'Medan', '11', 'None', 180, 90),
(5, 'Emma', 'Garcia', 'F', '1995-02-07', 'Bali', '51', 'Dust', 150, 50),
(6, 'Noah', 'Lee', 'M', '1987-11-21', 'Yogyakarta', '34', 'None', 170, 75),
(7, 'Isabella', 'Perez', 'F', '1993-09-15', 'Semarang', '33', 'Latex', 155, 60),
(8, 'Lucas', 'Davis', 'M', '1990-01-30', 'Aceh', '11', 'None', 160, 70),
(9, 'Mason', 'Lopez', 'M', '2000-05-05', 'Palembang', '16', 'Shellfish', 168, 85),
(10, 'Amelia', 'Hernandez', 'F', '1997-08-20', 'Malang', '35', 'None', 162, 55),
(11, 'Ethan', 'Moore', 'M', '1991-04-03', 'Solo', '33', 'None', 173, 78),
(12, 'Mia', 'Jackson', 'F', '1988-10-10', 'Makassar', '73', 'Eggs', 162, 59),
(13, 'Alexander', 'Adams', 'M', '1999-02-17', 'Batam', '21', 'Peanuts', 178, 80),
(14, 'Charlotte', 'Wright', 'F', '1983-12-02', 'Denpasar', '51', 'None', 167, 70),
(15, 'Harper', 'Green', 'F', '1996-06-25', 'Surabaya', '35', 'Dust', 160, 65),
(16, 'Jack', 'Scott', 'M', '1992-01-01', 'Samarinda', '64', 'None', 185, 82),
(17, 'Amos', 'King', 'M', '1994-08-14', 'Pontianak', '61', 'None', 175, 68),
(18, 'Benjamin', 'Baker', 'M', '1989-11-11', 'Kendari', '76', 'None', 172, 77),
(19, 'Elijah', 'Nelson', 'M', '1980-02-25', 'Cirebon', '32', 'None', 180, 85),
(20, 'Zoe', 'Carter', 'F', '1992-03-13', 'Balikpapan', '64', 'None', 158, 52);

-- --------------------------------------------------------

--
-- Table structure for table `province_names`
--

CREATE TABLE `province_names` (
  `province_id` char(2) NOT NULL,
  `province_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `province_names`
--

INSERT INTO `province_names` (`province_id`, `province_name`) VALUES
('11', 'Aceh'),
('12', 'Sumatera Utara'),
('13', 'Sumatera Barat'),
('14', 'Riau'),
('15', 'Jambi'),
('16', 'Sumatera Selatan'),
('17', 'Bengkulu'),
('18', 'Lampung'),
('19', 'Kepulauan Bangka Belitung'),
('21', 'Kepulauan Riau'),
('31', 'DKI Jakarta'),
('32', 'Jawa Barat'),
('33', 'Jawa Tengah'),
('34', 'DI Yogyakarta'),
('35', 'Jawa Timur'),
('36', 'Banten'),
('51', 'Bali'),
('52', 'Nusa Tenggara Barat'),
('53', 'Nusa Tenggara Timur'),
('61', 'Kalimantan Barat'),
('62', 'Kalimantan Tengah'),
('63', 'Kalimantan Selatan'),
('64', 'Kalimantan Timur'),
('65', 'Kalimantan Utara'),
('71', 'Sulawesi Utara'),
('72', 'Sulawesi Tengah'),
('73', 'Sulawesi Selatan'),
('74', 'Sulawesi Tengara'),
('75', 'Gorontalo'),
('76', 'Sulawesi Barat'),
('81', 'Maluku'),
('82', 'Maluku Utara'),
('91', 'Papua Barat'),
('94', 'Papua');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admissions`
--
ALTER TABLE `admissions`
  ADD PRIMARY KEY (`patient_id`,`admission_date`),
  ADD KEY `attending_doctor_id` (`attending_doctor_id`);

--
-- Indexes for table `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`doctor_id`);

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`patient_id`),
  ADD KEY `province_id` (`province_id`);

--
-- Indexes for table `province_names`
--
ALTER TABLE `province_names`
  ADD PRIMARY KEY (`province_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

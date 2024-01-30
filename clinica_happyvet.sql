-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 12/12/2023 às 23:44
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `clinica_happyvet`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `consulta`
--

CREATE TABLE `consulta` (
  `id` int(11) NOT NULL,
  `data` datetime NOT NULL,
  `preco_consulta` float(11,0) NOT NULL,
  `animal_id` int(11) NOT NULL,
  `veterinario_id` int(11) NOT NULL,
  `tratamento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `consulta`
--

INSERT INTO `consulta` (`id`, `data`, `preco_consulta`, `animal_id`, `veterinario_id`, `tratamento_id`) VALUES
(3, '2023-12-10 20:41:12', 45, 1, 1, 3),
(4, '2023-12-12 00:21:16', 60, 3, 2, 4),
(5, '2023-12-12 21:53:00', 20, 1, 2, 3),
(6, '2023-12-12 22:00:00', 60, 2, 2, 1),
(7, '2023-10-10 22:17:00', 70, 1, 2, 6);

-- --------------------------------------------------------

--
-- Estrutura para tabela `pet`
--

CREATE TABLE `pet` (
  `id` int(11) NOT NULL,
  `tipo_animal` varchar(50) NOT NULL,
  `raca` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `pet`
--

INSERT INTO `pet` (`id`, `tipo_animal`, `raca`) VALUES
(1, 'Gato', 'Siamês'),
(2, 'Cachorro', 'Galgo Italiano'),
(4, 'Gato', 'Sphynx'),
(5, 'Cachorro', 'Vira-Lata'),
(6, 'Gato', 'Vira-lata');

-- --------------------------------------------------------

--
-- Estrutura para tabela `tratamento`
--

CREATE TABLE `tratamento` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `preco` float(11,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tratamento`
--

INSERT INTO `tratamento` (`id`, `nome`, `preco`) VALUES
(1, 'Vacinação', 50),
(2, 'Limpeza Oral', 40),
(3, 'Dermatologia', 45),
(4, 'Ortopedia', 60),
(5, 'Fisioterapia', 35),
(6, 'Parasitologia', 25),
(7, 'Consulta Emergência', 70),
(8, 'Consulta', 50);

-- --------------------------------------------------------

--
-- Estrutura para tabela `veterinario`
--

CREATE TABLE `veterinario` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `veterinario`
--

INSERT INTO `veterinario` (`id`, `nome`) VALUES
(2, 'Pedro Medonça'),
(3, 'Joaquina Cirilo de Almeida'),
(4, 'Joaquim alves'),
(5, 'Raquel Teófilo'),
(8, 'Maria Luisa Lucena');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `animal_id` (`animal_id`),
  ADD KEY `veterinario_id` (`veterinario_id`),
  ADD KEY `tratamento_id` (`tratamento_id`),
  ADD KEY `preco_consulta` (`preco_consulta`) USING BTREE;

--
-- Índices de tabela `pet`
--
ALTER TABLE `pet`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `tratamento`
--
ALTER TABLE `tratamento`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `veterinario`
--
ALTER TABLE `veterinario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `consulta`
--
ALTER TABLE `consulta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `pet`
--
ALTER TABLE `pet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `tratamento`
--
ALTER TABLE `tratamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `veterinario`
--
ALTER TABLE `veterinario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

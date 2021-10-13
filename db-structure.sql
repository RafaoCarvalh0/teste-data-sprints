CREATE TABLE `usuarios` (
  `id_usuario` bigint unsigned NOT NULL AUTO_INCREMENT,
  `apelido_usuario` varchar(15) DEFAULT NULL,
  `senha_usuario` longtext,
  `email_usuario` varchar(70) DEFAULT NULL,
  `nome_usuario` varchar(100) DEFAULT NULL,
  `idade_usuario` int DEFAULT NULL,
  `endereco_usuario` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `id_usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
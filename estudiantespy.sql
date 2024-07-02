-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-07-2024 a las 09:38:53
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `estudiantespy`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencias`
--

CREATE TABLE `asistencias` (
  `id_asistencia` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `fecha_asistencia` date NOT NULL,
  `asistencia` varchar(11) DEFAULT NULL,
  `falta` varchar(11) DEFAULT NULL,
  `tardanza` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asistencias`
--

INSERT INTO `asistencias` (`id_asistencia`, `id_estudiante`, `fecha_asistencia`, `asistencia`, `falta`, `tardanza`) VALUES
(47, 9, '2024-07-02', 'Presente', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificaciones`
--

CREATE TABLE `calificaciones` (
  `id_calificacion` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `calificacion_final` int(11) DEFAULT NULL,
  `calificacion_1A` int(11) DEFAULT NULL,
  `calificacion_2A` int(11) DEFAULT NULL,
  `calificacion_3A` int(11) DEFAULT NULL,
  `calificacion_4A` int(11) DEFAULT NULL,
  `calificacion_1B` int(11) DEFAULT NULL,
  `calificacion_2B` int(11) DEFAULT NULL,
  `calificacion_3B` int(11) DEFAULT NULL,
  `calificacion_4B` int(11) DEFAULT NULL,
  `calificacion_1C` int(11) DEFAULT NULL,
  `calificacion_2C` int(11) DEFAULT NULL,
  `calificacion_3C` int(11) DEFAULT NULL,
  `calificacion_4C` int(11) DEFAULT NULL,
  `calificacion_1D` int(11) DEFAULT NULL,
  `calificacion_2D` int(11) DEFAULT NULL,
  `calificacion_3D` int(11) DEFAULT NULL,
  `calificacion_4D` int(11) DEFAULT NULL,
  `promedio1` decimal(5,2) DEFAULT NULL,
  `promedio2` decimal(5,2) DEFAULT NULL,
  `promedio3` decimal(5,2) DEFAULT NULL,
  `promedio4` decimal(5,2) DEFAULT NULL,
  `promedio_total` decimal(10,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `calificaciones`
--

INSERT INTO `calificaciones` (`id_calificacion`, `id_estudiante`, `id_curso`, `calificacion_final`, `calificacion_1A`, `calificacion_2A`, `calificacion_3A`, `calificacion_4A`, `calificacion_1B`, `calificacion_2B`, `calificacion_3B`, `calificacion_4B`, `calificacion_1C`, `calificacion_2C`, `calificacion_3C`, `calificacion_4C`, `calificacion_1D`, `calificacion_2D`, `calificacion_3D`, `calificacion_4D`, `promedio1`, `promedio2`, `promedio3`, `promedio4`, `promedio_total`) VALUES
(15, 9, 141, 78, 1, 88, 84, 87, 83, 86, 82, 85, 81, 84, 80, 83, 79, 82, 78, 81, 61.00, 85.00, 81.00, 84.00, 77.75),
(16, 8, 137, 92, 8, 94, 91, 93, 89, 93, 90, 92, 88, 92, 89, 91, 87, 91, 88, 90, 68.00, 92.50, 89.50, 91.50, 85.38),
(17, 7, 127, 87, 84, 90, 86, 88, 83, 89, 85, 87, 82, 88, 84, 86, 81, 87, 83, 85, 86.25, 86.25, 86.25, 86.25, 86.25),
(18, 9, 144, 80, 1, 82, 79, 81, 76, 81, 78, 80, 75, 80, 77, 79, 74, 79, 76, 78, 56.50, 80.50, 77.50, 79.50, 73.50),
(19, 8, 135, 91, 89, 93, 90, 92, 88, 92, 89, 91, 87, 91, 88, 90, 86, 90, 87, 89, 90.25, 90.25, 90.25, 90.25, 90.25),
(20, 7, 130, 89, 86, 92, 88, 90, 85, 90, 87, 89, 84, 89, 86, 88, 83, 88, 85, 87, 87.25, 87.25, 87.25, 87.25, 87.25),
(21, 9, 147, 82, 1, 84, 81, 83, 78, 83, 80, 82, 77, 82, 79, 81, 76, 81, 78, 80, 58.00, 82.50, 79.50, 81.50, 75.38),
(22, 8, 138, 93, 91, 95, 92, 94, 90, 94, 91, 93, 89, 93, 90, 92, 88, 92, 89, 91, 91.25, 91.25, 91.25, 91.25, 91.25),
(23, 7, 125, 86, 83, 89, 85, 88, 84, 89, 86, 88, 83, 88, 85, 87, 82, 87, 84, 86, 86.50, 86.50, 86.50, 86.50, 86.50),
(24, 9, 146, 79, 1, 81, 78, 82, 77, 82, 79, 81, 76, 81, 78, 80, 75, 80, 77, 79, 57.25, 81.00, 78.00, 80.50, 74.19),
(25, 8, 132, 90, 88, 92, 89, 91, 87, 91, 88, 90, 86, 90, 87, 89, 85, 89, 86, 88, 89.00, 89.00, 89.00, 89.00, 89.00),
(26, 7, 124, 88, 85, 90, 87, 89, 82, 87, 84, 86, 81, 86, 83, 85, 80, 85, 82, 84, 86.25, 86.25, 86.25, 86.25, 86.25),
(27, 9, 142, 80, 1, 82, 79, 81, 75, 80, 77, 79, 74, 79, 76, 78, 73, 78, 75, 77, 55.75, 79.75, 76.75, 78.75, 72.75),
(28, 7, 131, 90, 88, 92, 89, 91, 87, 91, 88, 90, 86, 90, 87, 89, 85, 89, 86, 88, 89.00, 89.00, 89.00, 89.00, 89.00),
(29, 7, 123, 85, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 13, 20, 20, 20, 18.25, 20.00, 20.00, 20.00, 19.56),
(30, 9, 69, 78, 1, 80, 77, 82, 74, 79, 76, 81, 73, 78, 75, 80, 72, 77, 74, 79, 55.00, 78.50, 75.50, 80.50, 72.38),
(31, 8, 136, 92, 1, 94, 91, 93, 89, 93, 90, 92, 88, 92, 89, 91, 87, 91, 88, 90, 66.25, 92.50, 89.50, 91.50, 84.94),
(32, 7, 129, 87, 84, 90, 86, 88, 83, 89, 85, 87, 82, 88, 84, 86, 81, 87, 83, 85, 86.25, 86.25, 86.25, 86.25, 86.25),
(33, 9, 143, 80, 1, 82, 79, 81, 76, 81, 78, 80, 75, 80, 77, 79, 74, 79, 76, 78, 56.50, 80.50, 77.50, 79.50, 73.50),
(34, 8, 134, 91, 89, 93, 90, 92, 88, 92, 89, 91, 87, 91, 88, 90, 86, 90, 87, 89, 90.25, 90.25, 90.25, 90.25, 90.25),
(35, 7, 128, 89, 86, 92, 88, 90, 85, 90, 87, 89, 84, 89, 86, 88, 83, 88, 85, 87, 87.25, 87.25, 87.25, 87.25, 87.25),
(36, 9, 148, 82, 1, 84, 81, 83, 78, 83, 80, 82, 77, 82, 79, 81, 76, 81, 78, 80, 58.00, 82.50, 79.50, 81.50, 75.38),
(37, 8, 140, 93, 91, 95, 92, 94, 90, 94, 91, 93, 89, 93, 90, 92, 88, 92, 89, 91, 89.50, 93.50, 90.50, 92.50, 91.50),
(38, 7, 126, 86, 83, 89, 85, 88, 84, 89, 86, 88, 83, 88, 85, 87, 82, 87, 84, 86, 86.50, 86.50, 86.50, 86.50, 86.50),
(39, 9, 145, 79, 1, 81, 78, 82, 77, 82, 79, 81, 76, 81, 78, 80, 75, 80, 77, 79, 57.25, 81.00, 78.00, 80.50, 74.19),
(40, 8, 133, 90, 88, 92, 89, 91, 87, 91, 88, 90, 86, 90, 87, 89, 85, 89, 86, 88, 89.00, 89.00, 89.00, 89.00, 89.00),
(41, 8, 139, 89, 86, 91, 88, 90, 85, 90, 87, 89, 84, 89, 86, 88, 83, 88, 85, 87, 84.50, 89.50, 86.50, 88.50, 87.25);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE `cursos` (
  `id_curso` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `id_profesor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`id_curso`, `nombre`, `descripcion`, `id_estudiante`, `id_profesor`) VALUES
(69, 'Matemáticas Básicas', 'Curso introductorio a las matemáticas', 9, 101),
(70, 'Ciencias Naturales', 'Estudio de la naturaleza y sus fenómenos', 1, 102),
(71, 'Lengua y Literatura', 'Estudio de la lengua y sus manifestaciones literarias', 1, 103),
(72, 'Historia Universal', 'Estudio de los eventos históricos a nivel global', 1, 104),
(73, 'Educación Física', 'Curso de actividades físicas y deportivas', 1, 105),
(74, 'Arte y Música', 'Curso de apreciación y expresión artística', 1, 106),
(75, 'Tecnología e Informática', 'Introducción a la tecnología y la informática', 1, 107),
(76, 'Ciencias Sociales', 'Estudio de las interacciones humanas en sociedad', 1, 108),
(77, 'Inglés Básico', 'Curso introductorio al idioma inglés', 1, 109),
(78, 'Geometría Avanzada', 'Curso avanzado de geometría', 2, 201),
(79, 'Biología Celular', 'Estudio avanzado de la biología celular', 2, 202),
(80, 'Literatura Clásica', 'Estudio de obras literarias clásicas', 2, 203),
(81, 'Historia del Arte', 'Estudio de los movimientos artísticos históricos', 2, 204),
(82, 'Deportes Avanzados', 'Curso de práctica deportiva avanzada', 2, 205),
(83, 'Música Instrumental', 'Curso avanzado de música instrumental', 2, 206),
(84, 'Programación Avanzada', 'Desarrollo de habilidades en programación', 2, 207),
(85, 'Ciencias Políticas', 'Estudio de sistemas políticos y su funcionamiento', 2, 208),
(86, 'Inglés Avanzado', 'Curso avanzado de inglés', 2, 209),
(87, 'Álgebra Lineal', 'Curso avanzado de álgebra', 3, 301),
(88, 'Ecología y Medio Ambiente', 'Estudio del entorno natural y sus problemas', 3, 302),
(89, 'Literatura Contemporánea', 'Estudio de la literatura contemporánea', 3, 303),
(90, 'Historia del Mundo Moderno', 'Estudio de los eventos históricos del mundo moderno', 3, 304),
(91, 'Atletismo', 'Curso de atletismo y habilidades físicas', 3, 305),
(92, 'Danza y Expresión Corporal', 'Curso de danza y expresión corporal', 3, 306),
(93, 'Desarrollo Web', 'Introducción al desarrollo web', 3, 307),
(94, 'Economía y Finanzas', 'Estudio de conceptos económicos y financieros', 3, 308),
(95, 'Inglés para Negocios', 'Curso de inglés orientado a negocios', 3, 309),
(96, 'Física Avanzada', 'Estudio avanzado de la física y sus leyes', 4, 401),
(97, 'Química Orgánica', 'Estudio de compuestos orgánicos y sus propiedades', 4, 402),
(98, 'Literatura Latinoamericana', 'Estudio de la literatura de América Latina', 4, 403),
(99, 'Historia Antigua', 'Estudio de la historia de civilizaciones antiguas', 4, 404),
(100, 'Baloncesto Avanzado', 'Curso avanzado de habilidades en baloncesto', 4, 405),
(101, 'Teatro y Actuación', 'Curso de teatro y técnicas de actuación', 4, 406),
(102, 'Bases de Datos', 'Introducción a las bases de datos', 4, 407),
(103, 'Psicología', 'Estudio de los procesos mentales y comportamientos', 4, 408),
(104, 'Inglés Académico', 'Curso de inglés orientado a estudios académicos', 4, 409),
(105, 'Cálculo Avanzado', 'Estudio avanzado de cálculo matemático', 5, 501),
(106, 'Biología Molecular', 'Estudio de la biología a nivel molecular', 5, 502),
(107, 'Literatura Española', 'Estudio de la literatura española', 5, 503),
(108, 'Historia Medieval', 'Estudio de la historia medieval europea', 5, 504),
(109, 'Natación Avanzada', 'Curso avanzado de técnicas de natación', 5, 505),
(110, 'Arte Dramático', 'Curso de técnicas de arte dramático', 5, 506),
(111, 'Desarrollo de Aplicaciones Móviles', 'Introducción al desarrollo de apps móviles', 5, 507),
(112, 'Sociología', 'Estudio de la sociedad y sus estructuras', 5, 508),
(113, 'Inglés para Viajes', 'Curso de inglés para viajar y turismo', 5, 509),
(114, 'Estadística Avanzada', 'Estudio avanzado de estadística aplicada', 6, 601),
(115, 'Ecología Avanzada', 'Estudio avanzado de ecología y medio ambiente', 6, 602),
(116, 'Literatura Universal', 'Estudio de la literatura mundial', 6, 603),
(117, 'Historia del Arte Contemporáneo', 'Estudio del arte contemporáneo', 6, 604),
(118, 'Gimnasia Olímpica', 'Curso de técnicas de gimnasia olímpica', 6, 605),
(119, 'Música Vocal', 'Curso de técnica vocal y canto', 6, 606),
(120, 'Inteligencia Artificial', 'Introducción a la inteligencia artificial', 6, 607),
(121, 'Antropología', 'Estudio de la cultura y la evolución humana', 6, 608),
(122, 'Inglés de Negocios Internacionales', 'Curso de inglés para negocios internacionales', 6, 609),
(123, 'Álgebra Abstracta', 'Estudio avanzado de álgebra abstracta', 7, 701),
(124, 'Geología Avanzada', 'Estudio avanzado de geología y minerales', 7, 702),
(125, 'Literatura Inglesa', 'Estudio de la literatura inglesa', 7, 703),
(126, 'Historia del Renacimiento', 'Estudio del renacimiento europeo', 7, 704),
(127, 'Voleibol Avanzado', 'Curso avanzado de habilidades en voleibol', 7, 705),
(128, 'Danza Contemporánea', 'Curso de danza contemporánea', 7, 706),
(129, 'Desarrollo Web Avanzado', 'Desarrollo avanzado de aplicaciones web', 7, 707),
(130, 'Filosofía', 'Estudio de las ideas y el pensamiento filosófico', 7, 708),
(131, 'Inglés Jurídico', 'Curso de inglés para el ámbito legal', 7, 709),
(132, 'Geometría Diferencial', 'Estudio avanzado de geometría diferencial', 8, 801),
(133, 'Biología Evolutiva', 'Estudio de la biología evolutiva', 8, 802),
(134, 'Literatura Francesa', 'Estudio de la literatura francesa', 8, 803),
(135, 'Historia del Siglo XX', 'Estudio de la historia del siglo XX', 8, 804),
(136, 'Atletismo Olímpico', 'Curso de técnicas avanzadas de atletismo', 8, 805),
(137, 'Música Orquestal', 'Curso de música orquestal', 8, 806),
(138, 'Seguridad Informática', 'Introducción a la seguridad informática', 8, 807),
(139, 'Psiquiatría', 'Estudio de los trastornos mentales y su tratamiento', 8, 808),
(140, 'Inglés Científico', 'Curso de inglés para el ámbito científico', 8, 809),
(141, 'Topología Algebraica', 'Estudio avanzado de topología algebraica', 9, 901),
(142, 'Ecología Marítima', 'Estudio de la ecología marina', 9, 902),
(143, 'Literatura Alemana', 'Estudio de la literatura alemana', 9, 903),
(144, 'Historia del Arte Oriental', 'Estudio del arte oriental', 9, 904),
(145, 'Béisbol Avanzado', 'Curso avanzado de habilidades en béisbol', 9, 905),
(146, 'Arte Contemporáneo', 'Estudio del arte contemporáneo', 9, 906),
(147, 'Desarrollo de Videojuegos', 'Introducción al desarrollo de videojuegos', 9, 907),
(148, 'Economía Internacional', 'Estudio de la economía a nivel internacional', 9, 908),
(149, 'Inglés Avanzado para Profesionales', 'Curso de inglés avanzado para profesionales', 9, 909);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id_estudiante` int(11) NOT NULL,
  `dni` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `edad` varchar(100) DEFAULT NULL,
  `año_de_ingreso` int(11) NOT NULL,
  `grado` varchar(50) NOT NULL,
  `seccion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id_estudiante`, `dni`, `nombre`, `apellido`, `edad`, `año_de_ingreso`, `grado`, `seccion`) VALUES
(7, 123456789, 'Juan', 'Pérez', '18', 2020, '2 Secundaria', 'A'),
(8, 987654321, 'María', 'Gómez', '17', 2019, 'Secundaria', 'B'),
(9, 456789123, 'Pedro', 'Sánchez', '16', 2021, 'Primaria', 'C');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `id_profesor` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `curso` varchar(100) NOT NULL,
  `codigo` int(11) NOT NULL,
  `Contrasena` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`id_profesor`, `nombre`, `curso`, `codigo`, `Contrasena`) VALUES
(1, 'Nombre del Profesor', 'Curso del Profesor', 12345, '123'),
(2, 'Ana Martinez', 'Matemáticas', 1001, '123'),
(3, 'camasca dummar', 'algoritmos', 12, '123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD PRIMARY KEY (`id_asistencia`),
  ADD KEY `id_estudiante` (`id_estudiante`);

--
-- Indices de la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD PRIMARY KEY (`id_calificacion`),
  ADD KEY `fk_calificaciones_estudiante` (`id_estudiante`),
  ADD KEY `fk_calificaciones_curso` (`id_curso`);

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id_curso`),
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `fk_profesor` (`id_profesor`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id_estudiante`),
  ADD UNIQUE KEY `dni` (`dni`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`id_profesor`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  MODIFY `id_asistencia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT de la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  MODIFY `id_calificacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id_curso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=150;

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id_estudiante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `profesores`
--
ALTER TABLE `profesores`
  MODIFY `id_profesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD CONSTRAINT `asistencias_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`);

--
-- Filtros para la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD CONSTRAINT `fk_calificaciones_curso` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`),
  ADD CONSTRAINT `fk_calificaciones_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

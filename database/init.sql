DROP TABLE IF EXISTS frequencia CASCADE;
DROP TABLE IF EXISTS notas CASCADE;
DROP TABLE IF EXISTS avaliacoes CASCADE;
DROP TABLE IF EXISTS matriculas CASCADE;
DROP TABLE IF EXISTS disciplinas CASCADE;
DROP TABLE IF EXISTS estudantes CASCADE;

CREATE TABLE estudantes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);

CREATE TABLE disciplinas (
    codigo VARCHAR(10) PRIMARY KEY, -- Ex: "LP101"
    nome VARCHAR(100) NOT NULL,
    aulas_planejadas INT,
    aulas_ministradas INT
);

CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    estudante_id INT REFERENCES estudantes(id),
    disciplina_codigo VARCHAR(20) REFERENCES disciplinas(codigo),
    semestre VARCHAR(10) NOT NULL, -- Ex: "2026.1", "2026.2"
    situacao VARCHAR(30) -- Ex: "Cursando"
);

CREATE TABLE avaliacoes (
    id SERIAL PRIMARY KEY,
    disciplina_codigo VARCHAR(20) REFERENCES disciplinas(codigo),
    titulo VARCHAR(50) NOT NULL, -- Ex: "AV1N1"
    escala_maxima INT
);

CREATE TABLE notas (
    id SERIAL PRIMARY KEY,
    avaliacao_id INT REFERENCES avaliacoes(id),
    estudante_id INT REFERENCES estudantes(id),
    valor NUMERIC(5,2) -- Deixei ser NULL e aceitar valores esquisitos propositalmente 
);

CREATE TABLE frequencia (
    id SERIAL PRIMARY KEY,
    estudante_id INT REFERENCES estudantes(id),
    disciplina_codigo VARCHAR(10) REFERENCES disciplinas(codigo),
    aulas_presente INT
);

INSERT INTO estudantes (nome, email) VALUES 
('Alana Margarida', 'alana@aluno.ifce.edu.br'),
('Antônio Vinicius', 'vinicius@aluno.ifce.edu.br'),
('Gustavo Rodrigues', 'gustavo@aluno.ifce.edu.br'),
('Iure Diniz', 'iure@aluno.ifce.edu.br'),
('João Victor', NULL);

INSERT INTO disciplinas (codigo, nome, aulas_planejadas, aulas_ministradas) VALUES 
('CC101', 'Sistemas Distribuídos', 40, 30),
('CC102', 'Inteligência Artificial', 50, 40),
('CC103', 'Libras', 30, 20);

INSERT INTO matriculas (estudante_id, disciplina_codigo, semestre, situacao) VALUES 
(1, 'CC101', '2026.1', 'CURSANDO'),
(1, 'CC102', '2026.1', NULL),
(1, 'CC103', '2026.1', 'CURSANDO'),
(2, 'CC101', '2026.1', 'CURSANDO'),
(2, 'CC102', '2026.1', 'CURSANDO'),
(2, 'CC103', '2026.1', 'CURSANDO'),
(3, 'CC101', '2026.1', NULL),
(3, 'CC102', '2026.1', 'CURSANDO'),
(3, 'CC103', '2026.1', NULL),
(4, 'CC101', '2026.1', 'CURSANDO'),
(4, 'CC102', '2026.1', 'CURSANDO'),
(4, 'CC103', '2026.1', NULL),
(5, 'CC101', '2026.1', 'CURSANDO'),
(5, 'CC102', '2026.1', 'CURSANDO'),
(5, 'CC103', '2026.1', 'CURSANDO');

INSERT INTO avaliacoes (disciplina_codigo, titulo, escala_maxima) VALUES 
('CC101', 'AV1N1', 10),
('CC102', 'Seminário', 10),
('CC103', 'Trabalho Avaliativo', 100);

INSERT INTO notas (avaliacao_id, estudante_id, valor) VALUES 
(1, 1, 8.5),   
(2, 1, 9.0),
(3, 1, 57.5),    
(1, 2, 4.5),   
(2, 2, 10.0),
(3, 2, 79.0),
(1, 3, 7.0),
(2, 3, 9.5),      
(3, 3, 85.0),  
(1, 4, NULL),
(2, 4, NULL),
(3, 4, 99.5),  
(1, 5, 3.5),
(2, 5, 10.0),  
(3, 5, 92.7);  

INSERT INTO frequencia (estudante_id, disciplina_codigo, aulas_presente) VALUES 
(1, 'CC101', 25),
(1, 'CC102', 35),
(1, 'CC103', NULL),
(2, 'CC101', 25),
(2, 'CC102', 30),
(2, 'CC103', 18), 
(3, 'CC101', 27),
(3, 'CC102', 39),
(3, 'CC103', 19),
(4, 'CC101', 29),
(4, 'CC102', NULL),
(4, 'CC103', 15),
(5, 'CC101', 15),
(5, 'CC102', 20),
(5, 'CC103', 20);
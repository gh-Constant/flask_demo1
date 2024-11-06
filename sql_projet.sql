-- Connect to MySQL as root first
DROP TABLE IF EXISTS etudiant;
CREATE TABLE etudiant (
id_etudiant INT AUTO_INCREMENT
, nom_etudiant VARCHAR(255)
, groupe_etudiant VARCHAR(255)
, PRIMARY KEY(id_etudiant)
);

INSERT INTO etudiant (id_etudiant, nom_etudiant, groupe_etudiant) 
VALUES
(NULL, 'tom','A1'),
(NULL, 'enzo','A1'),
(NULL, 'laurence','A2'),
(NULL, 'theo','A2'),
(NULL, 'theo','B1')
;


SELECT id_etudiant AS id, nom_etudiant AS nom, groupe_etudiant AS groupe
FROM etudiant
ORDER BY nom;

INSERT INTO etudiant(id_etudiant, nom_etudiant, groupe_etudiant) VALUES (NULL, 'test1', 'test1');

DELETE FROM etudiant WHERE id_etudiant=2;

UPDATE etudiant SET nom_etudiant = 'test2', groupe_etudiant= 'test3' WHERE id_etudiant=3;
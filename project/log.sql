CREATE TABLE `db_tennis`.`adherants` (
  `adherant_id` INT NOT NULL AUTO_INCREMENT,
  `prenom` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `age` INT(3) NOT NULL,
  `tel` INT NOT NULL,
  `adresse` VARCHAR(500) NOT NULL,
  `ville` VARCHAR(45) NOT NULL,
  `zip` INT(5) NOT NULL,
  `date_naissance` DATE NOT NULL,
  `sexe` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`adherant_id`),
  UNIQUE INDEX `tel_UNIQUE` (`tel` ASC) VISIBLE);

ALTER TABLE `db_tennis`.`adherants` 
ADD COLUMN `email` VARCHAR(60) NOT NULL AFTER `tel`,
CHANGE COLUMN `ville` `ville` VARCHAR(25) NOT NULL ,
ADD UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE;
;
ALTER TABLE `db_tennis`.`adherants` 
ADD COLUMN `date_inscription` DATETIME NOT NULL AFTER `sexe`,
CHANGE COLUMN `tel` `tel` VARCHAR(10) NOT NULL ;


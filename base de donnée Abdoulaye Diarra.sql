
CREATE SCHEMA IF NOT EXISTS `hotellerie` DEFAULT CHARACTER SET utf8 ;
USE `hotellerie` ;

CREATE TABLE IF NOT EXISTS `hotellerie`.`chambre` (
  `Num` INT NOT NULL,
  `Disponibilite` ENUM('Libre', 'Occupee') NULL,
  `Niveau` INT NULL,
  PRIMARY KEY (`Num`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `hotellerie`.`hotel` (
  `Nom` VARCHAR(45) NULL,
  `Nbre_niveau` INT NULL,
  `Nbre_chambre` INT NULL,
  `Adresse` VARCHAR(45) NULL,
  `Tel` VARCHAR(45) NULL,
  `Nbre_etoiles` ENUM('1', '2', '3', '4', '5') NULL)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `hotellerie`.`client` (
  `Id_client` INT NOT NULL,
  `Prenom_client` VARCHAR(45) NULL,
  `Nom_client` VARCHAR(45) NULL,
  `Telephone_client` VARCHAR(45) NULL,
  PRIMARY KEY (`Id_client`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `hotellerie`.`facture` (
  `Id_facture` INT NOT NULL,
  `Tarif_chambre` INT NULL,
  `Tarif_services` INT NULL,
  `Total` INT NULL,
  PRIMARY KEY (`Id_facture`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `hotellerie`.`reservation` (
  `Id_reserv` INT NOT NULL,
  `Date_reserv` DATE NULL,
  `Date_entree` DATE NULL,
  `Date_sortie` DATE NULL,
  `Nuitee` INT NULL,
  PRIMARY KEY (`Id_reserv`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `hotellerie`.`services` (
  `Nom_service` ENUM('Petit dejeuner', 'Bar', 'Telephone') NULL,
  `Tarif_service` INT NULL)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `hotellerie`.`categorie` (
  `Classe` ENUM('Economique', 'Standing', 'Affaire') NULL,
  `Type_tarif` ENUM('Normal', 'Special') NULL)
ENGINE = InnoDB;



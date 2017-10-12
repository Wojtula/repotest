CREATE TABLE premia(
    id VARCHAR(20) PRIMARY KEY,
    premia NUMERIC,
    );
    
    
CREATE TABLE dzial(
    id INTEGER PRIMARY KEY,
    nazwa VARCHAR(40),
    siedziba VARCHAR(40),
    );
    
CREATE TABLE pracownicy(
    id VARCHAR(6) PRIMARY KEY,
    nazwiskoVARCHAR(40),
    imie VARCHAR(40),
    stanowisko VARCHAR(40),
    data_zatr VARCHAR(23),
    płaca NUMERIC,
    premia NUMERIC,
    id_dzial INTEGER,
    FOREIGN KEY(stanowisko) REPERENCES premia(id),
    FOREIGN KEY(id_dzial) REPERENCES dzial(id),
    );

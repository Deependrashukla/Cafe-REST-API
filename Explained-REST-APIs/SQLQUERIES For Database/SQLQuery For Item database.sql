SELECT @@SERVERNAME
use cafe;
CREATE TABLE item(
    id autoincrement,
    name varchar(50),
    price int,
    PRIMARY KEY (id)
	)

select * from item


INSERT INTO item (id, price, name) VALUES('aaaa', 60, 'tomato');
INSERT INTO item (id, price, name) VALUES('bbbb', 50, 'potato');

UPDATE item set price = 30, name = 'soup' where id = 'aaaa';

DROP TABLE item;




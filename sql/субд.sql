CREATE DATABASE usersdb;

USE usersdb;
CREATE TABLE users (
    id INTEGER AUTO_INCREMENT PRIMARY KEY, 
    firstname VARCHAR(30), 
    age INTEGER
);
INSERT INTO users (firstname, age) VALUES ('Tom', 34);

USE usersdb;
SELECT * FROM users;

DROP DATABASE productsdb;

CREATE DATABASE productsdb;
 
USE productsdb;
 
CREATE TABLE Customers
(
    Id INT, -- 
    Age INT,
    FirstName VARCHAR(20),
    LastName VARCHAR(20)
);

RENAME TABLE Customers TO Clients;

TRUNCATE TABLE Clients;

DROP TABLE Clients;

USE productsdb;
 
CREATE TABLE Customers
(
    Id INT PRIMARY KEY, -- Первичный ключ уникально идентифицирует строку в таблице 
    Age INT,
    FirstName VARCHAR(20),
    LastName VARCHAR(20)
);

CREATE TABLE Customers
(
    Id INT PRIMARY KEY AUTO_INCREMENT, -- позволяет указать, что значение столбца будет автоматически увеличиваться при добавлении новой строки. Данный атрибут работает для столбцов, которые представляют целочисленный тип или числа с плавающей точкой.
    Age INT,
    FirstName VARCHAR(20),
    LastName VARCHAR(20)
);

CREATE TABLE Customers
(
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Age INT,
    FirstName VARCHAR(20),
    LastName VARCHAR(20),
    Phone VARCHAR(13) UNIQUE -- указывает, что столбец может хранить только уникальные значения.
);


CREATE TABLE Customers
(
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Age INT,
    FirstName VARCHAR(20) NOT NULL,-- null и not null это атрибуты задающие условия, null это атрибут который не требует обязательного заполнения, а not null наоборот обязателен!
    LastName VARCHAR(20) NOT NULL,
    Email VARCHAR(30) NULL,
    Phone VARCHAR(20) NULL
);

CREATE TABLE Customers
(
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Age INT DEFAULT 18, -- атрибут default задает значение по умолчанию
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Email VARCHAR(30) NOT NULL UNIQUE,
    Phone VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE Customers
(
    Id INT AUTO_INCREMENT,
    Age INT DEFAULT 18 CHECK(Age >0 AND Age < 100), -- Атрибут CHECK задает ограничение для диапазона значений, которые могут храниться в столбце.
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Email VARCHAR(30) CHECK(Email !=''),
    Phone VARCHAR(20) CHECK(Phone !='')
)


CREATE TABLE Customers
(
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Age INT, 
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Phone VARCHAR(20) NOT NULL UNIQUE
);
 
CREATE TABLE Orders
(
    Id INT PRIMARY KEY AUTO_INCREMENT,
    CustomerId INT,
    CreatedAt Date,
    FOREIGN KEY (CustomerId)  REFERENCES Customers (Id) -- Foreign key используется для соединения с таблицами,А после ключевого слова REFERENCES указывается имя связанной таблицы, а затем в скобках имя связанного столбца, на который будет указывать внешний ключ.
);

ALTER TABLE Customers
ADD Address VARCHAR(50) NULL -- добавление альтернативного столбца

ALTER TABLE Customers
DROP COLUMN Address; -- удаление его

CREATE DATABASE productsdb;
USE productsdb;
CREATE TABLE Products
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Manufacturer VARCHAR(20) NOT NULL,
    ProductCount INT DEFAULT 0,
    Price DECIMAL NOT NULL
);

INSERT Products(ProductName, Manufacturer, ProductCount, Price) 
VALUES ('iPhone X', 'Apple', 5, 76000);

INSERT Products(ProductName, Manufacturer, Price) 
VALUES ('Galaxy S9', 'Samsung', 63000);

INSERT Products(ProductName, Manufacturer, Price, ProductCount) 
VALUES ('Nokia 9', 'HDM Global', 41000, DEFAULT);

INSERT Products(ProductName, Manufacturer, Price, ProductCount) 
VALUES ('Nokia 9', 'HDM Global', 41000, NULL);

INSERT Products(ProductName, Manufacturer, Price, ProductCount) 
VALUES
('iPhone 8', 'Apple', 51000, 3),
('P20 Lite', 'Huawei', 34000, 4),
('Galaxy S8', 'Samsung', 46000, 2);


CREATE TABLE Products
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Manufacturer VARCHAR(20) NOT NULL,
    ProductCount INT DEFAULT 0,
    Price DECIMAL
);
  
INSERT INTO Products (ProductName, Manufacturer, ProductCount, Price)
VALUES
('iPhone X', 'Apple', 3, 76000),
('iPhone 8', 'Apple', 2, 51000),
('Galaxy S9', 'Samsung', 2, 56000),
('Galaxy S8', 'Samsung', 1, 41000),
('P20 Pro', 'Huawei', 5, 36000);

SELECT * FROM Products;

SELECT ProductName AS Title, Price * ProductCount AS TotalSum
FROM Products;

SELECT * FROM Products
WHERE Manufacturer = 'Samsung';

SELECT * FROM Products
WHERE ProductCount < 3;

SELECT * FROM Products
WHERE Price * ProductCount > 100000;


SELECT * FROM Products
WHERE Manufacturer = 'Samsung' AND Price > 50000

UPDATE Products
SET Price = Price + 3000;

UPDATE Products
SET Manufacturer = 'Samsung Inc.'
WHERE Manufacturer = 'Samsung';


UPDATE Products
SET Manufacturer = 'Samsung',
    ProductCount = ProductCount + 3
WHERE Manufacturer = 'Samsung Inc.';

UPDATE Products
SET ProductCount= DEFAULT
WHERE Manufacturer = 'Huawei';

DELETE FROM Products
WHERE Manufacturer='Huawei';

DELETE FROM Products
WHERE Manufacturer='Apple' AND Price < 60000;

DELETE FROM Products;

SELECT DISTINCT Manufacturer, ProductCount FROM Products;

SELECT * FROM Products
WHERE Price BETWEEN 20000 AND 50000;

SELECT * FROM Products
WHERE ProductName LIKE 'iPhone%';




SELECT * FROM Products
WHERE ProductName REGEXP 'Phone|Galaxy';

SELECT * FROM Products
WHERE ProductCount IS NULL;


SELECT ProductName, ProductCount
FROM Products
ORDER BY ProductCount DESC; -- сортировка по убыванию

SELECT ProductName, Price, Manufacturer
FROM Products
ORDER BY Manufacturer ASC, ProductName DESC;

	
SELECT AVG(Price) AS Average_Price FROM Products -- среднее значение

SELECT MIN(Price), MAX(Price) FROM Products -- минимальное и максимальное

SELECT SUM(ProductCount * Price) FROM Products -- сумма всех телефонов 

SELECT COUNT(*) AS ProdCount,
       SUM(ProductCount) AS TotalCount,
       MIN(Price) AS MinPrice,
       MAX(Price) AS MaxPrice,
       AVG(Price) AS AvgPrice
FROM Products



drop table orders
drop table products
drop table customers
CREATE TABLE Products
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Manufacturer VARCHAR(20) NOT NULL,
    ProductCount INT DEFAULT 0,
    Price DECIMAL NOT NULL
);
CREATE TABLE Orders
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductId INT NOT NULL,
    ProductCount INT DEFAULT 1,
    CreatedAt DATE NOT NULL,
    Price DECIMAL NOT NULL,
    FOREIGN KEY (ProductId) REFERENCES Products(Id) ON DELETE CASCADE
);

INSERT INTO Products (ProductName, Manufacturer, ProductCount, Price)
VALUES ('iPhone X', 'Apple', 2, 76000),
('iPhone 8', 'Apple', 2, 51000),
('iPhone 7', 'Apple', 5, 42000),
('Galaxy S9', 'Samsung', 2, 56000),
('Galaxy S8', 'Samsung', 1, 46000),
('Honor 10', 'Huawei', 2, 26000),
('Nokia 8', 'HMD Global', 6, 38000);
 
INSERT INTO Orders (ProductId, CreatedAt, ProductCount, Price)
VALUES
( 
    (SELECT Id FROM Products WHERE ProductName='Galaxy S8'),
    '2018-05-21', 
    2, 
    (SELECT Price FROM Products WHERE ProductName='Galaxy S8')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone X'),
    '2018-05-23',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone X')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone 8'),
    '2018-05-21',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone 8')
);

SELECT  CreatedAt, Price, 
        (SELECT ProductName FROM Products 
        WHERE Products.Id = Orders.ProductId) AS Product
FROM Orders;

SELECT * FROM Products
WHERE EXISTS 
(SELECT * FROM Orders WHERE Orders.ProductId = Products.Id)



CREATE TABLE Products
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Manufacturer VARCHAR(20) NOT NULL,
    ProductCount INT DEFAULT 0,
    Price DECIMAL NOT NULL
);
CREATE TABLE Customers
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL
);
CREATE TABLE Orders
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    ProductId INT NOT NULL,
    CustomerId INT NOT NULL,
    CreatedAt DATE NOT NULL,
    ProductCount INT DEFAULT 1,
    Price DECIMAL NOT NULL,
    FOREIGN KEY (ProductId) REFERENCES Products(Id) ON DELETE CASCADE,
    FOREIGN KEY (CustomerId) REFERENCES Customers(Id) ON DELETE CASCADE
);
INSERT INTO Products (ProductName, Manufacturer, ProductCount, Price)
VALUES ('iPhone X', 'Apple', 2, 76000),
('iPhone 8', 'Apple', 2, 51000),
('iPhone 7', 'Apple', 5, 42000),
('Galaxy S9', 'Samsung', 2, 56000),
('Galaxy S8', 'Samsung', 1, 46000),
('Honor 10', 'Huawei', 2, 26000),
('Nokia 8', 'HMD Global', 6, 38000);
 
INSERT INTO Customers(FirstName) VALUES ('Tom'), ('Bob'),('Sam');
 
INSERT INTO Orders (ProductId, CustomerId, CreatedAt, ProductCount, Price)
VALUES
( 
    (SELECT Id FROM Products WHERE ProductName='Galaxy S8'),
    (SELECT Id FROM Customers WHERE FirstName='Tom'),
    '2018-05-21', 
    2, 
    (SELECT Price FROM Products WHERE ProductName='Galaxy S8')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone X'),
    (SELECT Id FROM Customers WHERE FirstName='Tom'),
    '2018-05-23',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone X')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone X'),
    (SELECT Id FROM Customers WHERE FirstName='Bob'),
    '2018-05-21',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone X')
);


SELECT * FROM Orders, Customers;

SELECT C.FirstName, P.ProductName, O.*
FROM Orders AS O, Customers AS C, Products AS P
WHERE O.CustomerId = C.Id AND O.ProductId=P.Id;

SELECT Orders.CreatedAt, Customers.FirstName, Products.ProductName 
FROM Orders
JOIN Products ON Products.Id = Orders.ProductId AND Products.Manufacturer='Apple'
JOIN Customers ON Customers.Id=Orders.CustomerId
ORDER BY Customers.FirstName;





CREATE TABLE Customers
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    AccountSum DECIMAL
);
CREATE TABLE Employees
(
    Id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL
);
  
INSERT INTO Customers(FirstName, LastName, AccountSum) 
VALUES
('Tom', 'Smith', 2000),
('Sam', 'Brown', 3000),
('Mark', 'Adams', 2500),
('Paul', 'Ins', 4200),
('John', 'Smith', 2800),
('Tim', 'Cook', 2800);
  
INSERT INTO Employees(FirstName, LastName)
VALUES
('Homer', 'Simpson'),
('Tom', 'Smith'),
('Mark', 'Adams'),
('Nick', 'Svensson');

SELECT FirstName, LastName 
FROM Customers
UNION SELECT FirstName, LastName FROM Employees;


SELECT FirstName AS FName, LastName
FROM Customers
UNION SELECT FirstName, LastName
FROM Employees
ORDER BY FName DESC;


SELECT FirstName, LastName, AccountSum + AccountSum * 0.1 AS TotalSum 
FROM Customers WHERE AccountSum < 3000
UNION SELECT FirstName, LastName, AccountSum + AccountSum * 0.3 AS TotalSum 
FROM Customers WHERE AccountSum >= 3000;
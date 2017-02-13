-- DELETE FROM ProductsOnOrders;
-- DELETE FROM Orders;
-- DELETE FROM Products;
-- DELETE FROM PaymentTypes;
-- DELETE FROM Customers;

-- DROP TABLE IF EXISTS Customers;
-- DROP TABLE IF EXISTS PaymentTypes;
-- DROP TABLE IF EXISTS Products;
-- DROP TABLE IF EXISTS Orders;
-- DROP TABLE IF EXISTS ProductsOnOrders;

-- Uncomment above code after initial database creation --

CREATE TABLE `Customers` (
    `customerId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `customer_name` TEXT NOT NULL,
    `street_address` TEXT NOT NULL,
    `city` TEXT NOT NULL,
    `state` TEXT NOT NULL,
    `postal_code` INTEGER NOT NULL,
    `phone` TEXT NOT NULL,
    `active` INTEGER NOT NULL
);

INSERT INTO Customers VALUES (null, 'John Doe', '123 Testing Way', 'Exampleville', 'Florida', '12345', '123-456-1234', 0);
INSERT INTO Customers VALUES (null, 'Janet Jackson', '555 Poptart Drive', 'Beverly Hills', 'California', '90210', '911-111-1111', 1);


CREATE TABLE `PaymentTypes` (
    `paymentTypeId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `type` TEXT NOT NULL,
    `account_number` INTEGER NOT NULL,
    `customerId` INTEGER NOT NULL,
    FOREIGN KEY(`customerId`) REFERENCES `Customers`(`customerId`)
);

INSERT INTO PaymentTypes
  SELECT null, 'Visa', '1234567890', customerId
  FROM Customers c
  WHERE c.customer_name = 'John Doe';

INSERT INTO PaymentTypes
  SELECT null, 'MasterCard', '0987654321', customerId
  FROM Customers c
  WHERE c.customer_name = 'Janet Jackson';


CREATE TABLE `Products` (
    `productId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `title` TEXT NOT NULL,
    `description` TEXT NOT NULL,
    `price` DECIMAL(18,2) NOT NULL,
    `quantity` INTEGER NOT NULL
);

INSERT INTO Products VALUES (null, 'Bicycle', 'Two wheels, one speed', 300.00, 10);
INSERT INTO Products VALUES (null, 'Ice Cream', 'Chocolate', 5.00, 55);
INSERT INTO Products VALUES (null, 'Soccer Ball', 'Perfect for soccer', 15.00, 14);
INSERT INTO Products VALUES (null, 'Plastic Cups', 'For drinking things', 2.00, 300);


CREATE TABLE `Orders` (
    `orderId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date_created` TEXT NOT NULL,
    `customerId` INTEGER NOT NULL,
    `paymentTypeId` INTEGER NOT NULL,
    `payment_complete` INTEGER NOT NULL,
    FOREIGN KEY(`customerId`) REFERENCES `Customers`(`customerId`),
    FOREIGN KEY(`paymentTypeId`) REFERENCES `PaymentTypes`(`paymentTypeId`)
);

INSERT INTO Orders
  SELECT null, '01-01-2017', c.customerId, t.paymentTypeId, 0
  FROM Customers c, PaymentTypes t
  WHERE c.customer_name = 'Janet Jackson' and t.paymentTypeId = 2;

INSERT INTO Orders
  SELECT null, '02-03-2017', c.customerId, t.paymentTypeId, 0
  FROM Customers c, PaymentTypes t
  WHERE c.customer_name = 'John Doe' and t.paymentTypeId = 1;


CREATE TABLE `ProductsOnOrders` (
    `productsOnOrderId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `productId` INTEGER NOT NULL,
    `orderId` INTEGER NOT NULL,
    FOREIGN KEY(`productId`) REFERENCES `Products`(`productId`),
    FOREIGN KEY(`orderId`) REFERENCES `Orders`(`orderId`)
);

INSERT INTO ProductsOnOrders
  SELECT null, productId, orderId
  FROM Products p, Orders o
  WHERE p.productId = 2 and o.orderId = 2;

INSERT INTO ProductsOnOrders
  SELECT null, productId, orderId
  FROM Products p, Orders o
  WHERE p.productId = 1 and o.orderId = 1;


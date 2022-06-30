from sql import *
db = "propertyDb"
connect_db()
create_db(db)
engine = use_db(db)
engine.execute("""CREATE TABLE IF NOT EXISTS `propertys` (
  `propertyID` INT NOT NULL AUTO_INCREMENT,
  `propertyName` VARCHAR(255) NULL,
  `propertyNumber` INT NULL,
  `address` VARCHAR(255) NULL,
  PRIMARY KEY (`propertyID`))
""")

engine.execute(
    "INSERT INTO `propertys` (`propertyName`, `propertyNumber`, `address`) VALUES ('laptop', '1', 'Place')")

result = engine.execute(
    "SELECT * FROM `propertys`")

for r in result:
    print(r)

result = engine.execute(
    "SELECT COUNT(*) FROM `propertys`")
print(list(result)[0][0])

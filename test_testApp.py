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


def test_db_result():
    result = engine.execute(
        "SELECT COUNT(*) FROM `propertys`")

    row_num = int(list(result)[0][0])
    if row_num == 0:
        engine.execute(
            "INSERT INTO `propertys` (`propertyName`, `propertyNumber`, `address`) VALUES ('laptop', '1', 'Place')")
    result = engine.execute(
        "SELECT * FROM `propertys`")
    result_converted = str(list(result)[0][1])
    assert result_converted == "laptop"


test_db_result()
print("passed")

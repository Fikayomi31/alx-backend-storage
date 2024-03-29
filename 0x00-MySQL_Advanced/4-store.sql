-- script that creates a trigger to decrease the quantity
-- of an item after adding a new order

DELIMITER //
CREATE TRIGGER order_placed_decrease AFTER INSERT ON orders FOR EACH ROW
BEGIN
  UPDATE items SET quantity = quantity - NEW.number
  WHERE name = NEW.item_name;
END;
//
DELIMITER ;

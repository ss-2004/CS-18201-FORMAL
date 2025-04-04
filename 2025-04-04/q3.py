# Q3 Use Alloy Analyzer to formally specify and analyze a simple database schema for correctness.

# db_schema_validator.py

class Attribute:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Attr({self.name})"

class Table:
    def __init__(self, name, attributes, primary_key):
        self.name = name
        self.attrs = set(attributes)
        self.pk = primary_key
        if primary_key not in self.attrs:
            raise ValueError(f"Primary key '{primary_key}' not in attributes of table '{name}'")

    def __repr__(self):
        return f"Table({self.name}, attrs={[a.name for a in self.attrs]}, pk={self.pk.name})"

class ForeignKey:
    def __init__(self, from_table, from_attr, to_table, to_attr):
        self.from_table = from_table
        self.from_attr = from_attr
        self.to_table = to_table
        self.to_attr = to_attr

    def is_valid(self):
        return (self.from_attr in self.from_table.attrs) and (self.to_attr in self.to_table.attrs)

    def __repr__(self):
        return f"FK({self.from_table.name}.{self.from_attr.name} -> {self.to_table.name}.{self.to_attr.name})"

def define_schema():
    # Attributes
    user_id = Attribute("UserId")
    user_name = Attribute("UserName")
    user_email = Attribute("UserEmail")

    order_id = Attribute("OrderId")
    order_user_id = Attribute("OrderUserId")
    order_amount = Attribute("OrderAmount")

    # Tables
    user_table = Table("User", [user_id, user_name, user_email], user_id)
    order_table = Table("Order", [order_id, order_user_id, order_amount], order_id)

    # Foreign key: Order.OrderUserId -> User.UserId
    fk = ForeignKey(order_table, order_user_id, user_table, user_id)

    return user_table, order_table, [fk]

def validate_schema():
    user_table, order_table, foreign_keys = define_schema()

    print("Defined Tables:")
    print(user_table)
    print(order_table)
    print("\nDefined Foreign Keys:")
    for fk in foreign_keys:
        print(fk)

    print("\nValidation Results:")
    for fk in foreign_keys:
        if not fk.is_valid():
            print(f"[❌] Invalid foreign key: {fk}")
        else:
            print(f"[✅] Valid foreign key: {fk}")

if __name__ == "__main__":
    validate_schema()
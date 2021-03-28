import sqlite3


class Database:
	# init connection to db
	def __init__(self):
		self.connection = sqlite3.connect('database.db')
		self.cursor = self.connection.cursor()

	# close connection as object destroys
	def __del__(self):
		self.connection.close()

	# returns all rows
	def get_rows(self, col='id'):
		self.cursor.execute("SELECT * FROM products ORDER BY " + col)
		result = self.cursor.fetchall()
		
		return result

	# add a new row
	def add_row(self, sku, name, category, remains):
		query = """
			INSERT INTO products (sku, name, category, remains)
			VALUES (\'{}\', \'{}\', \'{}\', \'{}\')
			""".format(sku, name, category, remains)
		self.cursor.execute(query)
		self.connection.commit()

		return 'success'

	# delete a row by sku
	def delete_row(self, sku):
		query = "DELETE FROM products WHERE sku = {}".format(sku)
		self.cursor.execute(query)
		self.connection.commit()

		return 'success'

	# update remains number by sku
	def update_remains(self, sku, value):
		query = """
			UPDATE products SET remains = {}
			WHERE sku = {}
			""".format(value, sku)
		self.cursor.execute(query)
		self.connection.commit()

		return 'success'

	# reserve a product
	def reserve(self, sku, value=1):
		query = "UPDATE products SET reserved = {} WHERE sku = {}".format(value, sku)
		self.cursor.execute(query)
		self.connection.commit()

		return 'success'
 
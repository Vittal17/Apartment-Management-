import mysql.connector as ms
from tabulate import tabulate

# Function to check if connected to MySQL
def is_connected():
    try:
        connection = ms.connect(
            host="localhost",
            user="root",
            password="Vittal@1707"
        )
        return True
    except ms.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return False

# Function to get database connection
def get_database_connection():
    try:
        connection = ms.connect(
            host="localhost",
            user="root",
            password="Vittal@1707",
            database="ApartmentManagementDB"  # Replace with your database name
        )
        return connection
    except ms.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# variable to store boolean value
flag = is_connected()

# Database to be used
db = "ApartmentManagementDB"
db_tables = ["apartments","tenants", "maintenance_requests", "payments", "utilities"]
print(f"Using {db} Database")
print(f"All actions will happen inside {db} database")

if flag:
    try:
        # Checking if connected
        connection = get_database_connection()
        cursor = connection.cursor()

        # Selecting the database
        cursor.execute(f"USE {db};")
        print(f"Database changed to {db}")

        # Sample query to test the connection
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in the database:", tables)

        # Function to insert data into a table
        def insert_data():
            print("The table names are listed below")
            for i in range(len(db_tables)):
                print(i + 1, '.', db_tables[i])
            table_name = input("Enter the table name to insert data into: ").lower()

            if table_name == "tenants":
                name = input("Enter tenant name: ")
                contact_info = input("Enter contact information: ")
                apartment_id = int(input("Enter apartment id: "))
                lease_start_date = input("Enter lease start date (YYYY-MM-DD): ")
                lease_end_date = input("Enter lease end date (YYYY-MM-DD): ")
                query = "INSERT INTO tenants (name, contact_info, apartment_id, lease_start_date, lease_end_date) VALUES (%s, %s, %s, %s, %s)"
                values = (name, contact_info, apartment_id, lease_start_date, lease_end_date)

            elif table_name == "apartments":
                building_name = input("Enter building name: ")
                unit_number = input("Enter unit number: ")
                size = float(input("Enter apartment size (sq ft): "))
                rent_amount = float(input("Enter rent amount: "))
                query = "INSERT INTO apartments (building_name, unit_number, size, rent_amount) VALUES (%s, %s, %s, %s)"
                values = (building_name, unit_number, size, rent_amount)

            elif table_name == "maintenance_requests":
                tenant_id = int(input("Enter tenant id: "))
                apartment_id = int(input("Enter apartment id: "))
                request_date = input("Enter request date (YYYY-MM-DD): ")
                request_description = input("Enter request description: ")
                status = input("Enter request status: ")
                query = "INSERT INTO maintenance_requests (tenant_id, apartment_id, request_date, request_description, status) VALUES (%s, %s, %s, %s, %s)"
                values = (tenant_id, apartment_id, request_date, request_description, status)

            elif table_name == "payments":
                tenant_id = int(input("Enter tenant id: "))
                apartment_id = int(input("Enter apartment id: "))
                payment_date = input("Enter payment date (YYYY-MM-DD): ")
                amount = float(input("Enter payment amount: "))
                query = "INSERT INTO payments (tenant_id, apartment_id, payment_date, amount) VALUES (%s, %s, %s, %s)"
                values = (tenant_id, apartment_id, payment_date, amount)

            elif table_name == "utilities":
                apartment_id = int(input("Enter apartment id: "))
                utility_type = input("Enter utility type: ")
                usage_amount = float(input("Enter utility usage amount: "))
                charge_amount = float(input("Enter utility charge amount: "))
                query = "INSERT INTO utilities (apartment_id, utility_type, usage_amount, charge_amount) VALUES (%s, %s, %s, %s)"
                values = (apartment_id, utility_type, usage_amount, charge_amount)

            else:
                print("Invalid table name.")
                return

            cursor.execute(query, values)
            connection.commit()
            print(f"Data inserted into {table_name} table successfully.")

        # Function to update data in a table
        def update_data():
            print("The table names are listed below")
            for i in range(len(db_tables)):
                print(i + 1, '.', db_tables[i])
            table_name = input("Enter the table name to update data into: ").lower()

            if table_name == "tenants":
                tenant_id = int(input("Enter tenant id to update: "))
                column_name = input("Enter the column name to update: ")
                new_value = input("Enter the new value: ")
                query = f"UPDATE tenants SET {column_name} = %s WHERE tenant_id = %s"
                values = (new_value, tenant_id)

            elif table_name == "apartments":
                apartment_id = int(input("Enter apartment id to update: "))
                column_name = input("Enter the column name to update: ")
                new_value = input("Enter the new value: ")
                query = f"UPDATE apartments SET {column_name} = %s WHERE apartment_id = %s"
                values = (new_value, apartment_id)

            elif table_name == "maintenance_requests":
                request_id = int(input("Enter request id to update: "))
                column_name = input("Enter the column name to update: ")
                new_value = input("Enter the new value: ")
                query = f"UPDATE maintenance_requests SET {column_name} = %s WHERE request_id = %s"
                values = (new_value, request_id)

            elif table_name == "payments":
                payment_id = int(input("Enter payment id to update: "))
                column_name = input("Enter the column name to update: ")
                new_value = input("Enter the new value: ")
                query = f"UPDATE payments SET {column_name} = %s WHERE payment_id = %s"
                values = (new_value, payment_id)

            elif table_name == "utilities":
                utility_id = int(input("Enter utility id to update: "))
                column_name = input("Enter the column name to update: ")
                new_value = input("Enter the new value: ")
                query = f"UPDATE utilities SET {column_name} = %s WHERE utility_id = %s"
                values = (new_value, utility_id)

            else:
                print("Invalid table name.")
                return

            cursor.execute(query, values)
            connection.commit()
            print(f"Data in {table_name} table updated successfully.")

        # Function to delete data from a table
        def delete_data():
            print("The table names are listed below")
            for i in range(len(db_tables)):
                print(i + 1, '.', db_tables[i])
            table_name = input("Enter the table name to delete data from: ").lower()

            if table_name == "tenants":
                tenant_id = int(input("Enter tenant id to delete: "))
                query = "DELETE FROM tenants WHERE tenant_id = %s"
                values = (tenant_id,)

            elif table_name == "apartments":
                apartment_id = int(input("Enter apartment id to delete: "))
                query = "DELETE FROM apartments WHERE apartment_id = %s"
                values = (apartment_id,)

            elif table_name == "maintenance_requests":
                request_id = int(input("Enter request id to delete: "))
                query = "DELETE FROM maintenance_requests WHERE request_id = %s"
                values = (request_id,)

            elif table_name == "payments":
                payment_id = int(input("Enter payment id to delete: "))
                query = "DELETE FROM payments WHERE payment_id = %s"
                values = (payment_id,)

            elif table_name == "utilities":
                utility_id = int(input("Enter utility id to delete: "))
                query = "DELETE FROM utilities WHERE utility_id = %s"
                values = (utility_id,)

            else:
                print("Invalid table name.")
                return

            cursor.execute(query, values)
            connection.commit()
            print(f"Data deleted from {table_name} table successfully.")

        # Function to generate a report on tenant details
        def generate_tenant_report():
            query = """
                SELECT tenant_id, name, contact_info, apartment_id, lease_start_date, lease_end_date
                FROM tenants
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            if rows:
                print("\nTENANT REPORT")
                print(tabulate(rows, headers=["Tenant ID", "Name", "Contact Info", "Apartment ID", "Lease Start Date", "Lease End Date"], tablefmt="pretty"))
            else:
                print("No tenants found.")

        # Function to generate a report on apartment details
        def generate_apartment_report():
            query = """
                SELECT apartment_id, building_name, unit_number, size, rent_amount
                FROM apartments
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            if rows:
                print("\nAPARTMENT REPORT")
                print(tabulate(rows, headers=["Apartment ID", "Building Name", "Unit Number", "Size (sq ft)", "Rent Amount"], tablefmt="pretty"))
            else:
                print("No apartments found.")

        # Main menu
        def main_menu():
            print('\n' + '*'*95)
            print('\t\t\t\t MAIN MENU')
            print('*'*95)
            print('\t\t\t 1. Insert data into table')
            print('\t\t\t 2. Update data in table')
            print('\t\t\t 3. Delete data from table')
            print('\t\t\t 4. Generate Tenant Report')
            print('\t\t\t 5. Generate Apartment Report')
            print('\t\t\t 6. Exit')
            print("Enter your choice: ", end='')

        # Menu loop
        while True:
            main_menu()
            choice = input().strip()

            if choice == '1':
                insert_data()
            elif choice == '2':
                update_data()
            elif choice == '3':
                delete_data()
            elif choice == '4':
                generate_tenant_report()
            elif choice == '5':
                generate_apartment_report()
            elif choice == '6':
                break
            else:
                print("Please choose a valid number")

    except ms.Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
else:
    print("Failed to connect to MySQL")

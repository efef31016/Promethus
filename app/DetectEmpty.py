import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv("./.env")

class DetectEmpty:
    def __init__(self, tenant):
        self.tenant = tenant
        self.db_user = os.getenv("CLOUD_ADMIN_ACCOUNT")
        self.db_pass = os.getenv("CLOUD_ADMIN_PASSWORD")
        self.db_domain = os.getenv("CLOUD_DOMAIN")
        self.db_user = "postgres"
        self.db_pass = "aicreate360"
        self.db_domain = "35.185.130.55:5432/"
        self.schema = "ec"

    def check_table_empty(self,):
        '''
        True: success
        False: fail
        '''
        url_dev_cloud = f"postgresql://{self.db_user}:{self.db_pass}@{self.db_domain}{self.tenant}"
        for table_name in ["customer", "orders", "product"]:
            try:
                engine = create_engine(url_dev_cloud)
                with engine.connect() as connection:
                    result = connection.execute(text(f"SELECT COUNT(*) FROM {self.schema}.{table_name}"))
                    count = result.scalar()
                    if count == 0:
                        return False
                    else:
                        return True
            except:
                print(f"{self.schema}.{table_name} does not exist")


if __name__ == "__main__":
    detect_db = DetectEmpty("www.debalets.com.tw")
    print(detect_db.check_table_empty())

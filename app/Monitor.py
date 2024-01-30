import json
from DetectEmpty import DetectEmpty
from DetectComplete import DetectComplete

AIRFLOW_ALERT_PATH="/opt/airflow/dags/alert/app"
SERVICE_ALERT_PATH="/srv/ai-airflow/dags/alert/app"

class Monitor:

    detect_complete = DetectComplete()

    def __init__(self,):
        pass

    @classmethod
    def db_empty(cls, tenant):
        detect_db = DetectEmpty(tenant)
        status = detect_db.check_table_empty()
        return status

    @classmethod
    def update_detect(cls, customer_error=1, order_error=1, product_error=1, customer_num=0, order_num=0, product_num=0):
        cls.detect_complete.detect_customer(customer_error, customer_num)
        cls.detect_complete.detect_order(order_error, order_num)
        cls.detect_complete.detect_product(product_error, product_num)

    @staticmethod
    def save_state_to_file(tenant):
        state = {
            "customer_error": Monitor.detect_complete.customer_error,
            "order_error": Monitor.detect_complete.order_error,
            "product_error": Monitor.detect_complete.product_error,
            "customer_num": Monitor.detect_complete.customer_num,
            "order_num": Monitor.detect_complete.order_num,
            "product_num": Monitor.detect_complete.product_num,
        }
        filename = f"{AIRFLOW_ALERT_PATH}/{tenant}_detect_state.json"
        with open(filename, "w") as file:
            json.dump(state, file)
    

    @staticmethod
    def load_state_from_file(tenant):
        try:
            filename = f"{SERVICE_ALERT_PATH}/{tenant}_detect_state.json"
            with open(filename, "r") as file:
                state = json.load(file)
                Monitor.detect_complete.customer_error = state["customer_error"]
                Monitor.detect_complete.order_error = state["order_error"]
                Monitor.detect_complete.product_error = state["product_error"]
                Monitor.detect_complete.customer_num = state["customer_num"]
                Monitor.detect_complete.order_num = state["order_num"]
                Monitor.detect_complete.product_num = state["product_num"]
                #print(f"Loaded state for {tenant}: {state}")
        except FileNotFoundError:
            print(f"File not found: {filename}")

    #@staticmethod
    #def load_state_from_file(tenant):
    #    try:
    #        filename = f"{ALERT_PATH}/{tenant}_detect_state.json"
    #        with open(filename, "r") as file:
    #            state = json.load(file)
    #            Monitor.detect_complete.customer_error = state["customer_error"]
    #            Monitor.detect_complete.order_error = state["order_error"]
    #            Monitor.detect_complete.product_error = state["product_error"]
    #            Monitor.detect_complete.customer_num = state["customer_num"]
    #            Monitor.detect_complete.order_num = state["order_num"]
    #            Monitor.detect_complete.product_num = state["product_num"]
    #    except FileNotFoundError:
    #        pass

if __name__ == "__main__":
    condition = False
    fcn = lambda x : 0 if not condition else 1
    fail = 1
    Monitor.update_detect(customer_error=fcn(""), customer_num=fail)
    Monitor.save_state_to_file()

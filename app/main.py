# follow the response format rule: https://docs.google.com/document/d/1Z7VCpz6KVozLJ5khKLclmMUUpUUKdvnNQ12BRMBJogk/edit
from flask import Flask, Response
from prometheus_client import CONTENT_TYPE_LATEST
from Monitor import Monitor
from ResponseFormat import ResponseFormat

app = Flask(__name__)

tenants = ["www.setddg.com", "www.debalets.com.tw"]

res = ResponseFormat()
res.create_index(tenant_list=tenants)

@app.route("/metrics", methods=["GET"])
def metrics():

    for idx, tenant in enumerate(tenants):

        Monitor.load_state_from_file(tenant)

        # empty:0 or not empty:1
        status = Monitor.db_empty(tenant)
        res.set_value(which_index_name_prefix=0, which_tenant=idx, status=status)

        # lose:0 or not lose:1
        status_list = [(Monitor.detect_complete.customer_error, Monitor.detect_complete.customer_num),
                        (Monitor.detect_complete.order_error, Monitor.detect_complete.order_num),
                        (Monitor.detect_complete.product_error, Monitor.detect_complete.product_num)]
        # [customer, order, product]
        for group_idx, (status, fail_num) in enumerate(status_list):
            metric_index_status = group_idx * 2 + 1
            metric_index_fail_num = group_idx * 2 + 2

            # Set value for status and fail_num separately
            res.set_value(which_index_name_prefix=metric_index_status, which_tenant=idx, status=status)
            res.set_value(which_index_name_prefix=metric_index_fail_num, which_tenant=idx, status=fail_num)
    
        custom_metrics = res.filter_metrics()
        response = Response(custom_metrics, mimetype=CONTENT_TYPE_LATEST)

    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

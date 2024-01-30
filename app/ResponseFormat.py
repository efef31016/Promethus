from prometheus_client import generate_latest, Gauge, REGISTRY

class ResponseFormat:
    def __init__(self,):

        self.index_name_prefix = ["empty_check_",
                    "lose_check_customer_", "lose_check_customer_fail_num_",
                    "lose_check_order_", "lose_check_order_fail_num_",
                    "lose_check_product_", "lose_check_product_fail_num_"]
        
        self.index_desc = ["Database check status", 
                "if lose customer", "lose check number for customer metric",
                "if lose order", "lose check number for order metric",
                "if lose product", "lose check number for product metric"]
        
        self.alert_dict = {key:[] for key in self.index_desc}

    def create_index(self, tenant_list):
        for tenant in tenant_list:
            for i in range(len(self.index_name_prefix)):
                self.alert_dict[self.index_desc[i]].append(Gauge(f"{self.index_name_prefix[i]}{tenant.replace('.','_')}", self.index_desc[i]))

    def set_value(self, which_index_name_prefix, which_tenant, status):
        '''
        status: bool - True: no alert, False: alert
        '''
        self.alert_dict[self.index_desc[which_index_name_prefix]][which_tenant].set(status)

    def filter_metrics(self,):
        custom_metrics_prefixes = self.index_name_prefix
        all_metrics = generate_latest(REGISTRY).decode('utf-8')
        filtered_metrics = []

        for line in all_metrics.split('\n'):
            if any(line.startswith(prefix) for prefix in custom_metrics_prefixes):
                filtered_metrics.append(line)

        return '\n'.join(filtered_metrics)

if __name__ == "__main__":
    obj = ResponseFormat()

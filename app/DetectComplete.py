class DetectComplete:

    customer_error = 1
    order_error = 1
    product_error = 1
    
    customer_num = 0
    order_num = 0
    product_num = 0
    
    def __init__(self,):
        '''
        1: success
        0: fail
        '''
        pass

    def detect_customer(self, if_else_fcn, num):
        print("modify customer_error")
        DetectComplete.customer_error = if_else_fcn
        DetectComplete.customer_num = num

    def detect_order(self, if_else_fcn, num):
        print("modify order_error")
        DetectComplete.order_error = if_else_fcn
        DetectComplete.order_num = num

    def detect_product(self, if_else_fcn, num):
        print("modify product_error")
        DetectComplete.product_error = if_else_fcn
        DetectComplete.product_num = num

if __name__ == "__main__":
    # from DetectComplete import DetectComplete
    test = "a"
    test_if_else_fcn = lambda _ : 0 if test == "b" else 1
    fail = 20
    obj = DetectComplete()
    obj.detect_customer(test_if_else_fcn("no meaning"), fail)
    print(DetectComplete.error())
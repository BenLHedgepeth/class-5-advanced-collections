from step_1 import transform_products_to_list

def group_products_by_customer_and_invoice(products_string):
    '''Organize orders by customer and invoice number'''
    
    order_data = transform_products_to_list(products_string)
    customers = {}
    
    for order in order_data:
        cust_id = order[-2]
        invoice_nbr = order[0]
        
        customers.setdefault(cust_id, {})
        customers[cust_id].setdefault(invoice_nbr, [])
        customers[cust_id][invoice_nbr].append(order)
        
    return customers
    

        


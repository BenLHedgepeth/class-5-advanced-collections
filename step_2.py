from step_1 import transform_products_to_list

def group_products_by_customer(products_string):
    '''Organize orders by customer'''
    
    customers = {}
    
    orders = transform_products_to_list(products_string) 
    
    for order in orders:
        customer_id = order[-2]
        customers.setdefault(customer_id, [])
        customers[customer_id].append(order)
        
    return customers
    

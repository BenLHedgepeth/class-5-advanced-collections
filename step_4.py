from step_1 import transform_products_to_list

def calculate_total_per_invoices(products_string):
    '''Sum the total sales price for each customer's order'''
    
    purchase_data = transform_products_to_list(products_string)
    customer_invoices = {}
    
    for purchase in purchase_data:
        customer = purchase[-2]
        invoice_id = purchase[0]
        quantity_order = purchase[3]
        unit_price = purchase[-3]
        
        customer_invoices.setdefault(customer, {})
        customer_invoices[customer].setdefault(invoice_id, 0)
        customer_invoices[customer][invoice_id] += round(int(quantity_order) * float(unit_price), 2)
    
    return customer_invoices
    
    
    
    

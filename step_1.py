def transform_products_to_list(products_string):
    '''Return customer orders in an multi-dimensional array'''
    
    product_line = []
    
    items = products_string.split("\n")
    
    for item in items:
        if item:
            sku = item.split(",")
            product_line.append(sku)
    
    return product_line
    

    
    
    
    

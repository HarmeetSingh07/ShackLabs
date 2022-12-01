def comparison(name):
    import pandas as pd
    amz = pd.read_csv('amz_com-ecommerce_sample.csv',encoding= 'unicode_escape')    
    fk = pd.read_csv('flipkart_com-ecommerce_sample.csv',encoding= 'unicode_escape')
    
    import numpy as np
    index = fk['retail_price'].index[fk['retail_price'].apply(np.isnan)]
    fk.drop(index= index,inplace=True)
    
    df = pd.DataFrame({'Product name in Flipkart': fk[fk.product_name== name]['product_name'],
                            'Retail Price in Flipkart': fk[fk.product_name == name]['retail_price'],
                            'Discounted Price in Flipkart': fk[fk.product_name == name]['discounted_price'],
                            'Product name in Amazon': amz[amz.product_name== name]['product_name'],
                            'Retail Price in Amazon': amz[amz.product_name == name]['retail_price'],
                            'Discounted Price in Amazon': amz[amz.product_name == name]['discounted_price']})
    df = df.reset_index()
    df.drop('index',axis=1,inplace=True)
    return df

# name = "AW Bellies"
name  = input('Enter name of the product : ')
df = comparison(name)
df
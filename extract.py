sales_df=spark.read.format('csv').option('inferschema','true').schema(schema).load('/FileStore/tables/sales_csv.txt')
display(sales_df)

from pyspark.sql.functions import month,year,quarter

sales_df=sales_df.withColumn("orderyear",year(sales_df.Order_date))
display(sales_df)
sales_df=sales_df.withColumn("ordermonth",month(sales_df.Order_date))
sales_df=sales_df.withColumn("orderquarter",quarter(sales_df.Order_date))
display(sales_df)
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DateType

schema=StructType([
    StructField("product_id",IntegerType(),True),
    StructField("product_name",StringType(),True),
    StructField("price",StringType(),True)

])

menu_df=spark.read.format('csv').option('inferschema','true').schema(schema).load('/FileStore/tables/menu_csv.txt')
display(sales_df)
# Calculate total amount spent by each customer
total_spent_amount = (sales_df.join(menu_df, 'product_id')
                      .groupBy('customer_id')
                      .agg({'price': 'sum'})
                      .withColumnRenamed('sum(price)', 'total_spent')
                      .orderBy('customer_id'))

display(total_spent_amount)
# Calculate total amount spent by each product
total_spent_amount = (sales_df.join(menu_df, 'product_id')
                      .groupBy('product_name')
                      .agg({'price': 'sum'})
                      .withColumnRenamed('sum(price)', 'total_spent')
                      .orderBy('product_name'))

display(total_spent_amount)
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import sys

# Get job arguments
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

# Initialize Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Initialize the Glue job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="default",
    table_name="productinput",  
    transformation_ctx="S3bucket_node1"
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=S3bucket_node1,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://glue-step-function/output/",
        "partitionKeys": []
    },
    transformation_ctx="S3bucket_node3"
)

# Commit the job
job.commit()

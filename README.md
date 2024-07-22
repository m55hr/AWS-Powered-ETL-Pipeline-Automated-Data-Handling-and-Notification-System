![project](https://github.com/user-attachments/assets/1de4a735-2331-47f3-893d-7944718ddbcb)# AWS-Powered-ETL-Pipeline-Automated-Data-Handling-and-Notification-System
In my ETL pipeline project, I have orchestrated a sophisticated data processing workflow using AWS services. The pipeline is designed to automate the extraction, transformation, and loading of data. Here’s how it works:

•	Glue Crawler Setup: The pipeline starts with an AWS Glue Crawler that scans an S3 bucket where raw CSV files are stored. The Crawler reads the data and catalogs its schema, making it ready for transformation.

•	Data Transformation: Once the Crawler has successfully cataloged the data, it triggers a Glue ETL job. This job converts the CSV files into JSON format, ensuring that the data is structured in a more flexible and efficient format for further processing.

•	Data Storage: After transformation, the Glue ETL job saves the JSON files back to the S3 bucket, organizing them in a specified output location.

•	Event Monitoring: To monitor the completion of the Glue ETL job, I use Amazon EventBridge. EventBridge is configured to listen for specific events related to the Glue job's status.

•	Notification System: When the Glue job completes, EventBridge triggers an SNS topic. This SNS topic sends a notification to my email address, informing me of the job's completion and any relevant details.

•	Workflow Coordination: The entire process is managed through a Step Function that ensures the ETL job only starts after the Crawler has completed its task. This coordination guarantees that the data transformation occurs only when the raw data has been fully processed and cataloged.

This setup not only automates the data processing pipeline but also ensures timely notifications, efficient data handling, and robust monitoring of the entire ETL workflow.
![project](https://github.com/user-attachments/assets/3e75723d-e879-4b84-92e6-102082ecd1b7)
![1](https://github.com/user-attachments/assets/a21e4fb4-291d-48ea-ae7d-0c9e4ba070f1)

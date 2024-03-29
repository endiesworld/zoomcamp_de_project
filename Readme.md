# Problem statement 1, Data Source
_ _ _
    For this project, I reviewed the December 2022 U.K cycling journey data.
    'https://cycling.data.tfl.gov.uk/usage-stats/346JourneyDataExtract28Nov2022-04Dec2022.csv',
    'https://cycling.data.tfl.gov.uk/usage-stats/347JourneyDataExtract05Dec2022-11Dec2022.csv',
    'https://cycling.data.tfl.gov.uk/usage-stats/348JourneyDataExtract12Dec2022-18Dec2022.csv',
    'https://cycling.data.tfl.gov.uk/usage-stats/349JourneyDataExtract19Dec2022-25Dec2022.csv',
    'https://cycling.data.tfl.gov.uk/usage-stats/350JourneyDataExtract26Dec2022-01Jan2023.csv'

# Project Objective and Use case
_ _ _
    1. Visualize the daily trip count. This will help plan trafic control subsequently
    2. Visualise the top 10 busiest stations. This can be use for targeted marketing purposes.
    3. Visualise the top 10 bicycles with the highest operation time. This would help in maintenance/service plan for bicycles.

# Tools:
_ _ _ 
    . Cloud: GCP
    . Infrastructure as code (IaC): Terraform (Maga-ai)
    . Workflow orchestration: mage-ai
    . Data Warehouse: BigQuery
    . Data Lake: Google Cloud Storage
    . Batch processing: Bigquery-sql

# Running this project
_ _ _
    To run this project locally, the following prerequisite must be met:
    . Install docker and docker-compose in your machine
    . An active google cloud service account and project
    . Create and download google cloud service account key to the main project directory

# Download and run the project
    . git clone https://github.com/endiesworld/zoomcamp_de_project
    . cd zoomcamp_de_project
    . sudo lsof -i :6789 <!. This act is to confirm that port 6789 is free on the machine you intend to run this application on.>
    . docker stop $(docker ps -q) <!. Only do this if another docker container is using port 6789 .>
    . docker compose build <!. To build the project .>
    . Save the path to your google cloud service key as a value in the 'GOOGLE_SERVICE_ACC_KEY_FILEPATH:' in the file 'zoomcamp-DE/io_config.yml'.
    i.e You should only have this value for your google cloud service
        # Google
        GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/dtc-de-course-01-2024-2fd79da48386.json"

# Run the blocks for each pipeline jobs in the orther they have been made, following the order below:
_ _ _

# Problem statement 2: Creating a pipeline for processing this dataset and putting it to a datalake
<!-- To run the Data "Exporter Block" for this pipeline you must have created a bucket in GCP and have your bucket name save in the block as shown below:-->
    . bucket_name = 'Your_bucket_name'
    . object_key = 'Object_key_to_store_data.parquet'

# Problem statement 3: Creating a pipeline for moving the data from the lake to a data warehouse
<!-- Before running the Data "Data Loader" and "Exporter Block" for this pipeline you must do the below:-->
    Data "Data Loader" Block:
    . bucket_name = 'Your_bucket_name' 
    . object_key = 'Object_key_to_store_data.parquet'
        Data "Exporter" Block:
    . table_id = 'your_project_id.data_set.table_namedtc-de-course-01-2024.uk_cycling_data.dec_2022_journey' #Replace project_id.data_set.table_name

# Problem statement 4: Transforming the data in the data warehouse: prepare it for the dashboard
_ _ _ 
    . Create a query file in your bigquery.
    . Copy and paste all the 'bigquery_script_for_dashboard.sql' file
    . Run each block of script and read the comments below it for the dashboard visualization.

# Problem statement 4: Building a dashboard to visualize the data
Visualize the dashboard and confirm that it matches with that represented in the links below
    . Report link: https://lookerstudio.google.com/s/pjSs0CwvXjk
    . Report link: https://lookerstudio.google.com/s/sZFMRm2O078
    . Report link: https://lookerstudio.google.com/s/g_Hia0ZXJ9M



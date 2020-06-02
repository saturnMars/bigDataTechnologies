# Big Data Technologies (A.A 2019-2020)
## The Million Song Dataset (MSD)
### ETL, data exploration and Gaussian Mixture clustering in Databricks Community
The MSD is a database of popular songs spanning decades of music. It has been released to the public for research by The Echo Nest, a company that specializes in music intelligence services. The dataset has become more and more famed after its analysis competition released in Kaggle.com in 2012. 
The dataset is about 300 GB large and it contains a collection of audio features (loud- ness, tempo, etc.) and metadata (artist, year, etc.) for a million contemporary popular music tracks.

In this project, we suggest a simple **Big Data system to process and analyse the Million Song Dataset (MSD) using Spark through the handy Databricks platform in its community Edition which is available for free.** After displaying some statistics regarding the dataset, we have focused on creating different types of clusters based on different song attributes.

## Requirements
1. Create an account of [Databricks (Community)](https://community.cloud.databricks.com/)
2. Import the python notebooks *(import data, explore data* and *clustering)* into your workspace
3. [Download](http://static.echonest.com/millionsongsubset_full.tar.gz) the original subset (~2 GB) from the [Million Song Dataset website](http://millionsongdataset.com/)
4. Decompress the file (.gz) and upload all the folders into Databricks File System *(Data > Add Data > Upload File)*
5. In the file **"Import dataset"** change the variable *"ROOT_FOLDER"* according to your dataset path 
    - Default folder: *"/FileStore/tables/songs"*

# Authors (Group 11)
### - Bronzini Marco
### - Lazzerini Giacomo


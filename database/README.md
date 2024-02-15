# Wikinetes (Database)



## For Development: How to setup Database?

- **Step 0** : Install Docker

- **Step 1** : Spin a MongoDB container 

    ```bash
    docker run --name mongo -p 80:27017 -d mongo
    ```

- **Step 2** : Install Dependencies 
    ```
    python3-pip install pymongo
    ```

- **Step 3** : Use Python Script to Create Database & Collection, and Add Sample Documents

    ```bash
    curl https://raw.githubusercontent.com/thekarananand/wikinetes-new/main/database/setup-database.py | python3 -
    ```



Extract outreachy participants
==============================


# Requirements

2 possibilities

1. Install [conda](https://docs.conda.io/en/latest/miniconda.html)
2. Create conda environment with all the requirements

    ```
    $ conda env create -f environment.yml
    ```

3. Activate conda environment

    ```
    $ conda activate outreachy_tracking
    ```

# Usage

1. Save user data from Gitter channel (Settings --> Export room data --> Users)
2. Run the scripts

    ```
    $ python bin/get_participants.py --gitter_users <path to gitter user json file> --out <path to output CSV file>
    ```

3. Import the generated CSV file to Google sheet (File --> Import)
# simple-nhl-live-scores
Simple Python script to display live NHL scores in the terminal, fetched directly from the official NHL API.

![scores](https://github.com/user-attachments/assets/bf5bf728-f626-463d-9148-f371084d74cc)


## Requirements

  - `requests` library
  
Install the dependencies with the following command:

```
pip install -r requirements.txt
```
Alternatively, you can install the requests library directly with:
```
pip install requests
```

## Usage
Once the dependencies are installed, run the script with the following command:

  On macOS/Linux:
  ```
  python3 nhlscores.py
  ```
    
  On Windows:
  ```
  python nhlscores.py
  ```

## Optional Arguments
Adjust the score update interval (default: 30 seconds).
```
--update_interval SECONDS
```

Example: Fetch scores every 10 seconds:
```
python nhlscores.py --update_interval 10
```



## Setting Up And Using Virtual Environment (Optional)

Using a virtual environment is **highly recommended** to avoid conflicts with other Python projects.

**Note**: The venv module requires a minimum Python version of 3.3


1. **Create a virtual environment** in your project directory:

    On macOS/Linux:
    ```
    python3 -m venv venv
    ```
    On Windows:
    ```
    python -m venv venv
    ```
2. **Activate the virtual environment:**
    
    On macOS/Linux:
    ```
    source venv/bin/activate
    ```
    On Windows:
    ```
    .\venv\Scripts\activate
    ```

3. **Install the dependencies:** After activation, install the required packages:
    ```
    pip install -r requirements.txt
    ```
4. **Deactivate the virtual environment:** When finished, deactivate with:
    ```
    deactivate
    ```
## Running the Script with the Virtual Environment

After setting up **venv** and installing dependencies, run the script:

  On macOS/Linux:
  ```
  source venv/bin/activate
  python3 nhlscores.py
  deactivate
  ```
  On Windows:
  ```
  .\venv\Scripts\activate
  python nhlscores.py
  deactivate
  ```

## Creating a Windows Shortcut to Run the Script with a Virtual Environment (Optional)

1. Hold Alt and drag the nhlscores.py file to the desktop to create a shortcut.
2. Right-click the shortcut, select properties and modify the **Target** field to:
```
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -NoExit -Command "cd 'X:\YOUR PATH TO FILE\'; .\.venv\Scripts\Activate; python .\nhlscores.py"
```
Replace X:\YOUR PATH TO FILE\ with the actual path to the folder containing nhlscores.py

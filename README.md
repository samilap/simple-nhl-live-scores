# simple-nhl-live-scores
Simple Python script to display live NHL scores in the terminal, fetched directly from the official NHL API.

![scores](https://github.com/user-attachments/assets/bf5bf728-f626-463d-9148-f371084d74cc)


## Requirements

  - `requests` library
  
Install dependencies with:

```
pip install -r requirements.txt
```
Alternatively, install `requests` directly with:
```
pip install requests
```

## Usage
After installing dependencies, run the script with:

  **macOS/Linux:**
  ```
  python3 nhlscores.py
  ```
    
  **Windows:**
  ```
  python nhlscores.py
  ```

## Optional Arguments
Set the score update interval (default: 30 seconds):
```
--update_interval SECONDS
```

Example: Update scores every 10 seconds:
```
python nhlscores.py --update_interval 10
```



## (Optional) Using Virtual Environment

Using a virtual environment is **highly recommended** to avoid conflicts with other Python projects.

**Note**: The venv module requires Python 3.3 or higher.

1. **Setting Up venv and Installing Dependencies**

    **macOS/Linux:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
    ```
    **Windows:**
    ```
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    deactivate
    ```

2. **Running the Script**

    **macOS/Linux:**
    ```
    source venv/bin/activate
    python3 nhlscores.py
    deactivate
    ```
    **Windows:**
    ```
    .\venv\Scripts\activate
    python nhlscores.py
    deactivate
    ```

## (Optional) Example: Creating a Windows Shortcut to Run the Script with a Virtual Environment

1. Hold **Alt** and drag the `nhlscores.py` file to the desktop to create a shortcut.
2. Right-click the shortcut, select properties and modify the **Target** field to:
```
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -NoExit -Command "cd 'X:\YOUR PATH TO FILE\'; .\.venv\Scripts\Activate; python .\nhlscores.py"
```
Replace `X:\YOUR PATH TO FILE\` with the actual path to the folder containing `nhlscores.py`

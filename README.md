# simple-nhl-live-scores
Simple Python script to display NHL live scores in terminal.

![scores](https://github.com/user-attachments/assets/bf5bf728-f626-463d-9148-f371084d74cc)


## Requirements
  The required dependencies are:

  - `requests` library
  
You can install the dependencies using `pip` by running:

```
pip install -r requirements.txt
```

## Usage
Once the dependencies are installed, you can run the script using the following command:

  On macOS/Linux:
  ```
  python3 nhlscores.py
  ```
    
  On Windows:
  ```
  python nhlscores.py
  ```

## Optional Arguments
You can specify an optional argument to adjust the update interval.
```
--update_interval: Set the interval (in seconds) between fetching live NHL scores. The default is 30 seconds.
```
Example with a custom update interval of 10 seconds:
```
python nhlscores.py --update_interval 10
```



## Setting Up And Using Virtual Environment (Optional)

It is **highly recommended** to use a virtual environment to avoid conflicts with other Python projects.

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

3. **Install the required dependencies:**
    After activating the virtual environment, install the dependencies listed in requirements.txt:
    ```
    pip install -r requirements.txt
    ```
4. **Deactivate the Virtual Environment:**
	When you're done, you can deactivate the virtual environment with the following command:
    ```
    deactivate
    ```
## Usage with Virtual Environment

After setting up the virtual environment and installing the dependencies, you can run the script as follows:
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

## Creating a Windows Shortcut for Running the Script with a Virtual Environment (Optional)
You can create a shortcut to easily run the script with the virtual environment activated.

1. Create a shortcut by holding Alt and dragging the nhlscores.py file to the desktop.
2. Right-click the shortcut and edit the **Target** field to include the following command:
```
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -NoExit -Command "cd 'X:\YOUR PATH TO FILE\'; .\.venv\Scripts\Activate; python .\nhlscores.py"
```
Replace X:\YOUR PATH TO FILE\ with the actual path to the folder containing nhlscores.py.

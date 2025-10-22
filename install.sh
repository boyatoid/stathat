read -p "Do you want to create a virtual environment for these resources? (Y/N): " confirm
   if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
       echo "Creating virtual environment..."
       sleep 2
       python3 -m venv .stathat-env || { echo "Failed to create venv"; exit 1; }
       source .stathat-env/bin/activate || { echo "Failed to activate venv"; exit 1; }
       python3 -m pip install -r requirements.txt || { echo "Failed to install requirements"; exit 1; }
   else
       echo "Skipping virtual environment creation..."
       sleep 2
       python3 -m pip install -r requirements.txt || { echo "Failed to install requirements"; exit 1; }
   fi
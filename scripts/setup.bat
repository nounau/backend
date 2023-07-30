SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
APP_DIR=$(cd $SCRIPT_DIR  && cd .. && pwd)
cd $APP_DIR
echo "Current directory set to ${PWD}"
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
# pip3 install -r requirements-test.txt
export PYTHONPATH=${PWD}
export FLASK_APP=main
export FLASK_DEBUG=1
export ENV_FOR_DYNACONF=local

pause

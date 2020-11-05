export API_ENV='dev'
export LOG_PATH='./log/log.txt'
python -m pytest -s --alluredir=test_results/ test_headers.py
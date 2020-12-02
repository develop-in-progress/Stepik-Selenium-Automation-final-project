start /B pytest --browser_name=grid_firefox --tb=line -n=auto --alluredir=reports --reruns 1 &
start /B pytest --browser_name=grid_chrome --tb=line -n=auto --alluredir=reports --reruns=1

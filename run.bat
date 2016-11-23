if x%1x==xx (
	@echo language argument not provided
	exit /b 1
)
if %1==py (
	ruby bench.rb "python csa.py" > results-py.txt
	exit /b 0
)
if %1==js (
	ruby bench.rb "node csa.js" > results-js.txt
	exit /b 0
)
if %1==rb (
	ruby bench.rb "ruby csa.rb" > results-rb.txt
	exit /b 0
)
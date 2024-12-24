show_cases:
	pytest --collect-only

run_tests:
	echo "before tests"
	pytest
	echo "after test"


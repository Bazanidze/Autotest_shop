show_cases:
	pytest --collect-only

#run_tests:
#	echo "before tests"
#	source D:\Miniconda\Scripts\conda.exe; \
#	conda activate Practical_work_2; \
#	pytest; \
#	conda deactivate; \
#	echo "after test"

run_test:
	make show_cases
	echo 'Hello world'
	conda run -n Practical_work_2 pytest
	echo 'Hello world'
from prefect import flow

@flow
def print_name():
	print("Name")
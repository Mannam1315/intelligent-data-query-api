import mlflow

def log_experiment(run_name: str, accuracy: float):
    with mlflow.start_run(run_name=run_name):
        mlflow.log_metric("accuracy", accuracy)
        return f"Logged run '{run_name}' with accuracy={accuracy}"

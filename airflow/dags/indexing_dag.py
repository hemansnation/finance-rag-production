from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from rag_pipeline import load_and_chunk_pdf, create_vector_store
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 31),
    'retires': 1,
}

def check_for_new_reports():
    pdf_dir = "data/"
    pdfs = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    return pdfs

def process_and_index_report():
    pdfs = check_for_new_reports()
    for pdf in pdfs:
        chunks = load_and_chunk_pdf(f"data/{pdf}")
        create_vector_store(chunks)

with DAG('indexing_dag', default_args=default_args, schedule_interval='@daily') as dag:
    check_task = PythonOperator(
        task_id='check_for_new_reports',
        python_callable=check_for_new_reports
    )
    index_task = PythonOperator(
        task_id='process_and_index_report',
        python_callable=process_and_index_report
    )
    check_task >> index_task
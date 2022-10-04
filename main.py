import apache_beam as beam
from apache_beam.dataframe.io import read_csv
import typing


def main():
    with beam.Pipeline() as pipeline:
        input_data = (
            pipeline
                | "Transactions" >> read_csv("gs://cloud-samples-data/bigquery/sample-transactions/transactions.csv")
                | beam.Map(print)
        )

if __name__ == "__main__":
    main()

import pandas as pd


def create_date_dimension(start_date, end_date):

    dates = pd.date_range(
        start=start_date,
        end=end_date
    )

    dim_date = pd.DataFrame({
        "date": dates
    })

    dim_date["day"] = dim_date["date"].dt.day
    dim_date["month"] = dim_date["date"].dt.month
    dim_date["month_name"] = dim_date["date"].dt.month_name()
    dim_date["quarter"] = dim_date["date"].dt.quarter
    dim_date["year"] = dim_date["date"].dt.year
    dim_date["weekday"] = dim_date["date"].dt.day_name()

    return dim_date


if __name__ == "__main__":

    dim_date = create_date_dimension(
        "2016-01-01",
        "2018-12-31"
    )

    dim_date.to_csv(
        "data/processed/dim_date.csv",
        index=False
    )

    print(dim_date.head())
    print(f"Rows: {len(dim_date)}")
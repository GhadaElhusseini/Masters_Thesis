import pandas as pd


def load_vdem():
    """
    Loads V-Dem data and keeps selected columns.

    Returns:
        pd.DataFrame: cleaned V-Dem dataframe.
    """
    # Load CSV (hardcoded path)
    df_aggregate = pd.read_csv(
        "/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/V-Dem-CY-Core-v15.csv"
    )

    # Keep only important columns
    columns_to_keep = ["country_name", "year", "v2x_regime", "v2x_polyarchy", "v2x_liberal"]
    v_dem_df = df_aggregate[[col for col in columns_to_keep if col in df_aggregate.columns]]

    # Optional: drop missing rows
    # v_dem_df = v_dem_df.dropna(subset=["country_name", "year", "v2x_regime"])

    return v_dem_df


def load_maddison():
    """
    Loads Maddison data and keeps selected columns.

    Parameters:
        path (str): path to the Maddison CSV file.

    Returns:
        pd.DataFrame: cleaned Maddison dataframe.
    """
    df = pd.read_excel('/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/mpd2023_web.xlsx')

    # Keep only important columns
    #important_cols = ["country_name", "year", "gdp_per_capita", "population"]
    #df = df[important_cols]

    # Optional: drop missing rows
    #df = df.dropna(subset=["country_name", "year", "gdp_per_capita"])

    return df


def load_popgrowth_df():
    """
        Loads population growth data from Our World in Data .

        Parameters:
            path (str): path to the CSV file. - optional

        Returns:
            pd.DataFrame:
        """
    df = pd.read_csv('/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/population-growth-rate.csv')

    df.rename(columns={"Entity": "country", "Year": "year"}, inplace=True)
    df = df[(df["year"] <= 2022)]

    # Keep only important columns
    # important_cols = ["country_name", "year", "gdp", "gdp_per_capita", "population"]
    # df = df[important_cols]

    # Optional: drop missing rows
    # df = df.dropna(subset=["country_name", "year", "gdp_per_capita"])

    return df



def load_trade_share():
    """
        Loads trade share data from Our World in Data, and keeps selected columns., then turns into long format, then pivots to seperates the value columns .

        Parameters:
            hard coded

        Returns:
            pd.DataFrame:
        """
    df = pd.read_csv('/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/trade_share_data.csv')

    #  Keeping only relevant columns: COUNTRY, INDICATOR, years
    year_cols = [str(y) for y in range(1948, 2023)]  # adjust if needed
    df = df[['COUNTRY', 'INDICATOR'] + year_cols]

    # Melt to long format
    df_long = df.melt(id_vars=['COUNTRY', 'INDICATOR'],
                                              var_name='year', value_name='Value')

    # Pivot so exports and imports are separate columns

    df_long = df_long.pivot_table(index=['COUNTRY', 'year'],
                                                          columns='INDICATOR',
                                                          values='Value').reset_index()

    df_long["export_share"] = (df_long["Exports of goods, Free on board (FOB), US dollar"] /
                               (df_long["Exports of goods, Free on board (FOB), US dollar"]
                                      + df_long["Imports of goods, Cost insurance freight (CIF), US dollar"]
                              ))

    # Some renaming and Data filtering

    df_long.rename(columns={"COUNTRY": "country"}, inplace=True)


    return df_long


def load_TFP():
    """
    Loads total factor productivity data from the Penn World Tables, TFP at constant national prices (2021=1)
    Parameters:
        hard coded.

    Returns:
        pd.DataFrame: cleaned TFP data.
    """
    df = pd.read_excel('/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/TFP_Data.xlsx')

    # keep only the needed columns & format year column

    columns_to_keep = ["country", "year", "v2x_regime", "rtfpna"]
    df = df[[col for col in columns_to_keep if col in df.columns]]


    return df


def load_vdem_corr():
    """
    Loads Political Corruption index, Executive corruption index, Public sector corruption index  from the V_dem Database, v2x_corr, v2x_execorr, v2x_pubcorr
    Parameters:
        hard coded.

    Returns:
        pd.DataFrame: cleaned V_dem corruption data.
    """
    df = pd.read_csv('/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/V-Dem-CY-Full+Others-v15.csv')

    # keep only the needed columns & format year column

    df.rename(columns={"country_name": "country"}, inplace=True)
    cols_to_keep = ["country", "year", "v2x_corr", "v2x_execorr", "v2x_pubcorr"]
    df = df[cols_to_keep]


    # Filter for years 1950–2022
    df = df[(df["year"] >= 1950) & (df["year"] <= 2022)]


    return df



def load_vdem_corr():
    """
    Loads Political Corruption index, Executive corruption index, Public sector corruption index  from the V_dem Database, v2x_corr, v2x_execorr, v2x_pubcorr
    Parameters:
        hard coded.

    Returns:
        pd.DataFrame: cleaned V_dem corruption data.
    """
    df = pd.read_csv('/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/V-Dem-CY-Full+Others-v15.csv')

    # keep only the needed columns & format year column

    df.rename(columns={"country_name": "country"}, inplace=True)
    cols_to_keep = ["country", "year", "v2x_corr", "v2x_execorr", "v2x_pubcorr"]
    df = df[cols_to_keep]


    # Filter for years 1950–2022
    df = df[(df["year"] >= 1950) & (df["year"] <= 2022)]


    return df


def load_eth_frac():
    """
    Loads Ethnic Fractionalization data, Data source: Alesina, Devleeschauwer, Easterly, Kurlat and Wacziarg,
    Parameters:
        hard coded.

    Returns:
        pd.DataFrame: cleaned  data.
    """
    df = pd.read_excel("/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/Ethnic_Fractionalization.xlsx")

    # keep only the needed columns & format year column

    df.rename(columns={"cname": "country"}, inplace=True)
    cols_to_keep = ["country", "year", "fe_etfra"]
    df = df[cols_to_keep]


    # Filter for years 1950–2022
    df = df[(df["year"] >= 1950) & (df["year"] <= 2022)]


    return df

def load_lag_gdppc():
    """
    Loads lag of  gdp per capita from the maddissson data set,
    Parameters:
        hard coded.

    Returns:
        pd.DataFrame: cleaned  data.
    """
    df = pd.read_excel('/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/mpd2023_web.xlsx')

    # get the lagged value for the gdp per capita

    df = df.sort_values(["country", "year"])
    df["gdp_pc_lag1"] = df.groupby("country")["gdppc"].shift(1)

    # keep only the needed columns & format year column


    cols_to_keep = ["country", "year", "region", "gdp_pc_lag1"]
    df = df[cols_to_keep]


    # Filter for years 1950–2022
    df = df[(df["year"] >= 1950) & (df["year"] <= 2022)]


    return df

def load_inf_mor():
    """
        Loads infant mortality data from the World Bank WDI .

        Parameters:
            hard coded

        Returns:
            pd.DataFrame:
        """
    df = pd.read_csv("/Users/ghadaelhusseini/Documents/Kassel University Masters /Thesis/my_Data/Infant_mortality.csv")

    year_cols = [f"{y} [YR{y}]" for y in range(1960, 2023)]
    df = df[['Country Name', 'Series Name'] + year_cols]

    df = df.melt(
        id_vars=['Country Name', 'Series Name'],
        var_name='year',
        value_name='Value'
    )

    # Clean up year column
    df['year'] = df['year'].str.extract(r'(\d{4})').astype(int)

    df = df.rename(columns={
        "Country Name": "country",
    })

    #  Keeping only relevant columns: COUNTRY, INDICATOR, years
    cols_to_keep = ["country", "year", "Value"]
    df= df[cols_to_keep]

    return df



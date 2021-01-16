import geopandas as gpd
import matplotlib.pyplot as plt
import geoplot
import pandas as pd

powiaty = "powiaty.gpkg"

powiaty_gdf = gpd.read_file(powiaty, layer="powiaty")
gestosc_df = pd.read_csv("LUDN_2425_CTAB_20210108183351.csv", sep=";")
gestosc_df = gestosc_df[gestosc_df["Nazwa"].str.contains("Powiat")]
gestosc_df["Kod"] = gestosc_df["Kod"].astype(str)

powiaty_gdf["Kod"] = powiaty_gdf["jpt_kod_je"] + "000"
powiaty_gdf["Kod"] = powiaty_gdf["Kod"]
powiaty_gdf["Kod"] = powiaty_gdf["Kod"].str.lstrip("0")

df = powiaty_gdf.merge(gestosc_df, on="Kod", how="left")
df = df.rename(columns={"ludność na 1 km2;2019;[osoba]": "zaludnienie"})
df.plot(
    column="zaludnienie",
    cmap="RdYlGn_r",
    legend=True,
    figsize=(15, 15),
)

plt.show()
print(df[["Kod", "zaludnienie"]])

# print(powiaty_gdf[powiaty_gdf["Kod"].str.contains("0410000")][["jpt_nazwa_", "Kod"]])
# print(gestosc_df[gestosc_df["Kod"].str.contains("0410000")][["Nazwa", "Kod"]])
# print(gestosc_df[gestosc_df["Nazwa"].str.contains("nakielski")][["Nazwa", "Kod"]])
# print(df[df["Kod"].str.contains("0410000")][["Nazwa", "Kod"]])



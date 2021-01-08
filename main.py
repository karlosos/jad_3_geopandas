import geopandas
import matplotlib.pyplot as plt
import geoplot

world = geopandas.read_file(
    geopandas.datasets.get_path('naturalearth_lowres')
)
powiaty = 'powiaty.gpkg'

gdf = geopandas.read_file(powiaty, layer='powiaty')
gdf['area'] = gdf['geometry'].area

print(gdf.columns)

fig, ax = plt.subplots(1, figsize=(14, 14))
gdf.plot(ax=ax, edgecolor='0.4', linewidth=0.5,
         column='area', cmap='Greens', legend=True, scheme='quantiles',k=5)
ax.axis('off')
plt.show()


africa = world.query('continent == "Africa"')
#print(af)
ax = geoplot.cartogram(
    africa, scale='pop_est', limits=(0.2, 1),
    edgecolor='None', figsize=(7, 8)
)
geoplot.polyplot(africa, edgecolor='gray', ax=ax)
plt.show()

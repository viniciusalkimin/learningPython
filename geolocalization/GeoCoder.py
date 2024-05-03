from pygeocoder import Geocoder
address = 'avenida paulista, 100 Sao Paulo'
print(Geocoder("AIzaSyASxgLTeWqAsT_kHQSH9o5Tcir0ZcnZO1g").geocode(address).coordinates)

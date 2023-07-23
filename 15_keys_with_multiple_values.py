#example 1
# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"): "Mumbai", \
          ("28.33'34.1", "77.06'16.6"): "Delhi"}

# Traversing dictionary with multi-keys and creating
# different lists from it
lat = []
long = []
plc = []

for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i])
print(lat)
print(long)
print(plc)

#example 2

dict = {}
x,y,z = (10,20,30)
dict[x,y,z] = x+y-z
x,y,z = (3,6,5)
dict[x,y,z] = x+y-z
print(dict)
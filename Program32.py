d={}
print(d)
d={'id':4654,'name':'surya',1:101}
print(d)
l=[1,2,3]
print(type[l])
print(type[d])
print(d.keys())
print(d.values())
print(len(d))
print(d.items())
print(d['id'])
print(d['name'])
print(d[1])
print(d.get('id'))
print(d.get('name'))
print(d.get(1))
print(d.get('loc'))
d1={}
d1=d1.copy()
print(d1)
d1=d.copy()
print(d1)
print(d.keys())
print(d.values())
d.setdefault('gender')
print(d)
d['gender']='male'
print(d)
d.update(loc='vja')
print(d)
print(d.pop('loc'))

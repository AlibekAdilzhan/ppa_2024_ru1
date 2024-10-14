caps = {"Kazakhstan": "Astana", "USA": "Washington"}

v1 = caps.setdefault("France", "Paris")
print(v1)
print(caps)
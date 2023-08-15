proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

print(proto)
proto.append("dns")
protoa.append("dns")

print(proto)
proto2 = [22,80,443,53]

proto.extend(proto2)
print(proto)

protoa.append(proto2)

print(protoa)

#removes last item from the list and prints it
print("I have removed", (proto.pop()), "from the list.")

#prints new list
print(proto)


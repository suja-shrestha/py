data = {
"total":0,
"updated":[],
"deleted":[],
"data":[]
}

while True:
    entry= str(input("Input Entry: "))

    if entry == 'Exit':
        break

elif "Update" in entry and len(entry.split("Update")) == 2:    #update logic
    #aupdate1 
    #["update", "1", 'dasdass']
    data["data"].append(entry)
    print(f"Total Entries: {len(data['data'])}")
    print(f"Total Entries: {len(data['data'])}")
    print(f"Total Entries: {len(data['data'])}")
    print(f"Total Entries: {len(data['data'])}")
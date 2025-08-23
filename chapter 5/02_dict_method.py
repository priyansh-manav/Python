marks = {
    "vashu" : 98,
    "vishakha" : 100,
    "Priyansh" : 100,
    1 : "vashu"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"vishakha":99,"munmun":100})
# print(marks)

d = {}   #empty dist..

print(marks.get("vashu"))
print(marks.get("vashu1")) # print none
print(marks["vashu1"]) # RETURN AN ERROR
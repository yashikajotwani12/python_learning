mydict={
    "yashika":"222",
    "yashikkaaa":"uuuuu",
    "marks":[1,2,3],
    "anotherdictionary":{'yashik':"ya",
                        "yas": "uuu"}

}
print(mydict['yashika'])
print(mydict['marks'])
print(mydict['anotherdictionary']['yas'])
print(list(mydict.keys()))
print(mydict.values())
print(mydict.items())
print(mydict)
updatedict={
    "mmm":"ppp",
    "iiii":"wjndjwhdj"
}
mydict.update(updatedict)
print(mydict)
print(mydict.get("mmmm"))


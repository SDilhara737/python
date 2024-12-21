


st={"a1","a2","a3","a4"}
st2={"a1","a2","b1","b2"}

print(type(st))

st3=st.intersection(st2)
st4=st.union(st2)
print(st3,st4)

st.remove("a2")
print(st)

st.remove("a5")
print(st)

st.discard("a5")
print(st)
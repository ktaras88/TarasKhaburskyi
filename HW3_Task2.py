def reverse(st):
    endfirst = st.split(" ")
    endfirst = endfirst[-1::-1]
    st = ' '.join(endfirst)
    return st
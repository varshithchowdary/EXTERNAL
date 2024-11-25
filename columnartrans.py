import math
def encrypt(key,text):
    col_len=len(key)
    row_len=math.ceil(len(text)/col_len)
    text=text.ljust(row_len*col_len,'X')
    grid=[text[i:i+col_len]for i in range(0,len(text),col_len)]
    sorted_columns=sorted(range(col_len),key=lambda k:key[k])
    enc_text=''
    for col in sorted_columns:
        track=''
        for row in grid:
            track+=row[col]
        enc_text+=track
    return enc_text,grid 
def decrypt(grid):
    dec_text=''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dec_text+=grid[i][j]
    dec_text=dec_text.rstrip('X')
    return dec_text
print('text:')
text=input()
print("key:")
key=input()
enc_text,grid=encrypt(key,text)
print(enc_text)
print(decrypt(grid))

    
    
    
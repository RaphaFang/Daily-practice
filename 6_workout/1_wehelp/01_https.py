def checkHTTPS(s):
    
    if "HTTPS" in s:
        print("T")
        return True
    else:
        print("F")
        return False

s = input().upper()
checkHTTPS(s)

# ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

"""
    @param s:{String}
    @return :{Boolean}
"""
def checkHTTPS(s):
    if "HTTPS://" in s.upper():
        return True
    else:
        return False

s = ' '
checkHTTPS(s)
# test
m = 100
a_x = m * [1]
a_y = m * [1]
a_z = m * [1]
s_x = [(m-i+1)*((m-i+1)+1)/2 for i in range(m)]
s_y = [(m-i+1)*((m-i+1)+1)/2 for i in range(m)]
s_z = [(m-i+1)*((m-i+1)+1)/2 for i in range(m)]

def iscircle(x, y, z, i, e):
    s_x[i] = 0
    s_y[i] = 0
    s_z[i] = 0
    a_x[i] = x
    a_y[i] = y
    a_x[i] = z
    for j in range(m):
        s_x[j] += x
        s_y[j] += y
        s_z[j] += z

    for j in range(m/2):
        if abs(s_x[(i + j + 1) % m]) +
           abs(s_y[(i + j + 1) % m]) +
           abs(s_z[(i + j + 1) % m]) <= 3 * e:
            return True;
    return False

def play(yaw, pitch, roll, x, y, z, i):
    if iscircle(x, y, z, i % m, 2):
        print 'CIRCLE!!'

'''
Given (x, y) coordinates, create a function such that each coordinate is uniquely mapped to an integer. 
Also make sure that given an integer, you should be able to find (x, y) coordinates. 
So F(x, y) = z and also that inverse F(z) = (x, y).

Initial thoughts:
Pairing function

F(x, y) = 0.5 * (x + y) * (x + y + 1) + y

W(z) = int((sqrt(8*z + 1) - 1) / 2)
T(w) = (w ** 2 + w) / 2
y = z - T(W(z))
x = w - y
'''
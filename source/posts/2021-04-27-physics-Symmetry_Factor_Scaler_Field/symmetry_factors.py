import numpy as np

a = 3
b = 4
c = 4
# ---------------------------------------------
aa = 1 * a
ab = 4 * a
ac = 4 * a

ba = 2 * b
bb = 3 * b
bc = 4 * b

ca = 2 * c
cb = 4 * c
cc = 3 * c
# ---------------------------------------------7
ab += ba
ac += ca
bc += cb

aaa = aa * 7 * 5 * 3
order11 = aaa

aba = ab * 3
abb = ab * 4

aca = ac * 4
acb = ac * 3

bba = bb * 7 * 5 * 3
order12 = bba

bca = bc * 1
bcb = bc * 3
bcc = bc * 3

cca = cc * 4
ccb = cc * 1
ccc = cc * 2
# -----------------------------------------------
abb += aca
abb += bca
bcb += cca
acb += ccb

abaa = aba * 1 * 3
a_ = abaa
abab = aba * 4 * 3
b_ = abab

abba = abb * 3 * 3
c_ = abba
abbb = abb * 2 * 3
d_ = abbb

acba = acb * 3
acbb = acb * 2 * 3
g_ = acbb

bcba = bcb * 3
bcbb = bcb * 2

bcca = bcc * 2 * 3
l_ = bcca
bccb = bcc * 3

ccca = ccc * 1 * 3
o_ = ccca
cccb = ccc * 4 * 3
p_ = cccb
# --------------------------------
acbaa = acba * 1
e_ = acbaa
acbab = acba * 2
f_ = acbab

bcbaa = bcba * 2
h_ = bcbaa
bcbab = bcba * 1
i_ = bcbab

bcbba = bcbb * 2
j_ = bcbba
bcbbb = bcbb * 1
k_ = bcbbb

bccba = bccb * 1
m_ = bccba
bccbb = bccb * 2
n_ = bccbb
# --------------------------------

di = np.array(['a_', 'b_', 'c_', 'd_',
               'e_', 'f_', 'g_',
               'h_', 'i_', 'j_', 'k_',
               'o_', 'p_',
               'l_', 'm_', 'n_',
               'order11', 'order12'])
sum_all = np.array([a_, b_, c_, d_,
                    e_, f_, g_,
                    h_, i_, j_, k_,
                    l_, m_, n_,
                    o_, p_,
                    order11, order12])

print(sum_all.sum())
print(11 * 9 * 105)
for i in zip(di, sum_all):
    print(i)
print(h_ + j_ + n_ + 12 * 24)
print(12*(24 + 72 + 9))

from zqwblog.renderer.core import OrgPost, MdPost

op = OrgPost('./2021-10-05-physics-BEC_limit_Tc.org')
op.gen_html()
print(op.meta)

mp = MdPost('./2020-03-18-physics-OpticsTA.md')
mp.gen_html()
print(mp.meta)
sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
out = float(19.84953)
total = float(sp + rj + mg + es + out)
totalRound = round(total, 5)
print(f'{totalRound}, ou R$180.759,98')
psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
pout = ((out/total)*100)

pspRound = round(psp, 2)
prjRound = round(prj, 2)
pmgRound = round(pmg, 2)
pesRound = round(pes, 2)
poutRound = round(pout, 2)
print(f'Porcentagem de SP {pspRound}%')
print(f'Porcentagem de RJ {prjRound}%')
print(f'Porcentagem de MG {pmgRound}%')
print(f'Porcentagem de ES {pesRound}%')
print(f'Porcentagem de OUT {poutRound}%')

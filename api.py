#%%
team = 'Barcelona'
year='2011'
import requests as rq
r = rq.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team1='+str(team)+'&page=1').json()
print(r)

# %%
r

# %%
r['data'][0]['team1goals']
# %%
n = r['total']
s = 0
for i in range(n):
    s +=int(r['data'][i]['team1goals'])
s
# %%
r1 = rq.get('https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team2='+str(team)+'&page=1').json()
r1
for i in range(n):
    s +=int(r1['data'][i]['team2goals'])
print(s)
# %%

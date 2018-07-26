# -*- coding: utf-8 -*-

import os

directory = 'C:/Users/LYDDD/Desktop/s18/vis_s18g2/'
fin = open('data/data02.csv', 'r')
fout = open('data/team_total.csv', 'w')
# fout = open('data/data02.csv', 'w')

team_list = []
team_cnt = 0

for line in fin:
	if line.split(',')[0] != 'years' and int(line.split(',')[0]) >= 1986:
		team_a = line.split(',')[1]
		team_b = line.split(',')[2]
		if team_a not in team_list:
			team_list.append(team_a)
			team_cnt += 1
		if team_b not in team_list:
			team_list.append(team_b)
			team_cnt += 1

team_list.sort()

# print(team_list)
# print(team_cnt)

for i in range(team_cnt):
	fout.write(team_list[i] + '\n')

'''
for line in fin:
	if line.split(',')[0] != 'years' and int(line.split(',')[0]) >= 1986:
		fout.write(line)
'''
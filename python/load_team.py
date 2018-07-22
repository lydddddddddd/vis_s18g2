# -*- coding: utf-8 -*-

import os

fin = open('data01.csv', 'r')
fout = open('team_total.csv', 'w')

team_list = []
team_cnt = 0

for line in fin:
	if line.split(',')[0] != 'years':
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
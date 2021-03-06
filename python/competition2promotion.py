# -*- coding: utf-8 -*-

import os
import json
import copy

directory = 'C:/Users/LYDDD/Desktop/s18/vis_s18g2/'
fin = open('data/data02.csv', 'r')
fout = open('json/promotion_tree.json', 'w')

competition_list = []
tmp_list = []

next_year = 1990
for line in fin:
	if line.split(',')[0] != 'years':
		year = int(line.split(',')[0])
		if year >= 1986:
			if next_year == year:
				next_year += 4
				competition_list.append(copy.deepcopy(tmp_list))
				print(str(next_year - 8) + " " + str(len(tmp_list)))
				tmp_list = []
			tmp_list.append(line.split('\n')[0].split(','))
			# print(tmp_list)
competition_list.append(copy.deepcopy(tmp_list))
print(str(next_year - 4) + " " + str(len(tmp_list)))
# print(competition_list)

promotion_tree = {}

promotion_tree["name"] = "tree_data"
promotion_tree["data"] = []

for i in range(9):
	year = 1986 + i * 4
	one_year_tree = {}
	# 1st
	one_year_tree["year"] = year
	com = competition_list[i][-1]
	one_year_tree["name"] = com[1] if (int(com[3]) + int(com[5])) > (int(com[4]) + int(com[6])) else com[2]
	one_year_tree["weight"] = 1.0
	one_year_tree["children"] = [{}, {}]
	# final
	f1 = one_year_tree["children"][0]
	f2 = one_year_tree["children"][1]
	f1["name"] = com[1]
	f2["name"] = com[2]
	f1["weight"] = one_year_tree["weight"] * (int(com[3]) + int(com[5]) + 1) / (int(com[3]) + int(com[4]) + int(com[5]) + int(com[6]) + 2)
	f2["weight"] = one_year_tree["weight"] * (int(com[4]) + int(com[6]) + 1) / (int(com[3]) + int(com[4]) + int(com[5]) + int(com[6]) + 2)
	f1["score"] = int(com[3]) + int(com[5])
	f2["score"] = int(com[4]) + int(com[6])
	f1["children"] = [{}, {}]
	f2["children"] = [{}, {}]
	# simifinal
	sf1 = f1["children"][0]
	sf2 = f1["children"][1]
	sf3 = f2["children"][0]
	sf4 = f2["children"][1]
	if f1["name"] in competition_list[i][-3]:
		sf_p1 = -3
		sf_p2 = -4
	elif f2["name"] in competition_list[i][-3]:
		sf_p1 = -4
		sf_p2 = -3
	else:
		print("WRONG!!!")
		break
	sf1["name"] = competition_list[i][sf_p1][1]
	sf2["name"] = competition_list[i][sf_p1][2]
	sf3["name"] = competition_list[i][sf_p2][1]
	sf4["name"] = competition_list[i][sf_p2][2]
	sf1["weight"] = f1["weight"] * (int(competition_list[i][sf_p1][3]) + int(competition_list[i][sf_p1][5]) + 1) / (int(competition_list[i][sf_p1][3]) + int(competition_list[i][sf_p1][4]) + int(competition_list[i][sf_p1][5]) + int(competition_list[i][sf_p1][6]) + 2)
	sf2["weight"] = f1["weight"] * (int(competition_list[i][sf_p1][4]) + int(competition_list[i][sf_p1][6]) + 1) / (int(competition_list[i][sf_p1][3]) + int(competition_list[i][sf_p1][4]) + int(competition_list[i][sf_p1][5]) + int(competition_list[i][sf_p1][6]) + 2)
	sf3["weight"] = f2["weight"] * (int(competition_list[i][sf_p2][3]) + int(competition_list[i][sf_p2][5]) + 1) / (int(competition_list[i][sf_p2][3]) + int(competition_list[i][sf_p2][4]) + int(competition_list[i][sf_p2][5]) + int(competition_list[i][sf_p2][6]) + 2)
	sf4["weight"] = f2["weight"] * (int(competition_list[i][sf_p2][4]) + int(competition_list[i][sf_p2][6]) + 1) / (int(competition_list[i][sf_p2][3]) + int(competition_list[i][sf_p2][4]) + int(competition_list[i][sf_p2][5]) + int(competition_list[i][sf_p2][6]) + 2)
	sf1["score"] = int(competition_list[i][sf_p1][3]) + int(competition_list[i][sf_p1][5])
	sf2["score"] = int(competition_list[i][sf_p1][4]) + int(competition_list[i][sf_p1][6])
	sf3["score"] = int(competition_list[i][sf_p2][3]) + int(competition_list[i][sf_p2][5])
	sf4["score"] = int(competition_list[i][sf_p2][4]) + int(competition_list[i][sf_p2][6])
	sf1["children"] = [{}, {}]
	sf2["children"] = [{}, {}]
	sf3["children"] = [{}, {}]
	sf4["children"] = [{}, {}]
	# quarterfinal
	qf1 = sf1["children"][0]
	qf2 = sf1["children"][1]
	qf3 = sf2["children"][0]
	qf4 = sf2["children"][1]
	qf5 = sf3["children"][0]
	qf6 = sf3["children"][1]
	qf7 = sf4["children"][0]
	qf8 = sf4["children"][1]
	for j in range(-8, -4):
		if sf1["name"] in competition_list[i][j]:
			qf_p1 = j
		if sf2["name"] in competition_list[i][j]:
			qf_p2 = j
		if sf3["name"] in competition_list[i][j]:
			qf_p3 = j
		if sf4["name"] in competition_list[i][j]:
			qf_p4 = j
	qf1["name"] = competition_list[i][qf_p1][1]
	qf2["name"] = competition_list[i][qf_p1][2]
	qf3["name"] = competition_list[i][qf_p2][1]
	qf4["name"] = competition_list[i][qf_p2][2]
	qf5["name"] = competition_list[i][qf_p3][1]
	qf6["name"] = competition_list[i][qf_p3][2]
	qf7["name"] = competition_list[i][qf_p4][1]
	qf8["name"] = competition_list[i][qf_p4][2]
	qf1["weight"] = sf1["weight"] * (int(competition_list[i][qf_p1][3]) + int(competition_list[i][qf_p1][5]) + 1) / (int(competition_list[i][qf_p1][3]) + int(competition_list[i][qf_p1][4]) + int(competition_list[i][qf_p1][5]) + int(competition_list[i][qf_p1][6]) + 2)
	qf2["weight"] = sf1["weight"] * (int(competition_list[i][qf_p1][4]) + int(competition_list[i][qf_p1][6]) + 1) / (int(competition_list[i][qf_p1][3]) + int(competition_list[i][qf_p1][4]) + int(competition_list[i][qf_p1][5]) + int(competition_list[i][qf_p1][6]) + 2)
	qf3["weight"] = sf2["weight"] * (int(competition_list[i][qf_p2][3]) + int(competition_list[i][qf_p2][5]) + 1) / (int(competition_list[i][qf_p2][3]) + int(competition_list[i][qf_p2][4]) + int(competition_list[i][qf_p2][5]) + int(competition_list[i][qf_p2][6]) + 2)
	qf4["weight"] = sf2["weight"] * (int(competition_list[i][qf_p2][4]) + int(competition_list[i][qf_p2][6]) + 1) / (int(competition_list[i][qf_p2][3]) + int(competition_list[i][qf_p2][4]) + int(competition_list[i][qf_p2][5]) + int(competition_list[i][qf_p2][6]) + 2)
	qf5["weight"] = sf3["weight"] * (int(competition_list[i][qf_p3][3]) + int(competition_list[i][qf_p3][5]) + 1) / (int(competition_list[i][qf_p3][3]) + int(competition_list[i][qf_p3][4]) + int(competition_list[i][qf_p3][5]) + int(competition_list[i][qf_p3][6]) + 2)
	qf6["weight"] = sf3["weight"] * (int(competition_list[i][qf_p3][4]) + int(competition_list[i][qf_p3][6]) + 1) / (int(competition_list[i][qf_p3][3]) + int(competition_list[i][qf_p3][4]) + int(competition_list[i][qf_p3][5]) + int(competition_list[i][qf_p3][6]) + 2)
	qf7["weight"] = sf4["weight"] * (int(competition_list[i][qf_p4][3]) + int(competition_list[i][qf_p4][5]) + 1) / (int(competition_list[i][qf_p4][3]) + int(competition_list[i][qf_p4][4]) + int(competition_list[i][qf_p4][5]) + int(competition_list[i][qf_p4][6]) + 2)
	qf8["weight"] = sf4["weight"] * (int(competition_list[i][qf_p4][4]) + int(competition_list[i][qf_p4][6]) + 1) / (int(competition_list[i][qf_p4][3]) + int(competition_list[i][qf_p4][4]) + int(competition_list[i][qf_p4][5]) + int(competition_list[i][qf_p4][6]) + 2)
	qf1["score"] = int(competition_list[i][qf_p1][3]) + int(competition_list[i][qf_p1][5])
	qf2["score"] = int(competition_list[i][qf_p1][4]) + int(competition_list[i][qf_p1][6])
	qf3["score"] = int(competition_list[i][qf_p2][3]) + int(competition_list[i][qf_p2][5])
	qf4["score"] = int(competition_list[i][qf_p2][4]) + int(competition_list[i][qf_p2][6])
	qf5["score"] = int(competition_list[i][qf_p3][3]) + int(competition_list[i][qf_p3][5])
	qf6["score"] = int(competition_list[i][qf_p3][4]) + int(competition_list[i][qf_p3][6])
	qf7["score"] = int(competition_list[i][qf_p4][3]) + int(competition_list[i][qf_p4][5])
	qf8["score"] = int(competition_list[i][qf_p4][4]) + int(competition_list[i][qf_p4][6])
	qf1["children"] = [{}, {}]
	qf2["children"] = [{}, {}]
	qf3["children"] = [{}, {}]
	qf4["children"] = [{}, {}]
	qf5["children"] = [{}, {}]
	qf6["children"] = [{}, {}]
	qf7["children"] = [{}, {}]
	qf8["children"] = [{}, {}]
	# round of 16
	ef1 = qf1["children"][0]
	ef2 = qf1["children"][1]
	ef3 = qf2["children"][0]
	ef4 = qf2["children"][1]
	ef5 = qf3["children"][0]
	ef6 = qf3["children"][1]
	ef7 = qf4["children"][0]
	ef8 = qf4["children"][1]
	ef9 = qf5["children"][0]
	ef10 = qf5["children"][1]
	ef11 = qf6["children"][0]
	ef12 = qf6["children"][1]
	ef13 = qf7["children"][0]
	ef14 = qf7["children"][1]
	ef15 = qf8["children"][0]
	ef16 = qf8["children"][1]
	for j in range(-16, -8):
		if qf1["name"] in competition_list[i][j]:
			ef_p1 = j
		if qf2["name"] in competition_list[i][j]:
			ef_p2 = j
		if qf3["name"] in competition_list[i][j]:
			ef_p3 = j
		if qf4["name"] in competition_list[i][j]:
			ef_p4 = j
		if qf5["name"] in competition_list[i][j]:
			ef_p5 = j
		if qf6["name"] in competition_list[i][j]:
			ef_p6 = j
		if qf7["name"] in competition_list[i][j]:
			ef_p7 = j
		if qf8["name"] in competition_list[i][j]:
			ef_p8 = j
	ef1["name"] = competition_list[i][ef_p1][1]
	ef2["name"] = competition_list[i][ef_p1][2]
	ef3["name"] = competition_list[i][ef_p2][1]
	ef4["name"] = competition_list[i][ef_p2][2]
	ef5["name"] = competition_list[i][ef_p3][1]
	ef6["name"] = competition_list[i][ef_p3][2]
	ef7["name"] = competition_list[i][ef_p4][1]
	ef8["name"] = competition_list[i][ef_p4][2]
	ef9["name"] = competition_list[i][ef_p5][1]
	ef10["name"] = competition_list[i][ef_p5][2]
	ef11["name"] = competition_list[i][ef_p6][1]
	ef12["name"] = competition_list[i][ef_p6][2]
	ef13["name"] = competition_list[i][ef_p7][1]
	ef14["name"] = competition_list[i][ef_p7][2]
	ef15["name"] = competition_list[i][ef_p8][1]
	ef16["name"] = competition_list[i][ef_p8][2]
	ef1["weight"] = qf1["weight"] * (int(competition_list[i][ef_p1][3]) + int(competition_list[i][ef_p1][5]) + 1) / (int(competition_list[i][ef_p1][3]) + int(competition_list[i][ef_p1][4]) + int(competition_list[i][ef_p1][5]) + int(competition_list[i][ef_p1][6]) + 2)
	ef2["weight"] = qf1["weight"] * (int(competition_list[i][ef_p1][4]) + int(competition_list[i][ef_p1][6]) + 1) / (int(competition_list[i][ef_p1][3]) + int(competition_list[i][ef_p1][4]) + int(competition_list[i][ef_p1][5]) + int(competition_list[i][ef_p1][6]) + 2)
	ef3["weight"] = qf2["weight"] * (int(competition_list[i][ef_p2][3]) + int(competition_list[i][ef_p2][5]) + 1) / (int(competition_list[i][ef_p2][3]) + int(competition_list[i][ef_p2][4]) + int(competition_list[i][ef_p2][5]) + int(competition_list[i][ef_p2][6]) + 2)
	ef4["weight"] = qf2["weight"] * (int(competition_list[i][ef_p2][4]) + int(competition_list[i][ef_p2][6]) + 1) / (int(competition_list[i][ef_p2][3]) + int(competition_list[i][ef_p2][4]) + int(competition_list[i][ef_p2][5]) + int(competition_list[i][ef_p2][6]) + 2)
	ef5["weight"] = qf3["weight"] * (int(competition_list[i][ef_p3][3]) + int(competition_list[i][ef_p3][5]) + 1) / (int(competition_list[i][ef_p3][3]) + int(competition_list[i][ef_p3][4]) + int(competition_list[i][ef_p3][5]) + int(competition_list[i][ef_p3][6]) + 2)
	ef6["weight"] = qf3["weight"] * (int(competition_list[i][ef_p3][4]) + int(competition_list[i][ef_p3][6]) + 1) / (int(competition_list[i][ef_p3][3]) + int(competition_list[i][ef_p3][4]) + int(competition_list[i][ef_p3][5]) + int(competition_list[i][ef_p3][6]) + 2)
	ef7["weight"] = qf4["weight"] * (int(competition_list[i][ef_p4][3]) + int(competition_list[i][ef_p4][5]) + 1) / (int(competition_list[i][ef_p4][3]) + int(competition_list[i][ef_p4][4]) + int(competition_list[i][ef_p4][5]) + int(competition_list[i][ef_p4][6]) + 2)
	ef8["weight"] = qf4["weight"] * (int(competition_list[i][ef_p4][4]) + int(competition_list[i][ef_p4][6]) + 1) / (int(competition_list[i][ef_p4][3]) + int(competition_list[i][ef_p4][4]) + int(competition_list[i][ef_p4][5]) + int(competition_list[i][ef_p4][6]) + 2)
	ef9["weight"] = qf5["weight"] * (int(competition_list[i][ef_p5][3]) + int(competition_list[i][ef_p5][5]) + 1) / (int(competition_list[i][ef_p5][3]) + int(competition_list[i][ef_p5][4]) + int(competition_list[i][ef_p5][5]) + int(competition_list[i][ef_p5][6]) + 2)
	ef10["weight"] = qf5["weight"] * (int(competition_list[i][ef_p5][4]) + int(competition_list[i][ef_p5][6]) + 1) / (int(competition_list[i][ef_p5][3]) + int(competition_list[i][ef_p5][4]) + int(competition_list[i][ef_p5][5]) + int(competition_list[i][ef_p5][6]) + 2)
	ef11["weight"] = qf6["weight"] * (int(competition_list[i][ef_p6][3]) + int(competition_list[i][ef_p6][5]) + 1) / (int(competition_list[i][ef_p6][3]) + int(competition_list[i][ef_p6][4]) + int(competition_list[i][ef_p6][5]) + int(competition_list[i][ef_p6][6]) + 2)
	ef12["weight"] = qf6["weight"] * (int(competition_list[i][ef_p6][4]) + int(competition_list[i][ef_p6][6]) + 1) / (int(competition_list[i][ef_p6][3]) + int(competition_list[i][ef_p6][4]) + int(competition_list[i][ef_p6][5]) + int(competition_list[i][ef_p6][6]) + 2)
	ef13["weight"] = qf7["weight"] * (int(competition_list[i][ef_p7][3]) + int(competition_list[i][ef_p7][5]) + 1) / (int(competition_list[i][ef_p7][3]) + int(competition_list[i][ef_p7][4]) + int(competition_list[i][ef_p7][5]) + int(competition_list[i][ef_p7][6]) + 2)
	ef14["weight"] = qf7["weight"] * (int(competition_list[i][ef_p7][4]) + int(competition_list[i][ef_p7][6]) + 1) / (int(competition_list[i][ef_p7][3]) + int(competition_list[i][ef_p7][4]) + int(competition_list[i][ef_p7][5]) + int(competition_list[i][ef_p7][6]) + 2)
	ef15["weight"] = qf8["weight"] * (int(competition_list[i][ef_p8][3]) + int(competition_list[i][ef_p8][5]) + 1) / (int(competition_list[i][ef_p8][3]) + int(competition_list[i][ef_p8][4]) + int(competition_list[i][ef_p8][5]) + int(competition_list[i][ef_p8][6]) + 2)
	ef16["weight"] = qf8["weight"] * (int(competition_list[i][ef_p8][4]) + int(competition_list[i][ef_p8][6]) + 1) / (int(competition_list[i][ef_p8][3]) + int(competition_list[i][ef_p8][4]) + int(competition_list[i][ef_p8][5]) + int(competition_list[i][ef_p8][6]) + 2)
	ef1["score"] = int(competition_list[i][ef_p1][3]) + int(competition_list[i][ef_p1][5])
	ef2["score"] = int(competition_list[i][ef_p1][4]) + int(competition_list[i][ef_p1][6])
	ef3["score"] = int(competition_list[i][ef_p2][3]) + int(competition_list[i][ef_p2][5])
	ef4["score"] = int(competition_list[i][ef_p2][4]) + int(competition_list[i][ef_p2][6])
	ef5["score"] = int(competition_list[i][ef_p3][3]) + int(competition_list[i][ef_p3][5])
	ef6["score"] = int(competition_list[i][ef_p3][4]) + int(competition_list[i][ef_p3][6])
	ef7["score"] = int(competition_list[i][ef_p4][3]) + int(competition_list[i][ef_p4][5])
	ef8["score"] = int(competition_list[i][ef_p4][4]) + int(competition_list[i][ef_p4][6])
	ef9["score"] = int(competition_list[i][ef_p5][3]) + int(competition_list[i][ef_p5][5])
	ef10["score"] = int(competition_list[i][ef_p5][4]) + int(competition_list[i][ef_p5][6])
	ef11["score"] = int(competition_list[i][ef_p6][3]) + int(competition_list[i][ef_p6][5])
	ef12["score"] = int(competition_list[i][ef_p6][4]) + int(competition_list[i][ef_p6][6])
	ef13["score"] = int(competition_list[i][ef_p7][3]) + int(competition_list[i][ef_p7][5])
	ef14["score"] = int(competition_list[i][ef_p7][4]) + int(competition_list[i][ef_p7][6])
	ef15["score"] = int(competition_list[i][ef_p8][3]) + int(competition_list[i][ef_p8][5])
	ef16["score"] = int(competition_list[i][ef_p8][4]) + int(competition_list[i][ef_p8][6])
	ef1["children"] = []
	ef2["children"] = []
	ef3["children"] = []
	ef4["children"] = []
	ef5["children"] = []
	ef6["children"] = []
	ef7["children"] = []
	ef8["children"] = []
	ef9["children"] = []
	ef10["children"] = []
	ef11["children"] = []
	ef12["children"] = []
	ef13["children"] = []
	ef14["children"] = []
	ef15["children"] = []
	ef16["children"] = []
	# first round
	ef1_child_name = []
	ef2_child_name = []
	ef3_child_name = []
	ef4_child_name = []
	ef5_child_name = []
	ef6_child_name = []
	ef7_child_name = []
	ef8_child_name = []
	ef9_child_name = []
	ef10_child_name = []
	ef11_child_name = []
	ef12_child_name = []
	ef13_child_name = []
	ef14_child_name = []
	ef15_child_name = []
	ef16_child_name = []
	first_round_cnt = 36
	if year > 1994:
		first_round_cnt = 48
	for j in range(-16 - first_round_cnt, -16):
		if ef1["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef1_child_name:
				ef1_child_name.append(competition_list[i][j][1])
				ef1["children"].append({"name" : competition_list[i][j][1], "size" : ef1["weight"] / 4})
			if competition_list[i][j][2] not in ef1_child_name:
				ef1_child_name.append(competition_list[i][j][2])
				ef1["children"].append({"name" : competition_list[i][j][2], "size" : ef1["weight"] / 4})
		if ef2["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef2_child_name:
				ef2_child_name.append(competition_list[i][j][1])
				ef2["children"].append({"name" : competition_list[i][j][1], "size" : ef2["weight"] / 4})
			if competition_list[i][j][2] not in ef2_child_name:
				ef2_child_name.append(competition_list[i][j][2])
				ef2["children"].append({"name" : competition_list[i][j][2], "size" : ef2["weight"] / 4})
		if ef3["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef3_child_name:
				ef3_child_name.append(competition_list[i][j][1])
				ef3["children"].append({"name" : competition_list[i][j][1], "size" : ef3["weight"] / 4})
			if competition_list[i][j][2] not in ef3_child_name:
				ef3_child_name.append(competition_list[i][j][2])
				ef3["children"].append({"name" : competition_list[i][j][2], "size" : ef3["weight"] / 4})
		if ef4["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef4_child_name:
				ef4_child_name.append(competition_list[i][j][1])
				ef4["children"].append({"name" : competition_list[i][j][1], "size" : ef4["weight"] / 4})
			if competition_list[i][j][2] not in ef4_child_name:
				ef4_child_name.append(competition_list[i][j][2])
				ef4["children"].append({"name" : competition_list[i][j][2], "size" : ef4["weight"] / 4})
		if ef5["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef5_child_name:
				ef5_child_name.append(competition_list[i][j][1])
				ef5["children"].append({"name" : competition_list[i][j][1], "size" : ef5["weight"] / 4})
			if competition_list[i][j][2] not in ef5_child_name:
				ef5_child_name.append(competition_list[i][j][2])
				ef5["children"].append({"name" : competition_list[i][j][2], "size" : ef5["weight"] / 4})
		if ef6["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef6_child_name:
				ef6_child_name.append(competition_list[i][j][1])
				ef6["children"].append({"name" : competition_list[i][j][1], "size" : ef6["weight"] / 4})
			if competition_list[i][j][2] not in ef6_child_name:
				ef6_child_name.append(competition_list[i][j][2])
				ef6["children"].append({"name" : competition_list[i][j][2], "size" : ef6["weight"] / 4})
		if ef7["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef7_child_name:
				ef7_child_name.append(competition_list[i][j][1])
				ef7["children"].append({"name" : competition_list[i][j][1], "size" : ef7["weight"] / 4})
			if competition_list[i][j][2] not in ef7_child_name:
				ef7_child_name.append(competition_list[i][j][2])
				ef7["children"].append({"name" : competition_list[i][j][2], "size" : ef7["weight"] / 4})
		if ef8["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef8_child_name:
				ef8_child_name.append(competition_list[i][j][1])
				ef8["children"].append({"name" : competition_list[i][j][1], "size" : ef8["weight"] / 4})
			if competition_list[i][j][2] not in ef8_child_name:
				ef8_child_name.append(competition_list[i][j][2])
				ef8["children"].append({"name" : competition_list[i][j][2], "size" : ef8["weight"] / 4})
		if ef9["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef9_child_name:
				ef9_child_name.append(competition_list[i][j][1])
				ef9["children"].append({"name" : competition_list[i][j][1], "size" : ef9["weight"] / 4})
			if competition_list[i][j][2] not in ef9_child_name:
				ef9_child_name.append(competition_list[i][j][2])
				ef9["children"].append({"name" : competition_list[i][j][2], "size" : ef9["weight"] / 4})
		if ef10["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef10_child_name:
				ef10_child_name.append(competition_list[i][j][1])
				ef10["children"].append({"name" : competition_list[i][j][1], "size" : ef10["weight"] / 4})
			if competition_list[i][j][2] not in ef10_child_name:
				ef10_child_name.append(competition_list[i][j][2])
				ef10["children"].append({"name" : competition_list[i][j][2], "size" : ef10["weight"] / 4})
		if ef11["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef11_child_name:
				ef11_child_name.append(competition_list[i][j][1])
				ef11["children"].append({"name" : competition_list[i][j][1], "size" : ef11["weight"] / 4})
			if competition_list[i][j][2] not in ef11_child_name:
				ef11_child_name.append(competition_list[i][j][2])
				ef11["children"].append({"name" : competition_list[i][j][2], "size" : ef11["weight"] / 4})
		if ef12["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef12_child_name:
				ef12_child_name.append(competition_list[i][j][1])
				ef12["children"].append({"name" : competition_list[i][j][1], "size" : ef12["weight"] / 4})
			if competition_list[i][j][2] not in ef12_child_name:
				ef12_child_name.append(competition_list[i][j][2])
				ef12["children"].append({"name" : competition_list[i][j][2], "size" : ef12["weight"] / 4})
		if ef13["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef13_child_name:
				ef13_child_name.append(competition_list[i][j][1])
				ef13["children"].append({"name" : competition_list[i][j][1], "size" : ef13["weight"] / 4})
			if competition_list[i][j][2] not in ef13_child_name:
				ef13_child_name.append(competition_list[i][j][2])
				ef13["children"].append({"name" : competition_list[i][j][2], "size" : ef13["weight"] / 4})
		if ef14["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef14_child_name:
				ef14_child_name.append(competition_list[i][j][1])
				ef14["children"].append({"name" : competition_list[i][j][1], "size" : ef14["weight"] / 4})
			if competition_list[i][j][2] not in ef14_child_name:
				ef14_child_name.append(competition_list[i][j][2])
				ef14["children"].append({"name" : competition_list[i][j][2], "size" : ef14["weight"] / 4})
		if ef15["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef15_child_name:
				ef15_child_name.append(competition_list[i][j][1])
				ef15["children"].append({"name" : competition_list[i][j][1], "size" : ef15["weight"] / 4})
			if competition_list[i][j][2] not in ef15_child_name:
				ef15_child_name.append(competition_list[i][j][2])
				ef15["children"].append({"name" : competition_list[i][j][2], "size" : ef15["weight"] / 4})
		if ef16["name"] in competition_list[i][j]:
			if competition_list[i][j][1] not in ef16_child_name:
				ef16_child_name.append(competition_list[i][j][1])
				ef16["children"].append({"name" : competition_list[i][j][1], "size" : ef16["weight"] / 4})
			if competition_list[i][j][2] not in ef16_child_name:
				ef16_child_name.append(competition_list[i][j][2])
				ef16["children"].append({"name" : competition_list[i][j][2], "size" : ef16["weight"] / 4})
	# finish
	promotion_tree["data"].append(one_year_tree)

json.dump(promotion_tree, fout, indent = 4)
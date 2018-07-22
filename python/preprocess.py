# -*- coding: utf-8 -*-

import os
import re

directory = 'C:/Users/LYDDD/Desktop/s18/world-cup-master/'
fout = open('data.csv', 'w')
status = ''
year = ''
month = ''
day = ''
team_1 = ''
team_2 = ''
score_1 = ''
score_2 = ''
score_pen_1 = ''
score_pen_2 = ''


for folder in os.listdir(directory):
	# print(folder)
	if folder.find('--') != -1:
		year = folder.split('--')[0]
		place = folder.split('--')[1]
		# print(year + ' ' + place)
		for file in os.listdir(directory + folder):
			if file.find('.txt') != -1:
				# print(file)
				f = open(directory + folder + '/' + file)
				for line in f:
					match_num = line.split(' ')[0]
					if match_num != '' and match_num[0] == '(':
						# print(line)
						pos = 1
						status = 'load_date'
						while line.split(' ')[pos] == '' or line.split(' ')[pos][-1] != '\n':
							if line.split(' ')[pos] == '':
								pos += 1
								continue
							if status == 'load_date':
								if line.split(' ')[pos].isdigit() == True:
									day = line.split(' ')[pos]
									pos += 1
									month = line.split(' ')[pos]
									status = 'load_team_1'
									# fout.write(year + ',' + month + ',' + day + ',')
								elif line.split(' ')[pos] in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
									pos += 1
									month = line.split(' ')[pos].split('/')[0]
									day = line.split(' ')[pos].split('/')[1]
									pos += 1
									status = 'load_team_1'
									# fout.write(year + ',' + month + ',' + day + ',')
								else:
									status = 'exit'
							elif status == 'load_team_1':
								team_1 = line.split(' ')[pos]
								while line.split(' ')[pos + 1] != '' and line.split(' ')[pos + 1][0].isalpha() == True:
									team_1 += ' ' + line.split(' ')[pos + 1]
									pos += 1
								status = 'load_score'
								# fout.write(team_1 + ',')
							elif status == 'load_score':
								if line.split(' ')[pos] == '-':
									status = 'exit'
									pos += 1
									continue
								elif line.split(' ')[pos + 1] == '':
									result = re.split('[-–]', line.split(' ')[pos])
									result = [x for x in result if x]
									score_1 = result[0]
									score_2 = result[1]
									score_pen_1 = '0'
									score_pen_2 = '0'
								elif line.split(' ')[pos + 1][0] == '(':
									result = re.split('[-–]', line.split(' ')[pos])
									result = [x for x in result if x]
									score_1 = result[0]
									score_2 = result[1]
									score_pen_1 = '0'
									score_pen_2 = '0'
									pos += 1
								elif line.split(' ')[pos + 1] == 'a.e.t.':
									result = re.split('[-–]', line.split(' ')[pos])
									result = [x for x in result if x]
									score_1 = result[0]
									score_2 = result[1]
									score_pen_1 = '0'
									score_pen_2 = '0'
									pos += 3
								elif line.split(' ')[pos + 1] == 'pen.':
									result = re.split('[-–]', line.split(' ')[pos])
									result = [x for x in result if x]
									score_pen_1 = result[0]
									score_pen_2 = result[1]
									result = re.split('[-–]', line.split(' ')[pos + 2])
									result = [x for x in result if x]
									score_1 = result[0]
									score_2 = result[1]
									pos += 5
								status = 'load_team_2'
								# fout.write(score_1 + ',' + score_2 + ',' + score_pen_1 + ',' + score_pen_2 + ',')
							elif status == 'load_team_2':
								team_2 = line.split(' ')[pos]
								while line.split(' ')[pos + 1] != '' and line.split(' ')[pos + 1][0].isalpha() == True:
									team_2 += ' ' + line.split(' ')[pos + 1]
									pos += 1
								status = 'finish'
								# fout.write(team_2 + '\n')
							elif status == 'finish':
								fout.write(year + ',' + month + ',' + day + ',' + team_1 + ',' + team_2 + ',' + score_1 + ',' + score_2 + ',' + score_pen_1 + ',' + score_pen_2 + '\n')
								break
							elif status == 'exit':
								break
							pos += 1
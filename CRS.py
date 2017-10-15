

main_words =['corporate social responsibility', 'corporate conscience','csr','ethical business model']
key_words = [ 'ecomic', 'environmental', 'Social imperatives','business management','corporate','company', 'buisness','business model','industry self-regulation',
				'corporate self-regulation','ethical standards','spirit of the law','enterprise', 'conglomorate','responsible business']
key_issues = ['environmental management', 'eco-efficiency','responsible sourcing', 'stakeholders engagement', 'labour standards and working conditions', 
				'employee and community relations', 'company and community relations' , 'social enquiry', 'gender balance', 'human rights', 'anti-corruption measure'
				'good governance', 'community building']
key_benefits = ['improve brand image', 'enhance customer loyalty', 'better decision making']

list_of_lists = [main_words, key_words, key_issues, key_benefits]

points = 0;
value = 0;
main_words_points = 10;
key_words_points = 5;
key_issues_points = 3;
key_benefits_points = 2;



title = tup[0]
paragraphs = tup[1]
num_of_paragraphs = len(paragraphs) 

title = title.lower()


for i in range(len(list_of_lists)):
	for j in range(len(list_of_lists[i])):
		value = title.find(list_of_lists[i][j])
		if(value != -1):
			switcher ={
				list_of_lists[0]: points + main_words_points,
				list_of_lists[1]: points + key_words_points,
				list_of_lists[2]: points + key_issues_points,
				list_of_lists[3]: points + key_benefits_points,
			}


for i in range(num_of_paragraphs):
	string = paragraphs[i].lower()
	for j in range(len(list_of_lists[i])):
		for k in range(len(list_of_lists[i][j])):
			value = string.find(list_of_lists[i][j][k])
			if(value != -1):
				switcher ={
				list_of_lists[0]: points + main_words_points,
				list_of_lists[1]: points + key_words_points,
				list_of_lists[2]: points + key_issues_points,
				list_of_lists[3]: points + key_benefits_points,
				}

# for i in range(0, num_of_paragraphs):
# 	string = paragraphs[i].lower()

# 	for j in range(len(main_words)):
# 		value = string.find(main_words[j])
# 		if(value != -1):
# 			points += main_words_points

# 	for j in range(len(key_words)):
# 		value = string.find(key_words[j])
# 		if(value != -1):
# 			points += key_words_points


# 	for j in range(len(key_issues)):
# 		value = string.find(key_issues[j])
# 		if(value != -1):
# 			points += key_issues_points

# 	for j in range(len(key_benefits)):
# 		value = string.find(key_benefits[j])
# 		if(value != -1):
# 			points += key_benefits_points





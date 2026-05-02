import random

random.seed(42)
seqs_file=open("/work/yinlab/mislam17/course_project_1/part_4/random_selected_extracted_domains_02.faa").readlines()
f=open("/work/yinlab/mislam17/course_project_1/part_4/20250923_105539/analysis/GROUPS_140_Info.txt").readlines()[1:]
g=open("/work/yinlab/mislam17/course_project_1/part_4/20250923_105539/NodeTable_cs.txt").readlines()[1:]
char_ids=[x.rstrip().split("\t")[0] for x in open("/work/yinlab/mislam17/course_project_1/part_4/Characterized_ids_22_Sep_2025.txt").readlines()[1:]]
subfams_old=[int(x.split()[1]) for x in open("/work/yinlab/mislam17/course_project_1/part_4/20250923_105539/analysis/GROUPS_140_Info.txt").readlines()[1:]]
subfams=set([int(x.split()[1]) for x in open("/work/yinlab/mislam17/course_project_1/part_4/20250923_105539/analysis/GROUPS_140_Info.txt").readlines()[1:]])
#print (subfams)
#print ("Subfamily SubFam_seqs Char_seqs EC_nums")
random_final=[]
for x in sorted(subfams):
	#print (f"Subfamily {x}:",subfams_old.count(x))
	sub_ids=[]
	if subfams_old.count(x)>=20:
		for i in f:
			i=i.rstrip().split()
			if int(i[1])==x:
				for j in g:
					j=j.rstrip().split()
					if int(i[0])==int(j[0]):
						#print (i,j)
						if j[1].split("|")[0] not in sub_ids:
							sub_ids.append(j[1].split("|")[0])

	ids_common=set(sub_ids).intersection(set(char_ids))
	#print (ids_common)
	#print ("characterzied ids count:",len(ids_common))
	if len(ids_common)>=1:
		#print ("characterzied ids count:",len(ids_common))
			#print (sub_ids)
		if len(sub_ids)<=30:
			random_sample=sub_ids
		elif len(sub_ids)>= 30:
			random_sample=random.sample(sub_ids,30)
		random_sample.extend(ids_common)
		#print ("Random sample after adding the characterized ids",len(random_sample))
		random_final.extend(random_sample)
		#print (len(random_sample))
		ec_nums=[]
		for id in ids_common:
			for uu in open("/work/yinlab/mislam17/course_project_1/part_4/Characterized_ids_22_Sep_2025.txt").readlines()[1:]:
				uu=uu.split("\t")
				if id==uu[0]:
					#print (uu[1].rstrip())
					ec_nums.append(uu[1].rstrip().replace(" ", "").replace(",","|"))
		#print (f"Subfamily-{x}",subfams_old.count(x),len(set(ids_common)),"|".join(list(set(ec_nums))))
	else:
		pass
#print ("Total no. of seqs",len(random_final))
#print ("Total number of sequences:",len(set(random_final)))
for id in set(random_final):
	for x in range(0,len(seqs_file)):
		if id in seqs_file[x]:
			print (seqs_file[x].rstrip())
			print (seqs_file[x+1].rstrip())
			break



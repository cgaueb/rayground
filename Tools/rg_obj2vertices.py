import sys

def file_parser(filename):
	with open(filename) as f:
		return [' '.join(x.split()).split(" ") for x in f.readlines()]

def get_v(data):
	return [x[1:] for x in data if x[0]=='v']

def get_f(data):
	fs=[x[1:] for x in data if x[0]=='f']
	slashes=fs[0][0].count("/")
	return [[int(x.split(slashes*"/")[0]) for x in y] for y in fs]

def txt_v(v_data,f_data):
	all_f_data=[]
	for i in f_data:
		counter=0
		while(True):
			all_f_data.append(i[0])
			all_f_data.append(i[counter+1])
			all_f_data.append(i[counter+2])
			counter+=1
			if(counter+2>=len(i)):
				break

	txt=""
	for i in all_f_data:
		for k in v_data[i-1]:
				txt+=str(k)+","	
	return txt[:-1]

if __name__ == '__main__':
	obj_file=sys.argv[1]
	vert_file=sys.argv[2]
	data=file_parser(obj_file)
	v_data=get_v(data)
	f_data=get_f(data)

	out_file=open(vert_file,'w')
	out_file.write(txt_v(v_data,f_data))
	out_file.close()
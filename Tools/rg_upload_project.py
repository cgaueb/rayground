import sys

input_filename=sys.argv[1]
output_filename=sys.argv[2]
f = open(input_filename, "r")
data=f.read()
data=data.split('\x00')[:5]
scene=data[0]
generate=data[1]
hit=data[2]
miss=data[3]
post_process=data[4]
txt="updateProjectData(GetProjectID(), '{}', '{}', '{}', '{}', '{}');" .format(scene,generate,hit,miss,post_process)
txt=txt.replace("\n","\\n")
output_file=open(output_filename,'w')
output_file.write(txt)
output_file.close()
#coding=utf8
import quopri
import csv
#qp解码
def qp_decode(str):
	return quopri.decodestring(str).decode()

#qp编码
def qp_encode(str):
	return quopri.encodestring(str.encode()).decode()

f = csv.reader(open('./csv/other.csv', 'r', encoding = 'utf-8'))
with open("vcf/other.vcf","w", encoding = 'utf-8')as v:
	for row in f:
		print(row)
		v.write("BEGIN:VCARD"+"\n")
		v.write("VERSION:2.1"+"\n")
		v.write("N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;"+qp_encode(row[2] + '-' + row[0])+";;;\n")
		#v.write("FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"+qp_encode(row[2] + '-' + row[0])+"\n")
		#v.write("ORG;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"+qp_encode(row[1])+"\n")
		# v.write("TITLE;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:"+qp_encode(row[2])+"\n")
		v.write("TEL;CELL:"+row[3]+"\n")
		#v.write("TEL;WORK:"+row[4]+"\n")
		v.write("END:VCARD"+"\n")
print('finished')

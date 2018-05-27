from pwn import *
import itertools

def answer_is_invalid_input(answer):
	return "% Invalid input detected at '^' marker." in answer

	
def collect_answers(command, params, prompt, io):
	for param in params:
		io.sendline(command + " " + param)
		answer = io.recvregex(prompt).split(b'\r\n')[1:-1]
		yield (param, answer)

def generate_strings(alphabet, length):
	for item in itertools.product(alphabet, repeat=length):
		yield "".join(item)

prompt = 'banana 0 > '
command = "show"
chars = "abcdefghijklmnopqrstuvwxyz-"
count = 2


io = serialtube('/dev/ttyUSB0', baudrate=9600, timeout = 10000, convert_newlines=False)
io.newline = b'\n'
#io.send('?')
#io.send('\r')
#inputdata = io.recvregex('banana 0 > ')
#print (inputdata)
#print "LUL"


for command, answer in collect_answers(command, generate_strings(chars, count),prompt, io):
	if not answer_is_invalid_input(answer):
		print(command + ":")
		print("\n".join(answer))

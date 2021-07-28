#custom make file
#DISABLE RTTI INFO    -fno-rtti
ELIDE = -fno-elide-constructors
# nm -g -C --defined-only ${PROGNAME}.o
 
FILE=001_helloWorld
std=-std=c++11

all:exe run
    
 
exe:obj
	g++ ${std} ${FILE}.cpp  -o ${FILE}.o
 
obj:${FILE}.cpp
	g++ ${std} -Wall -c  ${FILE}.cpp
 
modules:${FILE}.cpp
	g++ -fmodules-ts ${std} -c ${FILE}.cpp
 
asm:${FILE}.cpp
	g++ ${std} -S -O0 ${FILE}.cpp
 
pre:${FILE}.cpp
	g++ ${std} -E  ${FILE}.cpp > ${FILE}.pre
 
run:
	./${FILE}.o
	
clean:
	rm *.o

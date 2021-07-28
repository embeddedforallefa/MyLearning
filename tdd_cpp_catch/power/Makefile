#custom make file
#DISABLE RTTI INFO    -fno-rtti
ELIDE = -fno-elide-constructors
# nm -g -C --defined-only ${PROGNAME}.o
 
PROJ = catch-tdd-test


INC_DIR = ./

SRC = \
	power.cpp \
	powerTest.cpp \

FLAGS = \
	-std=c++11 # if this causes errors, use '-std=c++0x' insead

INC = $(patsubst,%,-I%,$(INC_DIR))
EXE = $(PROJ)

all: BUILD RUN

BUILD:
	g++ $(FLAGS) $(INC) $(SRC) -o $(EXE)

RUN:
	./$(EXE)

clean:
	rm $(EXE)

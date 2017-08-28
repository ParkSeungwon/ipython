LIB = $(shell pkg-config python3 --libs)
INC = $(shell pkg-config python3 --cflags)
CFLAG = -std=c++11 -fmax-errors=1 -g
OBJ = $(patsubst %.cc, %.o, $(wildcard *.cc))
EXE = $(patsubst %.cpp, %.x, $(wildcard *.cpp))

all : $(EXE) $(OBJ)

%.x : %.cpp $(OBJ)
	g++ $< -o $@ $(OBJ) $(INC) $(CFLAG) $(LIB)

%.o : %.cc
	g++ -c $< $(INC) $(CFLAG)

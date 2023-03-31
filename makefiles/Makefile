CC=gcc
DEST=.build
EXENAME=main
SRC=$(shell find ../ -name "*.c")
OBJ=$(SRC:.c=.o)
LIBS=-lm
CFLAGS=-Wall -Wextra -pedantic -g -fsanitize=address -fno-omit-frame-pointer

renew: clean main

main: createbuildfolder prog

createbuildfolder:
	@TESTBF=$(wildcard $(DEST))
ifeq (,$(TESTBF))
	mkdir $(DEST)
endif

prog: $(OBJ)
	$(CC) -o $(EXENAME) $(wildcard $(DEST)/*.o) $(CFLAGS) $(LIBS)

%.o: %.c
	$(CC) $(CFLAGS) $(LIBS) -c $^ -o $(addprefix $(DEST)/,$(subst /,-,$(subst ../,,$@)))

clean:
	rm -rf $(EXENAME) $(DEST)

push:
	cd ../..
	git add .
	git commit -m "@$(USER)"
	git push
	cd -

.PHONY: main

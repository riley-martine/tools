CC = gcc
CFLAGS = -g -Wall -Wextra -Wlogical-op -Wjump-misses-init -Wdouble-promotion -Wshadow -Wformat=2 -Wmissing-prototypes -Wstrict-prototypes -pedantic -std=c99

all: prime

prime: prime.c
	$(CC) $(CFLAGS) prime.c -o prime

clean:
	rm -f prime

all: monika monika.dat

monika:
	./generate.py | tee monika

monika.dat:
	strfile monika monika.dat

clean:
	rm -f monika
	rm -f monika.dat

install: monika monika.dat
	install -m0644 monika /usr/share/games/fortunes
	install -m0644 monika.dat /usr/share/games/fortunes

.PHONY: all install clean

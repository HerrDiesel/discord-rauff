.DEFAULT_GOAL := setup_n_run
setup_n_run: setup run
setup:
	pip3 install -r requirements.txt
run:
	chmod +x discord-rauff.py
	./discord-rauff.py
install: setup
	mkdir -p /usr/bin /usr/share/man/man1
	cp discord-rauff.py /usr/bin/discord-rauff
	cp man/discord-rauff.1.gz /usr/share/man/man1/

	@echo "\ndiscord-rauff has been successfully installed!"
uninstall:
	rm -f /usr/bin/discord-rauff
	rm -f /usr/share/man/man1/discord-rauff.1.gz

	@echo "\ndiscord-rauff has been successfully uninstalled!"

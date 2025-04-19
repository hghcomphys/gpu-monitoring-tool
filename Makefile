PIXI=pixi
PIXILOCK=pixi.lock
PIXITOML=pixi.toml

.PHONY: all 
all: install gtop 

install: $(PIXITOML) $(PIXILOCK)
	@echo "Creating environment from $(PIXITOML) and $(PIXILOCK)..."
	$(PIXI) install

.PHONY: gtop 
gtop:
	@echo "Creating executable gtop..."
	@echo "$(PWD)/.pixi/envs/default/bin/python $(PWD)/gtop.py" > gtop
	@chmod +x gtop

.PHONY: pixi
pixi: check-pixi
	@echo "Pixi environment setup complete."

.PHONY: check-pixi
check-pixi:
	@command -v $(PIXICMD) >/dev/null 2>&1 || $(MAKE) install-pixi

.PHONY: install-pixi
install-pixi:
	@echo "Installing pixi..."
	@curl -fsSL https://pixi.sh/install.sh | bash
	@export PATH="$HOME/.pixi/bin:$PATH"
	@echo "Pixi installed."

.PHONY: clean
clean:
	rm -rf .pixi/*
	rm -f gtop




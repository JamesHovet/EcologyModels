pyinstaller run.py --noconfirm --log-level=INFO -w \
	--add-data="metaPopulationModel:." \
	--add-data="mesa:mesa" \
	--hidden-import="mesa" \
	--exclude-module="IPython" \
	--exclude-module="matplotlib" \
	--exclude-module="scipy" \

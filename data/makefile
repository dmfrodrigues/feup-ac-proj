all: processed/account.csv processed/card_comp.csv processed/card_dev.csv processed/client.csv processed/disp.csv processed/loan_comp.csv processed/loan_dev.csv processed/trans_comp.csv processed/trans_dev.csv

# Processed
processed/account.csv: raw/account.csv change-dates.py | processed
	python3 change-dates.py "date" < $< > $@

processed/card_comp.csv: raw/card_comp.csv change-dates.py | processed
	python3 change-dates.py "issued" < $< > $@

processed/card_dev.csv: raw/card_dev.csv change-dates.py | processed
	python3 change-dates.py "issued" < $< > $@

processed/client.csv: raw/client.csv process-client-birth-number.py | processed
	python3 process-client-birth-number.py < $< > $@

processed/disp.csv: raw/disp.csv | processed
	cp $< $@

processed/loan_comp.csv: raw/loan_comp.csv | processed
	python3 change-dates.py "date" < $< > $@

processed/loan_dev.csv: raw/loan_dev.csv | processed
	python3 change-dates.py "date" < $< > $@

processed/trans_comp.csv: raw/trans_comp.csv | processed
	python3 change-dates.py "date" < $< > $@

processed/trans_dev.csv: raw/trans_dev.csv | processed
	python3 change-dates.py "date" < $< > $@

processed:
	mkdir -p $@

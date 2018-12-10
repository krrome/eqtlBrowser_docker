import sys
import os
import yaml

if __name__ == "__main__":
	wd = sys.argv[1]

	static_folder = os.path.join(wd, "static")
	mongo_folder = os.path.join(wd, "mongodb_new_data")
	static_zip = static_folder + ".zip"
	mongo_zip = mongo_folder + "mongodb_new_data_2018_12_05.zip"

	if not os.path.exists(static_zip):
		os.system("python google_drive.py 1IHNAQDnLS-QwbINJtnxxR0_azAFzNAzL "+static_zip)
		if os.path.exists(static_folder):
			os.unlink(static_folder)
		os.system("unzip {0} -d {1}".format(static_zip, static_folder))

	if not os.path.exists(mongo_zip):
		os.system("python google_drive.py 1Jp0FwVb46RXVsbtcxHyzIzoEYSueIg67 "+mongo_zip)
		if os.path.exists(mongo_folder):
			os.unlink(mongo_folder)
		os.system("unzip {0} -d {1}".format(mongo_zip, mongo_folder))

	
	with open("docker-compose-template.yaml", "r") as ifh:
		compose_template = yaml.load(ifh)

	# set the mongodb volume link in the docker-compose file
	vol_list_mongo = []
	if 'volumes' in compose_template['services']['eqtl_mongodb']:
		vol_list_mongo = compose_template['services']['eqtl_mongodb']['volumes']
	else:
		compose_template['services']['eqtl_mongodb']['volumes'] = vol_list_mongo

	vol_list_mongo.append("{0}:{1}".format(mongo_folder, "/usr/share/mongo_data"))


	# set the static volume link in the docker-compose file
	vol_list_flask = []
	if 'volumes' in compose_template['services']['eqtl_flask']:
		vol_list_flask = compose_template['services']['eqtl_flask']['volumes']
	else:
		compose_template['services']['eqtl_flask']['volumes'] = vol_list_flask

	vol_list_flask.append("{0}:{1}".format(static_folder, "/etc/eqtl_browser/eqtlBrowser/ebrowse/static"))

	with open("docker-compose.yaml", "w") as ofh:
		yaml.dump(compose_template, ofh, default_flow_style=False)

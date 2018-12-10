import sys
import os
import yaml

def cut_last_folder(fname):
	return "/".join(fname.split("/")[:-1])

if __name__ == "__main__":
	wd = sys.argv[1]

	static_folder = os.path.join(wd, "static")
	mongo_folder = os.path.join(wd, "mongodb_new_data")

	if not os.path.exists(static_zip):
		os.system("python google_drive.py 1IHNAQDnLS-QwbINJtnxxR0_azAFzNAzL "+static_zip)
		if os.path.exists(static_folder):
			os.unlink(static_folder)
		os.system("unzip {0} -d {1}".format(static_zip, cut_last_folder(static_folder)))
	
	with open("docker-compose-template.yaml", "r") as ifh:
		compose_template = yaml.load(ifh)


	# set the static volume link in the docker-compose file
	vol_list_flask = []
	if 'volumes' in compose_template['services']['eqtl_flask']:
		vol_list_flask = compose_template['services']['eqtl_flask']['volumes']
	else:
		compose_template['services']['eqtl_flask']['volumes'] = vol_list_flask

	vol_list_flask.append("{0}:{1}".format(static_folder, "/etc/eqtl_browser/eqtlBrowser/ebrowse/static"))

	with open("docker-compose.yaml", "w") as ofh:
		yaml.dump(compose_template, ofh, default_flow_style=False)

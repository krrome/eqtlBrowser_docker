import sys
import os
import yaml

def cut_last_folder(fname):
    return "/".join(fname.split("/")[:-1])

def extend_if_exists(node, key, in_list):
    if key in node:
        node[key].extend(in_list)
    else:
        node[key] = in_list

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--interfix', action="store", default=None)
    parser.add_argument('--exp_port', action="store", default=80, type=int)
    parser.add_argument('path')
    args = parser.parse_args()
    wd = args.path


    static_folder = os.path.join(wd, "static")
    static_zip = static_folder + ".zip"

    os.system("python google_drive.py 1IHNAQDnLS-QwbINJtnxxR0_azAFzNAzL "+static_zip)
    if os.path.exists(static_folder):
        import shutil
        shutil.rmtree(static_folder)

    os.system("unzip {0} -d {1}".format(static_zip, cut_last_folder(static_folder)))
    os.unlink(static_zip)
    
    with open("docker-compose-template.yaml", "r") as ifh:
        compose_template = yaml.load(ifh)


    # set the static volume link in the docker-compose file
    extend_if_exists(compose_template['services']['eqtl_flask'], 'volumes', ["{0}:{1}".format(static_folder, "/etc/eqtl_browser/eqtlBrowser/ebrowse/static")])

    if args.interfix is not None:
        extend_if_exists(compose_template['services']['eqtl_flask'], 'environment', ["INTERFIX=%s"%args.interfix])

    extend_if_exists(compose_template['services']['eqtl_flask'], 'ports', ["%d:80"%args.exp_port])

    with open("docker-compose.yaml", "w") as ofh:
        yaml.dump(compose_template, ofh, default_flow_style=False)

import json
import os


def check_license(output, license_id):
    with open(os.path.join("data", "spdx.json"), mode="r", encoding="utf-8") as spdx_file:
        licenses = json.load(spdx_file)
        if license_id in licenses:
            output.info('license "%s" is a valid SPDX license identifier' % license_id)
        else:
            output.error('license "%s" is not a valid SPDX license identifier' % license_id)


def pre_export(output, conanfile, conanfile_path, reference, **kwargs):
    del conanfile_path, reference, kwargs

    if "license" not in conanfile.__dict__:
        output.info("recipe doesn't have a license attribute")
        return
    if isinstance(conanfile.license, str):
        licenses = [conanfile.license]
    elif isinstance(conanfile.license, (tuple, list)):
        licenses = conanfile.license
    else:
        output.error("don't know how to process license attribute which is neither string nor tuple")
        return
    for license_id in licenses:
        check_license(output, license_id)

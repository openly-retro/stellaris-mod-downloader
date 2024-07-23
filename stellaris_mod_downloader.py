import sys
import argparse
import tempfile
import subprocess

STELLARIS_WORKSHOP_ID = 281990

def download_mod(mod_id: int):
    # Create script file
    # use steamcmd to execute it, capturing output
    print(f"Making script to download mod ID {mod_id}...")
    script_contents = f"""
login anonymous
workshop_download_item {STELLARIS_WORKSHOP_ID} {mod_id}
quit
"""
    temp_script = tempfile.NamedTemporaryFile(mode="w")
    temp_script.write(script_contents)
    temp_script.seek(0)
    print("Downloading mod file. NOTHING WILL HAPPEN HERE UNTIL IT'S DONE DOWNLOADING.")
    result = run_steamcmd_script(temp_script.name)
    print("done?")
    temp_script.close()

def run_steamcmd_script(scriptfile_name):
    _result = ""
    downloader = subprocess.run([
        "steamcmd",
        "+runscript",
        scriptfile_name,
    ], capture_output=True, encoding='utf-8')
    # if "success" not in downloader.stdout:
    #     if "No match" in downloader.stdout:
    #        _result = "The mod ID wasn't found in the Stellaris workshop."
    #     else:
    #         _result = (
    #             "Mod failed to download for some odd reason:\n"
    #             f"{downloader.stdout}"
    #         )
    # else:


    print(downloader.stdout)


if __name__=="__main__":
    parser = argparse.ArgumentParser(
        prog="0xRetro Stellaris Mod Downloader",
        description="Download Stellaris mods from Steam"
    )
    parser.add_argument(
        '--mod-id',
        help='ID of the mod, which is at the end of the mod url, like sharedfiles/filedetails/?id=1234',
        required=True
    )
    args = parser.parse_args()
    download_mod(args.mod_id)

import os
import shutil
import sys

import sqlean as sqlite3
from dotenv.main import load_dotenv

from emby_api import divide_emby_versions, get_emby_libraries, merge_emby_versions
from enums.ProcessMode import ProcessMode

sqlite3.extensions.enable_all()
load_dotenv()
emby_config_dir = os.environ.get("EMBY_CONFIG_DIR")
shutil.copy(f"{emby_config_dir}/data/library.db", "./emby.db")


# has the same API as the default `sqlite3` module
def group_for_library(locations: list, process_mode: ProcessMode = ProcessMode.MERGE):
    with sqlite3.connect("./emby.db", uri=True) as conn:
        cursor = conn.cursor()
        rows = cursor.execute(
            rf"""
        select group_concat(Id) as Ids,
              regexp_substr(ProviderIds, 'Tmdb=(\d+)')   as Tmdbid
        from MediaItems
        where ({" or ".join([f"Path like '{loc}%'" for loc in locations])})
          and type = 5
          and ProviderIds <> ''
        group by regexp_substr(ProviderIds, 'Tmdb=(\d+)')
        having count(Id) > 1
        """
        )
        for ids, _ in rows:
            print("processing", ids)
            if (process_mode == ProcessMode.MERGE):
                merge_emby_versions(ids)
            else:
                divide_emby_versions(ids.split(',')[0])
            print("processed\n")


def process(process_mode: ProcessMode, paths:list):
    for lib in get_emby_libraries():
        merging_locations = list(
            filter(
                lambda x: not paths or any([x.startswith(path) for path in paths]), lib["locations"]
            )
        )

        if not merging_locations:
            continue

        print(f"{process_mode.name} library: {lib['name']}")
        print(*["                - " + loc for loc in merging_locations], sep="\n")

        group_for_library(merging_locations, process_mode)
        print("*" * 50)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        process(ProcessMode.MERGE, [])
    elif len(sys.argv) == 2:
        process(ProcessMode(int(sys.argv[1])), [])
    else:
        process(ProcessMode(int(sys.argv[1])), sys.argv[2:])

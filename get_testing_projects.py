import os
import shutil
import subprocess
from pathlib import Path

android = [
    ["https://github.com/bookdash/bookdash-android-app.git", "true"],
    ["https://github.com/signalapp/Signal-Android.git", "true"],
    ["https://github.com/halilozel1903/AndroidTVMovieParadise.git", "true"],
]
binaries = [

]
clojure = [

]
containers = [

]
cpp = [
    ["https://github.com/imneme/pcg-cpp.git", "true"],
    ["https://github.com/PCRE2Project/pcre2.git", "true"],
    ["https://github.com/odygrd/quill.git", "true"],
]
dart = [

]
dotnet = [
    ["https://github.com/AlexArchive/Ember.git", "true"],
    ["https://github.com/punker76/simple-music-player.git", "true"],
    ["https://github.com/jbe2277/musicmanager.git", "true"],
]
elixir = [

]
go = [
    ["https://github.com/DylanMeeus/GoAudio.git", "true"],
    ["https://github.com/dh1tw/gosamplerate.git", "true"],
    ["https://github.com/ergo-services/ergo.git", "true"],
    ["https://github.com/anthdm/hollywood.git", "true"],

]
haskell = [

]
java = [

]
javascript = [

]
php = [

]
python = [

]
ruby = [

]
rust = [

]
swift = [

]

slangs=[
    ["android", android],
    ["binaries", binaries],
    ["clojure", clojure],
    ["containers", containers],
    ["cpp", cpp],
    ["dart", dart],
    ["dotnet", dotnet],
    ["elixir", elixir],
    ["go", go],
    ["haskell", haskell],
    ["java", java],
    ["javascript", javascript],
    ["php", php],
    ["python", python],
    ["ruby", ruby],
    ["rust", rust],
    ["swift", swift],
]

# create directories for each project
for lang in slangs:
    try:
        os.mkdir(lang[0])
    except FileExistsError as e:
        print(f"Folder exists: {e}")
    os.chdir(lang[0])
    print(os.getcwd())
    for repo, command in lang[1]:
        gitcommand = f"git clone --filter=blob:none {repo}"
        print(gitcommand)
        subprocess.run(
            gitcommand, shell=True, check=False
        )
        dir_name = Path(repo[8:]).stem
        subprocess.run(
            command, shell=True, cwd=dir_name, check=False
        )
    os.chdir("..")
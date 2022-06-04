# this project is INCREDIBLY SCUFFED and olibomby probably will patches this kind of thing in his mapping tools within 1 second of dev time but whatever i do not care i do this for the educational purposes :halgohstare:

**the default scripts**
1. Colorhax : Base Script `colorhax=[starttime],[endtime],[colorhax pattern]`
2. Colorburst : Colorhaxs the specific pattern with a specified beat snap `colorburst=[starttime],[endtime],[colorhax pattern],[beatsnap (e.g. 6 | using 1/6 will encounter errors.)]`
3. Bookmarkhax : Swap colorhaxs using bookmarks `colorhax=[colorhax pattern]`

[wiki](https://github.com/ohm002/ColorHaxer/wiki)

### reminder for you
* the code is a spaghetti for sure so any good developers out there *PLEASE* roast my code in the issues tab u can call me yandev whatever
* if u wanna make a custom script (cus there are only 3 script LOL) then maybe just edit the Hax.py where bunch of spaghetties are in there so have fun
  * the default osuparse script are 
     ```Hax.isslider(LIST of parameters in that line) 
        Parse.AssembleBeatmapData(STRING of .osu file || OsuMap class object)
        Parse.ParseAllBeatmapData(STRING of .osu file) || will return an OsuMap class object
     ```
  * and everything kinda just works on 
  ``` 
  if the objects kinda match the conditions then run the default colorhax command for this
  ```


# how to use
1. create a text file (in this way that it can be archived and use later in case its ruined bcus of the mods)
2. the language is pretty simple tbh its kinda like
```
osufile=[path_to_your_osu_file]

[scriptname]=[parameters (naturally separated with,)]
```
3. for the starttime and endtime leave the parameters with "-" and the default value will be the start/end of the map, can use the milliseconds or in the 00:00:000 format
4. for the colorhax pattern, indefault it will be separate with "/" e,g, "1/8/3" (for the funny using the same color in the section works somehow LOL)


# to run the file on terminal
Python Build : ` py main.py [colorhax data file]`

Executable Build : ` main.exe [colorhax data file]`
 
---
if anyone has any question or feedback pls just dm me at ohm002#8123 i'm so lonely TY 



.

.

.

.

.

.

probably coming soon

- [ ] using opencv to decode the screenshot from olibomby's color manager to the colorhax file
- [ ] colorhax an object with a specified sv

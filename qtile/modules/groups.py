from libqtile.config import  Group, Match


__groups = {
    1: Group("", matches=[Match(wm_class=["google-chrome"])]),
    2: Group('󰨞', matches=[Match(wm_class=["code", "godot", "godot.desktop"])]),
    3: Group('', matches=[Match(wm_class=["alacritty", "Alacritty"])]),
    4: Group('󱍢', matches=[Match(wm_class=["discord", "slack", "spotify", "Spotify"])], layout="max")
}

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]
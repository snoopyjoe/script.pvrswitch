import xbmc,xbmcgui
xbmc.sleep(1000)
VisbleWindows = xbmc.getCondVisibility('[Window.IsActive(10700) | Window.IsActive(10702)]')
VisiblePVR = xbmc.getCondVisibility('!Pvr.IsPlayingTv + System.HasPVRAddon')

while not VisbleWindows:
    VisbleWindows = xbmc.getCondVisibility('[Window.IsActive(10700) | Window.IsActive(10702)]')
    if VisiblePVR and VisbleWindows:
        xbmc.sleep(1000)
        pvr_toggle_off = '{"jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": ' \
                                 '{"addonid": "pvr.iptvsimple", "enabled": false}, "id": 1}'
        xbmc.executeJSONRPC(pvr_toggle_off)
        xbmc.sleep(1000)
        pvr_toggle_on = '{"jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": ' \
                                '{"addonid": "pvr.iptvsimple", "enabled": true}, "id": 1}'
        xbmc.executeJSONRPC(pvr_toggle_on)
        break
    xbmc.sleep(1000)
else:
    if VisiblePVR:
        xbmc.sleep(1000)
        pvr_toggle_off = '{"jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": ' \
                                 '{"addonid": "pvr.iptvsimple", "enabled": false}, "id": 1}'
        xbmc.executeJSONRPC(pvr_toggle_off)
        xbmc.sleep(1000)
        pvr_toggle_on = '{"jsonrpc": "2.0", "method": "Addons.SetAddonEnabled", "params": ' \
                                '{"addonid": "pvr.iptvsimple", "enabled": true}, "id": 1}'
        xbmc.executeJSONRPC(pvr_toggle_on)
    else:
        xbmcgui.Dialog().dialog.ok('There are no PVR Clients installed', 'Please install to use PVR.')
